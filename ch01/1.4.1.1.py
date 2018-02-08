# -*- coding: utf-8 -*-
# 1.4.1.1
#%%
import os
if __name__ == '__main__':
    print('current Process (%s) start ...' % (os.getpid()))
    pid = os.fork()
    if pid < 0:
        print('error in fork')
    elif pid == 0:
        print(
            f'I am child process({os.getpid()}) and my parent process is ({os.getppid()})')
    else:
        print(f'I({os.getpid()}) created a chlid process ({pid}).')
