from workers.celery_app import celery
from ai.content_engine import generate_daily_content
from social.meta import post_facebook_instagram

@celery.task
def auto_post():
    content = generate_daily_content()
    post_facebook_instagram(content)
