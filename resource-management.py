import psutil
import time

period = input("بازه تکرار مورد نظر را به عدد وارد نمایید (چند بار تکرار بشه راضی میشی عزیزم ؟!) : ")
sleepTime = input("چند ثانیه تاخیر بین هر تکرار مد نظرته ؟ :) به عدد وارد کن ! (واحد:ثانیه) : ")

for i in range(int(period)):
    cpu_percent = psutil.cpu_percent(percpu=True)
    cpu_percent_total = psutil.cpu_percent()
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq().current
    mem_total = psutil.virtual_memory().total
    mem_used = psutil.virtual_memory().used
    mem_free = psutil.virtual_memory().available
    disk_usage = psutil.disk_usage('/')

    log = {
        'cpu percent': cpu_percent,
        'cpu percent (total)': cpu_percent_total,
        'cpu count': cpu_count,
        'cpu frequency': cpu_freq,
        'memory total': mem_total,
        'memory used': mem_used,
        'memory free': mem_free,
        'disk usage': {
            'total': disk_usage.total,
            'used': disk_usage.used,
            'free': disk_usage.free
        }
    }
    print(log)
    time.sleep(int(sleepTime))

