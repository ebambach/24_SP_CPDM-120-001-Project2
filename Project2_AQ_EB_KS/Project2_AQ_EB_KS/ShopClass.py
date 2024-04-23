# ------------------------------------------------------------------
# Project 2 Class Area: Shop Class
# ------------------------------------------------------------------

# Used for .ceil function calculating ideal intRentalTime/strRentalBasis
import math
import datetime
from datetime import datetime, timedelta
import CustomerClass as Customer

class ShopClass(object):
    # Initial Inventory
    intInitialSkisInventory = int()
    intInitialSnowboardsInventory = int()
    # Current Inventory
    intCurrentSkisInventory = int()
    intCurrentSnowboardsInventory = int()
    # Items Rented
    _intTotalItemsRented = int()
    # Prices for Skis
    _dblSkisHourly = float(15)
    _dblSkisDaily = float(50)
    _dblSkisWeekly = float(200)
    # Prices for Snowboards
    _dblSnowboardsHourly = float(10)
    _dblSnowboardsDaily = float(40)
    _dblSnowboardsWeekly = float(160)
    # Subtotal for Skis
    _dblSkisSubtotal = float(0)
    # Subtotal for Snowboards
    _dblSnowboardsSubtotal = float(0)
    # Estimated rental price
    _dblEstimateRentalPrice = float(0)
    # Which items are discounted and full price
    _intDiscountedSkis = int()
    _intFullPriceSkis = int()
    _intDiscountedSnowboards = int()
    _intFullPriceSnowboards = int()
    # The number of skis requested
    intSkisRequested = int()
    # The number of snowboards requested
    intSnowboardsRequested = int()
    # The time basis of the potential rental
    strRentalBasis = str()
    # The amount of time for the potential rental
    intTimeRequested = int()
    # Value of the family discount, will be 25 if the order includes at least three
    # items to give 25% for 3-5 items, otherwise, this is 0
    _dblFamilyDiscount = float()
    # Coupon code for 10% discount
    strCouponCode = str()
    # If strCouponCode ends with "BBP," this variable is set to 10 to give 10% off
    _dblCouponDiscount = float()
    # List of Customers
    CustomerList = []
    # Skis rented for the day
    intDailySkisRented = int()
    # Snowboards rented for the day
    intDailySnowboardsRented = int()
    # Boolean for checking availbility
    _blnValidation = False
    # Boolean for performing return, false if performing estimate, true if performing return
    _blnReturn = False
    # Daily revenue
    dblDailyRevenue = float()
    # Rental subtotal
    dblSubTotal = float()
    # Rental grand total
    dblGrandTotal = float()

    # Set the initial quantity of Skis and Snowboards, each with a default amount of 0
    # When everything starts, the current quantity should match the initial quantity
    def __init__(self, intInitialSkisInventory = 0, intInitialSnowboardsInventory = 0):
         self.intInitialSkisInventory = intInitialSkisInventory
         self.intInitialSnowboardsInventory = intInitialSnowboardsInventory
         self.intCurrentSkisInventory = self.intInitialSkisInventory
         self.intCurrentSnowboardsInventory = self.intInitialSnowboardsInventory

    def __str__(self):
          return "Initial Skis Inventory: {}, Initial Snowboards Inventory: {}".format(self.intInitialSkisInventory, self.intInitialSnowboardsInventory)

# ------------------------------------------------------------------
# ShopClass getters and setters
# ------------------------------------------------------------------
    @property
    def intInitialSkisInventory(self):
         return self._intInitialSkisInventory
     
    @intInitialSkisInventory.setter
    def intInitialSkisInventory(self, intInput):
          if intInput == int(intInput):
               if intInput >= 0:
                     self._intInitialSkisInventory = intInput
               else:
                    raise Exception("Initial Skis Inventory must be an integer equal to or greater than 0. The value of Initial Skis Inventory was: {}".format(intInput))
          else:
               raise Exception("Initial Skis Inventory must be an integer equal to or greater than 0. The value of Initial Skis Inventory was: {}".format(intInput))
          
    @property
    def intInitialSnowboardsInventory(self):
         return self._intInitialSnowboardsInventory
     
    @intInitialSnowboardsInventory.setter
    def intInitialSnowboardsInventory(self, intInput):
          if intInput == int(intInput):
               if intInput >= 0:
                     self._intInitialSnowboardsInventory = intInput
               else:
                    raise Exception("Initial Snowboards Inventory must be an integer equal to or greater than 0. The value of Initial Snowboards Inventory was: {}".format(intInput))
          else:
               raise Exception("Initial Snowboards Inventory must be an integer equal to or greater than 0. The value of Initial Snowboards Inventory was: {}".format(intInput))



