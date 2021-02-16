# CC_assign1
## Use the following commands to run your MPI programs:
mpiexec -mca btl ^openib --hostfile mpihosts -n 4 --display-map python -m mpi4py search.py
mpiexec -mca btl ^openib --hostfile mpihosts -n 4 --display-map python -m mpi4py chain.py
mpiexec -mca btl ^openib --hostfile mpihosts -n 8 --display-map python -m mpi4py chain.py

## Assignment Submission Guidelines:
You must submit your work using Blackboard Learn and respect the following rules:
• Only 1 submission per group
• Submission must include the following :
    o source code files
    o a PDF report containing the following:
▪ List the group member names, and describe the contribution of each member.
▪ Show the results obtained by running the MPI programs in Q.1 and Q.2 Screenshots are recommended to show the program outputs. 

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


### <!-- blocking: send/recv -->
comm.send(0, dest=r, tag=11)
comm.recv(source=MPI.ANY_SOURCE, tag=11)

### <!-- non-blocking: isend/irecv -->
comm.isend(0, dest=r, tag=11)
req = comm.irecv(source=MPI.ANY_SOURCE, tag=11)
if(req.Test() == True): # check if it has received any message without getting blocked
    print ("received msg")

### <!-- Collective Communication: broadcast -->
comm.bcast(data, root=0)

### <!-- Collective Communication: scatter -->
comm.scatter(data, root=0)

### <!-- Collective Communication: gather -->
comm.Barrier()
comm.gather(data, root=0)

### <!-- Collective Communication: reduce -->
comm.reduce(data, op=MPI.SUM root=0)

MPI MAX, MPI MIN: maximum and minimum
MPI MAXLOC, MPI MINLOC: maximum and minimum with corresponding array index
MPI SUM, MPI PROD: sum and product	
MPI LAND, MPI LOR: logical AND and OR
MPI BAND, MPI BOR: bitwise AND and OR

### <!-- NUMPY -->
comm.Recv([data, MPI>INT], source=MPI.ANY_SOURCE, tag=11)
comm.Send([data, MPI>INT], dest=r, tag=11)
comm.Scatter(sendbuf, recvbuf, root=0)
