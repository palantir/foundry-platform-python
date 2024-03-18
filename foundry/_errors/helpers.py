import json
import requests
from importlib import import_module
from json import JSONDecodeError
from typing import Dict, Any


def format_error_message(fields: Dict[str, Any]) -> str:
    return json.dumps(fields, sort_keys=True, indent=4)
