# -----------------------------------------------------------------
# Assignment Name:      Project 2
# Name:                 Team B
# -----------------------------------------------------------------
import CustomerClass as Customer
import ShopClass as Shop



# ------------------------------------------------------------------
# Project 2 Class Test Area
# ------------------------------------------------------------------

try:
	# Testing Area
	test1 = Shop.ShopClass(100,100)  

	test1.calc_estimatebestrentalprice(8, "Hourly", 2, 2)
	#test0 = Customer.CustomerClass("Crystal Clear", 1, 1, 0, 1, 0, 0, "")

	#print(repr(test0))

	test1.calc_estimatebestrentalprice(10, "Hourly", 1, 0, 0)
except Exception as e:
	print(e)
	
	
input()
