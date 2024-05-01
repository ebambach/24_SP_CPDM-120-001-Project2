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
    # Numerical value of discounts applied to the order
    dblDiscountValue = float()

    # Set the initial quantity of Skis and Snowboards, each with a default amount of 0
    # When everything starts, the current quantity should match the initial quantity
    def __init__(self, intInitialSkisInventory = 0, intInitialSnowboardsInventory = 0):
         ShopClass.intInitialSkisInventory = intInitialSkisInventory
         ShopClass.intInitialSnowboardsInventory = intInitialSnowboardsInventory
         ShopClass.intCurrentSkisInventory = self.intInitialSkisInventory
         ShopClass.intCurrentSnowboardsInventory = self.intInitialSnowboardsInventory

    def __str__(self):
          return "Initial Skis Inventory: {}, Initial Snowboards Inventory: {}".format(ShopClass.intInitialSkisInventory, ShopClass.intInitialSnowboardsInventory)

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
# Method to return the currently available number of Skis
# ------------------------------------------------------------------    
    def get_CurrentSkisInventory():
        return ShopClass.intCurrentSkisInventory



# ------------------------------------------------------------------
# Method to return the currently available number of Snowboards
# ------------------------------------------------------------------    
    def get_CurrentSnowboardsInventory():
        return ShopClass.intCurrentSnowboardsInventory



# ------------------------------------------------------------------
# Method to return the number of Skis rented for the day
# ------------------------------------------------------------------    
    def get_DailyRentedSkis(self):
        return ShopClass.intDailySkisRented


# ------------------------------------------------------------------
# Method to return the number of Snowboards rented for the day
# ------------------------------------------------------------------    
    def get_DailyRentedSnowboards(self):
        return ShopClass.intDailySnowboardsRented



# ------------------------------------------------------------------
# Method to return the daily revenue
# ------------------------------------------------------------------    
    def get_DailyRevenue(self):
        return ShopClass.dblDailyRevenue



# ------------------------------------------------------------------
# Method to start estimate based on a customer's request for time and stock
# Variables:
# Numerical value of the rental time,
# String value of the rental basis, which may be "Hourly," "Daily," or "Weekly,"
# Numerical value of Skis requested,
# Numerical value of Snowboards request,
# String value of Coupon Code (if any)
# Methods called:
# getFamilyDiscount to apply the 25% discount to 3-5 items, if applicable
# getCouponDiscount to apply the 10% discount to the whole order, if coupon code ending with "BBP" given
# calcEstimateBestRentalPrice to determine the best price based on the time requested and the time basis
# ------------------------------------------------------------------ 
    def start_Request(self, intTimeRequested = 0, strRentalBasis = "Hourly", intSkisRequested = 0, intSnowboardsRequested = 0, strCouponCode = ""):
        self._blnReturn = False
        self.strRentalBasis = strRentalBasis
        # The request has been validated, if the order includes at least
        # 3 items, apply the family discount
        ShopClass.getFamilyDiscount(intSkisRequested, intSnowboardsRequested)
        # If the strCouponCode endswith "BBP," give the 10% discount
        ShopClass.getCouponDiscount(self, strCouponCode)
        # Provide an estimate of the best price based on how much time
        # is requested, and the basis of said time ("Hourly," "Daily," or "Weekly")
        ShopClass.calcEstimateBestRentalPrice(self, intTimeRequested, ShopClass._intFullPriceSkis, ShopClass._intDiscountedSkis, 
                                          ShopClass._intFullPriceSnowboards, ShopClass._intDiscountedSnowboards)
        
        return ShopClass._dblEstimateRentalPrice


