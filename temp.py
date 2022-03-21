import numpy as np
import matplotlib.pyplot as plt

p0 = 0.1
p1 = 0.4
p2 = 0.5

xinf = -10
xsup = 10
ysup = 15
yinc = 1.6
gens = 12
rad = 0.07
thick = 2

fig, ax = plt.subplots()

fig.set_figheight(30)
fig.set_figwidth(15)


ax.set_aspect(1)
plt.xlim(xinf,xsup)
plt.ylim(-0.5,ysup)
ax.set_xticks([])
ax.set_yticks([])

gen = [[0]]
circle=plt.Circle((0,0),0.05, color='black')
ax.add_artist(circle)

for g in range(1,gens):
    gen.append([])
    for j in range(len(gen[g-1])):
        rnd = np.random.choice(np.arange(0, 3), p=[p0, p1, p2])
        if rnd==1:
            a=gen[g-1][j]
            gen[g].append(a)
            circle=plt.Circle((gen[g-1][j],yinc*g),rad, color='black')
            plt.plot([gen[g-1][j],gen[g-1][j]],[yinc*(g-1),yinc*g],color='black', linewidth = thick)
            ax.add_artist(circle)
        if rnd==2:
            radius = min([gen[g-1][j]-xinf]+[xsup-gen[g-1][j]]+[abs(x-gen[g-1][j]) for x in gen[g-1][:j]]+[abs(x-gen[g-1][j]) for x in gen[g-1][j+1:]])/2
            a=gen[g-1][j]
            gen[g].append(a-(2/3)*radius)
            circle=plt.Circle((gen[g][-1],yinc*g),rad, color='black')
            plt.plot([a,gen[g][-1]],[yinc*(g-1),yinc*g],'black', linewidth = thick)
            ax.add_artist(circle)
            gen[g].append(a+(2/3)*radius)
            circle=plt.Circle((gen[g][-1],yinc*g),rad, color='black')
            plt.plot([a,gen[g][-1]],[yinc*(g-1),yinc*g],'black', linewidth = thick)
            ax.add_artist(circle)
plt.show()