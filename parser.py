import re

def is_valid_metaurl(metaurl):
    # Define a regular expression pattern to match the format with or without trailing slash
    pattern = r'^(\d+(\.\d+)+/)*\d+(\.\d+)+/?$'
    
    # Use the re.match function to check if the string matches the pattern
    return bool(re.match(pattern, metaurl))

# Test cases
print(is_valid_metaurl('/3.4.4'))  # Valid
print(is_valid_metaurl('/3.4.4/'))  # Valid (with trailing slash)
print(is_valid_metaurl('/5.3.5/3.4.3'))  # Valid
print(is_valid_metaurl('/4.5.100/3.14.4/3.4.5'))  # Valid

# Invalid examples
print(is_valid_metaurl('/-3.4.4'))  # Invalid (negative integer)
print(is_valid_metaurl('/3.4.4/5.3.5/3.4.3'))  # Invalid (no trailing slash)
print(is_valid_metaurl('/3.4.4//3.4.4/'))  # Invalid (double slashes)
