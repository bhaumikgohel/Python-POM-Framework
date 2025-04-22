import logging

class LogGen:

    @staticmethod
    def GenLog():

        logging.basicConfig(filename='./Logs/',format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return  logger

    #Import the logging package
    # By using logging package we confi the File and Foramat it define Date and Time format
    # By using loggin we can set different Logger Level like INFO, DEBUG, WARNING etc
    # It return the logger