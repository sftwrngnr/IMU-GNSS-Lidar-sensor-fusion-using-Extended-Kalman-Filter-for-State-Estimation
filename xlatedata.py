from pickle import TRUE
import time
import datetime
import numpy


fnames = [ "data/UERecode1.txt"] # "data/velodyne_points.csv",
timeOff = -53806943784960.0

def getCoord(tField):
    return float(tField[2:])

def getTime(tField):
    tf = tField.split(":")
    myTime = tf[1] + ":" + tf[2] + ":" + tf[3]
    myDate = tf[1][:-3]
    testTime = numpy.longdouble(time.mktime(datetime.datetime.strptime(myTime, "%Y-%m-%d %H:%M:%S").timetuple()) * 10e8) + timeOff
    return testTime


def proc_uer_line(instr):
    fields = instr.split(",")
    cTime = getTime(fields[0])
    x = getCoord(fields[2])
    y = getCoord(fields[3])
    z = 0.0
    return("%16.0f,%5.2f,%5.2f,%4.2f" %(cTime , x ,y ,z))


for nm in fnames:
    frst = TRUE
    print()
    with open(nm, "r") as f:
        for inln in f:
            print(proc_uer_line(inln[:-1]))


