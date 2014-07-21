def get_average(feats):
  n_e = len(feats[0])
  f_avg = [0] * n_e 

  for feat in feats:
    for i in range(n_e):
      f_avg[i] += feat[i]

  n_f = len(feats)
  for i in range(n_e):
    f_avg[i] /= float(n_f)
  return f_avg 

def euclidean_dist(f1, f2, n_e):
  sum = 0
  for i in range(n_e):
    v = f1[i] - f2[i]
    sum += v * v
  return sum

def get_variable(feats, f_avg):
  n_e = len(feats[0])

  sum = 0
  for feat in feats:
    sum += euclidean_dist(feat, f_avg, n_e)
  return sum / len(feats)

def get_feats(p_in):
  feat_all = []

  n_cur = 0
  for line in open(p_in):
    n_cur += 1
    if n_cur == 1:
      continue

    arr = line.strip().split(',')
    score, feat = arr[1], arr[2:]
 
    feat_float = [float(ele) for ele in feat]
    feat_all.append(feat_float)
 
  return feat_all

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 3:
    print '<usage> in divide'
    exit(-1)

  import gc
  gc.disable()

  feats = get_feats(sys.argv[1])  
  f_avg = get_average(feats)
  var = get_variable(feats, f_avg)

  print 1 / float(sys.argv[2]) / var

