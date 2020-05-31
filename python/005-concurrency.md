
# `concurrent.futures.ThreadPoolExecutor`

```
from concurrent import futures

cc_list = ['a', 'b', 'c']
MAX_WORKERS = 10

workers = min(MAX_WORKERS, len(cc_list))  
with futures.ThreadPoolExecutor(workers) as executor:  
  res = executor.map(download_one, sorted(cc_list))  

return list(res)
```
- CPython interpreter has Global Interpreter Lock (GIL) which allows only one thread at a time to execute Python bytecodes. However, I/O operations release GIL so other threads can work concurrently. If there is an I/O opertion in `download_one` method CPU will switch to another thread in `ThreadPoolExecutor`.


# `as_completed`
```

from concurrent import futures

def download_one(a):
    print(a)
    return a +1

def download_many(cc_list):
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            results.append(res)

    return results

results = download_many([1,2,3])
print(results)

```
- will print something similar to this;

```
1
2
3
[4, 3, 2]
```

- `as_completed` prints the results of the thread when it is completed. So the order may change. But the future can be from another executor.

# `concurrent.futures.ProcessPoolExecutor`

- `ProcessPoolExecutor` has the same interface with `ThreadPoolExecutor` but `max_workers` is optional. The default value of `max_workers` is the number of CPU in OS `os.cpu_count()`.

- `ProcessPoolExecutor` bypasses the GIL. So, we can use several CPUs.
- Using `PyPy` Just-in-time compiler (JIT) instead of `CPython` interpreter also increase the performance for CPU-intensive work.
