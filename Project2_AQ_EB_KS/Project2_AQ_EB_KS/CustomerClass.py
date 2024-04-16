# -----------------------------------------------------------------
# Assignment Name:      Project 2
# Name:                 Team B
# -----------------------------------------------------------------

# ------------------------------------------------------------------
# Project 2 Class Area
# ------------------------------------------------------------------
class CustomerClass(object):
	_intTotalItemsRented = int(0)
	_dblDiscount = float(0)
# ------------------------------------------------------------------
# CustomerClass constructor
# ------------------------------------------------------------------	
	def __init__(self, strName, intID, intRentalTime, strRentalBasis, intSkisRented = 0, intSnowboardsRented = 0, intRentalWeeks = 0, strCouponCode = ""):
		self.strName = strName
		self.intID = intID
		self.intRentalTime = intRentalTime
		self.strRentalBasis = strRentalBasis
		self.intSkisRented = intSkisRented
		self.intSnowboardsRented = intSnowboardsRented
		self.strCouponCode = strCouponCode

		CustomerClass._intTotalItemsRented = self.intSkisRented + self.intSnowboardsRented

	def __str__(self):
		return "The Customer is renting {} items".format(CustomerClass._intTotalItemsRented)
	
	# def __repr__(self):
	# 	strRepr = ("Name: {}, ID: {}, \n# of Skis rented: {}, # of Snowboards rented: {}," 
	# 	"\n# of hours: {}, # of days: {}, # of weeks: {},"
	#     "\nCoupon code: {}".format(self.strName, self.intID, self.intSkisRented, 
	# 	self.intSnowboardsRented, self.intRentalHours, self.intRentalDays, self.intRentalWeeks, self.strCouponCode))
	# 	return strRepr
 
	def __repr__(self):
		strRepr = ("Name: {} \nID: {} \nRental Duration: {}, {}\n# of Skis rented: {} \n# of Snowboards rented: {}" 
	    "\nCoupon code: {}".format(self.strName, self.intID, self.intRentalTime, self.strRentalBasis, self.intSkisRented, 
		self.intSnowboardsRented, self.strCouponCode))
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
	def intRentalTime(self):
		return self._intRentalTime
	
	@intRentalTime.setter
	def intRentalTime(self, intInput):
		if(intInput < 0):
			raise Exception("The rental time has to be greater than 0. The value of intRentalTime was: {}".format(intInput))
			self._intRentalTime = 0
		else:
			self._intRentalTime = intInput

	@property
	def strRentalBasis(self):
		return self._strRentalBasis

	@strRentalBasis.setter
	def strRentalBasis(self, intInput):
		if (intInput == "Hourly") or (intInput == "Daily") or (intInput == "Weekly"):
			self._strRentalBasis = intInput
		else:
			raise Exception("The rental basis must be Hourly, Daily, or Weekly. The rental basis entered was: {}".format(intInput))
			self._strRentalBasis = ""

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
		
# Testing

Test = CustomerClass("Ana", 123, 8, "Hourly", 2, 2)
print(Test)
print(repr(Test))