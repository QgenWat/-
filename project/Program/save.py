import numpy as np

f1 = open('r.txt', 'w')
k = 1
l0 = 10
r1 = np.array([-1, -1, -1])
r2 = np.array([1, 1, 1])
v1 = v2 = np.array([0, 0, 0])
m1 = 0.2
m2 = 4
dt = 0.025
x = 200
r = r2 - r1
dr = r[0] ** 2 + r[1] ** 2 + r[2] ** 2
f = k * (dr - l0)
a1 = f / m1 * r
a2 = -f / m2 * r
f1.write(str(2) + '\n' + '\n')
f1.write('Ar\t{0}\t{1}\t{2}\n'.format(str(r1[0]), str(r1[1]), str(r1[2])))
f1.write('Ar\t{0}\t{1}\t{2}\n'.format(str(r2[0]), str(r2[1]), str(r2[2])))
for i in range(x):
    a1h = a2h = np.array([0, 0, 0])
    r1 = r1 + v1 * dt + 0.5 * a1 * dt ** 2
    r2 = r2 + v2 * dt + 0.5 * a2 * dt ** 2
    r = r2 - r1
    dr = r[0] ** 2 + r[1] ** 2 + r[2] ** 2
    f = k * (dr - l0)
    a1h = f / m1 * r
    a2h = -f / m2 * r
    v1 = v1 + 0.5 * (a1 + a1h) * dt
    v2 = v2 + 0.5 * (a2 + a2h) * dt
    a1 = a1h
    a2 = a2h
    f1.write(str(2) + '\n' + '\n')
    f1.write('Ar\t{0}\t{1}\t{2}\n'.format(str(r1[0]), str(r1[1]), str(r1[2])))
    f1.write('Ar\t{0}\t{1}\t{2}\n'.format(str(r2[0]), str(r2[1]), str(r2[2])))
