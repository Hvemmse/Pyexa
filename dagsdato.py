#!/usr/bin/python

#codet on 24-02-22 from Frank Simens
#Contact frank@simens.dk



import calendar

from datetime import datetime

dato =datetime.today().strftime('%d-%m-%Y')

print('Date to day is ', dato)

aar_raw = datetime.today().strftime('%Y')
aar =int(aar_raw)
maaned_raw =datetime.today().strftime('%m')
maaned  =int(maaned_raw)
cal = calendar.month(aar, maaned)
print ('Here is the calendar: ')
print (cal)

