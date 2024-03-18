from typing import Any, Dict
from foundry._errors.helpers import format_error_message


class PalantirRPCException(Exception):
    def __init__(self, error_metadata: Dict[str, Any]):
        super().__init__(format_error_message(error_metadata))
        self.name: str = error_metadata["errorName"]
        self.parameters: Dict[str, Any] = error_metadata["parameters"]
        self.error_instance_id: str = error_metadata["errorInstanceId"]