# ------------------------------------------------------------------
# Method to start estimate based on a customer's request for time and stock
# Variables:
# Numerical value of the rental time,
# String value of the rental basis, which may be "Hourly," "Daily," or "Weekly,"
# Numerical value of Skis requested,
# Numerical value of Snowboards request,
# String value of Coupon Code (if any)
# ------------------------------------------------------------------ 
    def start_Request(self, intTimeRequested = 0, strRentalBasis = "Hourly", intSkisRequested = 0, intSnowboardsRequested = 0, strCouponCode = ""):
        self._blnReturn = False
        self.strRentalBasis = strRentalBasis
        # Validate the input for the request
        self.intTimeRequested(intTimeRequested)
        if self._blnValidation == True:
            #self.strRentalBasis(strRentalBasis)
            if self._blnValidation == True:
                self.intSkisRequested(intSkisRequested)
                if self._blnValidation == True:
                    self.intSnowboardsRequested(intSnowboardsRequested)
                    if self._blnValidation == True:
                        print("Your prospective rental includes:")
                        # The request has been validated, if the order includes at least
                        # 3 items, apply the family discount
                        self.getFamilyDiscount(intSkisRequested, intSnowboardsRequested)
                        # If the strCouponCode endswith "BBP," give the 10% discount
                        self.getCouponDiscount(strCouponCode)
                        # Provide an estimate of the best price based on how much time
                        # is requested, and the basis of said time ("Hourly," "Daily," or "Weekly")
                        self.calcEstimateBestRentalPrice(self.intTimeRequested, self._intFullPriceSkis, self._intDiscountedSkis, 
                                          self._intFullPriceSnowboards, self._intDiscountedSnowboards)
                        self.confirmRental()



# ------------------------------------------------------------------
# Method to start return based on a customer's existing rental
# ------------------------------------------------------------------ 
    def return_Rental(self, intID):
        self._blnReturn = True
        for obj in self.CustomerList:
            if intID == obj.intID:
                print("Your rental involved:")
                self.strRentalBasis = obj.strRentalBasis
                # Find the difference between when the rental started and when it was returned
                intTimeDifference = self.time_Difference(obj.dtmRentalStart, datetime.now())
                # Give family discount to 3-5 items if present
                self.getFamilyDiscount(obj.intSkisRented, obj.intSnowboardsRented)
                # If the strCouponCode endswith "BBP," give the 10% discount
                self.getCouponDiscount(obj.strCouponCode)
                # Provide an estimate of the best price based on how much time
                # is requested, and the basis of said time ("Hourly," "Daily," or "Weekly")
                self.calcEstimateBestRentalPrice(intTimeDifference, self._intFullPriceSkis, self._intDiscountedSkis, 
                                          self._intFullPriceSnowboards, self._intDiscountedSnowboards)
                # Add the stock back into the inventory
                self.returnSkis(obj.intSkisRented)
                self.returnSnowboards(obj.intSnowboardsRented)
                # Print invoice
                print(" ")
                print("Rental summary:")
                print("Name: " + obj.strName)
                print("Skis rented: " + str(obj.intSkisRented))
                print("Snowboards rented: " + str(obj.intSnowboardsRented))                
                if self.strRentalBasis == "Hourly":
                    print("Rental duration: " + str(intTimeDifference) + " hours")
                elif self.strRentalBasis == "Daily":
                    print("Rental duration: " + str(self.intTimeRequested) + " days")
                else:
                    print("Rental duration: " + str(intTimeDifference) + " weeks")
                print("Rental subtotal: " + str(self.dblSubTotal))
                if self._dblFamilyDiscount == 25:
                    print("Family discount applied")
                if self._dblCouponDiscount == 10:
                    print("Coupon discount appplied")
                print("Rental grand total: " + str(self.dblGrandTotal))



