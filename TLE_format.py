import re
filename = input('Enter file name: ')
#f = open('TLE Candidates 20180405 - Master.tsv','r')
f = open(filename,'r')
g = open('Mystery_TLEs.txt','w')
spaces1 = [' ',' ','   ',' ','  ','  ',' ',' ','']
spaces2 = [' ','  ',' ',' ','  ',' ',' ',' ','']

satnum = 1 #init
while(True):
	try:
		line = f.next()
		params = line.split('\t')  #assuming lines in f are tsv
		if params[0] == str(1):
			x=params[4]
			if params[4].startswith('-'):
				params[4]='-.'+x.split('.')[1]
			else:
				params[4]=' .'+x.split('.')[1]
			#satid = params[1]
			#satnum = satid.partition('U')[0]
			params[1]=str(satnum).zfill(05)+'U' #overwrite sat-id with incrementing satid
			concat = zip(params,spaces1)
			formatted = list(sum(concat,()))
			flat = ''.join(formatted)
			g.write(flat)
			#newfile.write(flat)
			continue
		elif params[0] == str(2):
			params[1]=params[1].zfill(05)
			params[4]=params[4].zfill(07)
			params[1] = str(satnum).zfill(05)
			concat = zip(params,spaces2)
			formatted = list(sum(concat,()))
			flat = ''.join(formatted)
			g.write(flat)
			#newfile.write(flat)
			#newfile.close()
			satnum=satnum+1 #increment satnum
			continue
		else:
			#Then must be name (line zero)
			detab = line.split('\t')
			while '' in detab: detab.remove('')
			title = list(detab)
			title.remove('\r\n')
			clean = ''.join(detab)
			title = ''.join(title)
			#newfile = open(title+'.txt','w')
			g.write(clean)
			#newfile.write(clean)
	except:
		break
f.close()
g.close()