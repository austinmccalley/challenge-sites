# Make a dict with each value n and its fibonacci value
cache = {}

def fibonacci(n):
    if n not in cache.keys(): # If we do not know the result then add the result using other fibonacci function
        cache[n] = _fib(n) # Add the result to the cache
    return cache[n] # Return the cache of that value n


# General fibonacci function
def _fib(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

