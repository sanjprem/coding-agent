import re
from pathlib import Path

def validate_path(path):
    allowed_base = Path("C:/Users/sanjp/Voyage/Organizations")
    try:
        full_path = Path(path).resolve()
        return allowed_base in full_path.parents
    except:
        return False

def sanitize_input(text):
    return re.sub(r'[^a-zA-Z0-9_\-/. ]', '', text)