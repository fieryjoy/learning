from celery import Celery, Task

app = Celery()
app.config_from_object('celeryconf')


class DebugTask(Task):
    abstract = True

    def __call__(self, *args, **kwargs):
        print('TASK STARTING: {0.name}[{0.request.id}]'.format(self))
        return super(DebugTask, self).__call__(*args, **kwargs)


class Scheduler(object):
    def __init__(self, app):
        self.app = app


@app.task(base=DebugTask)
def add(x, y): return x + y

if __name__ == '__main__':
    app.worker_main()
