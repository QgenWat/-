m = [0]*100
    #p = 0
    #for j in range(100):
        #rh[j] = rh[j] + dt * v[j] + 0.5 * a[j] * (dt ** 2)
        #rhh = rh[j] - r0[j]
        #p += rhh[0] ** 2 + rhh[1] ** 2 + rhh[2] ** 2
    #fh.write(str(p / 100) + '\n')
    #p=0
    #for j in range(100):
        #rh[j] = rh[j] + dt * v[j] + 0.5 * a[j] * (dt ** 2)
        #m[j] = r0[j][0]*rh[j][0]+r0[j][1]*rh[j][1]+r0[j][2]*rh[j][2]
    #for jj in range(100):
        #for j in range(jj+1, 100):
            #p +=m[jj]+m[j]
    #fk.write(str(p / (100*99*0.5)) + '\n')
ln = 100
t = 5*10 ** -15
x = 9999
b = 3
l = 6.93
sigm = 3.4 * 10 ** -10
m = 6.63 * 10 ** -26
eps = 1.6568 * 10 ** -21
dt = t * (eps / (m * sigm ** 2)) ** 0.5
print(dt)