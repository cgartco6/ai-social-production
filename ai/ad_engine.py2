from social.meta_business import (
    create_campaign,
    create_adset,
    create_ad_creative,
    create_ad,
    activate_campaign
)
from ai.content_engine import generate_daily_content
from core.config import META_PAGE_ID

def launch_growth_ad():
    content = generate_daily_content()
    campaign = create_campaign("AI Growth Campaign")
    adset = create_adset(campaign["id"])
    creative = create_ad_creative(content, META_PAGE_ID)
    ad = create_ad(adset["id"], creative["id"])
    activate_campaign(campaign["id"])
    return ad
