# ------------------------------------------------------------------
# Project 2 Class Area: Shop Class
# ------------------------------------------------------------------

# Used for .ceil function calculating ideal intRentalTime/strRentalBasis
import math

class Shop(object):

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