# ------------------------------------------------------------------
# Validation for value of the rental time
# ------------------------------------------------------------------
    def intTimeRequested(self, intInput):
        if intInput == int(intInput):
            if intInput > 0:
                self.intTimeRequested = intInput
                self._blnValidation = True
            else:
                self._blnValidation = False
                raise Exception("The amount of time for a rental must be an integer greater than 0. The value of the time requested was: {}".format(intInput))
        else:
            self._blnValidation = False
            raise Exception("The amount of time for a rental must be an integer greater than 0. The value of the time requested was: {}".format(intInput))



# ------------------------------------------------------------------
# Validation for basis of the rental time
# ------------------------------------------------------------------
    def strRentalBasis(self, strInput):
        if (strInput == "Hourly") or (strInput == "Daily") or (strInput == "Weekly"):
            self._strRentalBasis = strInput
            self._blnValidation = True
        else:
            self._blnValidation = False
            raise Exception("The rental basis must be Hourly, Daily, or Weekly. The rental basis entered was: {}".format(strInput))
            self._strRentalBasis = ""



# ------------------------------------------------------------------
# Validation for number of Skis
# ------------------------------------------------------------------
    def intSkisRequested(self, intInput):
        if intInput == int(intInput):
            if intInput > -1:
                self._intSkisRequested = intInput
                self._blnValidation = True
            else:
                self._blnValidation = False
                raise Exception("Skis Rented must be an integer equal to or greater than 0. The value of Skis Rented was: {}".format(intInput))
        else:
            self._blnValidation = False
            raise Exception("Skis Rented must be an integer equal to or greater than 0. The value of Skis Rented was: {}".format(intInput))



# ------------------------------------------------------------------
# Validation for number of Snowboards
# ------------------------------------------------------------------
    def intSnowboardsRequested(self, intInput):
        if intInput == int(intInput):
            if intInput > -1:
                self._intSnowboardsRequested = intInput
                self._blnValidation = True
            else:
                self._blnValidation = False
                raise Exception("Snowboards Rented must be an integer equal to or greater than 0. The value of Snowboards Rented was: {}".format(intInput))
        else:
            self._blnValidation = False
            raise Exception("Snowboards Rented must be an integer equal to or greater than 0. The value of Snowboards Rented was: {}".format(intInput))



# ------------------------------------------------------------------
# Method to display the currently available number of Skis and Snowboards
# ------------------------------------------------------------------    
    def display_CurrentInventory(self):
        if self.intCurrentSkisInventory == 1:
            print("There is currently " + str(self.intCurrentSkisInventory) + " pair of skis available to rent.")
        else:
            print("There are currently " + str(self.intCurrentSkisInventory) + " pairs of skis available to rent.")
        if self.intCurrentSnowboardsInventory == 1:
            print("There is currently " + str(self.intCurrentSnowboardsInventory) + " snowboard available to rent.")
        else:
            print("There are currently " + str(self.intCurrentSnowboardsInventory) + " snowboards available to rent.")



# ------------------------------------------------------------------
# Method to check if the request number of Skis and Snowboards are available for rent
# ------------------------------------------------------------------ 
    def check_CurrentInventory(self, intRequestedSkis = 0, intRequestedSnowboards = 0):
        if intRequestedSkis > self.intCurrentSkisInventory:
            if intRequestedSkis == 1:
                print("This rental cannot be completed, " + str(intRequestedSkis) + " pair of skis is more than what is currently available.")
            else:
                print("This rental cannot be completed, " + str(intRequestedSkis) + " pairs of skis is more than what is currently available.")
            self.display_CurrentInventory()
            self._blnValidation = False
        elif intRequestedSnowboards > self.intCurrentSnowboardsInventory:
            if intRequestedSnowboards == 1:
                print("This rental cannot be completed, " + str(intRequestedSnowboards) + " snowboard is more than what is currently available.")
            else:
                print("This rental cannot be completed, " + str(intRequestedSnowboards) + " snowboards is more than what is currently available.")
            self.display_CurrentInventory()
        else:
            self._blnValidation = True



# ------------------------------------------------------------------
# Method to print when rental begins
# ------------------------------------------------------------------
    def rentalTime(self):
        now = datetime.now()
        print("The current time is " + str(now.month) + "-" + str(now.day) + "-" + str(now.year) + 
                  " at " + str(now.hour) + ":" + str(now.minute) + ".")



