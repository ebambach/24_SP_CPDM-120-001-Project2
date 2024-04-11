class ShopClass(object):
    """description of class"""

class Shop:
    def __init__(self):
        self.inventory = {'skis': 10, 'snowboards': 8}  # Initial inventory
        self.daily_skis_rented = 0
        self.daily_snowboards_rented = 0
        self.daily_revenue = 0

    def display_inventory(self):
        print("Available Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item.capitalize()}: {quantity}")

    def rent_equipment(self, equipment_type, quantity, rental_period):
        if equipment_type not in self.inventory:
            print("Sorry, we don't have that equipment.")
            return

        if quantity > self.inventory[equipment_type]:
            print("Sorry, we don't have enough inventory for that quantity.")
            return

        if rental_period == "hourly":
            price = self.get_hourly_price(equipment_type) * quantity
        elif rental_period == "daily":
            price = self.get_daily_price(equipment_type) * quantity
        elif rental_period == "weekly":
            price = self.get_weekly_price(equipment_type) * quantity
        else:
            print("Invalid rental period.")
            return

        self.inventory[equipment_type] -= quantity
        self.update_daily_rental_stats(equipment_type, quantity)
        self.daily_revenue += price
        print(f"Renting {quantity} {equipment_type} for {rental_period} at ${price}")

    def update_daily_rental_stats(self, equipment_type, quantity):
        if equipment_type == 'skis':
            self.daily_skis_rented += quantity
        elif equipment_type == 'snowboards':
            self.daily_snowboards_rented += quantity

    def get_hourly_price(self, equipment_type):
        if equipment_type == 'skis':
            return 15
        elif equipment_type == 'snowboards':
            return 10

    def get_daily_price(self, equipment_type):
        if equipment_type == 'skis':
            return 50
        elif equipment_type == 'snowboards':
            return 40

    def get_weekly_price(self, equipment_type):
        if equipment_type == 'skis':
            return 200
        elif equipment_type == 'snowboards':
            return 160

# Testing the Shop class
shop = Shop()
shop.display_inventory()
shop.rent_equipment('skis', 2, 'daily')
shop.rent_equipment('snowboards', 1, 'weekly')
shop.display_inventory()
print(f"Daily skis rented: {shop.daily_skis_rented}")
print(f"Daily snowboards rented: {shop.daily_snowboards_rented}")
print(f"Daily revenue: ${shop.daily_revenue}")

