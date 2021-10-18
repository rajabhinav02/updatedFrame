import inspect
import logging


#class logg:`

def loggingcontent(loglevel = logging.DEBUG):

    testname= inspect.stack()[1][3]
    logger = logging.getLogger(testname)
    logger.setLevel(logging.DEBUG)
    #filehandler = logging.FileHandler("{0}.log".format(testname), mode = "w")
    filehandler = logging.FileHandler("automation.log", mode = "a")
    filehandler.setLevel(loglevel)
    format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(format)
    logger.addHandler(filehandler)
    return logger