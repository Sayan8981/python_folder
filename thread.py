import queue
import threading
import time

item = [34,5,4,6,3,126,2,3,4,5,5,6,6,7,342,7,231,7,78,121,43,1,3,3,3,45,3,5,643,75,865,5,375,6,7,578,76]
print (len(item))

def test(item_part):
    count = 0
    count += 1
    #item[thread_no_start:thread_no_end]
    print (f'{item_part}')
    print (f'{count}')
    q.task_done()
    
def func(q, thread_no_end, thread_no_start):
    while not q.empty():
        task = q.get()
        if task is None:
            break
        time.sleep(2)
        if thread_no_start < 0:
            thread_no_start = 0
        print(f'Thread #{thread_no_start,thread_no_end} is doing task in the queue.')
        test(item[thread_no_start:thread_no_end])

        #return item[thread_no_start:thread_no_end]

q = queue.Queue()
gap  = 5
for i in range(len(item),0,-gap):
    print (i)
    worker = threading.Thread(target=func, args=(q,i,i-gap), daemon = True)
    q.put(worker)
    worker.start()
    
q.join()