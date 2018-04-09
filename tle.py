### TLE Library

class tle(object):
	#'''Class tle: is a container.'''
	def __init__(self):
		#instantiate TLE dictionary container
		self.__dict_init__()
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

		return 0
	def __line_two(self, parameters):
		return 0
	def __dict_init__(self):
		self.tle_dict = {}
		self.tle_dict['name'] = str()
		#Line One of TLE
		self.tle_dict['1'] = {}
		self.tle_dict['1']['satid'] = str()			#Satellite identifier = satellite number + classification 
		self.tle_dict['1']['intldez'] = str()		#International designator 
		self.tle_dict['1']['epoch'] = str()			#epoch
		self.tle_dict['1']['dnd1'] = str()			#First derivative of mean motion
		self.tle_dict['1']['dnd2'] = str()			#Second derivative of mean motion
		self.tle_dict['1']['bstar'] = str()			#Normalized ballistic coeficient
		self.tle_dict['1']['ephemeris'] = str()		#Ephemeris model: 1=SGP, 2=SGP4, 3=SDP4, 4=SGP8, 5=SDP8
		self.tle_dict['1']['element'] = int()		#Element number: increment of TLE
		#self.tle_dict['1']['checksum']
		#Line Two of TLE
		self.tle_dict['2'] = {}
		self.tle_dict['2']['satnum'] = str()			#Satellite number
		self.tle_dict['2']['i'] = float()			#Inclination [degrees]
		self.tle_dict['2']['raan'] = float()		#Right Ascension of the Ascending node [degrees]
		self.tle_dict['2']['e'] = float()	  		#eccentricity
		self.tle_dict['2']['periapsis'] = float()	#argument of periapsis [degrees]
		self.tle_dict['2']['M'] = float()			#Mean anomaly [degrees]
		self.tle_dict['2']['n'] = float()			#Mean motion [revolutions/day]
		self.tle_dict['2']['revs'] = int()			#number of revolutions at epoch
		#self.tle_dict['2']['checksum'] = 
		return 0


#Factory design pattern
#import tle
#modify parameters
#show parameters
#export tle