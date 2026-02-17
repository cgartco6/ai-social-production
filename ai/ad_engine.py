from ai.content_engine import generate_daily_content
from social.meta_business import (
    create_campaign,
    create_adset,
    create_ad_creative,
    create_ad,
    activate_campaign
)
from core.config import META_PAGE_ID

def launch_ai_ad():
    content = generate_daily_content()

    campaign = create_campaign("AI Growth Campaign")
    campaign_id = campaign.get("id")

    adset = create_adset(campaign_id)
    adset_id = adset.get("id")

    creative = create_ad_creative(content, META_PAGE_ID)
    creative_id = creative.get("id")

    ad = create_ad(adset_id, creative_id)
    activate_campaign(campaign_id)

    return {
        "campaign": campaign,
        "adset": adset,
        "creative": creative,
        "ad": ad
  }
