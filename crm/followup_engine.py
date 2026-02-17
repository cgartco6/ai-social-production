from ai.llm_engine import generate_text

def generate_followup(name):
    return generate_text(f"Create professional sales follow-up for {name}")
