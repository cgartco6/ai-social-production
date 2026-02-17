from ai.llm_engine import generate_text
from ai.strategic_engine import get_brand_strategy

def generate_daily_content(brand="outback"):
    strategy = get_brand_strategy(brand)
    prompt = f"Create engaging social media post based on: {strategy}"
    return generate_text(prompt)
