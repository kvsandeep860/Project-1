from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionconfig:
    root_dir:Path
    source_url:str
    local_data_file:Path
    unzip_dir:Path
    
@dataclass
class Datavalidationconfig:
    root_dir:Path
    unzip_data_dir:Path
    status_file:str
    all_schema:dict