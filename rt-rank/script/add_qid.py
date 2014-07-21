def write_to_file(p_in, p_out):
  f_out = open(p_out, 'w')

  for line in open(p_in):
    arr = line.strip().split(' ')
    new_line = ' '.join(arr[0:1] + ['qid:1'] + arr[1:]) + '\n'
    f_out.write(new_line)
  f_out.close() 

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 3:
    print '<usage> in out'
    exit(-1)

  import gc
  gc.disable()

  write_to_file(sys.argv[1], sys.argv[2])

