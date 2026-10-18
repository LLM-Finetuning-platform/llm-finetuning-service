import pyarrow.fs as pafs
from src.core.modules.data.dataset import IDataSet
from config.settings.dataset import Keys, IAMRole

class MiniIOLocal(IDataSet):

    def _format_adaptation_s3(self)->( pafs.FileSystem ):
        if isinstance(self.config.access, Keys):
           return pafs.S3FileSystem(
               access_key = self.config.access.access_key,
               enpoint_url = self.config.access.enpoint_url,
               secret_key = self.config.access.secret_key
           ) 
        elif isinstance(self.config.access,IAMRole):
            raise Exception("""Mini IO needs Keys rather than IAM Role""")
     
        raise Exception("""Check the access config type""") 