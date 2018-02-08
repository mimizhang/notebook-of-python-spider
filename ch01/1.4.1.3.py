# -*- coding: utf-8 -*-
# 1.4.1.3
#%%
from multiprocessing import Pool
import os
import time
import random


def run_task(name):
    print('Task %s (pid = %s) is running...' % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s end.' % name)


if __name__ == '__main__':
    print('Current process %s.' % os.getpid())
    p = Pool(processes=3)
    # for i in range(5):
    #     p.apply_async(run_task, args=(i,))
    p.map(run_task, range(8))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
