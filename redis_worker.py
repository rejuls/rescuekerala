import os

import redis
from rq import Worker, Queue, Connection


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'floodrelief.settings')
redis_url = os.environ.get("REDIS_URL", "redis://localhost:6379")

listen = ["high", "default", "low", "smsjob", "bulkcsvjob","volunteergroup"]
conn = redis.from_url(redis_url)


if __name__ == "__main__":
    import django
    django.setup()
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
