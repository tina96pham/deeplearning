import os
import sys
from Xray.exception import XRayException

class S3Operation:
    def sync_folder_to_s3()-> None:
        """uloading data"""
        try:
            pass
        except Exception as e:
            raise XRayException(e, sys)
        
    
    def sync_folder_from_s3()-> None:
        """downloading data"""
        try:
            pass
        except Exception as e:
            raise XRayException(e,sys)