# ------------------------------------------------------------------
# Method to start return based on a customer's existing rental
# ------------------------------------------------------------------ 
    def return_Rental(self, strName, intID, strRentalBasis, intSkisRented, intSnowboardsRented, strCouponCode, dtmRentalStart):
        ShopClass._blnReturn = True
        ShopClass.strRentalBasis = strRentalBasis
                # Find the difference between when the rental started and when it was returned
                # To test different time values, use code such as intTimeDifference = self.time_Difference(obj.dtmRentalStart + timedelta(hours=-4), datetime.now())
        intTimeDifference = ShopClass.time_Difference(self, dtmRentalStart, datetime.now())
                # Give family discount to 3-5 items if present
        ShopClass.getFamilyDiscount(intSkisRented, intSnowboardsRented)
                # If the strCouponCode endswith "BBP," give the 10% discount
        ShopClass.getCouponDiscount(self, strCouponCode)
                # Provide an estimate of the best price based on how much time
                # is requested, and the basis of said time ("Hourly," "Daily," or "Weekly")
        ShopClass.calcEstimateBestRentalPrice(self, intTimeDifference, ShopClass._intFullPriceSkis, ShopClass._intDiscountedSkis, 
                                          ShopClass._intFullPriceSnowboards, ShopClass._intDiscountedSnowboards)
                # Add the stock back into the inventory
        ShopClass.returnSkis(self, intSkisRented)
        ShopClass.returnSnowboards(self, intSnowboardsRented)

        return ShopClass.dblSubTotal, ShopClass.dblDiscountValue, ShopClass.dblGrandTotal        


# ------------------------------------------------------------------
# Method to get when datetime.now()
# ------------------------------------------------------------------
    def rentalTime(self):
        now = datetime.now()
        return now



# ------------------------------------------------------------------
# Discount Coupons for Total Items Rented 
# ------------------------------------------------------------------
   
    # Applying discount based on the total number of items rented
    def getFamilyDiscount(intSkisRented = 0, intSnowboardsRented = 0):
        ShopClass.intSkisRented = intSkisRented
        ShopClass.intSnowboardsRented = intSnowboardsRented

        _intItemsRented = ShopClass.intSkisRented + ShopClass.intSnowboardsRented

        # Determining which items get a discount, discounting Skis before Snowboards
        if _intItemsRented < 3:
            ShopClass._intFullPriceSkis = intSkisRented
            ShopClass._intFullPriceSnowboards = intSnowboardsRented
            ShopClass._intDiscountedSkis = 0
            ShopClass._intDiscountedSnowboards = 0
        else:
            ShopClass._dblFamilyDiscount = 25
            if _intItemsRented < 6:
                ShopClass._intFullPriceSkis = 0
                ShopClass._intFullPriceSnowboards = 0
                ShopClass._intDiscountedSkis = intSkisRented
                ShopClass._intDiscountedSnowboards = intSnowboardsRented
            else:
                if intSkisRented >= 5:
                    ShopClass._intDiscountedSkis = 5
                    ShopClass._intFullPriceSkis = intSkisRented - 5
                    ShopClass._intDiscountedSnowboards = 0
                    ShopClass._intFullPriceSnowboards = intSnowboardsRented
                else:
                    ShopClass._intDiscountedSkis = intSkisRented
                    ShopClass._intFullPriceSkis = 0
                    ShopClass._intDiscountedSnowboards = 5 - intSkisRented
                    ShopClass._intFullPriceSnowboards = intSnowboardsRented - ShopClass._intDiscountedSnowboards        



    # Applying discount based on the coupon code
    def getCouponDiscount(self, strCouponCode):
        ShopClass.strCouponCode = strCouponCode
        if ShopClass.strCouponCode.endswith("BBP"):
            ShopClass._dblCouponDiscount = 10



