### TLE Library

class tle(object):
	#'''Class tle: is a container.'''
	def __init__(self):
		#instantiate TLE dictionary container
		self.__dict_init()
	def import_tle(self, filename):
		#import from TLE plaintext file
		self.tle_dict = {}
		self.tle_dict['name'] = ''
		self.tle_dict['1'] = {}
		self.tle_dict['2'] = {}
		fp = open(filename,'r')
		while True:
			line = fp.next()
			if ' ' not in line :
				#then is sat name
				satname = line.strip('\n')
			else:
				try:
					parameters = line.strip('\n').split(' ')
				except:
					parameters = line.split(' ')
				while '' in parameters: parameters.remove('')
		fp.close()
		return 0
	def export_tle(self):
		#As plaintext to file, to csv, or as pandas.DataFrame
		return 0;
	#def modify(self,):
		#modifies one or more TLE parameters and yields a new tle object
	def __line_one(self, parameters):
		spaces1 = [' ',' ','   ','  ','  ','  ',' ','  ','']
		return 0
	def __line_two(self, parameters):
		spaces2 = [' ','  ',' ',' ',' ',' ',' ','  ','']
		return 0
	def __dict_init(self):
		self.tle_dict = {}
		self.tle_dict['name'] = str()
		#Line One of TLE
		self.tle_dict['1'] = {}
		self.tle_dict['1']['satid'] = {'value': str(), 'length': 0}			#Satellite identifier = satellite number + classification 
		self.tle_dict['1']['intldez'] = {'value': str(), 'length': 0}		#International designator 
		self.tle_dict['1']['epoch'] = {'value': str(), 'length': 0}			#epoch
		self.tle_dict['1']['dnd1'] = {'value': str(), 'length': 0}			#First derivative of mean motion
		self.tle_dict['1']['dnd2'] = {'value': str(), 'length': 0}			#Second derivative of mean motion
		self.tle_dict['1']['bstar'] = {'value': str(), 'length': 0}			#Normalized ballistic coeficient
		self.tle_dict['1']['ephemeris'] = {'value': str(), 'length': 0}		#Ephemeris model: 1=SGP, 2=SGP4, 3=SDP4, 4=SGP8, 5=SDP8
		self.tle_dict['1']['element'] = {'value': int(), 'length': 0}		#Element number: increment of TLE
		self.tle_dict['1']['checksum'] = {'value': int(), 'length': 0}		#Checksum for line 1 (mod 10?)
		#Line Two of TLE
		self.tle_dict['2'] = {}
		self.tle_dict['2']['satnum'] = {'value': str(), 'length': 0}		#Satellite number
		self.tle_dict['2']['i'] = {'value': float(), 'length': 0}			#Inclination [degrees]
		self.tle_dict['2']['raan'] = {'value': float(), 'length': 0}		#Right Ascension of the Ascending node [degrees]
		self.tle_dict['2']['e'] = {'value': float(), 'length': 0}	  		#eccentricity
		self.tle_dict['2']['periapsis'] = {'value': float(), 'length': 0}	#argument of periapsis [degrees]
		self.tle_dict['2']['M'] = {'value': float(), 'length': 0}			#Mean anomaly [degrees]
		self.tle_dict['2']['n'] = {'value': float(), 'length': 0}			#Mean motion [revolutions/day]
		self.tle_dict['2']['revs'] = {'value': int(), 'length': 0}			#number of revolutions at epoch
		self.tle_dict['2']['checksum'] = {'value': int(), 'length': 0}		#Checksum for line 2 (mod 10?)
		return 0


#Factory design pattern
#import tle
#modify parameters
#show parameters
#export tle