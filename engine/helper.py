import re

# extract search term
def extract_yt_term(command):
    # Regular expression pattern to extract the search term
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Search for the pattern in the command 
    match = re.search(pattern, command, re.IGNORECASE)
    # Return the search term if found and None otherwise 
    return match.group(1) if match else None