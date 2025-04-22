import configparser

# Create Object of Config Parser class and It will access to read the Config.ini file
config = configparser.RawConfigParser()

# Pass the config.ini path to read.
config.read("./Configuration/config.ini")


# Create Class to access or get value of config file
# Each and every veriable have seprate static method
# By using static method we can access the directly no need to create class object

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        # by using the get() method we can access the value of config file and store in veriable
        url = config.get('common info',"baseURL")
        return url

    @staticmethod
    def getUseremail():
        # by using the get() method we can access the value of config file and store in veriable
        # Pass the config category name in section and then pass the value of it
        username = config.get('common info',"useremail")
        return  username

    @staticmethod
    def getUserPassword():
        # by using the get() method we can access the value of config file and store in veriable
        password = config.get('common info',"userpassword")
        return password