# ------------------------------------------------------------------
# Method for Calculating Estimate Rental Price (Best Price)
# ------------------------------------------------------------------
    def calcEstimateBestRentalPrice(self, intRentalTime = 0, _intFullPriceSkis = 0, _intDiscountedSkis = 0, _intFullPriceSnowboards = 0, _intDiscountedSnowboards = 0):

        if ShopClass.strRentalBasis == "Hourly":
            if intRentalTime * (ShopClass._dblSkisHourly + ShopClass._dblSnowboardsHourly) > ShopClass._dblSkisWeekly + ShopClass._dblSnowboardsWeekly:
                # Weekly was determined to be cheaper than Hourly, charge the Weekly rate  
                ShopClass.strRentalBasis = "Weekly"
                ShopClass.intTimeRequested = math.ceil(intRentalTime / 168)
                # Calculate the pre-discount price
                ShopClass.dblSubTotal = ((_intFullPriceSkis + _intDiscountedSkis) * intRentalTime * ShopClass._dblSkisWeekly) + ((_intFullPriceSnowboards + _intDiscountedSnowboards) * intRentalTime * ShopClass._dblSnowboardsWeekly)
                # Calculate for subtotal weekly price of discounted skis + price of non-discounted skis
                _dblSkisSubtotal = ((_intDiscountedSkis * intRentalTime * ShopClass._dblSkisWeekly) * (1 - ((ShopClass._dblFamilyDiscount + ShopClass._dblCouponDiscount) / 100))) + (_intFullPriceSkis * intRentalTime * ShopClass._dblSkisWeekly)
                # Calculate for subtotal weekly price of discounted snowboards + price of non-discounted snowboards
                _dblSnowboardsSubtotal = ((_intDiscountedSnowboards * intRentalTime * ShopClass._dblSnowboardsWeekly) * (1 - ((ShopClass._dblFamilyDiscount + ShopClass._dblCouponDiscount) / 100))) + (_intFullPriceSnowboards * intRentalTime * ShopClass._dblSnowboardsWeekly)
                # Calculate for Estimated RentalPrice by adding the Skis Subtotal and Snowboards Subtotal
                ShopClass._dblEstimateRentalPrice = _dblSkisSubtotal + _dblSnowboardsSubtotal
            else:
                if intRentalTime * (ShopClass._dblSkisHourly + ShopClass._dblSnowboardsHourly) > ShopClass._dblSkisDaily + ShopClass._dblSnowboardsDaily:
                    # Daily was determined to be cheaper than Hourly, charge the Daily rate  
                    ShopClass.strRentalBasis = "Daily"
                    ShopClass.intTimeRequested = math.ceil(intRentalTime / 24)
                    # Calculate the pre-discount price
                    ShopClass.dblSubTotal = ((_intFullPriceSkis + _intDiscountedSkis) * intRentalTime * ShopClass._dblSkisDaily) + ((_intFullPriceSnowboards + _intDiscountedSnowboards) * intRentalTime * ShopClass._dblSnowboardsDaily)
                    # Calculate for subtotal daily price of discounted skis + price of non-discounted skis
                    _dblSkisSubtotal = ((_intDiscountedSkis * intRentalTime * ShopClass._dblSkisDaily) * (1 - ((ShopClass._dblFamilyDiscount + ShopClass._dblCouponDiscount) / 100))) + (_intFullPriceSkis * intRentalTime * ShopClass._dblSkisDaily)
                    # Calculate for subtotal daily price of discounted snowboards + price of non-discounted snowboards
                    _dblSnowboardsSubtotal = ((_intDiscountedSnowboards * intRentalTime * ShopClass._dblSnowboardsDaily) * (1 - ((ShopClass._dblFamilyDiscount + ShopClass._dblCouponDiscount) / 100))) + (_intFullPriceSnowboards * intRentalTime * ShopClass._dblSnowboardsDaily)
                    # Calculate for Estimated RentalPrice by adding the Skis Subtotal and Snowboards Subtotal
                    ShopClass._dblEstimateRentalPrice = _dblSkisSubtotal + _dblSnowboardsSubtotal
                else:
                    # Charge the Hourly rate
                    ShopClass.strRentalBasis = "Hourly"
                    # Calculate the pre-discount price
                    ShopClass.dblSubTotal = ((_intFullPriceSkis + _intDiscountedSkis) * intRentalTime * ShopClass._dblSkisHourly) + ((_intFullPriceSnowboards + _intDiscountedSnowboards) * intRentalTime * ShopClass._dblSnowboardsHourly)
                    # Calculate for subtotal hourly price of discounted skis + price of non-discounted skis
                    _dblSkisSubtotal = ((_intDiscountedSkis * intRentalTime * ShopClass._dblSkisHourly) * (1 - ((ShopClass._dblFamilyDiscount + ShopClass._dblCouponDiscount) / 100))) + (_intFullPriceSkis * intRentalTime * ShopClass._dblSkisHourly)
                    # Calculate for subtotal hourly price of discounted snowboards + price of non-discounted snowboards
                    _dblSnowboardsSubtotal = ((_intDiscountedSnowboards * intRentalTime * ShopClass._dblSnowboardsHourly) * (1 - ((ShopClass._dblFamilyDiscount + ShopClass._dblCouponDiscount) / 100))) + (_intFullPriceSnowboards * intRentalTime * ShopClass._dblSnowboardsHourly)
                    # Calculate for Estimated RentalPrice by adding the Skis Subtotal and Snowboards Subtotal
                    ShopClass._dblEstimateRentalPrice = _dblSkisSubtotal + _dblSnowboardsSubtotal
        else:
            if ShopClass.strRentalBasis == "Daily":
                if intRentalTime * (ShopClass._dblSkisDaily * ShopClass._dblSnowboardsDaily) > ShopClass._dblSkisWeekly + ShopClass._dblSnowboardsWeekly:
                    # Weekly was determined to be cheaper than Daily, charge the Weekly rate
                    ShopClass.strRentalBasis = "Weekly"
                    ShopClass.intTimeRequested = math.ceil(intRentalTime / 168)
                    # Calculate the pre-discount price
                    ShopClass.dblSubTotal = ((_intFullPriceSkis + _intDiscountedSkis) * intRentalTime * ShopClass._dblSkisWeekly) + ((_intFullPriceSnowboards + _intDiscountedSnowboards) * intRentalTime * ShopClass._dblSnowboardsWeekly)
                    # Calculate for Subtotal weekly price of discounted skis + price of non-discounted skis
                    _dblSkisSubtotal = ((_intDiscountedSkis * intRentalTime * ShopClass._dblSkisWeekly) * (1 - ((ShopClass._dblFamilyDiscount + ShopClass._dblCouponDiscount) / 100))) + (_intFullPriceSkis * intRentalTime * ShopClass._dblSkisWeekly)
                    # Calculate for Subtotal weekly price of discounted snowboards + price of non-discounted snowboards
                    _dblSnowboardsSubtotal = ((_intDiscountedSnowboards * intRentalTime * ShopClass._dblSnowboardsWeekly) * (1 - ((ShopClass._dblFamilyDiscount + ShopClass._dblCouponDiscount) / 100))) + (_intFullPriceSnowboards * intRentalTime * ShopClass._dblSnowboardsWeekly)
                    # Calculate for Estimated RentalPrice by adding the Skis Subtotal and Snowboards Subtotal
                    ShopClass._dblEstimateRentalPrice = _dblSkisSubtotal + _dblSnowboardsSubtotal
                else:
                    # charge the Daily rate
                    ShopClass.strRentalBasis = "Daily"
                    ShopClass.intTimeRequested = math.ceil(intRentalTime / 24)
                    # Calculate the pre-discount price
                    ShopClass.dblSubTotal = ((_intFullPriceSkis + _intDiscountedSkis) * intRentalTime * ShopClass._dblSkisDaily) + ((_intFullPriceSnowboards + _intDiscountedSnowboards) * intRentalTime * ShopClass._dblSnowboardsDaily)
                    # Calculate for Subtotal daily price of discounted skis + price of non-discounted skis
                    _dblSkisSubtotal = ((_intDiscountedSkis * intRentalTime * ShopClass._dblSkisDaily) * (1 - ((ShopClass._dblFamilyDiscount + ShopClass._dblCouponDiscount) / 100))) + (_intFullPriceSkis * intRentalTime * ShopClass._dblSkisDaily)
                    # Calculate for Subtotal daily price of discounted snowboards + price of non-discounted snowboards
                    _dblSnowboardsSubtotal = ((_intDiscountedSnowboards * intRentalTime * ShopClass._dblSnowboardsDaily) * (1 - ((ShopClass._dblFamilyDiscount + ShopClass._dblCouponDiscount) / 100))) + (_intFullPriceSnowboards * intRentalTime * ShopClass._dblSnowboardsDaily)
                    # Calculate for Estimated RentalPrice by adding the Skis Subtotal and Snowboards Subtotal
                    ShopClass._dblEstimateRentalPrice = _dblSkisSubtotal + _dblSnowboardsSubtotal
            else:
                # Charge the Weekly rate
                ShopClass.strRentalBasis = "Weekly"
                ShopClass.intTimeRequested = math.ceil(intRentalTime / 168) 
                # Calculate the pre-discount price
                ShopClass.dblSubTotal = ((_intFullPriceSkis + _intDiscountedSkis) * intRentalTime * ShopClass._dblSkisWeekly) + ((_intFullPriceSnowboards + _intDiscountedSnowboards) * intRentalTime * ShopClass._dblSnowboardsWeekly)
                # Calculate for Subtotal weekly price of discounted skis + price of non-discounted skis
                _dblSkisSubtotal = ((_intDiscountedSkis * intRentalTime * ShopClass._dblSkisWeekly) * (1 - ((ShopClass._dblFamilyDiscount + ShopClass._dblCouponDiscount) / 100))) + (_intFullPriceSkis * intRentalTime * ShopClass._dblSkisWeekly)
                # Calculate for Subtotal weekly price of discounted snowboards + price of non-discounted snowboards
                _dblSnowboardsSubtotal = ((_intDiscountedSnowboards * intRentalTime * ShopClass._dblSnowboardsWeekly) * (1 - ((ShopClass._dblFamilyDiscount + ShopClass._dblCouponDiscount) / 100))) + (_intFullPriceSnowboards * intRentalTime * ShopClass._dblSnowboardsWeekly)
                # Calculate for Estimated RentalPrice by adding the Skis Subtotal and Snowboards Subtotal
                ShopClass._dblEstimateRentalPrice = _dblSkisSubtotal + _dblSnowboardsSubtotal 
                
        if ShopClass._blnReturn == True:
            # Set the grand total of the rental return to the calculated price
            ShopClass.dblGrandTotal = ShopClass._dblEstimateRentalPrice
            # Set the numerical value of the discount applied to the order
            ShopClass.dblDiscountValue = ShopClass.dblSubTotal - ShopClass.dblGrandTotal
            ShopClass.collect_Fee(self)
            return ShopClass.dblSubTotal, ShopClass.dblDiscountValue, ShopClass.dblGrandTotal
        return ShopClass._dblEstimateRentalPrice