# ------------------------------------------------------------------
# Methods to rents equipment on either an hourly, a daily, or a weekly basis
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# Method to rent Skis on an hourly basis
# ------------------------------------------------------------------  
    def rentSkisHourly(self, intRequestedSkis):
        # Confirm if the Inventory has enough equipment to rent
        self.check_CurrentInventory(intRequestedSkis)
        if self._blnValidation == True:            
            # State how many Skis they rented, that the time basis is hourly, at what time the rental occurred, and how much
            # each pair of Skis cost to rent.
            if intRequestedSkis == 1:
                print("Your rental is set for " + str(intRequestedSkis) +" pair of skis on an hourly basis.")
            else:
                print("Your rental is set for " + str(intRequestedSkis) + " pairs of skis on an hourly basis.")
            self.rentalTime()
            print("The hourly rent is $" + str(self._dblSkisHourly) + " per hour for each pair of skis.")
            
            self._blnValidation = False



# ------------------------------------------------------------------
# Method to rent Snowboards on an hourly basis
# ------------------------------------------------------------------  
    def rentSnowboardsHourly(self, intRequestedSnowboards):
        # Confirm if the Inventory has enough equipment to rent
        self.check_CurrentInventory(intRequestedSnowboards)
        if self._blnValidation == True:            
            # State how many Snowboards they rented, that the time basis is hourly, at what time the rental occurred, and how much
            # each pair of Snowboards cost to rent.
            if intRequestedSnowboards == 1:
                print("Your rental is set for " + str(intRequestedSnowboards) +" snowboard on an hourly basis.")
            else:
                print("Your rental is set for " + str(intRequestedSnowboards) + " snowboards on an hourly basis.")
            self.rentalTime()
            print("The hourly rent is $" + str(self._dblSnowboardsHourly) + " per hour for each snowboard.")
            # Reduce the current inventory by the quantity of Snowboards that were rented.
            
            self._blnValidation = False



# ------------------------------------------------------------------
# Method to rent Skis on a daily basis
# ------------------------------------------------------------------  
    def rentSkisDaily(self, intRequestedSkis):
        # Confirm if the Inventory has enough equipment to rent
        self.check_CurrentInventory(intRequestedSkis)
        if self._blnValidation == True:            
            # State how many Skis they rented, that the time basis is daily, at what time the rental occurred, and how much
            # each pair of Skis cost to rent.
            if intRequestedSkis == 1:
                print("Your rental is set for " + str(intRequestedSkis) +" pair of skis on an daily basis.")
            else:
                print("Your rental is set for " + str(intRequestedSkis) + " pairs of skis on an daily basis.")
            self.rentalTime()
            print("The daily rent is $" + str(self._dblSkisDaily) + " per day for each pair of skis.")            
            
            self._blnValidation = False



# ------------------------------------------------------------------
# Method to rent Snowboards on a daily basis
# ------------------------------------------------------------------  
    def rentSnowboardsDaily(self, intRequestedSnowboards):
        # Confirm if the Inventory has enough equipment to rent
        self.check_CurrentInventory(intRequestedSnowboards)
        if self._blnValidation == True:            
            # State how many Snowboards they rented, that the time basis is daily, at what time the rental occurred, and how much
            # each pair of Snowboards cost to rent.
            if intRequestedSnowboards == 1:
                print("Your rental is set for " + str(intRequestedSnowboards) +" snowboard on an daily basis.")
            else:
                print("Your rental is set for " + str(intRequestedSnowboards) + " snowboards on an daily basis.")
            self.rentalTime()
            print("The daily rent is $" + str(self._dblSnowboardsDaily) + " per day for each snowboard.")
            
            self._blnValidation = False



# ------------------------------------------------------------------
# Method to rent Skis on a weekly basis
# ------------------------------------------------------------------  
    def rentSkisWeekly(self, intRequestedSkis):
        # Confirm if the Inventory has enough equipment to rent
        self.check_CurrentInventory(intRequestedSkis)
        if self._blnValidation == True:            
            # State how many Skis they rented, that the time basis is weekly, at what time the rental occurred, and how much
            # each pair of Skis cost to rent.
            if intRequestedSkis == 1:
                print("Your rental is set for " + str(intRequestedSkis) +" pair of skis on an weekly basis.")
            else:
                print("Your rental is set for " + str(intRequestedSkis) + " pairs of skis on an weekly basis.")
            self.rentalTime()
            print("The weekly rent is $" + str(self._dblSkisWeekly) + " per week for each pair of skis.")
            
            self._blnValidation = False



