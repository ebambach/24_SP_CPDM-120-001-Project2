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
               if intInput > 0:
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
               if intInput > 0:
                     self._intInitialSnowboardsInventory = intInput
               else:
                    raise Exception("Initial Snowboards Inventory must be an integer equal to or greater than 0. The value of Initial Snowboards Inventory was: {}".format(intInput))
          else:
               raise Exception("Initial Snowboards Inventory must be an integer equal to or greater than 0. The value of Initial Snowboards Inventory was: {}".format(intInput))

    
# ------------------------------------------------------------------
# Method to display the currently available number of Skis and Snowboards
# ------------------------------------------------------------------    
    def display_CurrentInventory(self):
        print("There are currently " + str(self.intCurrentSkisInventory) + " pairs of skis available to rent.")
        print("There are currently " + str(self.intCurrentSnowboardsInventory) + " snowboards available to rent.")



# ------------------------------------------------------------------
# Methods to rents equipment on either an hourly, a daily, or a weekly basis
# Because we allow for Skis and/or Snowboards to be rented, the methods
# allow for "0" to be rented.
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# Method to rent Skis on an hourly basis
# ------------------------------------------------------------------  
    def rentSkisHourly(self, intRequestedSkis):
        # If the customer is trying to rent Skis, make sure that the number request is greater  -1 
        if intRequestedSkis < 0:
            print("This rental cannot be completed by asking to rent " + str(intRequestedSkis) + " pairs of skis.")
            print("Please try again with a number of skis greater than -1, if you would like to rent skis.")
            return None

        # If the number of skis requested is greater than -1, make sure that the number requested does
        # not exceed the number currently available       
        elif intRequestedSkis > self.intCurrentSkisInventory:
            print("This rental cannot be completed, " + str(intRequestedSkis) + " pairs of skis is more than what is currently available.")
            print("We currently have " + str(intCurrentSkisInventory) + " pairs of skis available to rent.")
            return None
        # With the numbers validated, complete the rental.                
        else:
            now = datetime.datetime.now()
            # State how many Skis they rented, that the time basis is hourly, at what time the rental occurred, and how much
            # each pair of Skis cost to rent.
            if intRequestedSkis == 1:
                print("You have successfully rented " + str(intRequestedSkis) +" pair of skis on an hourly basis.")
            else:
                print("You have rented " + str(intRequestedSkis) + " pairs of skis on an hourly basis.")
            print("Your rental began on " + str(now.month) + "-" + str(now.day) + "-" + str(now.year) + 
                  " at " + str(now.hour) + ":" + str(now.minute) + ".")
            print("The hourly rent $" + str(self._dblSkisHourly) + " per hour for each pair of skis.")
            # Reduce the current inventory by the quantity of Skis that were rented.
            self.intCurrentSkisInventory -= intRequestedSkis
            return now



# ------------------------------------------------------------------
# Method to rent Snowboards on an hourly basis
# ------------------------------------------------------------------  
    def rentSnowboardsHourly(self, intRequestedSnowboards):
        # If the customer is trying to rent Snowboards, make sure that the number request is greater  -1 
        if intRequestedSnowboards < 0:
            print("This rental cannot be completed by asking to rent " + str(intRequestedSnowboards) + " pairs of skis.")
            print("Please try again with a number of skis greater than -1, if you would like to rent skis.")
            return None

        # If the number of skis requested is greater than -1, make sure that the number requested does
        # not exceed the number currently available       
        elif intRequestedSnowboards > self.intCurrentSnowboardsInventory:
            print("This rental cannot be completed, " + str(intRequestedSnowboards) + " pairs of skis is more than what is currently available.")
            print("We currently have " + str(intCurrentSnowboardsInventory) + " pairs of skis available to rent.")
            return None
        # With the numbers validated, complete the rental.                
        else:
            now = datetime.datetime.now()
            # State how many Snowboards they rented, that the time basis is hourly, at what time the rental occurred, and how much
            # each pair of Snowboards cost to rent.
            if intRequestedSnowboards == 1:
                print("You have successfully rented " + str(intRequestedSnowboards) + " snowboards on an hourly basis.")
            else:
                print("You have rented " + str(intRequestedSnowboards) + " pairs of skis on an hourly basis.")
            print("Your rental began on " + str(now.month) + "-" + str(now.day) + "-" + str(now.year) + 
                  " at " + str(now.hour) + ":" + str(now.minute) + ".")
            print("The hourly rent $" + str(self._dblSnowboardsHourly) + " per hour for each snowboards.")
            # Reduce the current inventory by the quantity of Snowboards that were rented.
            self.intCurrentSnowboardsInventory -= intRequestedSnowboards
            return now



