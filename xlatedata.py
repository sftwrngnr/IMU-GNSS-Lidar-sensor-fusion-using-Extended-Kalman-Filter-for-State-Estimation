from pickle import TRUE
import time
import datetime
import numpy


fnames = [ "data/UERecode1.txt"] # "data/velodyne_points.csv",
#timeOff = 

def getTime(tField):
    tf = tField.split(":")
    myTime = tf[1] + ":" + tf[2] + ":" + tf[3]
    myDate = tf[1][:-3]
    print(myTime)
    testTime = numpy.longdouble(time.mktime(datetime.datetime.strptime(myTime, "%Y-%m-%d %H:%M:%S").timetuple()) * 10e8)
    print( time.mktime(datetime.datetime.strptime(myTime, "%Y-%m-%d %H:%M:%S").timetuple()))
    print( time.mktime(datetime.datetime.strptime(myDate, "%Y-%m-%d").timetuple()))
    print(testTime)
    print(1616037858056215080.0)
    print (1616037858056215080.0 - testTime)


def proc_uer_line(instr):
    fields = instr.split(",")
    print(fields[0])
    getTime(fields[0])


for nm in fnames:
    frst = TRUE
    print()
    with open(nm, "r") as f:
        for inln in f:
            print(inln[:-1])
            proc_uer_line(inln[:-1])


