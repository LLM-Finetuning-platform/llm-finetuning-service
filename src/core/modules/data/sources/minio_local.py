import pyarrow.fs as pafs

from config.settings.dataset import IAMRole, Keys
from src.core.modules.data.dataset import IDataSet
from src.utils.lib.exceptions.format import RayDataFormatError


class MiniIOLocal(IDataSet):
    def _format_adaptation_s3(self) -> pafs.FileSystem:
        if isinstance(self.config.access, Keys):
            return pafs.S3FileSystem(
                access_key=self.config.access.access_key,
                enpoint_url=self.config.access.enpoint_url,
                secret_key=self.config.access.secret_key,
            )
        elif isinstance(self.config.access, IAMRole):
            raise TypeError("""Mini IO needs Keys rather than IAM Role""")

        raise RayDataFormatError("""Check the access config type""")
