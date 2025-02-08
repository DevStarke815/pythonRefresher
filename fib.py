# fib.py

@lru_cache
@timer
def fib(n: int) -> int:
    ...

if __name__ == "__main__":
    fib(100)
