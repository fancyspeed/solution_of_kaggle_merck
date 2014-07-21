import mymath
import myio

import random
import time
import math

def gradent(param, y, y_train, D_train, idx, ydx, cur_idx = -1):
    n_f_train = len(D_train[0])
    n_f_dimen = len(D_train[0][0])

    R_i = 0
    Z = 0

    M1 = []
    M2 = []
    for p in range( n_f_dimen ):
        M1.append(0)
        M2.append(0)

    for j in range( n_f_train ):
        if j == cur_idx: continue
        if y_train[j][ydx] == 'NaN': continue
        y_j = int(y_train[j][ydx])

        S_ij = 0
        for p in range( n_f_dimen ):
            S_ij += - param[p][ydx] * D_train[idx][j][p]

        S_ij = math.exp( S_ij )
        Z += S_ij
        R_i += y_j * S_ij

        for p in range( n_f_dimen ):
            tmp = - S_ij * D_train[idx][j][p]
            M1[p] += y_j * tmp 
            M2[p] += tmp 

    R_i /= Z

    L_i = math.log(y + 1.0) - math.log(R_i + 1.0) 

    grad = []
    tmp = -2 * L_i / (R_i + 1) / Z
    for p in range( n_f_dimen ):
        G_p = ( M1[p] - M2[p] * R_i ) * tmp
        grad.append(G_p)

    loss = L_i * L_i

    return loss, grad, R_i


def update(grad, param, ydx, alpha):
    for p in range(len(param)):
        param[p][ydx] += - alpha * grad[p]


def train(param, y_train, D_train, alpha):
    sum_loss = 0
    n_line = 0

    n_f_train = len(D_train)
    n_y_train = len(y_train[0])

    for idx in range( n_f_train ):
        for ydx in range( n_y_train ):
            if y_train[idx][ydx] == 'NaN': continue
            y = int(y_train[idx][ydx])

            loss, grad, R_i = gradent(param, y, y_train, D_train, idx, ydx, idx)
            update(grad, param, ydx, alpha)

            sum_loss += loss
            n_line += 1

    return math.sqrt(sum_loss / n_line)


def validation(param, y_train, y_valid, D_valid):
    sum_loss = 0
    n_line = 0

    n_f_valid = len(D_valid)
    n_y_valid = len(y_valid[0])

    for idx in range( n_f_valid ):
        for ydx in range( n_y_valid ):
            if y_valid[idx][ydx] == 'NaN': continue
            y = int(y_valid[idx][ydx])

            loss, grad, R_i = gradent(param, y, y_train, D_valid, idx, ydx, -1)

            sum_loss += loss
            n_line += 1

    return math.sqrt(sum_loss / n_line)


def predict(param, y_train, D_test):
    n_f_test = len(D_test)
    n_y_train = len(y_train[0])

    y_pred = []

    for idx in range( n_f_test ):
        Y = []

        for ydx in range( n_y_train ):
            y = 100
            loss, grad, R_i = gradent(param, y, y_train, D_test, idx, ydx, -1)
            Y.append(R_i)

        y_pred.append(Y)

    return y_pred

  
def SGD(param, y_train, D_train, y_valid, D_valid, alpha, max_iter, epsilon): 
    print 'start sgd, alpha:%f, max iter:%d, epsilon:%f' % (alpha, max_iter, epsilon)

    last_valid = validation(param, y_train, y_valid, D_valid)
    print 'validation:', last_valid, 'time:', int(time.time())

    i_iter = 0
    while i_iter < max_iter:
        cur_train = train(param, y_train, D_train, alpha)
        cur_valid = validation(param, y_train, y_valid, D_valid)

        print 'iter:%d, train:%f, validation:%f, last:%f' % (i_iter, cur_train, cur_valid, last_valid), 'time:', int(time.time())

        if cur_valid + epsilon > last_valid:
            break
        last_valid = cur_valid
        i_iter += 1

    print 'sgd is finished'
    return param


def split_train(features, labels, train_ratio):
    n = len(features_train)

    f_train = [] 
    y_train = [] 
    f_valid = [] 
    y_valid = []

    for i in range(n):
        if random.random() < train_ratio:
            f_train.append(features[i])
            y_train.append(labels[i])
        else:
            f_valid.append(features[i])
            y_valid.append(labels[i])

    return f_train, y_train, f_valid, y_valid


if __name__ == '__main__':
    # disable garbage collector
    import gc
    gc.disable()

    from config import *

    import sys
    if len(sys.argv) >= 4:
        path_train = sys.argv[1]
        path_test = sys.argv[2]
        path_result = sys.argv[3]
    print 'training file:', path_train
    print 'test file:', path_test
    print 'result file:', path_result

    # read files
    features_train, sales, feat_info = myio.read_train(path_train)
    features_test = myio.read_test(path_test)

    print 'train:%d, test:%d, dimen:%d' % (len(features_train), len(features_test), len(features_train[0]))

    # split training data
    f_train, y_train, f_valid, y_valid = split_train(features_train, sales, train_ratio)

    # get variables and init parameters
    param = mymath.v_rand_2d( len(f_train[0]), len(y_train[0]), w_0 )

    f_avg = mymath.get_average(f_train)
    f_var = mymath.get_variable(f_train, f_avg)
    f_stdd = mymath.v_sqrt(f_var)

    D_train = mymath.calc_dist(f_train, f_train, f_stdd)
    D_valid = mymath.calc_dist(f_valid, f_train, f_stdd)

    print 'after init param and D_train, D_valid, time:', int(time.time())

    # stochastic gradent descent
    param = SGD(param, y_train, D_train, y_valid, D_valid, alpha, max_iter, epsilon) 

    # prediction
    f_test = []
    for idx in features_test:
        f_test.append(features_test[idx])

    D_test = mymath.calc_dist(f_test, features_train, f_stdd)
    y_pred = predict(param, sales, D_test)

    # write to file
    myio.write_result(y_pred, path_sample, path_result)
  

