# fib.py
from functools import lru_cache
import time
import matplotlib.pyplot as plt

timing_results = [] 

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() #init timer
        result = func(*args, **kwargs) #execute
        end_time = time.perf_counter() #end the timeR
        duration = end_time - start_time 
        timing_results.append((args[0], duration))
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
    
    #extract our x and y
    x_vals = [n for n, _ in timing_results]
    y_vals = [time for _, time in timing_results]

    #plot formatting
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, linestyle='-', color='b') 
    plt.title("Fibonacci Execution Time (fib(100))")
    plt.xlabel("Fibonacci n")
    plt.ylabel("Time (seconds)")
    plt.grid(True)

    plt.savefig("fib_timing_plot.png")
    print("Plot saved as 'fib_timing_plot.png'")