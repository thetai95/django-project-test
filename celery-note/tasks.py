from celery import Celery
from time import sleep

app = Celery(
    'tasks',
    backend='redis://localhost',
    broker='redis://localhost:6379'
)


@app.task
def add(x, y):
    sleep(5)
    return x + y