# ------------------------------------------------------------------
# Method to calculate time difference between initial requested time and actual rental time
# ------------------------------------------------------------------
    def time_Difference(self, estimated_Time, actual_Time):
        # Trim down the time to Year, Month, Day and Hour:Minutes
        estimated_Time = str(estimated_Time)[:-10]
        actual_Time = str(actual_Time)[:-10]
        estimated_Time = datetime.strptime(estimated_Time, "%Y-%m-%d %H:%M")
        actual_Time = datetime.strptime(actual_Time, "%Y-%m-%d %H:%M")
        intDaysDifference = (abs(actual_Time.day - estimated_Time.day))
        if intDaysDifference > 0:
            ShopClass.strRentalBasis = "Daily"
            return intDaysDifference
        else:
            intHoursDifference = (abs(actual_Time.hour - estimated_Time.hour))
            ShopClass.strRentalBasis = "Hourly"
            return intHoursDifference



# ------------------------------------------------------------------
# Method to return Skis to inventory
# ------------------------------------------------------------------
    def returnSkis(self, intReturnedSkis):
        ShopClass.intCurrentSkisInventory += intReturnedSkis



# ------------------------------------------------------------------
# Method to return Snowboards to inventory
# ------------------------------------------------------------------
    def returnSnowboards(self, intReturnedSnowboards):
        ShopClass.intCurrentSnowboardsInventory += intReturnedSnowboards



# ------------------------------------------------------------------
# Method to accumulate the daily revenue when a rental is returned
# ------------------------------------------------------------------
    def collect_Fee(self):
        ShopClass.dblDailyRevenue += ShopClass._dblEstimateRentalPrice


