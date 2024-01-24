import json
from pathlib import Path



class DataReader:
    
    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parent.parent
        file_path = BASE_DIR / 'config' / 'testData.json'
        with open(file_path, 'r') as file:
            self.test_data = json.load(file)

    @classmethod
    @property
    def careers_department_name(cls):
        return cls().test_data['CareersPage']['department']

    @classmethod
    @property
    def get_careers_language(cls):
        return cls().test_data['CareersPage']['language']

    @classmethod
    @property
    def get_careers_total_jobs(cls):
        return cls().test_data['CareersPage']['total_jobs']


