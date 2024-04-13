import time

def now_time():
  return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))