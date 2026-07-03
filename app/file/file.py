import json
import os
import fcntl
from typing import Any
from datetime import datetime, timezone
from app.core.config import settings

class File:
    def __init__(self) -> None:
        self.file_path = settings.file_path
        directory = os.path.dirname(self.file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

    def save_to_file(self, data: Any) -> None:
        record = {
            "saved_at": datetime.now(timezone.utc).isoformat(),
            "data": data,
        }
        self._write_record(record)
        
    
    def _write_record(self, record:dict)->None:
        with open(self.file_path, "a", encoding="utf-8") as file:
            fcntl.flock(file, fcntl.LOCK_EX)
            try:
                file.write(json.dumps(record) + "\n")
                file.flush()
            finally:
                fcntl.flock(file, fcntl.LOCK_UN)
        return
    
