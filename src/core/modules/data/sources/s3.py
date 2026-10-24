import pyarrow.fs as pafs

from config.settings.dataset import IAMRole, Keys
from src.core.modules.data.dataset import IDataSet
from src.utils.lib.exceptions.format import RayDataFormatError


class S3(IDataSet):
    def _format_adaptation_s3(self) -> pafs.FileSystem:
        if isinstance(self.config.access, IAMRole):
            return pafs.S3FileSystem(
                role_arn=self.config.access.role_arn,
                session_name=self.config.access.session_name,
                region=self.config.access.region,
            )
        elif isinstance(self.config.access, Keys):
            raise TypeError("""Mini IO needs Keys rather than IAM Role""")

        raise RayDataFormatError("""Check the access config type""")
