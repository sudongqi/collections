import random
from multiprocessing import Process, Queue
from bayes_opt import BayesianOptimization
from bayes_opt.util import UtilityFunction


class Worker(Process):
    def __init__(self, inp, out, f, worker_id):
        super(Worker, self).__init__()
        self.worker_id = worker_id
        self.inp = inp
        self.out = out
        self.f = f

    def run(self):
        print('worker {} started'.format(self.worker_id))
        while True:
            inp = self.inp.get()
            res = self.f(**inp)
            self.out.put({'worker_id': self.worker_id, 'params': inp, 'target': res})


def serialize_dict(d):
    return ' '.join(map(str, d.values()))


def uniform_sample(bounds, explored):
    while True:
        d = {k: random.uniform(*v) for k, v in bounds.items()}
        d_key = serialize_dict(d)
        if d_key not in explored:
            explored.add(d_key)
            return d


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
    explored = set()

    processes = []
    for i in range(num_workers):
        inp.put(uniform_sample(bounds, explored))
        worker = Worker(inp=inp, out=out, f=f, worker_id=i)
        worker.start()
        processes.append(worker)

    res = []
    curr_best_res = -float('inf')
    while len(res) < max_attempt and abs(best_res - curr_best_res) > delta:
        r = out.get()
        try:
            optimizer.register(params=r['params'], target=r['target'])
            new_point = optimizer.suggest(uf)
            inp.put(new_point)
            explored.add(serialize_dict(new_point))
            res.append(r)
            curr_best_res = max(curr_best_res, r['target'])
            print(r)
        except:
            print('params={} failed ... trying a new random point'.format(r['params']))
            inp.put(uniform_sample(bounds, explored))

    print('best = {}, took {} steps, {} step/worker'.format(
        curr_best_res,
        len(res),
        len(res) / num_workers
    ))

    for worker in processes:
        worker.terminate()


def black_box_function(x, y):
    return -x ** 2 - (y - 1) ** 2 + 1


if __name__ == '__main__':
    search(
        f=black_box_function,
        best_res=-3,
        bounds={'x': (2, 4), 'y': (-3, 3)},
        num_workers=8
    )
