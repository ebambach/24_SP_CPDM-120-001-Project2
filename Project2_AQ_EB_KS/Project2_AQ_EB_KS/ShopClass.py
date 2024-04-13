# ------------------------------------------------------------------
# Project 2 Class Area: Shop Class
# ------------------------------------------------------------------

# Used for .ceil function calculating ideal intRentalTime/strRentalBasis
import math

class ShopClass(object):
    # Initial Inventory
     intInitialSkisInventory = int()
     intInitialSnowboardsInventory = int()
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

    def __init__(self, intInitialSkisInventory, intInitialSnowboardsInventory):
         self.intInitialSkisInventory = intInitialSkisInventory
         self.intInitialSnowboardsInventory = intInitialSnowboardsInventory
	    
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
               if intInput > -1:
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
               if intInput > -1:
                     self._intInitialSnowboardsInventory = intInput
               else:
                    raise Exception("Initial Snowboards Inventory must be an integer equal to or greater than 0. The value of Initial Snowboards Inventory was: {}".format(intInput))
          else:
               raise Exception("Initial Snowboards Inventory must be an integer equal to or greater than 0. The value of Initial Snowboards Inventory was: {}".format(intInput))

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
