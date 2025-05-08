import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Create a spatial grid
x=np.linspace(0,1.0,201)
y=np.linspace(0,1.0,201)
X,Y=np.meshgrid(x,y)
T_1=np.zeros_like(X)
x_1=np.linspace(0.005,0.995,199)
q_1=np.linspace(0.005,0.995,199)
T_2=np.zeros_like(X)
q_2=np.zeros_like(x_1)

# Boundary condition
T_top=0
T_left=0
T_right=0
T_bottom=100

# Set number of iterations
iterations=8000

# Set Boundary condition
T_1[-1:,:]=T_top
T_1[:1,:]=T_bottom
T_1[:,:1]=T_right
T_1[:,-1:]=T_left
T_2[-1:,:]=T_top
T_2[:1,:]=T_bottom
T_2[:,:1]=T_right
T_2[:,-1:]=T_left

# Define demage
T_1[100:,80:121]=0
T_2[80:121,100:]=0
for i in range(iterations):
    for k in range(1,200):
        for j in range(1,200):
            if j>99 and k>79 and k<121:
                break
            else:
                T_1[j,k]=0.25*(T_1[j+1][k]+T_1[j-1][k]+T_1[j][k+1]+T_1[j][k-1])
for i in range(iterations):
    for k in range(1,200):
        for j in range(1,200):
            if k>99 and j>79 and j<121:
                break
            else:
                T_2[j,k]=0.25*(T_2[j+1][k]+T_2[j-1][k]+T_2[j][k+1]+T_2[j][k- 1])
for i in range(1,200):
    q_1[i-1]=T_1[0,i]-T_1[1,i]
    q_2[i-1]=T_2[0,i]-T_2[1,i]
print(np.trapezoid(q_1,x_1))
print(np.trapezoid(q_2,x_1))

#完成可视化
fig=plt.figure(figsize=(8,8))
ax1=fig.add_subplot(2,2,1)
ax1.contourf(X,Y,T_1,50,cmap='jet')
rect = Rectangle((0.4, 0.5), 0.2, 0.5, linewidth=1, edgecolor='white', facecolor='none')
ax1.add_patch(rect)
ax1.set_aspect('equal')
ax1.set_title('vertical defeat')
ax2=fig.add_subplot(2,2,2)
ax2.contourf(X,Y,T_2,50,cmap='jet')
rect2 = Rectangle((0.5,0.4), 0.5, 0.2, linewidth=1, edgecolor='white', facecolor='none')
ax2.add_patch(rect2)
ax2.set_aspect('equal')
ax2.set_title('horizontal defeat')
ax3=fig.add_subplot(2,2,3)
ax3.plot(x_1,q_1)
ax3.set_title('bottom temperature gradient 2')
ax4=fig.add_subplot(2,2,4)
ax4.plot(x_1,q_2)
ax4.set_title('bottom temperature gradient 3')
plt.show()