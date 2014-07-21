path_train = '../data/TrainingDataset.csv'
path_test = '../data/TestDataset.csv'

file_train = open(path_train)
file_test = open(path_test)

header_train = file_train.readline()
header_train_list_origin = header_train.strip().split(',')
header_train_list = [str.strip('\"') for str in header_train_list_origin]

feat_idx_train = {}
for idx in range(1, len(header_train_list)):
  header_class, header_num = header_train_list[idx].split('_')
  feat_idx_train[idx] = (header_class, header_num)

header_test = file_test.readline()
header_test_list_origin = header_test.strip().split(',')
header_test_list = [str.strip('\"') for str in header_test_list_origin]

feat_idx_test = {}
for idx in range(1, len(header_test_list)):
  header_class, header_num = header_test_list[idx].split('_')
  feat_idx_test[idx] = (header_class, header_num)

for idx in range(12, len(header_train_list)):
  if header_train_list[idx] != header_test_list[idx-11]:
    print idx, 'header not equal:', header_train_list[idx], header_test_list[idx-12]

file_test.close()
file_train.close()
