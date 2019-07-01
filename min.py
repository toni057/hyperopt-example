#from numpy._distributor_init import NUMPY_MKL
# import time
from hyperopt import fmin, tpe, hp
from hyperopt.mongoexp import MongoTrials


def f(x):
    return x**2

trials = MongoTrials('mongo://localhost:1234/mongodbpath/jobs', exp_key='exp6')
best = fmin(f, hp.uniform('x', -2, 2), trials=trials, algo=tpe.suggest, max_evals=100)
