import queue
import threading
import time

class thread_test(object):
    
    item = [34,5,4,6,3,126,2,3,4,5,5,6,6,7,342,7,231,7,78,121,43,1,3,3,3,45,3,5,643,75,865,5,375,6,7,578,76]
    print (len(item))

    def test(self, item_part):
        count = 0
        count += 1
        print (f'{item_part}')
        print (f'{count}')
        self.q.task_done()
        
    def func(self, q, thread_no_start, thread_no_end):
        while not q.empty():
            task = q.get()
            if task is None:
                break
            time.sleep(2)
            if thread_no_start < 0:
                thread_no_start = 0
            print(f'Thread #{thread_no_start,thread_no_end} is doing task in the queue.')
            self.test(self.item[thread_no_start:thread_no_end])

    def run(self):
        self.q = queue.Queue()
        gap  = 5
        for i in range(0,len(self.item),gap):
            print (i)
            worker = threading.Thread(target=self.func, args=(self.q,i,i+gap), daemon = True)
            self.q.put(worker)
            worker.start()
            
        self.q.join()
        
if __name__ == '__main__':        
    thread_test().run()        