import concurrent.futures
import sys
import math
import time
import os
from decimal import Decimal, getcontext
from argument_parser import ArgumentParser
from general_utils import get_commands_arguments_dict
import multiprocessing as mp
from functools import reduce
from operator import mul


def factorial(start, end):
    start = start if start > 0 else 1
    fact = Decimal(reduce(mul, range(start, (end + 1)), 1))
    return fact


def calculate_euler_number_with_precision(start_idx, end_idx, d):
    sum = Decimal(0)
    print(f'Starting execution of [{start_idx},{end_idx}] by process {os.getpid()}')
    for k in range(start_idx,end_idx+1):
        print(f'Executing process {os.getpid()} for index {k}')
        max_computed_value = max(key for key in d.keys() if key <= 2*k)
        d[2 * k] = d[max_computed_value]*factorial(max_computed_value + 1, 2*k)
        next_sum = Decimal(2*k + 1) / Decimal(d[2*k])
        sum = sum + next_sum
    return sum


def _helper(partial_sum_arguments):
    return calculate_euler_number_with_precision(partial_sum_arguments[0], partial_sum_arguments[1], partial_sum_arguments[2])


def parrale_sum(n, num_processes, granularity, quiet_output=False):
    delimeter = num_processes*granularity
    step = math.ceil(n / delimeter)
    with mp.Manager() as manager:
        d = manager.dict()
        d[1] = 1
        #Adding the shared dict to every partial interval
        parts = [[start+1, start+step, d] for start in range(0, n, step)]
        parts[-1] = [parts[-1][0], n, d]
        with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
            partial_sums = executor.map(_helper, parts)
    return Decimal(1) + sum(partial_sums)


if __name__ == '__main__':
    commands_dict = get_commands_arguments_dict(sys.argv)
    commands = ArgumentParser(**commands_dict)
    getcontext().prec = commands.precision
    start = time.perf_counter()
    res = parrale_sum(commands.precision, commands.num_processors, commands.granularity, commands.quiet_output)
    end = time.perf_counter()
    print(f'Time took for execution {int((end - start)*1000)}ms with '
          f'{commands.num_processors} processors and granularity {commands.granularity}')
