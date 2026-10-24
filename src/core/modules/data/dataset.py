from abc import ABC, abstractmethod

import ray
from ray.data import Dataset

from config.settings.dataset import DatasetConfig


class IDataSet(ABC):
    def __init__(self, dataConfig: DatasetConfig):
        self.config = dataConfig
        self.dataset = self._database()

    @abstractmethod
    def _format_adaptation_s3(self):
        """Based on type of datasource update to s3 Ray compatible format"""

    def _database(self) -> Dataset | None:
        fs = self._format_adaptation_s3()
        return ray.data.read_parquet(paths=self.config.paths, filesystem=fs)

    @property
    def data(self) -> Dataset | None:
        return self.dataset
