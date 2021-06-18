
def mask_access_key(key: str) -> str:
    "Helper function to mask access key"

    key_length = len(key)
    prefix, postfix = 4, -2

    if key_length > 6:
        return f"{key[:prefix]}{'*'*len(key[prefix:postfix])}{key[postfix:]}"
    return f"{'*'*key_length}"
