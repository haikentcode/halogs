# halogs

````
Python Project To Store logs in log file .This is helpful when you are
working on some project and want to keep some information somewhere ,
so it's easy to use halogs and then open terminal and by using one or two commands ,
store useful information and access stored information easily through  terminal
Technology  used in this Project are (Python Programming language and Mongodb for Database )
````

Use given Python Script For use halogs in Command Line(Terminal)


````bash
>>halogs -h  # for help documentation

>>halogs -r logsFileName  # list all logs in file

>>halogs -lf  # list all logs File Name

>>halogs -w logFileName #  to write log
Title:haikent
Text:this testing
By:hitesh
````


#Python Script

```python
from halogs import halogs as ha

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-w", "--write", help="write log to logfile")
parser.add_argument("-r", "--read", help="read log file")
parser.add_argument("-lf", "--listfile", help="show list of save logfiles",action="store_true")
parser.add_argument("-c", "--clear", help="clear a logfile")

args=parser.parse_args()

if args.listfile:
    hk=hk=ha.log("")
    hk.logFilesList()


if args.write:
    logfile=args.write
    hk=ha.log(logfile)
    hk.writeLog(raw_input("Title:"),raw_input("Text:"),raw_input("By:"))

if args.read:
    logfile=args.read
    hk=ha.log(logfile)
    hk.showLogs(logfile)

if args.clear:
    logfile=args.clear
    hk=ha.log(logfile)
    hk.deleteAllLogs(logfile)
```
