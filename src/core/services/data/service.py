from config.settings.dataset import DatasetConfig
from src.core.modules.data.sources import minio_local, s3


class DataService:
    def __init__(self,config: DatasetConfig):
            self.config = config
            self.service = self._service()
    def _service(self):
            if self.config.type.value:
               return s3.S3(self.config)
            return minio_local.MiniIOLocal(self.config)

    @property
    def dataService(self):
            return self.service