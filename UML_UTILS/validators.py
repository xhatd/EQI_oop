# utils/validators.py

import re

def is_valid_name(name):
    """
    Validate that the name contains only alphanumeric characters and underscores,
    and is between 2 and 50 characters in length.
    
    Args:
        name (str): The name to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    if not (1 <= len(name) <= 50):
        return False
    
    # Check if name matches the regex pattern
    pattern = r'^[a-zA-Z0-9_]+$'
    return re.match(pattern, name) is not None
