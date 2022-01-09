import multiprocessing as mp
import time
from multiprocessing import Value, Array
import numpy as np
import ctypes as c


def sleepy_man(n,i):
    #n = np.frombuffer(n.get_obj())
    n[i] += 1
    print('Starting to sleep')
    time.sleep(1)
    print('Done sleeping')
    

if __name__ == '__main__':
    
    n1 = np.zeros((5, 5), dtype=np.int32)
    shared_array = mp.Array(c.c_int32, n1.size, lock=False)
    n = np.ctypeslib.as_array(shared_array).reshape((5,5))
    tic = time.time()

    process_list = []
    for i in range(3):
        p =  mp.Process(target= sleepy_man, args = (n,i))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    toc = time.time()

    print(n[:])
    print('Done in {:.4f} seconds'.format(toc-tic))