# ------------------------------------------------------------------
# Method to rent Snowboards on a weekly basis
# ------------------------------------------------------------------  
    def rentSnowboardsWeekly(self, intRequestedSnowboards):
        # Confirm if the Inventory has enough equipment to rent
        self.check_CurrentInventory(intRequestedSnowboards)
        if self._blnValidation == True:            
            # State how many Snowboards they rented, that the time basis is weekly, at what time the rental occurred, and how much
            # each pair of Snowboards cost to rent.
            if intRequestedSnowboards == 1:
                print("Your rental is set for " + str(intRequestedSnowboards) +" snowboard on an weekly basis.")
            else:
                print("Your rental is set for " + str(intRequestedSnowboards) + " snowboards on an weekly basis.")
            self.rentalTime()
            print("The weekly rent is $" + str(self._dblSnowboardsWeekly) + " per week for each snowboard.")
            
            self._blnValidation = False


# ------------------------------------------------------------------
# Method to return Skis to inventory
# ------------------------------------------------------------------
    def returnSkis(self, intReturnedSkis):
        self.intCurrentSkisInventory += intReturnedSkis



# ------------------------------------------------------------------
# Method to return Snowboards to inventory
# ------------------------------------------------------------------
    def returnSnowboards(self, intReturnedSnowboards):
        self.intCurrentSnowboardsInventory += intReturnedSnowboards



# ------------------------------------------------------------------
# Discount Coupons for Total Items Rented 
# ------------------------------------------------------------------
   
    # Applying discount based on the total number of items rented
    def getFamilyDiscount(self, intSkisRented = 0, intSnowboardsRented = 0):
        self.intSkisRented = intSkisRented
        self.intSnowboardsRented = intSnowboardsRented

        _intItemsRented = self.intSkisRented + self.intSnowboardsRented

        # Determining which items get a discount, discounting Skis before Snowboards
        if _intItemsRented < 3:
            self._intFullPriceSkis = intSkisRented
            self._intFullPriceSnowboards = intSnowboardsRented
            self._intDiscountedSkis = 0
            self._intDiscountedSnowboards = 0
        else:
            self._dblFamilyDiscount = 25
            if _intItemsRented < 6:
                self._intFullPriceSkis = 0
                self._intFullPriceSnowboards = 0
                self._intDiscountedSkis = intSkisRented
                self._intDiscountedSnowboards = intSnowboardsRented
            else:
                if intSkisRented >= 5:
                    self._intDiscountedSkis = 5
                    self._intFullPriceSkis = intSkisRented - 5
                    self._intDiscountedSnowboards = 0
                    self._intFullPriceSnowboards = intSnowboardsRented
                else:
                    self._intDiscountedSkis = intSkisRented
                    self._intFullPriceSkis = 0
                    self._intDiscountedSnowboards = 5 - intSkisRented
                    self._intFullPriceSnowboards = intSnowboardsRented - _intDiscountedSnowboards
        
        print("Total Items Rented: ", _intItemsRented)
        print("Full Price Skis: ", self._intFullPriceSkis)
        print("25% Discounted Skis: ", self._intDiscountedSkis)
        print("Full Price Snowboards: ", self._intFullPriceSnowboards)
        print("25% Discounted Snowboards: ", self._intDiscountedSnowboards)



    # Applying discount based on the coupon code
    def getCouponDiscount(self, strCouponCode):
        self.strCouponCode = strCouponCode
        if self.strCouponCode.endswith("BBP"):
            print("Coupon Discount: 10%")
            self._dblCouponDiscount = 10



