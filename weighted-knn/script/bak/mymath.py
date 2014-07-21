import math
import random

def v_sqrt(v):
  v_new = []
  for e in v:
    v_new.append( math.sqrt(e) )
  return v_new


def get_average(f_train):
  f_average = []

  for idx in range( len(f_train[0]) ):
    sums = 0
    num = 0

    for i in range( len(f_train) ):
      if f_train[i][idx] == 'NaN':
        continue
      sums += float(f_train[i][idx])
      num += 1

    if num > 0:
      f_average.append(sums / num)
    else:
      f_average.append(0)

  return f_average


def get_variable(f_train, f_average):
  feat_variable = []

  for idx in range( len(f_train[0]) ):
    sums = 0
    num = 0

    for i in range( len(f_train) ):
      if f_train[i][idx] == 'NaN':
        continue
      v_diff = float(f_train[i][idx]) - f_average[idx]
      sums += math.pow(v_diff, 2)
      num += 1

    if num > 0:
      feat_variable.append(sums / num)
    else:
      feat_variable.append(0)

  return feat_variable


def v_rand(len, v0):
  v = []
  for i in range( len ):
    e = random.random() * v0
    v.append( e )
  return v


def v_rand_2d(len1, len2, v0):
  v = []
  for i in range( len1 ):
    v2 = []
    for j in range( len2 ):
      e = 0.1 + 0.9 *random.random()
      e *= v0
      v2.append( e )
    v.append( v2 )
  return v


def init_dict(len, v0 = 0):
  v = []
  for i in range( len ):
    v.append( v0 )

  return v


def init_dict_2d(len1, len2, v0 = 0):
  v = []
  for i in range( len1 ):
    v2 = []
    for j in range( len2 ):
      v2.append( v0 )
    v.append(v2)

  return v


def init_dict_3d(len1, len2, len3, v0 = 0):
  v = []
  for i in range( len1 ):
    v2 = []
    for j in range( len2 ):
      v3 = []
      for k in range( len3 ):
        v3.append( v0 )
      v2.append( v3 )
    v.append( v2 )

  return v


def mahala_dist(f1, f2, f_var):
    if f_var <= 0.00000001:
        return 0, 0
    if f1 == 'NaN' or f2 == 'NaN':
        return 0, 0

    diff = float(f1) - float(f2)
    return math.fabs( diff ) / f_var, 1


def calc_dist(f1_train, f2_train, f_stdd):
    n_f1_train = len(f1_train)
    n_f2_train = len(f2_train)
    n_f_dimen = len(f1_train[0])

    print 'before init 3d: %d, %d, %d' % (n_f1_train, n_f2_train, n_f_dimen)
    D_train = init_dict_3d(n_f1_train, n_f2_train, n_f_dimen)
    P_train = init_dict_2d(n_f1_train, n_f2_train)

    for i in range( n_f1_train ):
        for j in range( n_f2_train ):
            for p in range( n_f_dimen ):
                diff, flag = mahala_dist(f1_train[i][p], f2_train[j][p], f_stdd[p])
                D_train[i][j][p] = diff
                P_train[i][j] += flag

    for i in range( n_f1_train ):
        for j in range( n_f2_train ):
          if P_train[i][j] == 0: continue
          P_train[i][j] = math.pow(P_train[i][j], -0.5)

    for i in range( n_f1_train ):
        for j in range( n_f2_train ):
            for p in range( n_f_dimen ):
                D_train[i][j][p] *= P_train[i][j]

    return D_train


if __name__ == '__main__':
  print 'testing v_sqrt([1,2])'
  v = [1, 2]
  print v_sqrt(v)

  print 'testing init_dist_3d(2, 3, 2, 0.2)'
  v = init_dict_3d(2, 3, 2, 0.2)
  print v

  print 'testing v_rand_2d(2, 3, 0.001)'
  v = v_rand_2d(2, 3, 0.001)
  print v

  print 'testing mahala_dist(0.3, -1.8, 5)'
  print  mahala_dist('0.3', '-1.8', 5)

  print 'testing mahala_dist(NaN, 3, 2)'
  print mahala_dist('NaN', 3, 2)

  print 'testing mahala_dist(3, 4, 0)'
  print mahala_dist(3, 4, 0)

  print 'testing get_average([[1, 2, 5],[8, 2, 6]])'
  f_avg = get_average([[1, 2, 5],[8, 2, 6]])
  print f_avg
  f_var = get_variable([[1, 2, 5],[8, 2, 6]], f_avg) 
  print f_var

  f_stdd = v_sqrt(f_var)
  print 'testing calc_dist([[1, 2, 5],[8, 2, 6]], [[1, 2, 5],[8, 2, 6]], f_stdd)'
  D_train = calc_dist([[1, 2, 5],[8, 2, 6]], [[1, 2, 5],[8, 2, 6]], f_stdd)
  print D_train
  print 'testing calc_dist([[3, 5, NaN]], [[1, 2, 5],[8, 2, 6]], f_stdd)'
  D_train = calc_dist([[3, 5, 'NaN']], [[1, 2, 5],[8, 2, 6]], f_stdd)
  print D_train
  D_train = calc_dist([[3, 5, 'NaN']], [[1, 2, 5],[8, 2, 6]], [1,1,1])
  print D_train


