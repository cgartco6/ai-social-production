from core.scheduler import start_scheduler
from ai.content_engine import generate_daily_content
from social.meta import post_facebook_instagram
from ai.ad_engine import launch_ai_ad

def run_cycle():
    content = generate_daily_content()
    post_id = post_facebook_instagram(content)
    launch_ai_ad()

if __name__ == "__main__":
    start_scheduler(run_cycle)
