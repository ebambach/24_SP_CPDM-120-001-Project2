# -----------------------------------------------------------------
# Assignment Name:      Project 2
# Name:                 Team B
# -----------------------------------------------------------------
from ShopClass import ShopClass
import datetime
from datetime import datetime, timedelta
# ------------------------------------------------------------------
# Project 2 Class Area
# ------------------------------------------------------------------
class CustomerClass(object):
	_intTotalItemsRented = int(0)
	_intOrderItemsRented = int(0)
	_dblDiscount = float(0)

# ------------------------------------------------------------------
# CustomerClass constructor
# ------------------------------------------------------------------	
	def __init__(self, strName, intID, intRentalTime, strRentalBasis, intSkisRented = 0, intSnowboardsRented = 0, strCouponCode = "", dtmRentalStart = 0):
		self.strName = strName
		self.intID = intID
		self.intRentalTime = intRentalTime
		self.strRentalBasis = strRentalBasis
		self.intSkisRented = intSkisRented
		self.intSnowboardsRented = intSnowboardsRented
		self.strCouponCode = strCouponCode
		self.dtmRentalStart = dtmRentalStart

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
	def strRentalBasis(self, strInput):
		if (strInput == "Hourly") or (strInput == "Daily") or (strInput == "Weekly"):
			self._strRentalBasis = strInput
		else:
			raise Exception("The rental basis must be Hourly, Daily, or Weekly. The rental basis entered was: {}".format(strInput))
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



# ------------------------------------------------------------------
# Method for when a Customer is ready to rent items
# ------------------------------------------------------------------
	def start_Rental(self, intRentalTime, strRentalBasis, intSkisRented, intSnowboardsRented, strCouponCode):
		blnValidRental = bool(False)
		# Were any pieces of equipment actually requested?
		if intSkisRented > 0 or intSnowboardsRented > 0:
			intSkisInventory = int(ShopClass.get_CurrentSkisInventory())
			intSnowboardsInventory = int(ShopClass.get_CurrentSnowboardsInventory())
			# Is the request less than or equal to the current inventory?
			if intSkisInventory >= intSkisRented and intSnowboardsInventory>= intSnowboardsRented:			   
				# Remove the amount of equipment rented from the current inventory
				ShopClass.intCurrentSkisInventory -= intSkisRented
				ShopClass.intCurrentSnowboardsInventory -= intSnowboardsRented

				# Record the amount of equipment rented to the Customer
				self.intSkisRented += intSkisRented
				self.intSnowboardsRented += intSnowboardsRented				

				# Add the amount of equipment rented to the value for the day's rentals
				ShopClass.intDailySkisRented += intSkisRented
				ShopClass.intDailySnowboardsRented += intSnowboardsRented

				blnValidRental = True
				# Calculate the estimated best price
				ShopClass.start_Request(self, intRentalTime, strRentalBasis, intSkisRented, intSnowboardsRented, strCouponCode)
			else:
				blnValidRental = False
		else:
			blnValidRental = False

		return blnValidRental



# ------------------------------------------------------------------
# Method for when a Customer is ready to return Skis and/or Snowboards
# ------------------------------------------------------------------
	def end_Rental(self, strName, intID, strRentalBasis = "Hourly", intSkisRented = 0, intSnowboardsRented = 0, strCouponCode = "", dtmRentalStart = datetime.now() + timedelta(hours=-3)):
		# Return the amount of equipment rented to the current inventory
		ShopClass.intCurrentSkisInventory += intSkisRented
		ShopClass.intCurrentSnowboardsInventory += intSnowboardsRented

		# Perform the math to get the grand total of the order
		ShopClass.return_Rental(self, strName, intID, strRentalBasis, intSkisRented, intSnowboardsRented, strCouponCode, dtmRentalStart)

		# Add the grand total to the daily revenue
		ShopClass.collect_Fee(ShopClass.dblGrandTotal)
