import os

#application configuration 

class Config(object):
    #parent config class having general settings for all environments setting them as default
    DEBUG = False
    CSRF_ENABLED = True
    SECRET =os.getenv('SECRET')

class DevelopmentConfig(Config):
    #development-configurations
    DEBUG = True

class TestingConfig(Config):
    #testing configurations
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    #staging configurations 
    DEBUG = True

class ProductionConfig(Config):
    #production configurations
    #NB:In production testing and debugging should be set to false.
    DEBUG = False
    TESTING = False

#this app_config is used to simplify exporting these four environments
app_config = {'development':DevelopmentConfig,
              'testing':TestingConfig,
              'staging':StagingConfig,
              'production':ProductionConfig
             }