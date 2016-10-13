from celery_app import app

@app.task
def add(x,y):
#    import time
#    import random
#    time.sleep(random.randint(0, 12))
    return x + y

@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def append(a):
    return a + a
