import mymath
import time

print 'before init:', int(time.time())
v = mymath.init_dict_3d(200, 200, 200, 0.1)

print 'before iter:', int(time.time())
for i in range(200):
  for j in range(200):
    for k in range(200):
      a = 0.3 * v[i][j][k]

print 'after iter:', int(time.time())
