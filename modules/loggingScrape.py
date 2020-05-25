#import logging functionalities
import logging

# may define different logging solutions in one file and call them in other files
logging.basicConfig(filename='scraperLog.txt',level=logging.ERROR,format =  '%(levelname)s - %(asctime)s - %(message)s')
