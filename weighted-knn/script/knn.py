import math
import myio
import mymath

def euclidean_dist(line_train, line_test):
  dist = 0.0

  for idx in range( len(line_train) ):
    v_train = line_train[idx]
    v_test = line_test[idx]
    v_diff = v_train - v_test
    v_square = math.pow(v_diff, 2)
    dist += v_square
  return dist


def get_KNN(line_test, features_train, K=3):
  dist_dict = {}

  for idx in range( len(features_train) ):
    dist_dict[idx] = euclidean_dist(features_train[idx], line_test)

  idx_list = sorted(dist_dict.items(), key = lambda d:d[1], reverse=False)
  idxs = [id for id, value in idx_list[:K]]
  return idxs


def predict_line(line_test, features_train, scores_train, K):
  idx_list = get_KNN(line_test, features_train, K)
  print 'neighbors:', idx_list 

  sum = 0
  for i in range(len(idx_list)):
    sum += scores_train[idx_list[i]]  

  return sum / len(idx_list) 


def predict(features_train, features_test, scores_train, K=3):
  print 'start to predict...'

  n_test = len(features_test)
  n_dim = len(features_test[0])

  scores_test = []

  for idx in range(n_test):
    print 'predict:', idx

    pred = predict_line(features_test[idx], features_train, scores_train, K)

    scores_test.append(pred)
  return scores_test

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 5:
    print '<usage> train test out K'
    exit(-1)

  import gc
  gc.disable()

  scores_train, features_train = myio.read_train(sys.argv[1])
  print 'n of train', len(features_train)
  print 'd of train', len(features_train[0])
  features_test = myio.read_test(sys.argv[2])
  print 'n of test', len(features_test)
  print 'd of test', len(features_test[1])

  scores_test = predict(features_train, features_test, scores_train, int(sys.argv[4]))

  myio.write_pred(scores_test, sys.argv[3])


