"""

Same usage as timer2, but uses 3.X keyword only default arguments
instead of dict pops for simpler code.  No need to host range() out of
tests in 3.X: always a generator.  This is for 3.X

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

def total(func, *pargs, _reps=1000, **kargs):
    start = timer()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *pargs, _reps=5, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(func, *pargs, _reps1=5, **kargs):
    return min(total(func, *pargs, **kargs) for i in range(_reps1))

