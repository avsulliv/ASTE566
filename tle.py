### TLE Library

class tle(object):
	#'''Class tle: is a container.'''
	def __init__(self):
		#instantiate TLE dictionary container
		self.__dict_init()
	def import_tle(self, filename):
		#import from TLE plaintext file
		fp = open(filename,'r')
		while True:
			try: 
				line = fp.next()
				line = line.strip('\r\n') #strip EOL characters - will strip either '\r\n' or '\n'
			except:
				break #break while loop if EOF
			parameters=line.split(' ')
			while('' in parameters): parameters.remove('')   #purge any empty list entries
			if parameters[0] == '1':
				#do line one
				#self.__line_one(parameters)
				self.__line_one(parameters)
				print line
			elif parameters[0] == '2':
				#do line two
				#self.__line_two(parameters)
				print line
			else:
				#If it is the satellite name (aka not line 1 or line 2 of TLE format)
				satname = line
				self.tle_dict['name'] = satname
		fp.close()
		return 0
	def export_tle(self):
		#As plaintext to file, to csv, or as pandas.DataFrame
		return 0;
	#def modify(self,):
		#modifies one or more TLE parameters and yields a new tle object

	### PRIVATE METHODS ###
	def __line_one(self, parameters):
		'''Extracts parameters list for line one of a TLE. Imports into the tle_dict dictionary fields.\n'''
		spaces1 = [' ',' ',' ',' ',' ',' ',' ',' ','']
		#extract parameters list
		linenum = parameters[0]  #linenum = str('1')
		satid = parameters[1].rjust(self.tle_dict[linenum]['satid']['length'])  #right adjust the satid string to length = 6
		parameters[1] = satid
		intldez = parameters[2].ljust(self.tle_dict[linenum]['intldez']['length'])  #left adjust intldez to length = 8
		parameters[2] = intldez
		epoch = parameters[3].ljust(self.tle_dict[linenum]['epoch']['length']) #left adjust epoch to length = 14
		parameters[3] = epoch
		dnd1 = parameters[4].rjust(self.tle_dict[linenum]['dnd1']['length']) #right adjust Mean Motion 1st derivative length = 10
		parameters[4] = dnd1
		dnd2 = parameters[5].rjust(self.tle_dict[linenum]['dnd2']['length']) #right adjust Mean Motion 2nd derivative len = 8
		parameters[5] = dnd2
		bstar = parameters[6].rjust(self.tle_dict[linenum]['bstar']['length']) #right adjust ballistic coeff. len = 8
		parameters[6] = bstar
		ephemeristype = parameters[7] #ephemeris should only be len = 1
		elementnum = parameters[8][:-1]   #keep all characters in parameters[8] string except for last character
		elementnum = elementnum.rjust(self.tle_dict[linenum]['checksum']['length']) #right adjust element number len = 4
		checksum = parameters[8][-1:]     #checksum digit is only the last character in the parameters[8] string

		parameters[8] = elementnum  #exclude checksum value from paramaters
		print parameters

		#Compute checksum
		s = ''.join(list(sum(zip(parameters,spaces1),())))   #Do a bunch of shit to merge the parameter values back into a flat string
		checkval = self.__tle_checksum(s)

		#length format and pad strings and load into tle_dict dictionary attribute
		self.tle_dict[linenum]['satid']['value'] = satid
		self.tle_dict[linenum]['intldez']['value'] = intldez
		self.tle_dict[linenum]['epoch']['value'] = epoch
		self.tle_dict[linenum]['dnd1']['value'] = dnd1
		self.tle_dict[linenum]['dnd2']['value'] = dnd2
		self.tle_dict[linenum]['bstar']['value'] = bstar
		self.tle_dict[linenum]['ephemeris']['value'] = ephemeristype
		self.tle_dict[linenum]['element']['value'] = elementnum

		self.tle_dict[linenum]['checksum']['value'] = str(checkval)
		return 0
	def __line_two(self, parameters):
		spaces2 = [' ',' ',' ',' ',' ',' ',' ',' ','']
		#extract parameters list
		linenum = parameters[0]  #linenum = str('2')
		satnum = parameters[1].rjust(self.tle_dict[linenum]['satnum']['length'])  #right adjust the satnum string to length = 5
		parameters[1] = satnum
		inclination = parameters[2].ljust(self.tle_dict[linenum]['inc']['length'])  #left adjust inc to length = 8
		parameters[2] = inclination
		raan = parameters[3].rjust(self.tle_dict[linenum]['inc']['length'])  #right adjust raan to length = 8
		parameters[3] = raan
		eccentricity = parameters[4].rjust(self.tle_dict[linenum]['e']['length'],'0')  #right adjust eccentricity to length = 7, pad zeros
		parameters[4] = eccentricity
		periapsis = parameters[5].rjust(self.tle_dict[linenum]['periapsis']['length'])  #right adjust arg of periapsis to length = 8
		parameters[5] = eccentricity

		return 0
	def __dict_init(self):
		self.tle_dict = {}
		self.tle_dict['name'] = str()
		#Line One of TLE
		self.tle_dict['1'] = {}
		self.tle_dict['1']['satid'] = {'value': str(), 'length': 6}			#Satellite identifier = satellite number + classification 
		self.tle_dict['1']['intldez'] = {'value': str(), 'length': 8}		#International designator 
		self.tle_dict['1']['epoch'] = {'value': str(), 'length': 14}		#epoch
		self.tle_dict['1']['dnd1'] = {'value': str(), 'length': 10}			#First derivative of mean motion
		self.tle_dict['1']['dnd2'] = {'value': str(), 'length': 8}			#Second derivative of mean motion
		self.tle_dict['1']['bstar'] = {'value': str(), 'length': 8}			#Normalized ballistic coeficient
		self.tle_dict['1']['ephemeris'] = {'value': str(), 'length': 1}		#Ephemeris model: 1=SGP, 2=SGP4, 3=SDP4, 4=SGP8, 5=SDP8
		self.tle_dict['1']['element'] = {'value': int(), 'length': 4}		#Element number: increment of TLE
		self.tle_dict['1']['checksum'] = {'value': int(), 'length': 1}		#Checksum for line 1 (mod 10?)
		#Line Two of TLE
		self.tle_dict['2'] = {}
		self.tle_dict['2']['satnum'] = {'value': str(), 'length': 5}		#Satellite number
		self.tle_dict['2']['inc'] = {'value': float(), 'length': 8}			#Inclination [degrees]
		self.tle_dict['2']['raan'] = {'value': float(), 'length': 8}		#Right Ascension of the Ascending node [degrees]
		self.tle_dict['2']['e'] = {'value': float(), 'length': 7}	  		#eccentricity
		self.tle_dict['2']['periapsis'] = {'value': float(), 'length': 8}	#argument of periapsis [degrees]
		self.tle_dict['2']['M'] = {'value': float(), 'length': 8}			#Mean anomaly [degrees]
		self.tle_dict['2']['n'] = {'value': float(), 'length': 10}			#Mean motion [revolutions/day]
		self.tle_dict['2']['revs'] = {'value': int(), 'length': 5}			#number of revolutions at epoch
		self.tle_dict['2']['checksum'] = {'value': int(), 'length': 1}		#Checksum for line 2 (mod 10?)
		return 0
	def __format_satid(self,s):
		'''Accepts input string, returns formatted satellite ID (i.e. - 25544U)\n'''
		#strip 
	def __tle_checksum(self,s):
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


#Factory design pattern
#import tle
#modify parameters
#show parameters
#export tle