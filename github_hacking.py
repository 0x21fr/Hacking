#!/usr/bin/python

import datetime


DATA = [
"#     #    #     #####  #    # ### #     #  #####   ", 
"#     #   # #   #     # #   #   #  ##    # #     #  ",
"#     #  #   #  #       #  #    #  # #   # #        ",
"####### #     # #       ###     #  #  #  # #  ####  ",
"#     # ####### #       #  #    #  #   # # #     #  ",
"#     # #     # #     # #   #   #  #    ## #     #  ",
"#     # #     #  #####  #    # ### #     #  #####   "]


DATE_Start = datetime.datetime(2018, 11, 25)
DATE_Now   = datetime.datetime.now()

DELTA = (DATE_Now - DATE_Start).days

Y = (DATE_Now.weekday() + 1)%7
X = (DELTA / 7)%52


F = open("date.txt","w")
F.write(str(DATE_Now))
F.close()


if DATA[Y][X] == "#" :

	print "OK"
