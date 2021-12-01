import time
from statistics import mean

# from memory_profiler import memory_usage

# import psutil  # type: ignore
import tracemalloc

from typing import Callable


def trace_cpu(fn: Callable, iterations: int = 1):
    def wrapper(*args, **kwargs):
        times = []
        for _ in range(iterations):
            start_time = time.perf_counter_ns()
            ret = fn(*args, **kwargs)
            end_time = time.perf_counter_ns()

            total_nano = end_time - start_time
            times.append(total_nano)

        mean_nanos = int(mean(times))

        micro, nano = divmod(mean_nanos, 1000)
        milli, micro = divmod(micro, 1000)
        seconds, milli = divmod(milli, 1000)
        trace = (seconds, milli, micro, nano)

        return ret, trace

    return wrapper


def trace_mem(fn: Callable):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        tracemalloc.reset_peak()

        ret = fn(*args, **kwargs)
        _, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        # mem, ret = memory_usage((fn, args, kwargs), retval=True)
        # mem = [int(i * 1024 * 1024) for i in mem]
        # peak = max(mem)

        total_bytes = peak
        kbs, bs = divmod(total_bytes, 1024)
        mbs, kbs = divmod(kbs, 1024)
        trace = (mbs, kbs, bs)

        return ret, trace

    return wrapper


def benchmark(fn: Callable, iterations: int = 1):
    def wrapper(*args, **kwargs):
        cret, cpu_trace = trace_cpu(fn, iterations)(*args, **kwargs)
        _, mem_trace = trace_mem(fn)(*args, **kwargs)

        seconds, milli, micro, nano = cpu_trace
        cpu_info = f"{seconds}s {milli}ms {micro}μs {nano}ns"

        mbs, kbs, bs = mem_trace
        mem_info = f"{mbs}mb {kbs}kb {bs}b"

        print(f"{fn.__module__}.{fn.__qualname__:<10} \t {cpu_info} \t {mem_info}")

        return cret

    return wrapper