# ------------------------------------------------------------------
# Method for Calculating Estimate Rental Price (Best Price)
# ------------------------------------------------------------------
    def calcEstimateBestRentalPrice(self, intRentalTime = 0, _intFullPriceSkis = 0, _intDiscountedSkis = 0, _intFullPriceSnowboards = 0, _intDiscountedSnowboards = 0):

        if self.strRentalBasis == "Hourly":
            if intRentalTime * (self._dblSkisHourly + self._dblSnowboardsHourly) > self._dblSkisWeekly + self._dblSnowboardsWeekly:
                # Weekly was determined to be cheaper than Hourly, charge the Weekly rate  
                self.strRentalBasis = "Weekly"
                if self.intSkisRented > 0:
                    self.rentSkisWeekly(self.intSkisRented)
                if self.intSnowboardsRented > 0:
                    self.rentSnowboardsWeekly(self.intSnowboardsRented)
                self.intTimeRequested = math.ceil(self.intTimeRequested  / 168)
                # Calculate the pre-discount price
                self.dblSubTotal = ((_intFullPriceSkis + _intDiscountedSkis) * intRentalTime * self._dblSkisWeekly) + ((_intFullPriceSnowboards + _intDiscountedSnowboards) * intRentalTime * self._dblSnowboardsWeekly)
                # Calculate for subtotal weekly price of discounted skis + price of non-discounted skis
                _dblSkisSubtotal = ((_intDiscountedSkis * intRentalTime * self._dblSkisWeekly) * (1 - ((self._dblFamilyDiscount + self._dblCouponDiscount) / 100))) + (_intFullPriceSkis * intRentalTime * self._dblSkisWeekly)
                # Calculate for subtotal weekly price of discounted snowboards + price of non-discounted snowboards
                _dblSnowboardsSubtotal = ((_intDiscountedSnowboards * intRentalTime * self._dblSnowboardsWeekly) * (1 - ((self._dblFamilyDiscount + self._dblCouponDiscount) / 100))) + (_intFullPriceSnowboards * intRentalTime * self._dblSnowboardsWeekly)
                # Calculate for Estimated RentalPrice by adding the Skis Subtotal and Snowboards Subtotal
                self._dblEstimateRentalPrice = _dblSkisSubtotal + _dblSnowboardsSubtotal
            else:
                if intRentalTime * (self._dblSkisHourly + self._dblSnowboardsHourly) > self._dblSkisDaily + self._dblSnowboardsDaily:
                    # Daily was determined to be cheaper than Hourly, charge the Daily rate  
                    self.strRentalBasis = "Daily"
                    if self.intSkisRented > 0:
                        self.rentSkisDaily(self.intSkisRented)
                    if self.intSnowboardsRented > 0:
                        self.rentSnowboardsDaily(self.intSnowboardsRented)
                    self.intTimeRequested = math.ceil(self.intTimeRequested / 24)
                    # Calculate the pre-discount price
                    self.dblSubTotal = ((_intFullPriceSkis + _intDiscountedSkis) * intRentalTime * self._dblSkisDaily) + ((_intFullPriceSnowboards + _intDiscountedSnowboards) * intRentalTime * self._dblSnowboardsDaily)
                    # Calculate for subtotal daily price of discounted skis + price of non-discounted skis
                    _dblSkisSubtotal = ((_intDiscountedSkis * intRentalTime * self._dblSkisDaily) * (1 - ((self._dblFamilyDiscount + self._dblCouponDiscount) / 100))) + (_intFullPriceSkis * intRentalTime * self._dblSkisDaily)
                    # Calculate for subtotal daily price of discounted snowboards + price of non-discounted snowboards
                    _dblSnowboardsSubtotal = ((_intDiscountedSnowboards * intRentalTime * self._dblSnowboardsDaily) * (1 - ((self._dblFamilyDiscount + self._dblCouponDiscount) / 100))) + (_intFullPriceSnowboards * intRentalTime * self._dblSnowboardsDaily)
                    # Calculate for Estimated RentalPrice by adding the Skis Subtotal and Snowboards Subtotal
                    self._dblEstimateRentalPrice = _dblSkisSubtotal + _dblSnowboardsSubtotal
                else:
                    # Charge the Hourly rate
                    self.strRentalBasis = "Hourly"
                    if self.intSkisRented > 0:
                        self.rentSkisHourly(self.intSkisRented)
                    if self.intSnowboardsRented > 0:
                        self.rentSnowboardsHourly(self.intSnowboardsRented)
                    # Calculate the pre-discount price
                    self.dblSubTotal = ((_intFullPriceSkis + _intDiscountedSkis) * intRentalTime * self._dblSkisHourly) + ((_intFullPriceSnowboards + _intDiscountedSnowboards) * intRentalTime * self._dblSnowboardsHourly)
                    # Calculate for subtotal hourly price of discounted skis + price of non-discounted skis
                    _dblSkisSubtotal = ((_intDiscountedSkis * intRentalTime * self._dblSkisHourly) * (1 - ((self._dblFamilyDiscount + self._dblCouponDiscount) / 100))) + (_intFullPriceSkis * intRentalTime * self._dblSkisHourly)
                    # Calculate for subtotal hourly price of discounted snowboards + price of non-discounted snowboards
                    _dblSnowboardsSubtotal = ((_intDiscountedSnowboards * intRentalTime * self._dblSnowboardsHourly) * (1 - ((self._dblFamilyDiscount + self._dblCouponDiscount) / 100))) + (_intFullPriceSnowboards * intRentalTime * self._dblSnowboardsHourly)
                    # Calculate for Estimated RentalPrice by adding the Skis Subtotal and Snowboards Subtotal
                    self._dblEstimateRentalPrice = _dblSkisSubtotal + _dblSnowboardsSubtotal
        else:
            if self.strRentalBasis == "Daily":
                if intRentalTime * (self._dblSkisDaily * self._dblSnowboardsDaily) > self._dblSkisWeekly + self._dblSnowboardsWeekly:
                    # Weekly was determined to be cheaper than Daily, charge the Weekly rate
                    self.strRentalBasis = "Weekly"
                    if self.intSkisRented > 0:
                        self.rentSkisWeekly(self.intSkisRented)
                    if self.intSnowboardsRented > 0:
                        self.rentSnowboardsWeekly(self.intSnowboardsRented)
                    self.intTimeRequested = math.ceil(self.intTimeRequested  / 168)
                    # Calculate the pre-discount price
                    self.dblSubTotal = ((_intFullPriceSkis + _intDiscountedSkis) * intRentalTime * self._dblSkisWeekly) + ((_intFullPriceSnowboards + _intDiscountedSnowboards) * intRentalTime * self._dblSnowboardsWeekly)
                    # Calculate for Subtotal weekly price of discounted skis + price of non-discounted skis
                    _dblSkisSubtotal = ((_intDiscountedSkis * intRentalTime * self._dblSkisWeekly) * (1 - ((self._dblFamilyDiscount + self._dblCouponDiscount) / 100))) + (_intFullPriceSkis * intRentalTime * self._dblSkisWeekly)
                    # Calculate for Subtotal weekly price of discounted snowboards + price of non-discounted snowboards
                    _dblSnowboardsSubtotal = ((_intDiscountedSnowboards * intRentalTime * self._dblSnowboardsWeekly) * (1 - ((self._dblFamilyDiscount + self._dblCouponDiscount) / 100))) + (_intFullPriceSnowboards * intRentalTime * self._dblSnowboardsWeekly)
                    # Calculate for Estimated RentalPrice by adding the Skis Subtotal and Snowboards Subtotal
                    self._dblEstimateRentalPrice = _dblSkisSubtotal + _dblSnowboardsSubtotal
                else:
                    # charge the Daily rate
                    self.strRentalBasis = "Daily"
                    if self.intSkisRented > 0:
                        self.rentSkisDaily(self.intSkisRented)
                    if self.intSnowboardsRented > 0:
                        self.rentSnowboardsDaily(self.intSnowboardsRented)
                    self.intTimeRequested = math.ceil(self.intTimeRequested / 24)
                    # Calculate the pre-discount price
                    self.dblSubTotal = ((_intFullPriceSkis + _intDiscountedSkis) * intRentalTime * self._dblSkisDaily) + ((_intFullPriceSnowboards + _intDiscountedSnowboards) * intRentalTime * self._dblSnowboardsDaily)
                    # Calculate for Subtotal daily price of discounted skis + price of non-discounted skis
                    _dblSkisSubtotal = ((_intDiscountedSkis * intRentalTime * self._dblSkisDaily) * (1 - ((self._dblFamilyDiscount + self._dblCouponDiscount) / 100))) + (_intFullPriceSkis * intRentalTime * self._dblSkisDaily)
                    # Calculate for Subtotal daily price of discounted snowboards + price of non-discounted snowboards
                    _dblSnowboardsSubtotal = ((_intDiscountedSnowboards * intRentalTime * self._dblSnowboardsDaily) * (1 - ((self._dblFamilyDiscount + self._dblCouponDiscount) / 100))) + (_intFullPriceSnowboards * intRentalTime * self._dblSnowboardsDaily)
                    # Calculate for Estimated RentalPrice by adding the Skis Subtotal and Snowboards Subtotal
                    self._dblEstimateRentalPrice = _dblSkisSubtotal + _dblSnowboardsSubtotal
            else:
                # Charge the Weekly rate
                self.strRentalBasis = "Weekly"
                if self.intSkisRented > 0:
                    self.rentSkisWeekly(self.intSkisRented)
                if self.intSnowboardsRented > 0:
                    self.rentSnowboardsWeekly(self.intSnowboardsRented)
                self.intTimeRequested = math.ceil(self.intTimeRequested / 168) 
                # Calculate the pre-discount price
                self.dblSubTotal = ((_intFullPriceSkis + _intDiscountedSkis) * intRentalTime * self._dblSkisWeekly) + ((_intFullPriceSnowboards + _intDiscountedSnowboards) * intRentalTime * self._dblSnowboardsWeekly)
                # Calculate for Subtotal weekly price of discounted skis + price of non-discounted skis
                _dblSkisSubtotal = ((_intDiscountedSkis * intRentalTime * self._dblSkisWeekly) * (1 - ((self._dblFamilyDiscount + self._dblCouponDiscount) / 100))) + (_intFullPriceSkis * intRentalTime * self._dblSkisWeekly)
                # Calculate for Subtotal weekly price of discounted snowboards + price of non-discounted snowboards
                _dblSnowboardsSubtotal = ((_intDiscountedSnowboards * intRentalTime * self._dblSnowboardsWeekly) * (1 - ((self._dblFamilyDiscount + self._dblCouponDiscount) / 100))) + (_intFullPriceSnowboards * intRentalTime * self._dblSnowboardsWeekly)
                # Calculate for Estimated RentalPrice by adding the Skis Subtotal and Snowboards Subtotal
                self._dblEstimateRentalPrice = _dblSkisSubtotal + _dblSnowboardsSubtotal 
                
        print("The Rental Price is: ", self._dblEstimateRentalPrice)
        if self._blnReturn == True:
            # Set the grand total of the rental return to the calculated price
            self.dblGrandTotal = self._dblEstimateRentalPrice
            self.collect_Fee()
        return self._dblEstimateRentalPrice



