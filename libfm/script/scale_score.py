def write_to_file(p_in, p_out, scale):
  f_out = open(p_out, 'w')

  for line in open(p_in):
    arr = line.strip().split(' ')
    old_score = float(arr[0])
    new_score = old_score * scale
    arr[0] = str(new_score)
    new_line = ' '.join(arr) + '\n'
    f_out.write(new_line)
  f_out.close() 

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 4:
    print '<usage> in out scale'
    exit(-1)

  import gc
  gc.disable()

  scale = int(sys.argv[3])
  write_to_file(sys.argv[1], sys.argv[2], scale)

