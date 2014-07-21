def parse_train_header(header_train):
  print 'start to parse header...'

  header_train_list_origin = header_train.strip().split(',')
  header_train_list = [str.strip('\"') for str in header_train_list_origin]

  feat_info = []
  for idx in range( len(header_train_list) ):
    header_class, header_num = header_train_list[idx].split('_')
    feat_info.append( (header_class, header_num) )

  return feat_info


def read_train(path_train):
  print 'start to read training file...'

  file_train = open(path_train)

  header_train = file_train.readline()
  feat_info = parse_train_header(header_train)[12:]

  sales = []
  features = []

  for line in file_train:
    arr = line.strip().split(',')
    sales.append(arr[0:12])
    features.append(arr[12:])

  file_train.close()
  print 'lines:', len(features)

  return features, sales, feat_info


def read_test(path_test):
  print 'start to read test file...'

  file_test = open(path_test)
  header_test = file_test.readline()

  features = {}

  for line in file_test:
    arr = line.strip().split(',')
    features[int(arr[0])] = arr[1:]

  file_test.close()
  print 'lines:', len(features)

  return features


def write_result(y_pred, path_sample, path_result):
  file_out = open(path_result, 'w')

  header_line = open(path_sample).readline()
  file_out.write(header_line)

  for idx in range( len(y_pred) ) :
    pred_list_str = [str(value) for value in y_pred[idx]]
    line = str(idx+1) + ',' + ','.join(pred_list_str)
    file_out.write(line + '\n')

  file_out.close()

def save_model(param, path_model):
  file_out = open(path_model, 'w')

  for i in range( len(param) ):
    line = ','.join([ str(e) for e in param[i] ])
    file_out.write(line + '\n')

  file_out.close()


if __name__ == '__main__':
  path_train = '../data/TrainingDataset.csv'
  path_test = '../data/TestDataset.csv'
  path_sample = '../result/sample_submission_using_training_column_means.csv'
  path_result = 'pred.csv'
  
  print 'testing reading files'
  features_train, sales, feat_info = read_train(path_train)
  features_test = read_test(path_test)
  print features_test[1]
  print 'train:%d, test:%d, dimen:%d' % (len(features_train), len(features_test), len(features_train[0]))

  print 'testing to write file'
  write_result([[1,2,5], [3,8,2]], path_sample, path_result)

  print 'testing to save model'
  save_model([[1,3],[4,8]], 'model.txt')
  

