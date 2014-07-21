def get_head_train(line):
  arr = line.strip().split(',')[2:]
  #head = [ele.split('_')[1] for ele in arr]
  head = [str(i+1) for i in range(len(arr))]
  return head
  
def trans_train(p_in, p_out):
  f_out = open(p_out, 'w')

  n_cur = 0
  for line in open(p_in):
    n_cur += 1
    if n_cur == 1:
      head = get_head_train(line)
      continue

    arr = line.strip().split(',')
    score, values = arr[1], arr[2:]
    
    feat = []
    for i in range(len(values)):
      if float(values[i]) != 0:
        feat.append(head[i] + ':' + values[i]) 

    new_line = score + ' ' + ' '.join(feat) + '\n'
    f_out.write(new_line)
  
  f_out.close()

def get_head_test(line):
  arr = line.strip().split(',')[1:]
  #head = [ele.split('_')[1] for ele in arr]
  head = [str(i+1) for i in range(len(arr))]
  return head
  
def trans_test(p_in, p_out):
  f_out = open(p_out, 'w')

  n_cur = 0
  for line in open(p_in):
    n_cur += 1
    if n_cur == 1:
      head = get_head_test(line)
      continue

    arr = line.strip().split(',')
    score, values = '0', arr[1:]
    
    feat = []
    for i in range(len(values)):
      if float(values[i]) != 0:
        feat.append(head[i] + ':' + values[i]) 

    new_line = score + ' ' + ' '.join(feat) + '\n'
    f_out.write(new_line)
  
  f_out.close()

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 4:
    print '<usage> in out train/test'
    exit(-1)

  if sys.argv[3] == 'train':
    trans_train(sys.argv[1], sys.argv[2])
  else:
    trans_test(sys.argv[1], sys.argv[2])

