from tasks import add, append, xsum
from celery import chord, group

print("HERE")
res = chord((add.s(i, i) for i in range(10)), xsum.s())()
print(res.get())
res = group(add.s(i, i) for i in range(10))()
print(res.get())
res = chord(add.s(x,x) for x in range(7))(append.si('complete and '), interval=1)
print(res.get())
