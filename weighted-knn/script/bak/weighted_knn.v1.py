from knn import *
import random
import time

def init(len_f, len_y, mu0 = 0.001):
    param = []

    for i in range(len_f):
        pi = []
        for j in range(len_y):
            m = random.random() * mu0
            pi.append(m)
        param.append(pi)

    return param


def mahala_dist(f1, f2, f_var):
    if f_var <= 0.00000001:
        return 0
    if f1 == 'NaN' or f2 == 'NaN':
        return 0

    diff = float(f1) - float(f2)
    diff = diff * diff
    return math.sqrt( diff / f_var )


def gradent(param, f_var, f, y, f_train, y_train, ydx, cur_idx = -1):
    n_f_train = len(f_train)
    n_f_dimen = len(f_train[0])

    R_i = 0
    Z = 0

    M1 = []
    M2 = []
    for p in range(len(f_train[0])):
        M1.append(0)
        M2.append(0)

    for j in range( n_f_train ):
        if j == cur_idx: continue
        if y_train[j][ydx] == 'NaN': continue

        F_ij = []
        n_p = 0

        for p in range( n_f_dimen ):
            diff = mahala_dist(f[p], f_train[j][p], f_var[p])
            F_ij.append(diff)
            n_p += 1
        w_p = 1 / math.sqrt( n_p )

        S_ij = 0
        for p in range( n_f_dimen ):
            F_ij[p] *= - w_p * F_ij[p]
            S_ij += param[p][ydx] * F_ij[p]

        S_ij = math.exp( S_ij )
        Z += S_ij
        R_i += int(y_train[j][ydx]) * S_ij

        for p in range( n_f_dimen ):
            M1[p] += int(y_train[j][ydx]) * S_ij * F_ij[p]
            M2[p] += S_ij * F_ij[p]

    R_i /= Z

    loss = math.log(y + 1.0) - math.log(R_i + 1.0) 
    loss = loss * loss

    grad = []
    for p in range(n_f_dimen):
        G_p = M1[p] - M2[p] * R_i
        G_p /= Z
        grad.append(G_p)

    return loss, grad


def update(grad, param, ydx, alpha):
    for p in range(len(param)):
        param[p][ydx] += - alpha * grad[p]


def train(param, f_var, f_train, y_train, alpha):
    sum_loss = 0
    n_line = 0

    n_f_train = len(f_train)
    n_y_train = len(y_train[0])

    for idx in range( n_f_train ):
        f = f_train[idx]

        for ydx in range( n_y_train ):
            if y_train[idx][ydx] == 'NaN': continue
            y = int(y_train[idx][ydx])

            loss, grad = gradent(param, f_var, f, y, f_train, y_train, ydx, idx)
            update(grad, param, ydx, alpha)

            sum_loss += loss
            n_line += 1

            if n_line % 100 == 0:
                print 'loops:', n_line 

    return math.sqrt(sum_loss / n_line)


def validation(param, f_var, f_train, y_train, f_valid, y_valid):
    sum_loss = 0
    n_line = 0

    n_f_valid = len(f_valid)
    n_y_valid = len(y_valid[0])

    for idx in range( n_f_valid ):
        f = f_valid[idx]

        for ydx in range( n_y_valid ):
            if y_valid[idx][ydx] == 'NaN': continue
            y = int(y_valid[idx][ydx])

            loss, grad = gradent(param, f_var, f, y, f_train, y_train, ydx, -1)

            sum_loss += loss
            n_line += 1

            if n_line % 100 == 0:
                print 'loops:', n_line 

    return math.sqrt(sum_loss / n_line)


def SGD(param, f_var, f_train, y_train, f_valid, y_valid, alpha, max_iter, epsilon):
    print 'start sgd, alpha:%f, max iter:%d, epsilon:%f' % (alpha, max_iter, epsilon)

    last_valid = validation(param, f_var, f_train, y_train, f_valid, y_valid)
    print 'validation:', last_valid, 'time:', int(time.time())

    i_iter = 0
    while i_iter < max_iter:
        cur_train = train(param, f_var, f_train, y_train, alpha)
        cur_valid = validation(param, f_var, f_train, y_train, f_valid, y_valid)

        print 'iter:%d, train:%f, validation:%f, last:%f' % (i_iter, cur_train, cur_valid, last_valid), 'time:', int(time.time())

        if cur_valid + epsilon > last_valid:
            break
        last_valid = cur_valid
        i_iter += 1

    print 'sgd is finished'
    return param


if __name__ == '__main__':
    # disable garbage collector
    import gc
    gc.disable()

    # configure pathes 
    path_train = '../data/TrainingDataset.csv'
    path_test = '../data/TestDataset.csv'
    path_result = '../result/SGD01.csv'

    # read files
    features_train, sales, feat_info = read_train(path_train)
    features_test = read_test(path_test)

    # split training data
    n_train = 500

    f_train = features_train[:n_train]
    y_train = sales[:n_train]
    f_valid = features_train[n_train:]
    y_valid = sales[n_train:]

    # get variables and init parameters
    mu0 = 0.0001
    param = init(len(f_train[0]), len(y_train[0]), mu0)

    f_avg = get_average(f_train)
    f_var = get_variable(f_train, f_avg)

    # stochastic gradent descent
    alpha = 0.001
    max_iter = 1000
    epsilon = 0.0001

    param = SGD(param, f_var, f_train, y_train, f_valid, y_valid, alpha, max_iter, epsilon) 


