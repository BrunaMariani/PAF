import z1 as prt
import matplotlib.pyplot as plt
C_d_l = []
m_l = []
range1 = []
range2 = []
for i in range(100):
    C_d = 0.01*i
    C_d_l.append(C_d)
for i in range(100):
    m = 0.1*i
    m_l.append(m)
p1=prt.Projectile(10,45,0,0,0.01,1.22,0.1,0.05,0.1)
for element in C_d_l:
    p1.C_d = element
    d = p1.range()
    range1.append(d)

plt.plot(range1,C_d_l)
plt.show()

#p1.reset()
#p1=prt.Projectile(10,45,0,0,0.01,1.22,0.1,0.05,0.1)
#for element in m_l:
    #p1.m= element
    #d = p1.range()
    #range2.append(d)
#print(range2)








