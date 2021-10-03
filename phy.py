import matplotlib.pyplot as plt
import numpy as np

# l=[]
# l.append(0.1)
# r = int(input())
# for x in range (0,400,1): 
#     l.append(r*l[x]*(1-l[x]))
#     plt.plot(x,l[x])
# plt.show()

n = []
x_limit=150
for i in range (x_limit):
    n.append(i)

y = []
y.append(0.1)
k = 0.1

r = float(input())

for i in range (x_limit-1):
    k = r * k * (1 - k)
    y.append(k)


plt.xlabel("n")
plt.ylabel("$X_n$")
plt.title("r="+str(r))
plt.plot(n, y)#,c='g')
plt.show() 

