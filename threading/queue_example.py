import queue
import threading
import time

# !! ============================================================
# !! PRINT() ISNT THREADSAFE, BUT IT BREAKS ONLY A LITTLE HERE !!
# !! ============================================================

class Writer(threading.Thread):
	def __init__(self, name, q : queue.Queue):
		threading.Thread.__init__(self)
		self.name = name
		self.q = q

	def run(self):
		print(f"Output \n ** Starting the thread - {self.name}")
		for x in range(10):
			self.q.put(x)
			time.sleep(x/10)
			print(f"wrote {x}")
		print(f" ** Completed the thread - {self.name}")

class Reader(threading.Thread):
	def __init__(self, name, q : queue.Queue):
		threading.Thread.__init__(self)
		self.name = name
		self.q = q
		self.active = 1

	def run(self):
		print(f"Output \n ** Starting the thread - {self.name}")
		while self.active:
			try:
				val = self.q.get(block=True, timeout=0.45)
				print(f"read {val}")
			except queue.Empty:
				print("read empty queue")
		print(f" ** Completed the thread - {self.name}")


# fill the queue
qu = queue.Queue()
thread1 = Writer('First', qu)
thread2 = Reader('Second', qu)

# Start the threads
thread1.start()
thread2.start()

# Join the threads
thread1.join()
thread2.active = 0
thread2.join()