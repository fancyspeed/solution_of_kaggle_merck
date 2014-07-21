import math

def get_average(feats):
  n_e = len(feats[0])
  f_avg = [0] * n_e 

  for feat in feats:
    for i in range(n_e):
      f_avg[i] += feat[i]

  n_f = float(len(feats))
  for i in range(n_e):
    f_avg[i] /= n_f
  return f_avg 

def get_variable(feats, f_avg):
  n_e = len(feats[0])
  f_var = [0] * n_e

  for feat in feats:
    for i in range(n_e): 
      v = feat[i] - f_avg[i]
      f_var[i] += v * v 

  n_f = float(len(feats))
  for i in range(n_e):
    f_var[i] /= n_f
  return f_var

def get_stdvar(f_var):
  n_e = len(f_var)
  f_std = [0] * n_e

  for i in range(n_e):
    f_std[i] = math.sqrt(f_var[i]) 
  return f_std

def get_feats(p_in):
  feat_all = []

  n_cur = 0
  for line in open(p_in):
    n_cur += 1
    if n_cur == 1:
      continue
    arr = line.strip().split(',')
    feat = arr[2:]
    feat_int = [int(ele) for ele in feat]
    feat_all.append(feat_int)
 
  return feat_all

def get_flag(std):
  flag = []
  head = []
  n_cur = 1 

  for v in std:
    if v < 0.000001:
      flag.append(0)
    else:
      flag.append(1)
      head.append('D_' + str(n_cur))
      n_cur += 1
  return flag, head

def write_train(std, flag, head, p_in, p_out):
  f_out = open(p_out, 'w')
  arr = ['MOLECULE','Act'] + head
  new_line = ','.join(arr) + '\n'
  f_out.write(new_line)

  n_f = len(std)
  n_cur = 0
  for line in open(p_in):
    n_cur += 1
    if n_cur == 1:
      continue
    arr = line.strip().split(',')
    if len(arr) != n_f + 2: continue
    new_arr = []
    for i in range(n_f):
      if flag[i]:
        if float(arr[2+i]) < 0.000001:
          new_arr.append('0')
        else:
          new_arr.append('%f' % (float(arr[2+i]) / std[i]))
    new_line = ','.join(arr[0:2] + new_arr) + '\n'
    f_out.write(new_line)
  
  f_out.close()

def write_test(std, flag, head, p_in, p_out):
  f_out = open(p_out, 'w')
  arr = ['MOLECULE'] + head
  new_line = ','.join(arr) + '\n'
  f_out.write(new_line)

  n_f = len(std)
  n_cur = 0
  for line in open(p_in):
    n_cur += 1
    if n_cur == 1:
      continue
    arr = line.strip().split(',')
    if len(arr) != n_f + 1: continue
    new_arr = []
    for i in range(n_f):
      if flag[i]:
        if float(arr[1+i]) < 0.000001:
          new_arr.append('0')
        else:
          new_arr.append('%f' % (float(arr[1+i]) / std[i]))
    new_line = ','.join(arr[0:1] + new_arr) + '\n'
    f_out.write(new_line)
  
  f_out.close()

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 5:
    print '<usage> train test train_out test_out'
    exit(-1)

  import gc
  gc.disable()

  feats = get_feats(sys.argv[1])  
  print len(feats)

  f_avg = get_average(feats)
  print len(f_avg)

  var = get_variable(feats, f_avg)

  std = get_stdvar(var)

  flag, head = get_flag(std)
  print len(flag)

  write_train(std, flag, head, sys.argv[1], sys.argv[3])
  write_test(std, flag, head, sys.argv[2], sys.argv[4])
