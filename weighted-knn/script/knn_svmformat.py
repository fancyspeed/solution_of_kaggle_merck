import math
import myio
import mymath_svmformat as mymath

def get_KNN(line_test, field_test, features_train, fields_train, K):
  dist_dict = {}

  for idx in range( len(features_train) ):
    dist_dict[idx] = mymath.euclidean_dist(line_test, field_test, features_train[idx], fields_train[idx])

  idx_list = sorted(dist_dict.items(), key = lambda d:d[1], reverse=False)
  idxs = [id for id, value in idx_list[:K]]
  return idxs


def predict_line(line_test, field_test, features_train, fields_train, scores_train, K):
  idx_list = get_KNN(line_test, field_test, features_train, fields_train, K)
  print 'neighbors:', idx_list 

  sum = 0
  for i in range(len(idx_list)):
    sum += scores_train[idx_list[i]]  
  return sum / len(idx_list) 


def predict(features_train, fields_train, features_test, fields_test, scores_train, K=3):
  scores_test = []

  for idx in range( len(features_test) ):
    print 'predict:', idx
    pred = predict_line(features_test[idx], fields_test[idx], features_train, fields_train, scores_train, K)
    scores_test.append(pred)
  return scores_test

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 6:
    print '<usage> train test out NF K'
    exit(-1)

  import gc
  gc.disable()

  print 'loading train...'
  scores_train, features_train = myio.read_svm_train(sys.argv[1])
  fields_train = myio.get_fields(features_train)
  print 'done. n of train', len(features_train)

  print 'loading test...'
  scores_test, features_test = myio.read_svm_train(sys.argv[2])
  fields_test = myio.get_fields(features_test)
  print 'done. n of test', len(features_test)

  NF = int(sys.argv[4])
  print 'NF', NF
  K = int(sys.argv[5])
  print 'K', K

  print 'start to predict...'
  scores_test = predict(features_train, fields_train, features_test, fields_test, scores_train, K)
  print 'done.'

  myio.write_pred(scores_test, sys.argv[3])


