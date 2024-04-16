# ------------------------------------------------------------------
# Project 2 Class Area: Shop Class
# ------------------------------------------------------------------

# Used for .ceil function calculating ideal intRentalTime/strRentalBasis
import math
import datetime

class ShopClass(object):
    # Initial Inventory
    intInitialSkisInventory = int()
    intInitialSnowboardsInventory = int()
    # Current Inventory
    intCurrentSkisInventory = int()
    intCurrentSnowboardsInventory = int()
    # Prices for Skis
    _dblSkisHourly = float(15)
    _dblSkisDaily = float(50)
    _dblSkisWeekly = float(200)
    # Prices for Snowboards
    _dblSnowboardsHourly = float(10)
    _dblSnowboardsDaily = float(40)
    _dblSnowboardsWeekly = float(160)
    # Rental price
    _dblRentalPrice = float(0)
    _dblEstimateRentalPrice = float(0)
    # Boolean for checking availbility
    _blnValidation = False

    intRentalTime = int(0)

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
# Method to check the currently available number of Skis and Snowboards
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
        now = datetime.datetime.now()
        print("Your rental began on " + str(now.month) + "-" + str(now.day) + "-" + str(now.year) + 
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
                print("You have successfully rented " + str(intRequestedSkis) +" pair of skis on an hourly basis.")
            else:
                print("You have rented " + str(intRequestedSkis) + " pairs of skis on an hourly basis.")
            self.rentalTime()
            print("The hourly rent is $" + str(self._dblSkisHourly) + " per hour for each pair of skis.")
            # Reduce the current inventory by the quantity of Skis that were rented.
            self.intCurrentSkisInventory -= intRequestedSkis
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
                print("You have successfully rented " + str(intRequestedSnowboards) +" snowboard on an hourly basis.")
            else:
                print("You have rented " + str(intRequestedSnowboards) + " snowboards on an hourly basis.")
            self.rentalTime()
            print("The hourly rent is $" + str(self._dblSnowboardsHourly) + " per hour for each snowboard.")
            # Reduce the current inventory by the quantity of Snowboards that were rented.
            self.intCurrentSnowboardsInventory -= intRequestedSnowboards
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
                print("You have successfully rented " + str(intRequestedSkis) +" pair of skis on an daily basis.")
            else:
                print("You have rented " + str(intRequestedSkis) + " pairs of skis on an daily basis.")
            self.rentalTime()
            print("The daily rent is $" + str(self._dblSkisDaily) + " per day for each pair of skis.")
            # Reduce the current inventory by the quantity of Skis that were rented.
            self.intCurrentSkisInventory -= intRequestedSkis
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
                print("You have successfully rented " + str(intRequestedSnowboards) +" snowboard on an daily basis.")
            else:
                print("You have rented " + str(intRequestedSnowboards) + " snowboards on an daily basis.")
            self.rentalTime()
            print("The daily rent is $" + str(self._dblSnowboardsDaily) + " per day for each snowboard.")
            # Reduce the current inventory by the quantity of Snowboards that were rented.
            self.intCurrentSnowboardsInventory -= intRequestedSnowboards
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
                print("You have successfully rented " + str(intRequestedSkis) +" pair of skis on an weekly basis.")
            else:
                print("You have rented " + str(intRequestedSkis) + " pairs of skis on an weekly basis.")
            self.rentalTime()
            print("The weekly rent is $" + str(self._dblSkisWeekly) + " per week for each pair of skis.")
            # Reduce the current inventory by the quantity of Skis that were rented.
            self.intCurrentSkisInventory -= intRequestedSkis
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
                print("You have successfully rented " + str(intRequestedSnowboards) +" snowboard on an weekly basis.")
            else:
                print("You have rented " + str(intRequestedSnowboards) + " snowboards on an weekly basis.")
            self.rentalTime()
            print("The weekly rent is $" + str(self._dblSnowboardsWeekly) + " per week for each snowboard.")
            # Reduce the current inventory by the quantity of Snowboards that were rented.
            self.intCurrentSnowboardsInventory -= intRequestedSnowboards
            self._blnValidation = False



# ------------------------------------------------------------------
# Method for Calculating Estimate Rental Price (Best Price)
# ------------------------------------------------------------------
    def calc_estimatebestrentalprice(self, intRentalTime = 0, strRentalBasis = "Hourly", intSkisRented = 0, intSnowboardsRented = 0, _dblTotalDiscountPercent = 0):
        # Rental basis is either Hourly, Daily, or Weekly
        self.strRentalBasis = strRentalBasis
        self.intRentalTime = intRentalTime
        self.intSkisRented = intSkisRented
        self.intSnowboardsRented = intSnowboardsRented

        if strRentalBasis == "Hourly":
            if intRentalTime * (self._dblSkisHourly + self._dblSnowboardsHourly) > self._dblSkisWeekly + self._dblSnowboardsWeekly:
                # Weekly was determined to be cheaper than Hourly, charge the Weekly rate  
                strRentalBasis = "Weekly"
                if self.intSkisRented > 0:
                    self.rentSkisWeekly(self.intSkisRented)
                if self.intSnowboardsRented > 0:
                    self.rentSnowboardsWeekly(self.intSnowboardsRented)
                intRentalTime = math.ceil(intRentalTime  / 168)
                _dblEstimateRentalPrice = ((intSkisRented * intRentalTime * self._dblSkisWeekly) + (intSnowboardsRented * intRentalTime * self._dblSnowboardsWeekly)) * (1 - (_dblTotalDiscountPercent / 100))
            else:
                if intRentalTime * (self._dblSkisHourly + self._dblSnowboardsHourly) > self._dblSkisDaily + self._dblSnowboardsDaily:
                    # Daily was determined to be cheaper than Hourly, charge the Daily rate  
                    strRentalBasis = "Daily"
                    if self.intSkisRented > 0:
                        self.rentSkisDaily(self.intSkisRented)
                    if self.intSnowboardsRented > 0:
                        self.rentSnowboardsDaily(self.intSnowboardsRented)
                    intRentalTime = math.ceil(intRentalTime / 24)
                    _dblEstimateRentalPrice = ((intSkisRented * intRentalTime * self._dblSkisDaily) + (intSnowboardsRented * intRentalTime * self._dblSnowboardsDaily)) * (1 - (_dblTotalDiscountPercent / 100))
                else:
                    # Charge the Hourly rate
                    if self.intSkisRented > 0:
                        self.rentSkisHourly(self.intSkisRented)
                    if self.intSnowboardsRented > 0:
                        self.rentSnowboardsHourly(self.intSnowboardsRented)
                    _dblEstimateRentalPrice = ((intSkisRented * intRentalTime * self._dblSkisHourly) + (intSnowboardsRented * intRentalTime * self._dblSnowboardsHourly)) * (1 - (_dblTotalDiscountPercent / 100))
        else:
            if strRentalBasis == "Daily":
                if intRentalTime * (self._dblSkisDaily * self._dblSnowboardsDaily) > self._dblSkisWeekly + self._dblSnowboardsWeekly:
                    # Weekly was determined to be cheaper than Daily, charge the Weekly rate
                    strRentalBasis = "Weekly"
                    if self.intSkisRented > 0:
                        self.rentSkisWeekly(self.intSkisRented)
                    if self.intSnowboardsRented > 0:
                        self.rentSnowboardsWeekly(self.intSnowboardsRented)
                    intRentalTime = math.ceil(intRentalTime  / 168)
                    _dblEstimateRentalPrice = ((intSkisRented * intRentalTime * self._dblSkisWeekly) + (intSnowboardsRented * intRentalTime * self._dblSnowboardsWeekly)) * (1 - (_dblTotalDiscountPercent / 100))
                else:
                    # charge the Daily rate
                    if self.intSkisRented > 0:
                        self.rentSkisDaily(self.intSkisRented)
                    if self.intSnowboardsRented > 0:
                        self.rentSnowboardsDaily(self.intSnowboardsRented)
                    intRentalTime = math.ceil(intRentalTime / 24)
                    _dblEstimateRentalPrice = ((intSkisRented * intRentalTime * self._dblSkisDaily) + (intSnowboardsRented * intRentalTime * self._dblSnowboardsDaily)) * (1 - (_dblTotalDiscountPercent / 100))
            else:
                # Charge the Weekly rate
                if self.intSkisRented > 0:
                    self.rentSkisWeekly(self.intSkisRented)
                if self.intSnowboardsRented > 0:
                    self.rentSnowboardsWeekly(self.intSnowboardsRented)
                intRentalTime = math.ceil(intRentalTime  / 168)  
                _dblEstimateRentalPrice = ((intSkisRented * intRentalTime * self._dblSkisWeekly) + (intSnowboardsRented * intRentalTime * self._dblSnowboardsWeekly)) * (1 - (_dblTotalDiscountPercent / 100))
        return _dblEstimateRentalPrice
