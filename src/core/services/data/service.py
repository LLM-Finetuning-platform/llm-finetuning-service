from src.core.modules.data.sources import minio_local, s3
from config.settings.dataset import DatasetConfig

class DataService:
    def __init__(self,config: DatasetConfig):
        self.config = config
        try:
            self.service = self._service()
        except Exception as e:
            raise e
    def _service(self):
        if self.config.type.value:
           try:
               return s3.S3(self.config)
           except Exception as e:
               raise e
        try:
            return minio_local.MiniIOLocal(self.config)
        except Exception as e:
            raise e

    @property
    def dataService(self):
        try:
            return self.service
        except Exception as e:
            raise e