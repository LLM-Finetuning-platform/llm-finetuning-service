from pydantic_settings import BaseSettings
from pydantic import Field
from utils.enums.datasource import Datasources
from typing import List
class Keys(BaseSettings):
   access_key: str = Field(description="""Default access key""")
   secret_key: str = Field(description="""Default secret value""")
   enpoint_url: str = Field(description="""Endpoint url for the datasource""")
class IAMRole(BaseSettings):
   role: str = Field(description="""IAM role for access""")

class DatasetConfig(BaseSettings):
   type:  Datasources = Field(default=Datasources.miniIO, description="""Type of datasource""")
   format_virtual_address: bool = Field(default=False,description="""Virtual address format. >>> Not the full address but virtual naming for the full url or address""")
   paths: List[str] | str  = Field(description="""List of paths for the data or single path for the data""") 
   access: Keys | IAMRole = Field(description="""Access type and info for dataset""")