import sys, os
import time
import datetime
from datetime import timedelta
from datetime import date

filename = str(sys.argv[1])
fileSplit = filename.split('.')
TodaysDatePre = datetime.datetime.now()
newdate = TodaysDatePre.strftime("%m%d%Y")
NewFileName = fileSplit[0]+newdate+'.csv'
input_path = str(sys.argv[2])
final_output_path = 'C:\\NBCUniversal\\Final\\'

#open .csv file
#create linked list to store Driver and imbedded list containing sum of all laptimes
# and counts ie: {'Alonzo':[laptime,cnt]}, {'Ford':[laptime,cnt]}
d = {}

try:
    with open(input_path + filename) as fp:

        lines = fp.readlines()
        for line in lines:
            SplitLine = line.split(',')
            Driver = SplitLine[0]
            Laptime = float(SplitLine[1])
            if Driver in d:
                d [Driver][0] = d[Driver][0] + Laptime
                d [Driver][1] = d[Driver][1] + 1
            else:
                d [Driver] = [Laptime,1]

except:
    print('Issue may be bad input or blank lines.. continue')
    pass

#Roll through linked list and put into an imbedded list with averages stored
#and drivers name ie: [avg,'Bandini'] this will allow for an easy sort of ascending laptimes

e = [[]]

for i in d:
    e.append([round(d[i][0]/d[i][1],2),i])

e.pop(0)
# sort the list 
sorted_list = sorted(e)

#write the sorted list to a new file, after the top three are gathered stop writing
###open and output header in remote report file
Outputfile = open(final_output_path +'\\'+ NewFileName + '.csv','w+')
Outputfile.write('Driver,AverageLaptime\n')

prev_avg = 0
chng = 0

for l in sorted_list:
    # if the average is less than or equal to previous and the number hasn't changed 3 times
    # continue to write to the file, once change has happened more than twice kick out of loop
    # the logic here makes allowances for dense ranking, and will account for ties with no gaps
    if l[0] >= prev_avg and chng <=2:
        Outputfile.write(l[1] +','+ str(l[0])+'\n')
    else:
        break
    if l[0] != prev_avg:
        chng += 1
    prev_avg = l[0]
    

Outputfile.flush()
Outputfile.close
os.remove(input_path + filename)

