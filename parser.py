import re

def is_valid_metaurl(metaurl):
    # Define a regular expression pattern to match the format
    pattern = r'^/(-?\d+(\.\d+){2,3}/)+$'
    
    # Use the re.match function to check if the string matches the pattern
    return bool(re.match(pattern, metaurl))

# Test cases
print(is_valid_metaurl('/3.4.3/3.4.3/'))  # Valid
print(is_valid_metaurl('/-3.4.3/3.4.3/'))  # Valid
print(is_valid_metaurl('/3.4/3.4/'))  # Valid (two dots)
print(is_valid_metaurl('/3.4.3/3.4/'))  # Invalid (mismatched number of coordinates)
print(is_valid_metaurl('/3.4.3/3..4/'))  # Invalid (extra dot)
print(is_valid_metaurl('/3.4.3/3.4.3/4.5.6/'))  # Invalid (extra coordinate)
