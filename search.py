"""
1. Write a Python program search.py in which four processes search an array in parallel
(each process should get a fourth of the elements to search).

All the processes are searching the integer array for the element whose value is 11.

There is only one 11 in the entire array of 40,000 integers.

Before the searching begins ONLY the master process should read in the array elements from a data file
and distribute one fourth of the data to each of the other three processes and keep one fourth for its own search.

When one of the processes has found the element 11, 
it should notify all the other processes,
then print the index at which 11 was found (also include process rank in the output) and stop.

On receiving the notification the other processes should print out the index they are at that time
(include process rank in the output) and stop searching.

Login to your MPI master VM and download data file needed for this assignment as follows:
wget http://www.cs.utsa.edu/~plama/CS5573/data
"""

from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

NUMBER = 11
DTYPE = np.int64
filepath = "data"

# Only Rank 0 can read the data
if rank == 0:
    data = np.loadtxt(filepath, dtype=DTYPE)
    # data = np.array([i for i in range(size*1000000)])

    recv_shape = data.size // size
    send_buf = np.reshape(data, (size, recv_shape))
else:
    recv_shape = None
    send_buf = None

# Let each process know receive buffer size
recv_shape = comm.bcast(recv_shape, root=0)
recv_buf = np.empty(recv_shape, dtype=DTYPE)

# Divide data by number of process
comm.Scatter(send_buf, recv_buf)

# Non-blocking flag to notify other process that number is found
found = None
req = comm.irecv(found)

for index, value in enumerate(recv_buf):
    # Compare
    if value == NUMBER:
        # Notify other processors to stop
        for r in range(size):
            comm.isend(rank, dest=r)
        print(f"Rank {rank} found {NUMBER} at index: {index}, true index: {rank * recv_shape + index}")
        exit()
    # check if it has received any message without getting blocked
    elif req.Test() == True:
        print(f"Rank {rank} stop at index: {index}, true index: {rank * recv_shape + index}")
        exit()

print(f"Rank {rank} finish searching.")
