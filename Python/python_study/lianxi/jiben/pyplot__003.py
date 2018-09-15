import numpy as np
import matplotlib.pyplot as plt
labels='frogs','hogs','dogs','logs'
sizes=15,20,45,10
colors='yellowgreen','gold','lightskyblue','lightcoral'
explode=0,0.1,0,0
#添加标题
plt.title('Histogram of IQ',color='#123456')
#添加文字
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
# n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.text(60, .025, r'$mu=100, sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()
