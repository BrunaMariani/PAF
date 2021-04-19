import matplotlib.pyplot as plt
import zdk1 as vh
p = vh.VertikalniHitac(10,10)
y,v,t = p.vertikalni_hitac(0.01)

plt.plot(t,y)
plt.show()
plt.plot(t,v)
plt.show()