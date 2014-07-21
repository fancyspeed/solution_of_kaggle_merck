import math
import myio
import mymath_svmformat as mymath

class Weight_Knn():
  def __init__(self, NF, K, gamma):
    self.NF = NF
    self.K = K
    self.gamma = gamma

  def set_data(self, features_train, fields_train, features_test, fields_test, scores_train):
    self.features_train = features_train
    self.fields_train = fields_train
    self.features_test = features_test
    self.fields_test = fields_test
    self.scores_train = scores_train
    self.n_train = len(self.features_train)
    self.n_test = len(self.features_test)

  def get_KNN(self, idx_test): 
    dist_dict = {}
    for idx in range( self.n_train ):
      dist_dict[idx] = mymath.euclidean_dist(self.features_test[idx_test], self.fields_test[idx_test], self.features_train[idx], self.fields_train[idx])
    idx_list = sorted(dist_dict.items(), key = lambda d:d[1], reverse=False)

    neigh_pairs, tot_value = [], 0
    for idx, value in idx_list[0:self.K]:
      new_value = math.exp(-self.gamma * value)
      neigh_pairs.append( (idx, new_value) )
      tot_value += new_value
    return neigh_pairs, tot_value

  def predict_line(self, idx_test):
    neigh_pairs, tot_value = self.get_KNN(idx_test)
    print 'neighbors:', neigh_pairs 
    sum = 0
    for idx, value in neigh_pairs:
      sum += self.scores_train[idx] * value 
    return sum / tot_value

  def predict(self):
    scores_test = []
    for idx_test in range( self.n_test ):
      print 'predict:', idx_test
      pred = self.predict_line(idx_test)
      scores_test.append(pred)
    return scores_test

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 7:
    print '<usage> train test out NF K gamma'
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
  gamma = float(sys.argv[6])
  print 'gamma', gamma

  wknn = Weight_Knn(NF, K, gamma)  
  wknn.set_data(features_train, fields_train, features_test, fields_test, scores_train)

  print 'start to predict...'
  scores_test = wknn.predict()
  print 'done.'

  myio.write_pred(scores_test, sys.argv[3])


