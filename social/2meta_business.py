import requests
from core.config import META_ACCESS_TOKEN, META_AD_ACCOUNT_ID

GRAPH = "https://graph.facebook.com/v18.0"

def create_campaign(name):
    return requests.post(
        f"{GRAPH}/act_{META_AD_ACCOUNT_ID}/campaigns",
        data={
            "name": name,
            "objective": "ENGAGEMENT",
            "status": "PAUSED",
            "special_ad_categories": [],
            "access_token": META_ACCESS_TOKEN
        }
    ).json()

def create_adset(campaign_id):
    return requests.post(
        f"{GRAPH}/act_{META_AD_ACCOUNT_ID}/adsets",
        json={
            "name": "AI Adset",
            "campaign_id": campaign_id,
            "daily_budget": 5000,
            "billing_event": "IMPRESSIONS",
            "optimization_goal": "POST_ENGAGEMENT",
            "targeting": {"geo_locations": {"countries": ["ZA"]}},
            "status": "PAUSED",
            "access_token": META_ACCESS_TOKEN
        }
    ).json()

def create_ad_creative(message, page_id):
    return requests.post(
        f"{GRAPH}/act_{META_AD_ACCOUNT_ID}/adcreatives",
        json={
            "name": "AI Creative",
            "object_story_spec": {
                "page_id": page_id,
                "link_data": {
                    "message": message,
                    "link": "https://facebook.com"
                }
            },
            "access_token": META_ACCESS_TOKEN
        }
    ).json()

def create_ad(adset_id, creative_id):
    return requests.post(
        f"{GRAPH}/act_{META_AD_ACCOUNT_ID}/ads",
        json={
            "name": "AI Ad",
            "adset_id": adset_id,
            "creative": {"creative_id": creative_id},
            "status": "PAUSED",
            "access_token": META_ACCESS_TOKEN
        }
    ).json()

def activate_campaign(campaign_id):
    return requests.post(
        f"{GRAPH}/{campaign_id}",
        data={"status": "ACTIVE", "access_token": META_ACCESS_TOKEN}
    ).json()
