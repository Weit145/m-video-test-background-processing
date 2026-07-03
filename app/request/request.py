import logging
from typing import Any
import time
import requests
from app.core.config import settings
from app.file.file import File
logger = logging.getLogger(__name__)

class RequestWorker:
    def __init__(self) -> None:
        self.writer_file = File()
        self.session = requests.Session()

    def run(self)->None:
        timer = time.monotonic()
        while True:
            timer += settings.timer
            try:
                data = self._request()
                self.writer_file.save_to_file(data)
            except Exception as e:
                logger.error(f"Error: {e}")
            finally:
                sleep_time = max(0, timer - time.monotonic())
                time.sleep(sleep_time)

    
    def _request(self)->Any:
        params = {
            "page": 1,
            "page_size": 20
        }
        response = self.session.get(
                settings.url,
                params=params,
                timeout=5
            )
        response.raise_for_status()
        data = response.json()
        return data

worker_request = RequestWorker()
