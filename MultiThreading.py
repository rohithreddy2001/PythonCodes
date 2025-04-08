import time
import threading

from collections import deque
class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

pq = Queue()
def place_order(orders):
    for order in orders:
        pq.enqueue(order)
        print(f"Order Placed: {order}")
        time.sleep(0.5)

def serve_orders():
    time.sleep(1)
    while not pq.is_empty():
        order = pq.dequeue()
        print(f"Order Serving: {order}")
        time.sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']

t = time.time()

po_thread = threading.Thread(target=place_order, args=(orders, ))
so_thread = threading.Thread(target=serve_orders)

po_thread.start()
so_thread.start()

po_thread.join()
so_thread.join()

print(pq.buffer)

print(f"Time taken to execute: {round(time.time() - t, 4)}")
print("Hah... I am done with all the orders!")


# def calc_square(numbers):
#     # print("calculate square numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print('square:',n**2)
#
# def calc_cube(numbers):
#     # print("calculate cube of numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print('cube:',n**3)
#
# arr = [2,3,8,9]
#
# t = time.time()
#
# t1= threading.Thread(target=calc_square, args=(arr,))
# t2= threading.Thread(target=calc_cube, args=(arr,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print("done in : ",time.time()-t)
# print("Hah... I am done with all my work now!")