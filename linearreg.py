import numpy as np
import matplotlib.pyplot as plt
def estimatecoef(x,y):
    n=np.size(x)
    m_x,m_y=np.mean(x),np.mean(y)
    ss_xy=np.sum(x*y)-n*m_x*m_y
    ss_xx=np.sum(x*x)-n*m_x*m_x
    b_1=ss_xy/ss_xx
    b_0=m_y-b_1*m_x
    return (b_1,b_0)
def plot_reg(x,y,b):
    plt.scatter(x,y,color="m",marker="o",s=30)
    y_pred=b[0]+b[1]*x 
    plt.plot(x,y_pred,color="g")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])
b = estimatecoef(x, y)
print("Estimated coefficients:\nb_0={} \nb_1={}".format(b[0], b[1]))
plot_reg(x, y, b)

















