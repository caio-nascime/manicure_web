from dotenv import load_dotenv
import os 

load_dotenv()


class ConfigBase():

    FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    FLASK_APP = os.environ.get("FLASK_APP")


class ConfigDev(ConfigBase):

    DEBUG = True
    TESTING = False


class ConfigTest(ConfigBase):

    DEBUG = False
    TESTING = True


configs = {"teste" : ConfigTest, "desenvolvimento" : ConfigDev}