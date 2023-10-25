import json
from typing import Dict

def read_json(filepath: str, **args) -> Dict:
    with open(filepath, **args) as f:
        return json.load(f)


def write_json(data: dict, filepath: str) -> None:
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, sort_keys=False, indent=4, ensure_ascii=False)
