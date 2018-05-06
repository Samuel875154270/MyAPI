import csv
import random
import threading
import time


def write_csv(i):
    if lock.acquire(True):
        count = random.randint(1, 5)
        time.sleep(count)
        with open("demo.csv", "a", newline="") as file:
            csv_obj = csv.writer(file)
            csv_obj.writerow([count, i])
        lock.release()


open("demo.csv", "w").close()
threads = []
lock = threading.Lock()
for i in range(20):
    print(i)
    th = threading.Thread(target=write_csv, args=(i, ))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()
