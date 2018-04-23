#RECOMPUTES CHECKSUM OF TLE
from sys import argv

def tle_checksum(s):
	'''Computes the mod-10 checksum of TLE string 's' \n'''
	acc = 0
	for c in s:
		val = 0
		try:
			val = int(c)   #Convert character into integer
		except:
			if c == '-':
				val = 1
			else:
				val = 0					
		acc = acc + val
	checksum = acc%10 #compute modulo-10 checksum
	return checksum


#MAIN#

infile = argv[1]
F = infile.split('.')
outfile = F[0]+'_checked.'+F[-1:][0]
fp = open(infile,'r')
gp = open(outfile,'w+')

#Scan input file for lines with TLE data
while True:
	try: 
		line = fp.next()
		line = line.strip('\r\n') #strip EOL characters - will strip either '\r\n' or '\n'
	except:
		break #break while loop if EOF
	parameters=line.split(' ')
	while('' in parameters): parameters.remove('')   #purge any empty list entries
	if (parameters[0] == '1') or (parameters[0] == '2'):
		#do line one checksum
		s = line[:-1]   #s = all characters in 'line' except for the last one (the checksum digit).
		checksum = str(tle_checksum(s))   #checksum integer returned from subroutine and formatted as a string
		s = s+checksum+'\r\n' #append checksum character and add a newline char
		gp.writelines(s)
	else:
		#If it is the satellite name (aka not line 1 or line 2 of TLE format) - just write it to file
		s = line+'\r\n'
		gp.writelines(s)   #write to output file

fp.close()
gp.close()