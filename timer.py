"""
Home grown timing tools for function calls.
Does Total Time, Best-of Time, and Best-of Total Time
"""

import time, sys
if sys.version_info[0] == 3 and sys.version_info[1] >= 3:
    timer = time.perf_counter   #or process time
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    :param reps:
    :param func:
    :param pargs:
    :param kargs:
    :return: total time, last results
    """
    repslist = list(range(reps))  #done to not include range in timer
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    :param reps:
    :param func:
    :param pargs:
    :param kargs:
    :return: best time , last results
    """
    best = 2 ** 32 #big number
    for i in range(reps):
        start = timer()
        ret = func(*pargs,**kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:
    best of reps1 runs of (total of reps2 runs of func
    :param reps1:
    :param reps2:
    :param func:
    :param pargs:
    :param kargs:
    :return: best ret
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)
