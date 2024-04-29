# Implement `get_email` using `re` CPython library

def get_email(text):
    import re
    # Regular expression patterns
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        
    # Matching email addresses
    email_matches = re.findall(email_pattern, text)

    return email_matches[0]