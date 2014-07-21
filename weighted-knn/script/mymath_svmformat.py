import math

def euclidean_dist(line_test, field_test, line_train, field_train):
  dist = 0

  common_field = field_test.union(field_train) 
  for idx in common_field:
    v_test, v_train = 0, 0
    if idx in field_test:
      v_test = line_test[idx]
    if idx in field_train:
      v_train = line_train[idx]

    v_diff = v_test - v_train
    v_square = math.pow(v_diff, 2)
    dist += v_square
  return dist

def mahalanobis_dist(line_test, field_test, line_train, field_train, f_var):
  dist = 0

  common_field = field_test.union(field_train) 
  for idx in common_field:
    if f_var[idx] <= 0.00000001:
      continue

    v_test, v_train = 0, 0
    if idx in field_test:
      v_test = line_test[idx]
    if idx in field_train:
      v_train = line_train[idx]

    v_diff = v_test - v_train
    v_square = math.pow(v_diff, 2)
    dist += v_square / f_var[idx]
  return dist

def get_average(features_train, n_dim):
  f_avg = [0.0] * n_dim

  for feat in features_train:
    for idx in feat:
      f_avg[idx] += feat[idx] 
  
  n_feat = len(features_train)
  for idx in range(n_dim):
    f_avg[idx] /= n_feat 
  return f_avg

def get_variance(features_train, f_avg, n_dim):
  f_var = [0.0] * n_dim
  
  for feat in features_train:
    for idx in range(n_dim):
      v_train, v_avg = 0, f_avg[idx]
      if idx in feat:
        v_train = feat[idx]

      v_diff = v_train - v_avg
      f_var[idx] += math.pow( v_diff, 2 ) 
  
  n_feat = len(features_train)
  for idx in range(n_dim):
    f_var[idx] /= n_feat 
  return f_var
  

if __name__ == "__main__":
  f_train = []
  f1 = {1:1, 2:1, 4:2}
  f2 = {1:1, 2:2, 3:1}
  f_train.append(f1)
  f_train.append(f2)
  print 'f_train:', f_train

  f_avg = get_average(f_train, 5)
  f_var = get_variance(f_train, f_avg, 5)
  print 'f_avg:', f_avg
  print 'f_var:', f_var





 
