from configparser import ConfigParser



class Configuration:
    def __init__(self) -> None:
        self.config = ConfigParser()
        self.config.read("config/config.ini")

        
    @classmethod
    @property
    def default_browser(cls):
        return cls().config.get('basic info', 'browser')
    
    @classmethod
    @property
    def start_url(cls):
        return cls().config.get('basic info', 'url')
        
    @classmethod
    @property
    def timeout(cls):
        return cls().config.get('basic info', 'timeout')