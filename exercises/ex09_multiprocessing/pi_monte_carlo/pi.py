"""
pi.py - Example of Python multiprocessing.

Monte Carlo approximation of pi. Here's how it works:
1. Draw a square whose sides have length 2. Area of square = 4.
2. Inscribe a circle with diameter 2 within the square. Area of circle = pi.
3. Now start throwing darts randomly at the square.
If the dart hits are evenly distributed, the ratio of the number of hits inside
the circle to the total number of darts is equal to the ratio of the area of
the circle to the area of the square:
    (hits inside circle) / (number of throws) = pi / 4
4. Multiply both sides of the equation by 4 and you have the value of pi:
    4 * (hits / throws) = pi

The calculation is an example of an Embarrassingly Parallel problem, which
means that it's very easy to break the problem up into separate tasks. Tasks
don't need to coordinate or share data in any way, so there's no need for
inter-process communication, locking, etc. We like Embarrassingly Parallel
problems :)

Monte Carlo is not an efficient strategy. Even with 10**9 samples, the value
of pi produced is accurate only to 5 digits. But we'll keep the number of
samples small so it doesn't take too long to run.

Original version appeared in "Python High Performance Programming", by
Gabriele Lanaro.

This version has modifications to use the concurrent.futures module.
"""

from concurrent.futures import (
    ProcessPoolExecutor,
    ThreadPoolExecutor,
)
import concurrent.futures
import random

total_samples = 10**6  # total number of calculations


def calculate_one_sample():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    return 1 if x**2 + y**2 <= 1 else 0


# TODO: note the definition of the `pi_serial` method, which performs a
# calculation without using processes or threads. It calls
# calculate_one_sample() one million times and adds up all the return values.
# (no code change required)
def pi_serial():
    """Perform the Monte Carlo technique in a serial fashion"""
    hits = 0
    for _ in range(total_samples):
        hits += calculate_one_sample()
    # Or, if you prefer the compact generator expression syntax:
    # hits = sum(calculate_one_sample() for _ in range(total_samples))
    pi = 4.0 * hits/total_samples
    return pi


# TODO: note the definition of the `sample_multiple` method, which calls
# calculate_one_sample() 250,000 times and adds up all the return values.
# (no code change required)
def sample_multiple(chunk_size):
    hits = 0
    for _ in range(chunk_size):
        hits += calculate_one_sample()
    return hits
    # Or, generator expression equivalent:
    # return sum(calculate_one_sample() for _ in range(chunk_size))


# TODO: note the definition of the `pi_async` method. You'll define this method
# to call sample_multiple() with four parallel processes.
# (no code change required)
def pi_async():
    """
    Divide calculation into 4 chunks and create 4 processes to execute
    each chunk.
    """
    # ntasks = multiprocessing.cpu_count() # number of (virtual) CPU cores

    # TODO: note the definition of `chunk_size`. This will be the number of
    # calculations performed in each call to sample_multiple()
    # (no code change required)
    chunk_size = total_samples//4  # divide work into 4 chunks

    # TODO: define an empty set of Future instances named `futures`
    # HINT: see slide 9-46
    futures = ...

    # TODO: write a `with` statement to use a ProcessPoolExecutor.
    with ...
        # TODO: set up a `for` loop that executes 4 times.
        for ...
            # TODO: for each loop iteration, use a Process to execute
            # sample_multiple with the argument chunk_size.
            # Save the returned Future in a local variable.
            ...

            # TODO: add the returned Future to the `futures` set.
            ...

    # TODO: note the definition of `hits`
    # (no code change required)
    hits = 0

    # TODO: set up a `for` loop to get the result of each process as it
    # completes.
    # HINT: see slide 9-47
    # HINT: future.result() returns the result of the call to sample_multiple()
    for ...
        # TODO: add the process's result to `hits`
        hits += ...

    # TODO: note how the value of `hits` is used in the next statement
    # (no code change required)
    pi = 4.0 * hits/total_samples
    return pi


if __name__ == '__main__':
    print('pi_async() returned {}'.format(pi_async()))
    print('pi_serial() returned {}'.format(pi_serial()))

    # add calls to timeit here
