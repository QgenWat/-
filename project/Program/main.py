import numpy as np


def u(r1, r2):
    w = float()
    r = r2 - r1
    if r[0] == r[1] == r[2] == 0:
        w = 0
    else:
        rm = r[0] ** 2 + r[1] ** 2 + r[2] ** 2
        w = 4 * (rm ** -12 - rm ** -6)
    return w


def ac(r1, r2):
    w = np.array([])
    r = r2 - r1
    if r[0] == r[1] == r[2] == 0:
        w = r
    else:
        rm = r[0] ** 2 + r[1] ** 2 + r[2] ** 2
        c = -4 * (12 * rm ** -14 - 6 * rm ** -8)
        w = c * r
    return w


def find(r0, r, b, l):
    q = []
    gr = [[0, 0], [0, 0], [0, 0]]
    for i in range(3):
        if r0[i] + b <= l:
            gr[i][0] = r0[i] + b
        else:
            gr[i][0] = r0[i] + b - l
        if r0[i] - b >= 0:
            gr[i][1] = r0[i] - b
        else:
            gr[i][1] = r0[i] - b + l
    for i in r:
        tmp = np.array([0, 0, 0], float)
        if gr[0][1] <= i[0] <= gr[0][0]:
            tmp[0] = i[0]
        elif i[0] <= gr[0][0] <= gr[0][1]:
            if r0[0] < gr[0][0]:
                tmp[0] = i[0]
            else:
                tmp[0] = i[0] + l
        elif gr[0][0] <= gr[0][1] <= i[0]:
            if r0[0] > gr[0][1]:
                tmp[0] = i[0]
            else:
                tmp[0] = i[0] - l
        else:
            continue
        if gr[1][1] <= i[1] <= gr[1][0]:
            tmp[1] = i[1]
        elif i[1] <= gr[1][0] <= gr[1][1]:
            if r0[1] < gr[1][0]:
                tmp[1] = i[1]
            else:
                tmp[1] = i[1] + l
        elif gr[1][0] <= gr[1][1] <= i[1]:
            if r0[1] > gr[1][1]:
                tmp[1] = i[1]
            else:
                tmp[1] = i[1] - l
        else:
            continue
        if gr[2][1] <= i[2] <= gr[2][0]:
            tmp[2] = i[2]
        elif i[2] <= gr[2][0] <= gr[2][1]:
            if r0[2] < gr[2][0]:
                tmp[2] = i[2]
            else:
                tmp[2] = i[2] + l
        elif gr[2][0] <= gr[2][1] <= i[2]:
            if r0[2] > gr[2][1]:
                tmp[2] = i[2]
            else:
                tmp[2] = i[2] - l
        else:
            continue
        q.append(tmp)
    return np.array(q)


def cord(r0, a, v, dt, l):
    q = r0 + dt * v + 0.5 * a * dt ** 2
    q = q % l
    return q


f1 = open('r.txt', 'w')
f2 = open('v.txt', 'w')
f3 = open('a.txt', 'w')
f4 = open('E.txt', 'w')
f0 = open('ri.txt', 'r')
f00 = open('vi.txt', 'r')
ln = 50
a = f0.readlines()
for i in range(len(a)):
    a[i] = [float(j[:1]) for j in a[i].split('\t')]
r = np.array(a)
a = f00.readlines()
for i in range(len(a)):
    a[i] = [float(j) for j in a[i].split('\t')]
v = np.array(a)
b = 2.5
l = 5.11
sigm = 3.4 * 10 ** -10
m = 6.63 * 10 ** -26
eps = 1.6568 * 10 ** -21
t = 10 ** -14
dt = t * (eps / (m * sigm ** 2)) ** 0.5
x = 5000
ah = [np.array([0, 0, 0], float) for i in range(ln)]
a = [np.array([0, 0, 0], float) for i in range(ln)]
f1.write(str(ln) + '\n' + '\n')
E = U = K = 0
for j in range(ln):
    f1.write('Ar\t{0}\t{1}\t{2}\n'.format(str(r[j][0]), str(r[j][1]), str(r[j][2])))
f2.write(str(ln) + '\n' + '\n')
for j in range(ln):
    f2.write('Ar\t{0}\t{1}\t{2}\n'.format(str(v[j][0]), str(v[j][1]), str(v[j][2])))
for j in range(ln):
    q = find(r[j], r, b, l)
    for k in q:
        a[j] = a[j] + ac(r[j], k)
        U += u(r[j], k)
for i in range(ln):
    K += v[i][0] ** 2 + v[i][1] ** 2 + v[i][2] ** 2
E = 0.5 * (K + U)
f4.write(str(U*0.5) + '\t' + str(K*0.5) + '\t' + str(E) + '\n')
f3.write(str(ln) + '\n' + '\n')
for j in range(ln):
    f3.write('Ar\t{0}\t{1}\t{2}\n'.format(str(a[j][0]), str(a[j][1]), str(a[j][2])))
for i in range(x):
    U = E = K = 0
    f1.write(str(ln) + '\n' + '\n')
    f2.write(str(ln) + '\n' + '\n')
    f3.write(str(ln) + '\n' + '\n')
    for j in range(ln):
        r[j] = cord(r[j], a[j], v[j], dt, l)
        f1.write('Ar\t{0}\t{1}\t{2}\n'.format(str(r[j][0]), str(r[j][1]), str(r[j][2])))
    for j in range(ln):
        q = find(r[j], r, b, l)
        ah[j] = np.array([0, 0, 0])
        for k in q:
            U += u(r[j], k)
            ah[j] = ah[j] + ac(r[j], k)
        v[j] = v[j] + 0.5 * (a[j] + ah[j]) * dt
        K += v[j][0] ** 2 + v[j][1] ** 2 + v[j][2] ** 2
        f2.write('Ar\t{0}\t{1}\t{2}\n'.format(str(v[j][0]), str(v[j][1]), str(v[j][2])))
        f3.write('Ar\t{0}\t{1}\t{2}\n'.format(str(ah[j][0]), str(ah[j][1]), str(ah[j][2])))
    a = ah
    E = 0.5 * (K + U)
    f4.write(str(U*0.5) + '\t' + str(K*0.5) + '\t' + str(E) + '\n')
