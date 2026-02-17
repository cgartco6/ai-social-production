from core.database import SessionLocal, Lead

def capture_lead(name, email, source):
    db = SessionLocal()
    lead = Lead(name=name, email=email, source=source)
    db.add(lead)
    db.commit()
    db.close()
