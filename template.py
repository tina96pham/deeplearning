import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name= "Xray"

list_of_files= [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/cloud_storage/__init__.py",
    f"src/{project_name}/cloud_storage/s3_operation.py"
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformer.py",
    f"src/{project_name}/components/data_evaluation.py",
    f"src/{project_name}/components/data_pusher.py",
    f"src/{project_name}/components/data_training.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/entity/artifact_entity.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/exception.py",
    f"src/{project_name}/pipeline/logger.py",
    "test/integration_test/__init__.py",
     "test/unit_test/__init__.py",
    "experiment/experiment.ipynb",
    "bentoff.yaml",
    "init_setup.sh",
    "tox.ini",
    "requirement_dev.text",
    "requirement.text",
    "setup.py",
    "setup.chg"
]

# Step 4: Python logic to create all the files
''' for filepath in the list_of_file 
    1. convert path to be unversal using python library Path ( window file path is fpward slash)
    2. seprate folfer and file
    3. Create file directories if not exist
    4. Create the file by checking file existence and if exist file size need to be 0 to make sure bot wiping out file with work 
'''

for filepath in list_of_files:
    filepath= Path(filepath)

    filedir, filename= os.path.split(filepath)
    # Create directories if they don't exist already
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info (f"Creating directory; {filedir} for the file:  {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with  open(filepath, 'w', encoding='utf8') as f:
            pass
            logging.info(f"Creating an empty file :{filename}")
    else:
        logging.debug(f"{filename} already exists.")