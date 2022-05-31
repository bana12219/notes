"""Introduction

You're an IT administrator for a media production company that uses Network-Attached Storage (NAS) to store all data generated daily (e.g., videos, photos). One of your daily tasks is to back up the data in the production NAS (mounted at /data/prod on the server) to the backup NAS (mounted at /data/prod_backup on the server). A former member of the team developed a Python script (full path /scripts/dailysync.py) that backs up data daily. But recently, there's been a lot of data generated and the script isn't catching up to the speed. As a result, the backup process now takes more than 20 hours to finish, which isn't efficient at all for a daily backup.
What you'll do

    Identify what limits the system performance: I/O, Network, CPU, or Memory
    Use rsync command instead of cp to transfer data
    Get system standard output and manipulate the output
    Find differences between threading and multiprocessing
"""

"""
CPU bound

CPU bound means the program is bottlenecked by the CPU (Central Processing Unit). 
When your program is waiting for I/O (e.g., disk read/write, network read/write), 
CPU bound

CPU bound means the program is bottlenecked by the CPU (Central Processing Unit). 
When your program is waiting for I/O (e.g., disk read/write, network read/write), 
the CPU is free to do other tasks, even if your program is stopped. The speed of 
your program will mostly depend on how fast that I/O can happen; if you want to 
speed it up, you'll need to speed up the I/O. If your program is running lots of 
program instructions and not waiting for I/O, then it's CPU bound. Speeding up the 
CPU will make the program run faster.

In either case, the key to speeding up the program might not be to speed up the 
hardware but to optimize the program to reduce the amount of I/O or CPU it needs. 
Or you can have it do I/O while it also does CPU-intensive work. CPU bound implies 
that upgrading the CPU or optimizing code will improve the overall computing performance.
the CPU is free to do other tasks, even if your program is stopped. The speed of your 
program will mostly depend on how fast that I/O can happen; if you want to speed it up, 
you'll need to speed up the I/O. If your program is running lots of program instructions 
and not waiting for I/O, then it's CPU bound. Speeding up the CPU will make the program 
run faster.

In either case, the key to speeding up the program might not be to speed up the hardware 
but to optimize the program to reduce the amount of I/O or CPU it needs. Or you can have 
it do I/O while it also does CPU-intensive work. CPU bound implies that upgrading the CPU 
or optimizing code will improve the overall computing performance.
"""


sudo apt install python3-pip
pip3 install psutil
python3

import psutil
psutil.cpu_percent()
"""
This shows that CPU utilization is low. Here, you have a CPU with multiple cores; 
this means one fully loaded CPU thread/virtual core equals 1.2% of total load. 
So, it only uses one core of the CPU regardless of having multiple cores.

After checking CPU utilization, you noticed that they're not reaching the limit.

So, you check the CPU usage, and it looks like the script only uses a single core to run. 
But your server has a bunch of cores, which means the task is CPU-bound.

Now, using psutil.disk_io_counters() and psutil.net_io_counters() you'll get byte read 
and byte write for disk I/O and byte received and byte sent for the network I/O bandwidth.
 For checking disk I/O, you can use the following command:
"""
psutil.disk_io_counters()
psutil.net_io_counters()


"""
Basics rsync command

rsync(remote sync) is a utility for efficiently transferring and synchronizing files 
between a computer and an external hard drive and across networked computers by 
comparing the modification time and size of files. One of the important features of 
rsync is that it works on the delta transfer algorithm, which means it'll only sync 
or copy the changes from the source to the destination instead of copying the whole 
file. This ultimately reduces the amount of data sent over the network.

The basic syntax of the rsync command is below:
"""

"""
Basics rsync command

rsync(remote sync) is a utility for efficiently transferring and synchronizing files 
between a computer and an external hard drive and across networked computers by 
comparing the modification time and size of files. One of the important features of 
rsync is that it works on the delta transfer algorithm, which means it'll only sync or 
copy the changes from the source to the destination instead of copying the whole file. 
This ultimately reduces the amount of data sent over the network.

The basic syntax of the rsync command is below:
rsync [Options] [Source-Files-Dir] [Destination]

Some of the commonly used options in rsync command are listed below:

Options             Uses

-v              Verbose output
-q              Suppress message output
-a              Archive files and directory while synchronizing
-r              Sync files and directories recursively
-b              Take the backup during synchronization
-z              Compress file data during the transfer



"""

python3
import subprocess
src = "<source-path>" # replace <source-path> with the source directory
dest = "<destination-path>" # replace <destination-path> with the destination directory
subprocess.call(["rsync", "-arq", src, dest])



"""
Multiprocessing

Now, when you go through the hierarchy of the subfolders of /data/prod, 
data is from different projects (e.g., , beta, gamma, kappa) and they're 
independent of each other. So, in order to efficiently back up parallelly, 
use multiprocessing to take advantage of the idle CPU cores. Initially, 
because of CPU bound, the backup process takes more than 20 hours to finish, 
which isn't efficient for a daily backup. Now, by using multiprocessing, 
you can back up your data from the source to the destination parallelly by 
utilizing the multiple cores of the CPU.
"""
ls ~/scripts
