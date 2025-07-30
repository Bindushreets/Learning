#-------------------------------------------
''' 8 Steps of Using Multiprocessing :  '''
#-------------------------------------------

'''
    Multi Processing : In Python it is an advanced technique that can significantly enhance the 
                        performance of your applications, especially for CPU-bound tasks.
'''
#-----------------------------------------------
1. # Step 1: Know How To Create a New Process :
#-----------------------------------------------

''' 
# Ex :
            A new process named 'p' from the main process using 
            the 'Process' object from the multiprocessing module :

# Documentation :
            1.  os.getpid() method is used to get the ID of a process.
            2.  The start() method is to start the execution of the process.
                It can only be called once per process.
            3.  The join() method is to block the calling process 
                    until the specified process completes its execution.
                    Without it, the calling process might finish
                    before the child processes, especially in short-running programs.
'''

from multiprocessing import Process
import os

def print_square(num):
    print(f'Run Child process {os.getpid()}' ) 
        
    print(f"Square: {num * num}")


if __name__ == '__main__':
    print(f'Parent process {os.getpid()}')
    p = Process(target=print_square, args=(4,))
    p.start()
    
    p.join()

''' 
    Output :
            Parent process 6224
            Run Child process 24540
            Square: 16
'''
#---------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------
2. # Step 2: Execute Multiple Tasks in Parallel :
#--------------------------------------------------

'''
# Ex :
        Beginner v/s skilled person :
'''
#   Beginner code :

import time

def print_square(num):
    print(f"Square: {num * num}")
    time.sleep(1)  # Simulate a delay

if __name__ == "__main__":
    start_time = time.time()
    numbers = [1, 2, 3, 4]
    for num in numbers:
        print_square(num)
    print(f"Sequential Execution Time: {time.time() - start_time} seconds")

'''
    Beginner Output :
                    Square: 1
                    Square: 4
                    Square: 9
                    Square: 16
                    Sequential Execution Time: 4.013941526412964 seconds

    Here, we apply one second of sleeping to the print_square() function 
    to simulate a time-consuming operation, 
    so executing the function once will cost 1 second roughly.
    There are 4 times of executions, so the total time cost is roughly equal to 4 seconds.                    
'''

#   Skilled person code :

from multiprocessing import Process
import time


def print_square(num):
    print(f"Square: {num * num}")
    time.sleep(1)

