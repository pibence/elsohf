import numpy as np
import time
from timeit import default_timer as timer
from multiprocessing import Pool, cpu_count


def pi_approx(n: int):
    '''This function returns the number of coordinates which are 
    inside the circle for one quater.'''

    p = int()
    # random coordinate generation
    coord = np.random.rand(n, 2)
    
    # Check if the coordinates are inside the circle. if so, p is increased by 1
    for i in range(n):
        if (coord[i, 0]**2 + coord[i, 1]**2)**0.5 <= 1:
            p += 1
    return p
    


def main():
  '''This function calculates tue approximated value of pi.
  It calls the pi_approx function over all available cores 
  of the processor. Then sums the values and divides by the number
  of total generated numbers, then multiplies by 4 to form a whole circle''' 
    
    start = timer()
   
    # Creating a vector of the length of the cores
    core = cpu_count()
    n = 10000000 # given value of total random numbers generated. It can be modified.
    values = ([int(n / core)] * core)

    # Calling the function over all available cores
    with Pool() as pool:
        res = pool.map(pi_approx, values)
        print((sum(res) / n) * 4) # estimated value printed

    # Printing elapsed time
    end = timer()
    print(f'elapsed time: {end - start}')

if __name__ == '__main__':
    main()