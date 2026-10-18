import ray
from abc import ABC, abstractmethod
from pydantic import AnyHttpUrl
from ray.data import Dataset
from typing import Optional
from config.settings.dataset import DatasetConfig
class IDataSet(ABC):
    def __init__(self, dataConfig: DatasetConfig, url:AnyHttpUrl):
        self.url = url
        self.config = dataConfig
        try:
            self.dataset = self._database()
        except Exception as e:
            raise e

    @abstractmethod
    def _format_adaptation_s3(self):
        """"""
    def _database(self) -> Optional[Dataset]:
        try:
            fs = self._format_adaptation_s3()
            return ray.data.read_parquet(paths=self.config.paths,filesystem=fs) 
        except Exception as e:
            raise e
    @property
    def data(self)->Optional[Dataset]:
        return self.dataset


