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
		if intInput == int(intInput):
			if intInput > -1:
				self._intSkisRented = intInput
			else:
				raise Exception("Skis Rented must be an integer equal to or greater than 0. The value of Skis Rented was: {}".format(intInput))
		else:
			raise Exception("Skis Rented must be an integer equal to or greater than 0. The value of Skis Rented was: {}".format(intInput))

	@property
	def intSnowboardsRented(self):
		return self._intSnowboardsRented
	
	@intSnowboardsRented.setter
	def intSnowboardsRented(self, intInput):
		if intInput == int(intInput):
			if intInput > -1:
				self._intSnowboardsRented = intInput
			else:
				raise Exception("Snowboards Rented must be an integer equal to or greater than 0. The value of Snowboards Rented was: {}".format(intInput))
		else:
			raise Exception("Snowboards Rented must be an integer equal to or greater than 0. The value of Snowboards Rented was: {}".format(intInput))


	@property
	def intRentalTime(self):
		return self._intRentalTime
	
	@intRentalTime.setter
	def intRentalTime(self, intInput):
		if intInput == int(intInput):
			if intInput > -1:
				self._intRentalTime = intInput
			else:
				raise Exception("Rental Time must be an integer equal to or greater than 0. The value of Rental Time was: {}".format(intInput))
		else:
			raise Exception("Rental Time must be an integer equal to or greater than 0. The value of Rental Time was: {}".format(intInput))

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
		
		def __init__(self, intSkisRented, intSnowboardsRented, strRentalBasis, intRentalTime, bill):
			"""
			Our constructor method which instantiates various customer objects.
			"""
		
			self.intSkisRented = 0
			self.intSnowboardsRented = 0
			self.strRentalBasis = 0
			self.intRentalTime = 0
			self.bill = 0
   
		def requestSkis(self, intSkisRented):
			"""
			Takes a request from the customer for the number of Skis.
			"""
                     
			intSkisRented = input("How many skis would you like to rent?")
       
			# implement logic for invalid input
			try:
				intSkisRented = int(intSkisRented)
			except ValueError:
				print("That's not a positive integer!")
				return -1
			if intSkisRented < 1:
				print("Invalid input. Number of skis should be greater than zero!")
				return -1
			else:
				self.intSkisRented = intSkisRented
			return self.intSkisRented

		def requestSnowBoards(self, intSnowboardsRented):
			"""
			Takes a request from the customer for the number of bikes.
			"""
                     
			intSnowboardsRented = input("How many SnowBoards would you like to rent?")
       
			# implement logic for invalid input
			try:
				intSnowboardsRented = int(intSnowboardsRented)
			except ValueError:
				print("That's not a positive integer!")
				return -1
			if intSnowboardsRented < 1:
				print("Invalid input. Number of SnowBoards should be greater than zero!")
				return -1
			else:
				self.intSnowboardsRented = intSnowboardsRented
			return self.intSnowboardsRented
     
		def returnSkis(self):
			"""
			Allows customers to return their Skis to the rental shop.
			"""
			if self.strRentalBasis and self.rentalTime and self.intSkisRented:
				return self.intRentalTime, self.intRentalTime, self.intSkisRented  
			else:
				return 0,0,0
		
		def returnSnowBoards(self, intSnowboardsRented):
			"""
			Allows customers to return their SnowBoards to the rental shop.
			"""
			if self.strRentalBasis and self.intRentalTime and self.intSnowboardsRented:
				return self.intRentalTime, self.strRentalBasis, self.intSnowboardsRented  
			else:
				return 0,0,0
