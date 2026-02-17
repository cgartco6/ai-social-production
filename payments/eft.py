from core.config import EFT_BANK_NAME, EFT_ACCOUNT_NAME, EFT_ACCOUNT_NUMBER, EFT_BRANCH_CODE

def generate_eft_instructions(amount, reference):
    return {
        "bank": EFT_BANK_NAME,
        "account_name": EFT_ACCOUNT_NAME,
        "account_number": EFT_ACCOUNT_NUMBER,
        "branch_code": EFT_BRANCH_CODE,
        "amount": f"ZAR {amount}",
        "reference": reference
    }