# ------------------------------------------------------------------
# Method to rent Skis on a daily basis
# ------------------------------------------------------------------  
    def rentSkisDaily(self, intRequestedSkis):
        # If the customer is trying to rent Skis, make sure that the number request is greater  -1 
        if intRequestedSkis < 0:
            print("This rental cannot be completed by asking to rent " + str(intRequestedSkis) + " pairs of skis.")
            print("Please try again with a number of skis greater than -1, if you would like to rent skis.")
            return None

        # If the number of skis requested is greater than -1, make sure that the number requested does
        # not exceed the number currently available       
        elif intRequestedSkis > self.intCurrentSkisInventory:
            print("This rental cannot be completed, " + str(intRequestedSkis) + " pairs of skis is more than what is currently available.")
            print("We currently have " + str(intCurrentSkisInventory) + " pairs of skis available to rent.")
            return None
        # With the numbers validated, complete the rental.                
        else:
            now = datetime.datetime.now()
            # State how many Skis they rented, that the time basis is daily, at what time the rental occurred, and how much
            # each pair of Skis cost to rent.
            if intRequestedSkis == 1:
                print("You have successfully rented " + str(intRequestedSkis) +" pair of skis on a daily basis.")
            else:
                print("You have rented " + str(intRequestedSkis) + " pairs of skis on a daily basis.")
            print("Your rental began on " + str(now.month) + "-" + str(now.day) + "-" + str(now.year) + 
                  " at " + str(now.hour) + ":" + str(now.minute) + ".")
            print("The daily rent $" + str(self._dblSkisHourly) + " per day for each pair of skis.")
            # Reduce the current inventory by the quantity of Skis that were rented.
            self.intCurrentSkisInventory -= intRequestedSkis
            return now



# ------------------------------------------------------------------
# Method to rent Snowboards on a daily basis
# ------------------------------------------------------------------  
    def rentSnowboardsDaily(self, intRequestedSnowboards):
        # If the customer is trying to rent Snowboards, make sure that the number request is greater  -1 
        if intRequestedSnowboards < 0:
            print("This rental cannot be completed by asking to rent " + str(intRequestedSnowboards) + " pairs of skis.")
            print("Please try again with a number of skis greater than -1, if you would like to rent skis.")
            return None

        # If the number of skis requested is greater than -1, make sure that the number requested does
        # not exceed the number currently available       
        elif intRequestedSnowboards > self.intCurrentSnowboardsInventory:
            print("This rental cannot be completed, " + str(intRequestedSnowboards) + " pairs of skis is more than what is currently available.")
            print("We currently have " + str(intCurrentSnowboardsInventory) + " pairs of skis available to rent.")
            return None
        # With the numbers validated, complete the rental.                
        else:
            now = datetime.datetime.now()
            # State how many Snowboards they rented, that the time basis is daily, at what time the rental occurred, and how much
            # each pair of Snowboards cost to rent.
            if intRequestedSnowboards == 1:
                print("You have successfully rented " + str(intRequestedSnowboards) + " snowboards on a daily basis.")
            else:
                print("You have rented " + str(intRequestedSnowboards) + " pairs of skis on a daily basis.")
            print("Your rental began on " + str(now.month) + "-" + str(now.day) + "-" + str(now.year) + 
                  " at " + str(now.hour) + ":" + str(now.minute) + ".")
            print("The daily rent $" + str(self._dblSnowboardsHourly) + " per day for each snowboards.")
            # Reduce the current inventory by the quantity of Snowboards that were rented.
            self.intCurrentSnowboardsInventory -= intRequestedSnowboards
            return now



# ------------------------------------------------------------------
# Method to rent Skis on a weekly basis
# ------------------------------------------------------------------  
    def rentSkisWeekly(self, intRequestedSkis):
        # If the customer is trying to rent Skis, make sure that the number request is greater  -1 
        if intRequestedSkis < 0:
            print("This rental cannot be completed by asking to rent " + str(intRequestedSkis) + " pairs of skis.")
            print("Please try again with a number of skis greater than -1, if you would like to rent skis.")
            return None

        # If the number of skis requested is greater than -1, make sure that the number requested does
        # not exceed the number currently available       
        elif intRequestedSkis > self.intCurrentSkisInventory:
            print("This rental cannot be completed, " + str(intRequestedSkis) + " pairs of skis is more than what is currently available.")
            print("We currently have " + str(intCurrentSkisInventory) + " pairs of skis available to rent.")
            return None
        # With the numbers validated, complete the rental.                
        else:
            now = datetime.datetime.now()
            # State how many Skis they rented, that the time basis is weekly, at what time the rental occurred, and how much
            # each pair of Skis cost to rent.
            if intRequestedSkis == 1:
                print("You have successfully rented " + str(intRequestedSkis) +" pair of skis on a weekly basis.")
            else:
                print("You have rented " + str(intRequestedSkis) + " pairs of skis on a weekly basis.")
            print("Your rental began on " + str(now.month) + "-" + str(now.day) + "-" + str(now.year) + 
                  " at " + str(now.hour) + ":" + str(now.minute) + ".")
            print("The weekly rent $" + str(self._dblSkisHourly) + " per week for each pair of skis.")
            # Reduce the current inventory by the quantity of Skis that were rented.
            self.intCurrentSkisInventory -= intRequestedSkis
            return now



