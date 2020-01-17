"""
total(spam, 1, 2, a=3, b=4, _reps=1000) calls and times spam(1, 2, a=3, b=4)
_reps times, and returns total time for all run, with final result.

bestof(spam, 1, 2, a=3, b=4, _reps=5) run best-of-N timer to attempt to
filter out system load variation, and returns best of time among _reps tests.

bestoftotal(spam, 1, 2, a=3, b=4, _reps1=5, _reps=1000) runs best-of-totals
test, which takes the best among _reps1 runs of (the total -reps runs)

"""

import time, sys
if sys.version_info[0] == 3 and sys.version_info[1] >= 3:
    timer = time.perf_counter   #or process time
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(func, *pargs, **kargs):
    _reps = kargs.pop('_reps',1000) #passed-in or default to 1000
    repslist = list(range(_reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *pargs, **kargs):
    _reps = kargs.pop('_reps',5)
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(func, *pargs, **kargs):
    _reps1 = kargs.pop('_reps1',5)
    return min(total(func, *pargs, **kargs) for i in range(_reps1))