# ------------------------------------------------------------------
# Method to accumulate the daily revenue when a rental is returned
# ------------------------------------------------------------------
    def collect_Fee(self):
        self.dblDailyRevenue += self._dblEstimateRentalPrice



# ------------------------------------------------------------------
# Method to calculate time difference between initial requested time and actual rental time
# ------------------------------------------------------------------
    def time_Difference(self, estimated_Time, actual_Time):
        # Trim down the time to Year, Month, Day and Hour:Minutes
        estimated_Time = str(estimated_Time)[:-10]
        actual_Time = str(actual_Time)[:-10]
        estimated_Time = datetime.strptime(estimated_Time, "%Y-%m-%d %H:%M")
        actual_Time = datetime.strptime(actual_Time, "%Y-%m-%d %H:%M")
        intDaysDifference = (abs(actual_Time.day - estimated_Time.day)) #(abs((actual_Time - estimated_Time).days))
        if intDaysDifference > 0:
            self.strRentalBasis = "Daily"
            return intDaysDifference
        else:
            intHoursDifference = (abs(actual_Time.hour - estimated_Time.hour))
            self.strRentalBasis = "Hourly"
            return intHoursDifference



# ------------------------------------------------------------------
# Method to confirm rental
# ------------------------------------------------------------------
    def confirmRental(self):
        print(" ")
        print("Confirm rental?")
        strInput = str(input("Enter 1 for Yes, or 2 for No: "))
        if strInput == "1":
            strCustomerName = str(input("Please enter a name for the rental: "))
            intID = int(input("Please your phone number: "))
            self.CustomerList.append(Customer.CustomerClass(strCustomerName, intID, self.intTimeRequested, self.strRentalBasis, 
                                         self.intSkisRented, self.intSnowboardsRented, 
                                         self.strCouponCode, datetime.now()))
            self.intCurrentSkisInventory -= self.intSkisRented
            self.intCurrentSnowboardsInventory -= self.intSnowboardsRented
            self.intDailySkisRented += self.intSkisRented
            self.intDailySnowboardsRented += self.intSnowboardsRented
            print(" ")
            


