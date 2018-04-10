### Parse Satellite Schedule
import datetime as dt
import string
import re
from pandas import DataFrame as df
from sys import argv
import csv
import pytz

#CONSTANTS
in_columns = ['Date','Time','Satellite','Azm','Elv','Mag','Range','S.Azm','S.Elv']
out_columns = ['Satellite','NORAD_ID','AOS_UTC','LOS_UTC','AOS_Local','LOS_Local','Duration','AOS_AZ','AOS_EL','AOS_RNG','APEX_AZ','APEX_EL','APEX_RNG','LOS_AZ','LOS_EL','LOS_RNG']
outname = 'satpass_schedule.csv'
filename = argv[1]

fpr = open(filename,'r')

LOCAL=-7 #UTC offset - PST = -7, PDT=-8

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
     	y=line.split(',')
        y.pop() #pop off /r/n
        if not '' in y:
           formatted.writelines(line)
        else:
           continue
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
	AOS = DF2.ix[j+0]['Date']+' '+DF2.ix[j+0]['Time']
	print AOS
	LOS = DF2.ix[j+2]['Date']+' '+DF2.ix[j+2]['Time']
	print LOS

	#Format Timezoning
	if ('/' in AOS) and ('/' in LOS):
		datechar = '/'
		AOS_dt = dt.datetime.strptime(AOS, '%m/%d/%Y %H:%M:%S')
		LOS_dt = dt.datetime.strptime(LOS, '%m/%d/%Y %H:%M:%S')
	elif ('-' in AOS) and ('-' in LOS):
		datechar = '-'
		try:
			AOS_dt = dt.datetime.strptime(AOS, '%m-%d-%Y %H:%M:%S')
			LOS_dt = dt.datetime.strptime(LOS, '%m-%d-%Y %H:%M:%S')
		except:
			AOS_dt = dt.datetime.strptime(AOS, '%Y-%m-%d %H:%M:%S')
			LOS_dt = dt.datetime.strptime(LOS, '%Y-%m-%d %H:%M:%S')


	
	UTC = pytz.timezone("UTC")
	AOS_UTC = UTC.localize(AOS_dt) #Configure current AOS time to UTC zone
	LOS_UTC = UTC.localize(LOS_dt) #Configure current LOS time to UTC zone
	AOS_Local = AOS_UTC.astimezone(pytz.timezone("America/Los_Angeles"))  #Convert UTC to Los Angeles local time
	LOS_Local = LOS_UTC.astimezone(pytz.timezone("America/Los_Angeles"))  #Convert UTC to Los Angeles local time

	#Convert python datetime objects into datetime strings and populate in dataframe
	DF3.ix[i]['AOS_UTC']=AOS_UTC.strftime("%Y-%m-%d %H:%M:%S")
	DF3.ix[i]['LOS_UTC']=LOS_UTC.strftime("%Y-%m-%d %H:%M:%S")
	DF3.ix[i]['AOS_Local']=AOS_Local.strftime("%Y-%m-%d %H:%M:%S")
	DF3.ix[i]['LOS_Local']=LOS_Local.strftime("%Y-%m-%d %H:%M:%S")

	#OLD
	#Populate target UTC time parameters
	#DF3.ix[i]['AOS_UTC']=DF2.ix[j+0]['Date']+' '+DF2.ix[j+0]['Time']
	#DF3.ix[i]['LOS_UTC']=DF2.ix[j+2]['Date']+' '+DF2.ix[j+2]['Time']

	#Populate AOS EL/AZ/RNG
	DF3.ix[i]['AOS_AZ']=DF2.ix[j+0]['Azm']
	DF3.ix[i]['AOS_EL']=DF2.ix[j+0]['Elv']
	DF3.ix[i]['AOS_RNG']=DF2.ix[j+0]['Range']

	#Populate MAX EL/AZ/RNG
	DF3.ix[i]['APEX_AZ']=DF2.ix[j+1]['Azm']
	DF3.ix[i]['APEX_EL']=DF2.ix[j+1]['Elv']
	DF3.ix[i]['APEX_RNG']=DF2.ix[j+1]['Range']

	#Populate AOS EL/AZ/RNG
	DF3.ix[i]['LOS_AZ']=DF2.ix[j+2]['Azm']
	DF3.ix[i]['LOS_EL']=DF2.ix[j+2]['Elv']
	DF3.ix[i]['LOS_RNG']=DF2.ix[j+2]['Range']

	#Populate Satellite ID
	DF3.ix[i]['Satellite']=Satellite
	
	#Compute duration
	#datetime_object = dt.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
	#dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
	#'2018-03-05_00:07:09''
	delta=LOS_dt-AOS_dt
	DF3.ix[i]['Duration']=delta.seconds

	#Populate Local Time Parameters

DF3.to_csv(outname,index=False)