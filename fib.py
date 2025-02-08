# fib.py
from functools import lru_cache
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() #init timer
        result = func(*args, **kwargs) #execute
        end_time = time.perf_counter() #end the timeR
        duration = end_time - start_time 
        print(f"Finished in {duration:.8f}s: f({args[0]}) -> {result}")
        return result
    return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n-2)

    ...

if __name__ == "__main__":
    fib(100)
