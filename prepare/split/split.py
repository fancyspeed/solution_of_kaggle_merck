def split(p_in, p_record, p_valid, p_truth):
  print p_in

  n_line = 0
  for line in open(p_in):
    if line:
      n_line += 1
  print n_line

  n_split = n_line * 4 / 5

  f_record = open(p_record, 'w')
  f_valid = open(p_valid, 'w')
  f_truth = open(p_truth, 'w')

  cur = 0
  for line in open(p_in):
    cur += 1
    if cur == 1:
      arr = line.strip().split(',')
      f_record.write(','.join(arr) + '\n')
      arr2 = arr[0:1] + arr[2:]
      f_valid.write(','.join(arr2) + '\n')
      continue
    if cur <= n_split:
      f_record.write(line)
    else:
      arr = line.strip().split(',')
      valid = arr[0:1] + arr[2:]
      arr[0] = '\"' + arr[0] + '\"'
      truth = arr[0:1] + arr[1:2]
      f_valid.write(','.join(valid) + '\n')
      f_truth.write(','.join(truth) + '\n')

  f_record.close()
  f_valid.close()
  f_truth.close()

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 5:
    print '<usage> in record validation groundtruth'
    exit(-1)

  split(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
