# ------------------------------------------------------------------
# Project 2 Class Area: Shop Class
# ------------------------------------------------------------------

# Used for .ceil function calculating ideal intRentalTime/strRentalBasis
import math

class Shop(object):
    dblEstimateRentalPrice = float(0)
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

    intRentalTime = int(0)

    def __init__(self, intInitialSkisInventory, intInitialSnowboardsInventory):
         self.intInitialSkisInventory = intInitialSkisInventory
         self.intInitialSnowboardsInventory = intInitialSnowboardsInventory

# ------------------------------------------------------------------
# Calculate Estimate Rental Price (Best Price)
# ------------------------------------------------------------------
    def calc_estimatebestrentalprice(self, intRentalTime, strRentalBasis, intSkisRented, intSnowboardsRented):
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
                      dblEstimateRentalPrice = (intSkisRented * intRentalTime * _dblSkisWeekly) + (intSnowboardsRented * intRentalTime * _dblSnowboardsWeekly)
                else:
                     if intRentalTime * (_dblSkisHourly + _dblSnowboardsHourly) > _dblSkisDaily + _dblSnowboardsDaily:
                          strRentalBasis = "Daily"
                          intRentalTime = math.ceil(intRentalTime / 24)
                          dblEstimateRentalPrice = (intSkisRented * intRentalTime * _dblSkisDaily) + (intSnowboardsRented * intRentalTime * _dblSnowboardsDaily)
                     else:
                          dblEstimateRentalPrice = (intSkisRented * intRentalTime * _dblSkisHourly) + (intSnowboardsRented * intRentalTime * _dblSnowboardsHourly)
            else:
                 if strRentalBasis == "Daily":
                      if intRentalTime * (_dblSkisDaily * _dblSnowboardsDaily) > _dblSkisWeekly + _dblSkisDaily:
                           strRentalBasis = "Daily"
                           intRentalTime = math.ceil(intRentalTime / 7)
                      else:
                           dblEstimateRentalPrice = (intSkisRented * intRentalTime * _dblSkisDaily) + (intSnowboardsRented * intRentalTime * _dblSnowboardsDaily)
                 else:
                      dblEstimateRentalPrice = (intSkisRented * intRentalTime * _dblSkisWeekly) + (intSnowboardsRented * intRentalTime * _dblSnowboardsWeekly)
            return dblEstimateRentalPrice