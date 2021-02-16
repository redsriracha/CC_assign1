"""
2. Write a Python program chain.py that takes data (an integer) from process zero and sends
it to all of the other processes as shown in the figure below.

That is, process i should receive the data and send it to process i+1, until the last process is reached.

Process zero will get the data from the user (standard input) in a loop until a negative value is provided by the user.

Each process should print the following:
    print ("Process %d got %d\n" % (rank, value))

Users should be able to run chain.py using any number of processes
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

while True:
    # 0 gets the input, Non-0 receive value
    if rank == 0:
        value = int(input())
    else:
        value = comm.recv(source=rank-1, tag=rank-1)
        print(f"Rank {rank} recv from {rank-1} with tag: {rank-1}")

    # Send to next in chain, unless last
    if rank < size-1:
        comm.send(value, dest=rank+1, tag=rank)
        print(f"Rank {rank} send to {rank+1} with tag: {rank}")

    if value < 0:
        break

    print("Process %d got %d\n" % (rank, value))
