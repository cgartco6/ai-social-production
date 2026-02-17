from celery import Celery
from core.config import REDIS_URL

celery = Celery("ai_social", broker=REDIS_URL)
