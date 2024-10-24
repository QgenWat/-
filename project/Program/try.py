import numpy as np


def f_help(gr, r1, r2, l):
    tmp = [False, np.array([0, 0, 0], float), np.array([0, 0, 0], float)]
    for i in range(3):
        if gr[i][1] <= r2[i] <= gr[i][0]:
            tmp[1][i] = r2[i]
            tmp[2][i] = r1[i]
        elif r2[i] <= gr[i][0] <= gr[i][1]:
            if r1[i] < gr[i][0]:
                tmp[1][i] = r2[i]
                tmp[2][i] = r1[i]
            else:
                tmp[1][i] = r2[i] + l
                tmp[2][i] = r1[i] - l
        elif gr[i][0] <= gr[i][1] <= r2[i]:
            if r1[i] > gr[i][1]:
                tmp[1][i] = r2[i]
                tmp[2][i] = r1[i]
            else:
                tmp[1][i] = r2[i] - l
                tmp[2][i] = r1[i] + l
        else:
            break
        if i == 2:
            tmp[0] = True
    return tmp


def find(r, b, l, ln):
    qq = [[] for i in range(ln)]
    for i in range(ln):
        gr = [[0, 0], [0, 0], [0, 0]]
        for k in range(3):
            gr[k][0] = (r[i][k] + b) % l
            gr[k][1] = (r[i][k] - b) % l
        for j in range(i + 1, ln):
            tmp = f_help(gr, r[i], r[j], l)
            if tmp[0]:
                qq[i].append(tmp[1])
                qq[j].append(tmp[2])
    return qq


def u(r1, r2):
    r = r2 - r1
    rm = (r[0] ** 2 + r[1] ** 2 + r[2] ** 2) ** 0.5
    return 4 * (rm ** -12 - rm ** -6)


def ac(r1, r2):
    r = r2 - r1
    rm = (r[0] ** 2 + r[1] ** 2 + r[2] ** 2) ** 0.5
    c = -4 * (12 * (rm ** -13) - 6 * (rm ** -7))
    return c * (r / rm)


def coord(r0, a, v, dt, l):
    q = r0 + dt * v + 0.5 * a * (dt ** 2)
    return q % l


def wr(f, ln, m):
    f.write(str(ln) + '\n' + '\n')
    for j in range(ln):
        f.write('Ar\t{0}\t{1}\t{2}\n'.format(str(m[j][0]), str(m[j][1]), str(m[j][2])))


ln = 100
t = 5*10 ** -15
x = 9999
b = 3
l = 6.93
sigm = 3.4 * 10 ** -10
m = 6.63 * 10 ** -26
eps = 1.6568 * 10 ** -21
dt = t * (eps / (m * sigm ** 2)) ** 0.5
f1 = open('r.txt', 'w')
f2 = open('v.txt', 'w')
f3 = open('a.txt', 'w')
f4 = open('E.txt', 'w')
f0 = open('ri.txt', 'r')
f00 = open('vi.txt', 'r')
fh = open('dif.txt', 'w')
#fk = open('kor.txt', 'w')
a = f0.readlines()
for i in range(len(a)):
    a[i] = [float(j) for j in a[i].split('\t')]
r = np.array(a)
r0 = np.array(a)
rh = np.array(a)
a = f00.readlines()
for i in range(len(a)):
    a[i] = [float(j) for j in a[i].split('\t')]
v = np.array(a)
ah = [np.array([0, 0, 0], float) for i in range(ln)]
a = [np.array([0, 0, 0], float) for i in range(ln)]
E = U = K = 0
q = find(r, b, l, ln)
for i in range(ln):
    for j in q[i]:
        a[i] = a[i] + ac(r[i], j)
        U += u(r[i], j)
for i in range(ln):
    K += v[i][0] ** 2 + v[i][1] ** 2 + v[i][2] ** 2
E = 0.5 * (K + U)
f4.write(str(U * 0.5) + '\t' + str(K * 0.5) + '\t' + str(E) + '\n')
wr(f1, ln, r)
wr(f2, ln, v)
# wr(f3, ln, a)
p = 0
for i in range(x):
    for j in range(100):
        rh[j] = rh[j] + dt * v[j] + 0.5 * a[j] * (dt ** 2)
        rhh = rh[j] - r0[j]
        p += rhh[0] ** 2 + rhh[1] ** 2 + rhh[2] ** 2
    fh.write(str(p / 100) + '\n')
    p = 0
    U = E = K = 0
    for j in range(ln):
        r[j] = coord(r[j], a[j], v[j], dt, l)
    q = find(r, b, l, ln)
    for j in range(ln):
        ah[j] = np.array([0, 0, 0], float)
        for k in q[j]:
            ah[j] = ah[j] + ac(r[j], k)
            U += u(r[j], k)
        v[j] = v[j] + 0.5 * (a[j] + ah[j]) * dt
        a[j] = ah[j]
        K += v[j][0] ** 2 + v[j][1] ** 2 + v[j][2] ** 2
    E = 0.5 * (K + U)
    f4.write(str(U * 0.5) + '\t' + str(K * 0.5) + '\t' + str(E) + '\n')
    wr(f1, ln, r)
    wr(f2, ln, v)
    # wr(f3, ln, a)
