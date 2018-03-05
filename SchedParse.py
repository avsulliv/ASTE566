### Parse Satellite Schedule
import datetime as dt
import string
import re
from pandas import DataFrame as df
from sys import argv
import csv

#CONSTANTS
in_columns = ['Date','Time','Satellite','Azm','Elv','Mag','Range','S.Azm','S.Elv']
out_columns = ['Satellite','StartDate','StartTime','EndDate','EndTime','Duration']
outname = 'schedule-group4.csv'
filename = argv[1]

fpr = open(filename,'r')

#first format the input file
new = filename.split('.')[0]+"_formatted.csv"
formatted = open(new,'w')

#replace white space with commas (csv)
line = fpr.next()
#line='index,'+re.sub("\s+", ",", line.strip())+'\n'
line=re.sub("\s+", ",", line.strip())+'\n'
print line
formatted.writelines(line)
i=1
while(True):
     try: 
     	line = fpr.next()
     	if(line=='\r\n'): 
     		continue
     	#line=str(i)+','+re.sub("\s+", ",", line.strip())+'\n'
     	line=re.sub("\s+", ",", line.strip())+'\n'
     	print line
     	formatted.writelines(line)
     	i=i+1
     except: break

fpr.close()
formatted.close()
#NOW FORMATTED AS CSV

#Extract csv into DataFrame
DF = df.from_csv(new,sep=',',index_col=None)

#read CSV and format
#fpr = open(filename,'r')
#fwp = open(outname,'w')
#Fin = csv.reader(fp)

#dex = ['Date','Time']
#DF.set_index(dex)


length = len(DF.index)/3

DF3 = df(index=range(length),columns=out_columns)

for i in range(length):
	j=3*i
	DF2=DF[3*i:3*(i+1)].copy()
	#Extract parameters
	Satellite = DF2.ix[j+0]['Satellite']
	AOS = DF2.ix[j+0]['Date']+'_'+DF2.ix[j+0]['Time']
	LOS = DF2.ix[j+2]['Date']+'_'+DF2.ix[j+2]['Time']
	#Populate target parameters
	DF3.ix[i]['StartDate']=DF2.ix[j]['Date']
	DF3.ix[i]['StartTime']=DF2.ix[j]['Time']
	DF3.ix[i]['EndDate']=DF2.ix[j+2]['Date']
	DF3.ix[i]['EndTime']=DF2.ix[j+2]['Time']
	DF3.ix[i]['Satellite']=Satellite
	#Compute duration
	#datetime_object = dt.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
	#dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
	#'2018-03-05_00:07:09''
	AOS_dt = dt.datetime.strptime(AOS, '%Y-%m-%d_%H:%M:%S')
	LOS_dt = dt.datetime.strptime(LOS, '%Y-%m-%d_%H:%M:%S')
	delta=LOS_dt-AOS_dt
	DF3.ix[i]['Duration']=delta.seconds

DF3.to_csv(outname,index=False)