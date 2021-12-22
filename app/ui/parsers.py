import re
from typing import List

_CHILD_IDS_LIST_PATTERN = re.compile(r"\d+")


def parse_child_ids_list(text: str) -> List[int]:
    return [int(x) for x in _CHILD_IDS_LIST_PATTERN.findall(text)]
