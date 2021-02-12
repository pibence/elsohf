def fibonacci(n: int, cache: list= [1, 1]):
    '''This function returns the nth element of the Fibonacci sequence.
    In order to make the runtime shorter it stores the already generated
    values of the sequence in the cache. If an element is requested that
    already exists in the sequence, it is just read out from the cache.'''
    
    if n <= len(cache):
        return cache[n-1]
    else:
        for i in range(len(cache)+1, n+1):
            cache.append(sum(cache[-2:]))
        return cache[n-1]
    
print(fibonacci(4))    
