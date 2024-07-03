import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    if cleaned_number.startswith('380') and len(cleaned_number) == 12:
        cleaned_number = '+' + cleaned_number
    
    if not cleaned_number.startswith('+'):
        cleaned_number = '+38' + cleaned_number
    
    return cleaned_number
