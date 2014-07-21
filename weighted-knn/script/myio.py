def read_svm_train(p_in):
  scores = []
  feats = []

  for line in open(p_in):
    arr = line.strip().split(' ')
    scores.append( float(arr[0]) )
    feat = {}
    for pair in arr[1:]:
      idx, value = pair.split(':')
      feat[int(idx)] = float(value) 

    feats.append(feat)
  return scores, feats

def get_fields(feats):
  fields = []
  for feat in feats:
    fields.append( set(feat.keys()) )
  return fields

def read_train(p_in):
  scores = []
  feats = []

  n_cur = 0
  for line in open(p_in):
    n_cur += 1
    if n_cur == 1:
      continue

    arr = line.strip().split(',')
    feat = [int(value) for value in arr[2:]]
    feats.append(feat)
    scores.append(float(arr[1]))
  return scores, feats

def read_test(p_in):
  feats = []

  n_cur = 0
  for line in open(p_in):
    n_cur += 1
    if n_cur == 1:
      continue

    arr = line.strip().split(',')
    feat = [int(value) for value in arr[1:]]

    feats.append(feat)
  return feats

def write_pred(scores, p_out):
  f_out = open(p_out, 'w')
  for score in scores:
    new_line = '%f\n' % score
    f_out.write(new_line)
  f_out.close()  

if __name__ == '__main__':
  import gc
  gc.disable()

  path_train = '../../data/dog.stdscore/record_1.txt'
  path_test = '../../data/dog.stdscore/validation_1.txt'
  
  print 'testing reading files'
  scores, features_train = read_train(path_train)
  features_test = read_test(path_test)
  print features_train[1][-11:]
  print features_test[1][-11:]
  print 'train:%d, test:%d, dimen:%d' % (len(features_train), len(features_test), len(features_train[0]))

