import re

_MOBILE_PHONE_PATTERN = re.compile(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")


def is_phone_number(text: str) -> bool:
    return bool(_MOBILE_PHONE_PATTERN.fullmatch(text))
