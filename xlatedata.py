from pickle import TRUE
import time
import datetime
import numpy


fnames = [ "data/UERecode1.txt"] # "data/velodyne_points.csv",
timeOff = -53806943784960.0 #probably not needed anymore
zeroTimeVal = -1

def getCoord(tField):
    return float(tField[2:])

def getTime(tField):
    global zeroTimeVal
    tf = tField.split(":")
    myTime = tf[1] + ":" + tf[2] + ":" + tf[3]
    myDate = tf[1][:-3]
    testTime = time.mktime(datetime.datetime.strptime(myTime, "%Y-%m-%d %H:%M:%S").timetuple())
    if (zeroTimeVal == -1):
        zeroTimeVal = testTime
        testTime = 0 #Initial time value is zeroed out
    else:
        #We need to return the number of elapsed seconds
        testTime = testTime - zeroTimeVal
    return testTime


def proc_uer_line(instr):
    fields = instr.split(",")
    cTime = getTime(fields[0])
    x = getCoord(fields[2])
    y = getCoord(fields[3])
    z = 0.0
    return("%16.0f,%f,%f,%f" %(cTime , x ,y ,z))


for nm in fnames:
    frst = TRUE
    print()
    with open(nm, "r") as f:
        for inln in f:
            print(proc_uer_line(inln[:-1]))


