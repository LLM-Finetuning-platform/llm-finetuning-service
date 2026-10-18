import pyarrow.fs as pafs
from src.core.modules.data.dataset import IDataSet
from config.settings.dataset import Keys, IAMRole

class S3(IDataSet):

    def _format_adaptation_s3(self)->( pafs.FileSystem ):
        if isinstance(self.config.access, IAMRole):
           return pafs.S3FileSystem(
               
           ) 
        elif isinstance(self.config.access,Keys):
            raise Exception("""Mini IO needs Keys rather than IAM Role""")
     
        raise Exception("""Check the access config type""") 