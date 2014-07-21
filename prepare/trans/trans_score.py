def get_average(scores):
  sum = 0
  for score in scores:
    sum += score
  return sum / len(scores) 

def euclidean_dist(f1, f2):
  v = f1 - f2
  return v * v

def get_variable(scores, f_avg):
  sum = 0
  for score in scores:
    sum += euclidean_dist(score, f_avg)
  return sum / len(scores)

def get_scores(p_in):
  score_all = []

  cur = 0
  for line in open(p_in):
    cur += 1
    if cur == 1:
      continue
    arr = line.strip().split(',')
    score_all.append(float(arr[1]))
 
  return score_all

def trans_score(scores, avg, stdvar):
  scores_new = []
  for score in scores:
    score_new = (score - avg) / stdvar
    scores_new.append(score_new)
  return scores_new

def write_to_file(p_in, scores, p_out):
  f_out = open(p_out, 'w')

  cur = 0
  for line in open(p_in):
    cur += 1
    if cur == 1:
      f_out.write(line)
      continue
    arr = line.strip().split(',')
    arr[1] = str(scores[cur-2])
    new_line = ','.join(arr) + '\n'
    f_out.write(new_line)

  f_out.close() 

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 3:
    print '<usage> in out'
    exit(-1)

  import gc
  gc.disable()

  import math

  scores = get_scores(sys.argv[1])  
  print scores[-10:]

  f_avg = get_average(scores)
  print f_avg

  var = get_variable(scores, f_avg)
  stdvar = math.sqrt(var) 
  print stdvar

  scores_new = trans_score(scores, f_avg, stdvar)
  print scores_new[-10:]

  write_to_file(sys.argv[1], scores_new, sys.argv[2])


