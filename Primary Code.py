#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    t1=[]
    t2=[]
    if "AM" in s:
        t1=s.split(":")
        if "12" in t1[0]:
            t1[2]=t1[2].replace("AM","")
            val=str("00"+":"+t1[1]+":"+t1[2])
            return val
        else:
            t1[2]=t1[2].replace("AM","")
            val=str(t1[0]+":"+t1[1]+":"+t1[2])
            return val
    if "PM" in s:
        t2=s.split(":")
        if "12" in t2[0]:
            t2[2]=t2[2].replace("PM","")
            val=str("12"+":"+t2[1]+":"+t2[2])
            return val
        else:
            t2[2]=t2[2].replace("PM","")
            con=int(t2[0])
            con=con+12
            con=str(con)
            val=str(con+":"+t2[1]+":"+t2[2])
            return val
            


