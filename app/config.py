class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'http://newsapi.org/v2/everything?q=bitcoin&from=2020-10-29&sortBy=publishedAt&apiKey=0ac1c2d0556d41389f0ea5569f3c85b6'
    NEWS_SOURCE_BASE_URL = 'http://newsapi.org/v2/everything?q=bitcoin&from=2020-10-29&sortBy=publishedAt&apiKey=0ac1c2d0556d41389f0ea5569f3c85b6'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
