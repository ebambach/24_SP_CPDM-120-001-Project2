# -----------------------------------------------------------------
# Assignment Name:      Project 2
# Name:                 Team B
# -----------------------------------------------------------------

# ------------------------------------------------------------------
# Project 2 Class Area
# ------------------------------------------------------------------
class CustomerClass(object):
	_intTotalItemsRented = int(0)
	# Prices for Skis
	_dblSkisHourly = float(15)
	_dblSkisDaily = float(50)
	_dblSkilsWeekly = float(200)
	# Prices for Snowboards
	_dblSnowboardsHourly = float(10)
	_dblSnowboardsDaily = float(40)
	_dblSnowboardsWeekly = float(160)
	# Rental price
	_dblRentalPrice = float(0)
	# Discount, can get 10% for coupon and/or 25% for "family" order of 3-5 items
	_dblDiscount = float(0)
# ------------------------------------------------------------------
# CustomerClass constructor
# ------------------------------------------------------------------	
	def __init__(self, strName, intID, intSkisRented = 0, intSnowboardsRented = 0, intRentalHours = 0, 
			  intRentalDays = 0, intRentalWeeks = 0, strCouponCode = ""):
		self.strName = strName
		self.intID = intID
		self.intSkisRented = intSkisRented
		self.intSnowboardsRented = intSnowboardsRented
		self.intRentalHours = intRentalHours
		self.intRentalDays = intRentalDays
		self.intRentalWeeks = intRentalWeeks
		self.strCouponCode = strCouponCode

		CustomerClass._intTotalItemsRented = self.intSkisRented + self.intSnowboardsRented

	def __str__(self):
		return "The Customer is renting {} items".format(CustomerClass._intTotalItemsRented)
	
	def __repr__(self):
		strRepr = ("Name: {}, ID: {}, \n# of Skis rented: {}, # of Snowboards rented: {}," 
		"\n# of hours: {}, # of days: {}, # of weeks: {},"
	    "\nCoupon code: {}".format(self.strName, self.intID, self.intSkisRented, 
		self.intSnowboardsRented, self.intRentalHours, self.intRentalDays, self.intRentalWeeks, self.strCouponCode))
		return strRepr

		
# ------------------------------------------------------------------
# CustomerClass getters and setters
# ------------------------------------------------------------------	
	@property
	def strName(self):
		return self._strName
	
	@strName.setter
	def strName(self, strInput):
		if(str(strInput).isdecimal() == False):
			self._strName = strInput
		else:
			self._strName = ""
			raise Exception("The Name has to have letters. The value of Name was: {}".format(strInput))

	
	@property
	def intID(self):
		return self._intID
	
	@intID.setter
	def intID(self, intInput):
		if(intInput < 0):
			raise Exception("The ID has to be greater than 0. The value of ID was: {}".format(intInput))
			self._intID = 0
		else:
			self._intID = intInput

	@property
	def intSkisRented(self):
		return self._intSkisRented
	
	@intSkisRented.setter
	def intSkisRented(self, intInput):
		if(intInput < 0):
			raise Exception("The number of Skis rented has to be greater than 0. The value of intSkisRented was: {}".format(intInput))
			self._intSkisRented = 0
		else:
			self._intSkisRented = intInput

	@property
	def intSnowboardsRented(self):
		return self._intSnowboardsRented
	
	@intSnowboardsRented.setter
	def intSnowboardsRented(self, intInput):
		if(intInput < 0):
			raise Exception("The number of Snowboards rented has to be greater than 0. The value of intSnowboardsRented was: {}".format(intInput))
			self._intSnowboardsRented = 0
		else:
			self._intSnowboardsRented = intInput

	@property
	def intRentalHours(self):
		return self._intRentalHours
	
	@intRentalHours.setter
	def intRentalHours(self, intInput):
		if(intInput < 0):
			raise Exception("The number of hours for a rental has to be greater than 0. The value of intRentalHours was: {}".format(intInput))
			self._intRentalHours = 0
		else:
			self._intRentalHours = intInput

	@property
	def intRentalDays(self):
		return self._intRentalDays
			
	@intRentalDays.setter
	def intRentalDays(self, intInput):
		if(intInput < 0):
			raise Exception("The number of days for a rental has to be greater than 0. The value of intRentalDays was: {}".format(intInput))
			self._intRentalDays = 0
		else:
			self._intRentalDays = intInput

	@property
	def intRentalWeeks(self):
		return self._intRentalWeeks
			
	@intRentalWeeks.setter
	def intRentalWeeks(self, intInput):
		if(intInput < 0):
			raise Exception("The number of weeks for a rental has to be greater than 0. The value of intRentalWeeks was: {}".format(intInput))
			self._intRentalWeeks = 0
		else:
			self._intRentalWeeks = intInput

	@property
	def strCouponCode(self):
		return self._strCouponCode
	
	@strCouponCode.setter
	def strCouponCode(self, strInput):
		if(str(strInput).isdecimal() == False):
			self._strCouponCode = strInput
		else:
			self._strCouponCode = ""
			raise Exception("The coupon code has to have letters. The value of strCouponCode was: {}".format(strInput))