if __name__ == "__main__":
    start_time = time.time()
    numbers = [1, 2, 3, 4]
    processes = []

    for num in numbers:
        process = Process(target=print_square, args=(num,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Multiprocessing Execution Time: {time.time() - start_time} seconds")

'''
    Skilled Person Output :
                            Square: 1
                            Square: 4
                            Square: 9
                            Square: 16
                            Multiprocessing Execution Time: 1.20697021484375 seconds

    by creating four processes and running the print_square() function in parallel,
    the total execution time of the program can be reduced to 1 second.
'''
#---------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------
3. # Step 3: Use 'Pool' To Simplify Processes Management :
#-----------------------------------------------------------

''' The Pool class : Provides a more convenient way to manage multiple processes for parallel execution. '''

from multiprocessing import Pool
import time


def square(num):
    print(f"Square: {num * num}")
    time.sleep(1)

if __name__ == "__main__":
    start_time = time.time()
    with Pool(4) as pool:
        pool.map(square, [1, 2, 3, 4])
    print(f"Multiprocessing Execution Time: {time.time() - start_time} seconds")

'''
    Output :
            Square: 1
            Square: 4
            Square: 9
            Square: 16
            Multiprocessing Execution Time: 1.4555706977844238 seconds

    Here, We avoided many for-loops with the help of Pool class.
    Keep  : We used the context manager (the 'with' statement) to create a multiprocessing pool.
            If we create a pool directly, we should always remember to close it.
'''

# Manage a pool without context managers :

from multiprocessing import Pool
import time


def square(num):
    print(f"Square: {num * num}")
    time.sleep(1)


if __name__ == "__main__":
    start_time = time.time()

    # Create a pool of 4 processes
    pool = Pool(4)
    pool.map(square, [1, 2, 3, 4])
    # Close the pool to prevent new tasks from being submitted
    pool.close()
    pool.join()

    print(f"Multiprocessing Execution Time: {time.time() - start_time} seconds")

'''
    output :
            Square: 1
            Square: 4
            Square: 9
            Square: 16
            Multiprocessing Execution Time: 1.1987957954406738 seconds
'''
#---------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------
4. # Step 4: Implement One-To-One Inter-Process Communication with Pipe :
#-------------------------------------------------------------------------

''' If two processes need to exchange messages,
    the 'Pipe' module is the right tool.
    It allows two processes to exchange data directly through a duplex communication channel.

    Ex :
    The below code demonstrates that a Pipe object connects two ends :
        the parent connection and the child connection.
            Both ends can:
                    1.Send data using the send() method.
                    2.Receive data using the recv() method.
        Data sent on one end of the Pipe is immediately available to the other end.
        With the help of the Pipe, two processes can communicate with each other easily.
'''

from multiprocessing import Process, Pipe

def sender(conn):
    conn.send("Developer is saying hai..., from Child Process") # Send a message through the child connection
    conn.close()                                                # Close the connection when done

def receiver(conn):
    message = conn.recv()                 # Receive the message on the parent connection
    print(f"Parent received: {message}")

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()      # Create the pipe

    sender_process = Process(target=sender, args=(child_conn,))
    receiver_process = Process(target=receiver, args=(parent_conn,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.join()

'''
    Output :
            Parent received: Developer is saying hai..., from Child Process
'''
#---------------------------------------------------------------------------------------------------------------------

'''
    Documentation on Pipe :
    
    1. Key features :

            1.  Simple and Lightweight : Compared to other inter-process communication(IPC) mechanisms,
                                        Pipe is straightforward and better suited for two-process communication.
            2.  Full-Duplex : Data can flow in both directions simultaneously.
            3.  Automatic Serialization: The Pipe automatically serializes Python objects 
                                        (using pickle) when sending messages.

    2.  How does IPC (Inter-Process Communication) work through a pipe? :
                Each process has its own memory space and processes don't share memory,
                    the pipe is not implemented by letting the two processes access the same variables.
                    so IPC work through a Pipe by using below steps.

                        1.  Separate Buffers :
                            Each end of the Pipe maintains its own buffer.
                            These buffers are part of the operating system's IPC mechanisms,
                            such as pipes, sockets, or similar constructs, depending on the platform.

                        2.  Serialization :
                            When one process calls send(data) on its end of the pipe,
                            the data is serialized 
                            (converted into a byte stream using pickle or a similar serialization mechanism).
                            This byte stream is written into the sending end's buffer.

                        3.  Transmission :
                            The serialized data is passed through the pipe's underlying mechanism
                            (e.g., system-level pipe or socket) to the receiving end's buffer.

                        4.  Deserialization :
                            When the other process calls recv(),
                            the data is read from its end of the pipe's buffer.
                            This data is then deserialized back into a Python object.

    3.  Conclude :  The data is copied from the sending process's memory to the pipe's buffer 
                    and then to the receiving process's memory.
                    Therefore, even if two processes do not share memory directly, the IPC can happen.

    4. Cons : A Pipe is limited to communication between two processes
                    (the two ends of the pipe).
'''
#---------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
5. # Step 5: Apply Data Sharing Between Processes using Multiprocessing 'Queue' :
#---------------------------------------------------------------------------------
''' 
Documentation on Queue : 
    1.  Definition :
        In Python's multiprocessing module,
            Queue is a process-safe FIFO (First In, First Out) data structure, 
            It is a smart choice instead of 'Pipe'.
            
    2. There are two key operations for a multiprocessing queue :
        1.  put(data): Adds data to the queue.
        2.  get(): Retrieves data from the queue.

    3.  It can handle multiple producers (processes that put data into the queue) 
            and multiple consumers (processes that get data from the queue) concurrently.
    
    4.  'multiprocessing.Queue' in Python differs significantly from the normal 
            (thread-based) queue provided by the 'queue.Queue' module.
    
    5.  The queue.Queue is limited to threads within a single process,
            it cannot be used for communication between processes.
    
    6.  'queue.Queue' :
        In a multiprocessing context, the data will not be accessible to other processes
        because processes do not share memory.
        Each process gets its own memory space, making 'queue.Queue' ineffective.
    
    7. Does the 'multiprocessing.Queue' let different processes share memory?
        No, 
            because under the hood, the multiprocessing.
            Queue is built on top of 'multiprocessing.Pipe' and 'semaphores'.
    
    8.  'semaphores' :
            It is a variable or abstract data type, 
                used to control access to a common resource by multiple threads 
                and avoid critical section problems in a concurrent system
                such as a multitasking operating system.
            Semaphores are a type of synchronization primitive.
                A trivial semaphore is a plain variable that is changed
                (for example, incremented or decremented, or toggled)
                depending on programmer-defined conditions.
'''
#---------------------------------------------------------------------------------------------------------------------
from multiprocessing import Process, Queue
import os

# task for writing process
def write(q):
    print(f'Writing Process ID: {os.getpid()}')
    for value in ['Manoj', 'Bindu', 'BMTechhy.']:
        print(f'Write {value} to the queue.' )
        q.put(value)

# task for reading process
def read(q):
    print(f'Reading Process ID: {os.getpid()}')
    while True:
        if q.empty():
            break
        else:
            value = q.get(True)
            print(f'Read {value} from the queue.')

if __name__=='__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # the process pw is to write data to Queue:
    pw.start()
    # the process pr is to read data from Queue:
    pr.start()

    pw.join()
    pr.join()

'''
    Output :
            Writing Process ID: 11504
            Write Manoj to the queue.
            Write Bindu to the queue.
            Write BMTechhy. to the queue.
            Reading Process ID: 24012
            Read Manoj from the queue.
            Read Bindu from the queue.
            Read BMTechhy. from the queue.
'''
#------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
6. # Step 6: Apply Stack-like Inter-Process Data Sharing with Multiprocessing Lists :
#--------------------------------------------------------------------------------------
'''
    Manager.list :
                1.  Provides a way for processes to share a stack-like object.
                2.  It does not share memory directly between processes either.
'''

from multiprocessing import Process, Manager

import os

# Task for the writing process
def write(stack):
    print(f"Writing Process ID: {os.getpid()}")
    for value in ['Manoj', 'Bindu', 'BMTechhy']:
        print(f"Pushing {value} onto the stack.")
        stack.append(value)

# Task for the reading process
def read(stack):
    print(f"Reading Process ID: {os.getpid()}")
    while True:
        if stack:  # Check if the stack has elements
            value = stack.pop()  # Pop from the stack
            print(f"Popped {value} from the stack.")
        else:
            break

if __name__ == '__main__':
    with Manager() as manager:
        stack = manager.list()  # Shared stack
        pw = Process(target=write, args=(stack,))
        pr = Process(target=read, args=(stack,))

        # Start the writing process
        pw.start()
        pw.join()  # Wait for writing to complete

        # Start the reading process
        pr.start()
        pr.join()  # Wait for reading to complete

'''
Output :
        Writing Process ID: 13304
        Pushing Manoj onto the stack.
        Pushing Bindu onto the stack.
        Pushing BMTechhy onto the stack.
        Reading Process ID: 6396
        Popped BMTechhy from the stack.
        Popped Bindu from the stack.
        Popped Manoj from the stack.
'''
#---------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------
7. # Step 7: How To Share Memory Across Processes :
#----------------------------------------------------
'''
    1.  By default, processes do not share memory.
            Each process operates in its own memory space for isolation and safety.
            It is a core concept of multiprocessing.
            However, the overhead of copying large amounts of data is not always acceptable.

    2.  Is there any way to break the default rule?
            Yes.
            Python provides explicit mechanisms to share memory between processes when needed.
            To list a few :
                1.  multiprocessing.shared_memory (Python 3.8+)
                2.  multiprocessing.Value
                3.  multiprocessing.Array

        But we should be very careful when using them,
        given that sharing memory could cause the 'race condition' issue.

    3.  How do we implement atomic-like operations in Python to avoid race conditions?
            lock the shared variable whenever one process is handling it.
    
    4.  multiple processes may read the same initial value before 
            any of them writes the updated value back.
            As a result, some increments are 'lost,'
            leading to a final value that is less than actual value.

    5.  An atomic operation :
            Which means directly editing the variable in the shared memory,
            the race condition wouldn't happen.
            Two atomic operations cannot happen at the exact same time on the same variable
            because the hardware or operating system ensures mutual exclusion.

    Ex : Using 'multiprocessing.Value' to share an integer variable in memory for four processes.
'''

from multiprocessing import Process, Value

def increment(shared_counter):
    for _ in range(1000):
        shared_counter.value += 1

if __name__ == "__main__":
    shared_counter = Value('i', 0)  # Shared integer variable

    processes = [Process(target=increment, args=(shared_counter,)) for _ in range(4)]

    for process in processes:
        process.start()
    for process in processes:
        process.join()

    print(f"Final Counter Value: {shared_counter.value}")

'''
    Outputs:
            Final Counter Value: 2482
            Final Counter Value: 4000
            Final Counter Value: 3903
'''

'''
    It's 2482 instead of 4000.
    Every time if you execute the above program, the result probably will be different.
    Because,it's about race conditions.
    
    The variable changing operation here is a non-atomic operation,
    it's a read-modify-write operation:
        1.  Read: The current value is read from shared memory into a local register.
        2.  Modify: The value is incremented in the local register.
        3.  Write: The modified value is written back to shared memory.

    Therefore, multiple processes may read the same initial value before 
        any of them writes the updated value back.
        As a result, some increments are 'lost,' leading to a final value that is less than 4000.

    If it's an atomic operation,
        which means directly editing the variable in the shared memory,
        the case condition wouldn't happen.
        Two atomic operations cannot happen at the exact same time on the same variable
        because the hardware or operating system ensures mutual exclusion.
'''
#---------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
8. # Step 8: Use 'Locks' To Avoid Race Conditions in Shared-Memory Multiprocessing :
#------------------------------------------------------------------------------------

from multiprocessing import Process, Value, Lock

def increment(shared_counter, lock):
    for _ in range(1000):
        with lock:  # Ensure safe updates
            shared_counter.value += 1

if __name__ == "__main__":
    shared_counter = Value('i', 0)
    lock = Lock()

    processes = [Process(target=increment, args=(shared_counter, lock)) for _ in range(4)]

    for process in processes:
        process.start()
    for process in processes:
        process.join()

    print(f"Final Counter Value: {shared_counter.value}")

'''
    Output :
            Final Counter Value: 4000
'''

'''
    Now, the output is always 4000 no matter when you run it.
         Because the 'shared_counter' was locked during each operation,
         no other processes can read its value within the locked period.
'''
#---------------------------------------------------------------------------------------------------------------------