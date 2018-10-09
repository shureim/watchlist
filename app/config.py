class Config() :
    """
    Gereral configuration of the parent class
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProConfig(Config) :
    """
    production configuration of child class 

    Args :
        config - the parent configuration class with  general configuration settings
    """
    pass

class DevConfig(Config) :
    """
    Development configuration of the parent class

    Args:
        Config - the parent configuration class with  general configuration settings
    """


    DEBUG = True