# ------------------------------------------------------------------
# Method to rent Snowboards on a weekly basis
# ------------------------------------------------------------------  
    def rentSnowboardsWeekly(self, intRequestedSnowboards):
        # If the customer is trying to rent Snowboards, make sure that the number request is greater  -1 
        if intRequestedSnowboards < 0:
            print("This rental cannot be completed by asking to rent " + str(intRequestedSnowboards) + " pairs of skis.")
            print("Please try again with a number of skis greater than -1, if you would like to rent skis.")
            return None

        # If the number of skis requested is greater than -1, make sure that the number requested does
        # not exceed the number currently available       
        elif intRequestedSnowboards > self.intCurrentSnowboardsInventory:
            print("This rental cannot be completed, " + str(intRequestedSnowboards) + " pairs of skis is more than what is currently available.")
            print("We currently have " + str(intCurrentSnowboardsInventory) + " pairs of skis available to rent.")
            return None
        # With the numbers validated, complete the rental.                
        else:
            now = datetime.datetime.now()
            # State how many Snowboards they rented, that the time basis is weekly, at what time the rental occurred, and how much
            # each pair of Snowboards cost to rent.
            if intRequestedSnowboards == 1:
                print("You have successfully rented " + str(intRequestedSnowboards) + " snowboards on a weekly basis.")
            else:
                print("You have rented " + str(intRequestedSnowboards) + " pairs of skis on a weekly basis.")
            print("Your rental began on " + str(now.month) + "-" + str(now.day) + "-" + str(now.year) + 
                  " at " + str(now.hour) + ":" + str(now.minute) + ".")
            print("The weekly rent $" + str(self._dblSnowboardsHourly) + " per week for each snowboards.")
            # Reduce the current inventory by the quantity of Snowboards that were rented.
            self.intCurrentSnowboardsInventory -= intRequestedSnowboards
            return now



# ------------------------------------------------------------------
# Method for Calculating Estimate Rental Price (Best Price)
# ------------------------------------------------------------------
    def calc_estimatebestrentalprice(self, intRentalTime, strRentalBasis, intSkisRented, intSnowboardsRented, _dblTotalDiscountPercent):
            self.strRentalBasis = strRentalBasis
            self.intRentalTime = intRentalTime
            self.intSkisRented = intSkisRented
            self.intSnowboardsRented = intSnowboardsRented
            _dblSkisHourly = float(15)
            _dblSkisDaily = float(50)
            _dblSkisWeekly = float(200)
            _dblSnowboardsHourly = float(10)
            _dblSnowboardsDaily = float(40)
            _dblSnowboardsWeekly = float(160)

            if strRentalBasis == "Hourly":
                if intRentalTime * (_dblSkisHourly + _dblSnowboardsHourly) > _dblSkisWeekly + _dblSnowboardsWeekly:
                      strRentalBasis = "Weekly"
                      intRentalTime = math.ceil(intRentalTime  / 168)
                      _dblEstimateRentalPrice = ((intSkisRented * intRentalTime * _dblSkisWeekly) + (intSnowboardsRented * intRentalTime * _dblSnowboardsWeekly)) * (1 - (_dblTotalDiscountPercent / 100))
                else:
                     if intRentalTime * (_dblSkisHourly + _dblSnowboardsHourly) > _dblSkisDaily + _dblSnowboardsDaily:
                          strRentalBasis = "Daily"
                          intRentalTime = math.ceil(intRentalTime / 24)
                          _dblEstimateRentalPrice = ((intSkisRented * intRentalTime * _dblSkisDaily) + (intSnowboardsRented * intRentalTime * _dblSnowboardsDaily)) * (1 - (_dblTotalDiscountPercent / 100))
                     else:
                          _dblEstimateRentalPrice = ((intSkisRented * intRentalTime * _dblSkisHourly) + (intSnowboardsRented * intRentalTime * _dblSnowboardsHourly)) * (1 - (_dblTotalDiscountPercent / 100))
            else:
                 if strRentalBasis == "Daily":
                      if intRentalTime * (_dblSkisDaily * _dblSnowboardsDaily) > _dblSkisWeekly + _dblSkisDaily:
                           strRentalBasis = "Daily"
                           intRentalTime = math.ceil(intRentalTime / 7)
                      else:
                           _dblEstimateRentalPrice = ((intSkisRented * intRentalTime * _dblSkisDaily) + (intSnowboardsRented * intRentalTime * _dblSnowboardsDaily)) * (1 - (_dblTotalDiscountPercent / 100))
                 else:
                      _dblEstimateRentalPrice = ((intSkisRented * intRentalTime * _dblSkisWeekly) + (intSnowboardsRented * intRentalTime * _dblSnowboardsWeekly)) * (1 - (_dblTotalDiscountPercent / 100))
            return _dblEstimateRentalPrice
