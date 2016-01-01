try:
    from pymongo import MongoClient
except Exception as e:
    print e
    raise

import time
import datetime

class log:
    def __init__(self,logFileName):
        self.logFileName=logFileName
        self.client = MongoClient()
        self.db=self.client.halogs # data_base for written all logs
        if logFileName:
          self.logFile= self.db[self.logFileName]


    def  writeLog(self,title,txt,by="HAIOS"): # write log to specific log
         'title text by'
         logObj={

                   "title":title,
                   "txt":txt,
                   "date": datetime.datetime.utcnow(),
                   "time": time.time(),
                   "by"  : by
                 }
         id=self.logFile.insert_one(logObj).inserted_id
         print id

    def logFilesList(self):#show all logs list
          logsList=self.db.collection_names(include_system_collections=False)
          for logName in logsList:
               print logName

    def showLogs(self,logfile):#show all commited logs for a log
        logfile=self.db[logfile]
        alllogs=logfile.find()
        for logObj in alllogs:
            print "by:",logObj["by"],"Title:",logObj.get("title",None)," time:",logObj["date"]
            print "log:",logObj["txt"]
            print ""

    def deleteAllLogs(self,logfile):
        logfile=self.db[logfile]
        logfile.remove({})


if __name__=="__main__":
       mlog=log(raw_input("Enter log File Name:"))
       mlog.writeLog(raw_input("Enter Log Title:"),raw_input("Enter Log Text:"),raw_input("Enter Your Name:"))
       mlog.logFilesList()
       mlog.showLogs(raw_input("Enter log File Name to show all logs:"))
       mlog.deleteAllLogs(raw_input("Enter file Name to Clear all document:"))
