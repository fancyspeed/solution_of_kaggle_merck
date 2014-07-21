def get_head_train(line):
  arr = line.strip().split(',')[2:]
  #head = [ele.split('_')[1] for ele in arr]
  head = [str(i+1) for i in range(len(arr))]
  return head
  
def trans_train(p_in):
  n_cur = 0
  for line in open(p_in):
    n_cur += 1
    if n_cur == 1:
      head = get_head_train(line)
      print head[-1]

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2:
    print '<usage> in'
    exit(-1)

  trans_train(sys.argv[1])

