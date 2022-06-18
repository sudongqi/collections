import random
from multiprocessing import Process, Queue
from bayes_opt import BayesianOptimization
from bayes_opt.util import UtilityFunction


class Worker(Process):
    def __init__(self, inp, out, f):
        super(Worker, self).__init__()
        self.inp = inp
        self.out = out
        self.f = f

    def run(self):
        print('Worker started')
        # do some initialization here
        while True:
            inp = self.inp.get()
            res = self.f(**inp)
            self.out.put({'params': inp, 'target': res})


def black_box_function(x, y):
    return -x ** 2 - (y - 1) ** 2 + 1


def search(f, best_res, bounds, max_attempt=200, num_workers=8, delta=0.0001):
    inp = Queue()
    out = Queue()

    uf = UtilityFunction(kind="ucb",
                         kappa=2.576,
                         kappa_decay=1,
                         kappa_decay_delay=0,
                         xi=0.0,
                         )
    optimizer = BayesianOptimization(pbounds=bounds, f=f)

    processes = []
    for i in range(num_workers):
        inp.put({k: random.uniform(*v) for k, v in bounds.items()})
        worker = Worker(inp=inp, out=out, f=f)
        worker.start()
        processes.append(worker)

    res = []
    curr_best_res = - float('inf')
    while len(res) < max_attempt:
        r = out.get()
        try:
            optimizer.register(**r)
        except KeyError:
            print('duplicated inputs')
        new_point = optimizer.suggest(uf)
        inp.put(new_point)
        res.append(r)
        print(r)
        if abs(best_res - r['target']) < delta:
            break
        curr_best_res = max(curr_best_res, r['target'])

    print('best = {}, took {} steps, {} step/worker'.format(
        curr_best_res,
        len(res),
        len(res) / num_workers
    ))

    for worker in processes:
        worker.terminate()


if __name__ == '__main__':
    search(
        f=black_box_function,
        best_res=-3,
        bounds={'x': (2, 4), 'y': (-3, 3)}
    )
