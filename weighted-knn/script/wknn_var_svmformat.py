import math
import myio
import mymath

def simple_metric(line_train, line_test, feat_variable):
  dist = 0.0
  num = 0

  for idx in range( len(line_train) ):
    a = line_train[idx]
    b = line_test[idx]

    if a == 'NaN' or b == 'NaN':
      continue
    if feat_variable[idx] <= 0.0000001:
      continue

    v_train = float(a)
    v_test = float(b)
    v_diff = v_train - v_test
    v_square = math.pow(v_diff, 2)
    v_final = v_square / feat_variable[idx]

    dist += v_final
    num += 1

  return dist / math.pow(num + 1, 0.5)


def get_KNN(line_test, features_train, feat_variable, k=3):
  dist_dict = {}

  for idx in range( len(features_train) ):
    dist_dict[idx] = simple_metric(features_train[idx], line_test, feat_variable)

  idx_list = sorted(dist_dict.items(), key = lambda d:d[1], reverse=False)
  return idx_list[:k], k


def predict_line(line_test, features_train, sales, feat_variable):
  idx_list, k = get_KNN(line_test, features_train, feat_variable)
  print 'neighbors:', idx_list 

  pred_list = []

  for i in range(12):
    sums = 0
    num = 0

    for idx, value in idx_list:
      if sales[idx][i] == 'NaN':
        continue

      sums += float(sales[idx][i])
      num += 1

    if num > 0:
      pred_list.append(sums / num) 
    else:
      pred_list.append(1000)

  return pred_list


def predict(features_train, features_test, scores_train):
  print 'start to predict...'

  n_test = len(features_test)
  n_dim = len(features_test[0])

  #feat_average = mymath.get_average(features_train)
  #feat_variable = mymath.get_variable(features_train, feat_average)
  feat_variable = [1] * n_dim

  scores_test = []

  for idx in range(n_test):
    print 'predict:', idx

    pred = predict_line(features_test[idx], features_train, scores_train, feat_variable)

    pred_list_str = [str(value) for value in pred_list]
    line = str(idx) + ',' + ','.join(pred_list_str)
    file_out.write(line + '\n')

  file_out.close()


if __name__ == '__main__':
  import sys
  if len(sys.argv) < 5:
    print '<usage> train test out K'
    exit(-1)

  scores_train, features_train = myio.read_train(sys.argv[1])
  features_test = myio.read_test(sys.argv[2])

  print 'd of train', len(features_train[0])
  print 'd of test', len(features_test[1])

  scores_test = predict(features_train, features_test, scores_train)



