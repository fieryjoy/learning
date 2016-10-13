import os
from celery import Celery, chord

BROKER_URL=os.environ['BROKER_URL']
app = Celery('hello', backend='rpc://', broker=BROKER_URL)

@app.task
def add(x,y):
    import time
    import random
    time.sleep(random.randint(0, 12))
    return x + y


@app.task
def append(a):
    return a + a


def test_chord():
    res = chord(add.s(x,x) for x in range(7))(append.si('complete and '), interval=1)
    return res

print(test_chord())
