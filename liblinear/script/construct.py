def cons_test(p_valid, p_pred, p_out):
  f_out = open(p_out, 'w')

  f_pred = open(p_pred)

  n_cur = 0
  for line in open(p_valid):
    n_cur += 1
    if n_cur == 1:
      continue

    arr = line.strip().split(',')
    pred = f_pred.readline().strip()

    new_line = '\"' + arr[0] + '\"' + ',' + pred + '\n'
    f_out.write(new_line)
  
  f_out.close()

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 4:
    print '<usage> valid pred out'
    exit(-1)

  cons_test(sys.argv[1], sys.argv[2], sys.argv[3])
