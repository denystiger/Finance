import numpy as np

def linParts(numAtoms, numThreads):
    # partition of atoms with a single loop
    parts = np.linspace(0, numAtoms, min(numThreads, numAtoms)+1, dtype=int)
    return parts

def nestedParts(numAtoms, numThreads, upperTriang=False):
    # partition of atoms with an inner loop (e.g., quadratic load)
    parts = [0]
    numThreads_ = min(numThreads, numAtoms)

    for num in range(numThreads_):
        part = 1 + 4 * (parts[-1]**2 + parts[-1] + numAtoms * (numAtoms + 1.) / numThreads_)
        part = (-1 + part**0.5) / 2
        parts.append(part)

    parts = np.round(parts).astype(int)

    if upperTriang:
        # Reverse differences to mimic upper triangular load balancing
        parts = np.cumsum(np.diff(parts)[::-1])
        parts = np.append(np.array([0]), parts)

    return parts


import multiprocessing as mp

def processJobs(jobs, numThreads=24):
    """
    Process jobs in parallel using multiprocessing.
    :param jobs: A list of job dictionaries.
    :param numThreads: Number of worker processes.
    :return: List of results.
    """
    with mp.Pool(processes=numThreads) as pool:
        out = pool.map(worker, jobs)
    return out

# ✅ Replace this only in Jupyter
from multiprocessing.dummy import Pool as ThreadPool  # THREADS instead of processes

def processJobs(jobs, numThreads=24):
    """
    Process jobs in parallel using threads (Jupyter-compatible).
    :param jobs: A list of job dictionaries.
    :param numThreads: Number of threads.
    :return: List of results.
    """
    with ThreadPool(numThreads) as pool:
        out = pool.map(worker, jobs)
    return out

def worker(job):
    """
    Worker function to execute a job.
    :param job: A dictionary containing 'func' and its arguments.
    :return: Output of the func(**job).
    """
    func = job.pop('func')
    return func(**job)

import pandas as pd

def mpPandasObj(func, pdObj, numThreads=24, mpBatches=1, linMols=True, **kargs):
    """
    Parallelize a pandas job over multiple processes.

    :param func: Target function to apply; must return a DataFrame or Series.
    :param pdObj: Tuple (argName, atoms), where atoms will be partitioned.
    :param numThreads: Number of worker processes.
    :param mpBatches: Number of jobs per core.
    :param linMols: If True, use linear partitioning; else nested.
    :param kargs: Additional keyword args for func.
    :return: Concatenated result of all parallel jobs.
    """
    # Select partitioning method
    atoms = pdObj[1]
    argName = pdObj[0]
    totalJobs = numThreads * mpBatches
    parts = linParts(len(atoms), totalJobs) if linMols else nestedParts(len(atoms), totalJobs)

    # Create jobs
    jobs = []
    for i in range(1, len(parts)):
        job = {argName: atoms[parts[i-1]:parts[i]], 'func': func}
        job.update(kargs)
        jobs.append(job)

    # Execute
    if numThreads == 1:
        out = processJobs_(jobs)
    else:
        out = processJobs(jobs, numThreads=numThreads)

    # Concatenate output
    if isinstance(out[0], pd.DataFrame):
        result = pd.concat(out)
    elif isinstance(out[0], pd.Series):
        result = pd.concat(out)
    else:
        return out  # raw output (e.g. list of scalars)

    return result.sort_index()


