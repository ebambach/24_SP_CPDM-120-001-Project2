# -----------------------------------------------------------------
# Assignment Name:      Project 2
# Name:                 Team B
# -----------------------------------------------------------------
import CustomerClass as Customer
import ShopClass as ShopClass



# ------------------------------------------------------------------
# Project 2 Class Test Area
# ------------------------------------------------------------------

# try:
	# Testing Area
	test1 = ShopClass.ShopClass(100,100)  
	test1.start_Request(intTimeRequested = 1, strRentalBasis = "Hourly", intSkisRequested = 5, intSnowboardsRequested = 0, strCouponCode = "BBP")
	test1.return_Rental(1)
	#test1.calcEstimateBestRentalPrice(1, "Hourly", 4, 7, 0, 4, 6, 1, 25, 0)
	#test1.calc_estimatebestrentalprice(8, "Hourly", 2, 2, 10, 10)
	# print(repr(test1))
	# test0 = Customer.CustomerClass("Crystal Clear", 1, 1, 0, 1, 0, 0, "")
	#print(repr(test0))

	# test cases for the family discount, which applies when there are at three
	# items on the order, discounting up to five items on the order
	# the method discounts skis over snowboards, when available, as skis
	# cost more to rent
	#test1.getFamilyDiscount(2, 0)
	#test1.getFamilyDiscount(0, 2)
	#test1.getFamilyDiscount(2, 1)
	#test1.getFamilyDiscount(1, 2)
	#test1.getFamilyDiscount(4, 0)
	#test1.getFamilyDiscount(0, 4)
	#test1.getFamilyDiscount(5, 2)
	#test1.getFamilyDiscount(2, 5)
except Exception as e:
	print(e)


shop = ShopClass()
shop.getFamilyDiscount(2, 1)  # 2 Skis, 1 Snowboard

shop = ShopClass()
shop.getFamilyDiscount(4, 1)  # 4 Skis, 1 Snowboard

shop = ShopClass()
shop.getFamilyDiscount(2, 5)  # 2 Skis, 5 Snowboards

# 'Hourly Rental Basis - Skis Only: Test a scenario where only skis are rented on an hourly basis.

shop = ShopClass()
shop.calcEstimateBestRentalPrice(intRentalTime=3, strRentalBasis="Hourly", _intFullPriceSkis=3, _intDiscountedSkis=0, _intFullPriceSnowboards=0, _intDiscountedSnowboards=0, _dblFamilyDiscount=0, _dblCouponDiscount=0)

# 'Hourly Rental Basis - Snowboards Only: Test a scenario where only snowboards are rented on an hourly basis.

shop = ShopClass()
shop.calcEstimateBestRentalPrice(intRentalTime=4, strRentalBasis="Hourly", _intFullPriceSkis=0, _intDiscountedSkis=0, _intFullPriceSnowboards=4, _intDiscountedSnowboards=0, _dblFamilyDiscount=0, _dblCouponDiscount=0)

# 'Daily Rental Basis - Skis Only: Test a scenario where only skis are rented on a daily basis.

shop = ShopClass()
shop.calcEstimateBestRentalPrice(intRentalTime=2, strRentalBasis="Daily", _intFullPriceSkis=2, _intDiscountedSkis=0, _intFullPriceSnowboards=0, _intDiscountedSnowboards=0, _dblFamilyDiscount=0, _dblCouponDiscount=0)

# 'Daily Rental Basis - Snowboards Only: Test a scenario where only snowboards are rented on a daily basis.

shop = ShopClass()
shop.calcEstimateBestRentalPrice(intRentalTime=3, strRentalBasis="Daily", _intFullPriceSkis=0, _intDiscountedSkis=0, _intFullPriceSnowboards=3, _intDiscountedSnowboards=0, _dblFamilyDiscount=0, _dblCouponDiscount=0)

# 'Weekly Rental Basis - Skis Only: Test a scenario where only skis are rented on a weekly basis.

shop = ShopClass()
shop.calcEstimateBestRentalPrice(intRentalTime=1, strRentalBasis="Weekly", _intFullPriceSkis=1, _intDiscountedSkis=0, _intFullPriceSnowboards=0, _intDiscountedSnowboards=0, _dblFamilyDiscount=0, _dblCouponDiscount=0)

# 'Weekly Rental Basis - Snowboards Only: Test a scenario where only snowboards are rented on a weekly basis.

shop = ShopClass()
shop.calcEstimateBestRentalPrice(intRentalTime=2, strRentalBasis="Weekly", _intFullPriceSkis=0, _intDiscountedSkis=0, _intFullPriceSnowboards=2, _intDiscountedSnowboards=0, _dblFamilyDiscount=0, _dblCouponDiscount=0)

# 'Mixed Rental Basis - Skis and Snowboards: Test a scenario where both skis and snowboards are rented on different rental bases.

shop = ShopClass()
shop.calcEstimateBestRentalPrice(intRentalTime=5, strRentalBasis="Hourly", _intFullPriceSkis=2, _intDiscountedSkis=1, _intFullPriceSnowboards=3, _intDiscountedSnowboards=1, _dblFamilyDiscount=0, _dblCouponDiscount=0)

# 'With Family Discount Applied: Test a scenario where a family discount is applied.

shop = ShopClass()
shop.calcEstimateBestRentalPrice(intRentalTime=3, strRentalBasis="Daily", _intFullPriceSkis=3, _intDiscountedSkis=2, _intFullPriceSnowboards=0, _intDiscountedSnowboards=0, _dblFamilyDiscount=25, _dblCouponDiscount=0)

# 'With Coupon Discount Applied: Test a scenario where a coupon discount is applied.

shop = ShopClass()
shop.calcEstimateBestRentalPrice(intRentalTime=4, strRentalBasis="Weekly", _intFullPriceSkis=0, _intDiscountedSkis=0, _intFullPriceSnowboards=4, _intDiscountedSnowboards=0, _dblFamilyDiscount=0, _dblCouponDiscount=10)

#customer1 = strName, intID("Bob", 1)
#customer2 = strName, intID("Lance", 2)
#customer3 = strName, intID("Joe", 3)
#customer4 = strName, intID("Tanner", 4)

# Set up rental basis
#customer1.strRentalBasis == "Hourly"
#customer2.strRentalBasis == "Hourly"
#customer3.strRentalBasis == "Daily"
#customer4.strRentalBasis == "Weekly"

# determine number of skis and snowboards 
#customer1.intSkisRented = 1
#customer2.intSkisRented = 5 (apply_discount)
#customer3.intSnowboardsRented = 2
#customer4.intSnowboardsRented = 0

# detrmine rental time
#customer1.intRentalTime = datetime.now() + timedelta(hours=-4)
#customer2.intRentalTime = datetime.now() + timedelta(hours=-23)
#customer3.intRentalTime = datetime.now() + timedelta(days=-4)
#customer4.intRentalTime = datetime.now() + timedelta(weeks=-14)

# create request to return the skis and snowboards 
#request1 = customer1.returnSkis(intSkisRented)
#request2 = customer2.returnSkis(intSkisRented)
#request3 = customer3.returnSnowBoards(intSnowboardsRented)
#request4 = customer4.returnSnowBoards(intSnowboardsRented)

# return the skis and snowboards and get a bill
#shop1.returnSkis(request1)
#shop1.returnSkis(request2)
#shop1.returnSnowBoards(request3)
#shop1.returnSnowBoards(request4)      

