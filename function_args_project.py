from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type = 'Overnight'):
    from_lat = from_coords[0]
    from_long = from_coords[1]
    to_lat = to_coords[0]
    to_long = to_coords[1]
    distance = get_distance(*from_coords, *to_coords)
    shipping_rate = SHIPPING_PRICES[shipping_type]
    price = distance * shipping_rate
    return format_price(price)

# Test the function by calling
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here
def calculate_driver_cost(distance, *drivers):
    cheapest_driver = None
    cheapest_driver_price = None
    for i in drivers:
        driver_time = i.speed * distance
        price_for_driver = i.salary * driver_time
        if cheapest_driver == None:
            cheapest_driver = i
            cheapest_driver_price = price_for_driver
        elif price_for_driver < cheapest_driver_price:
            cheapest_driver = i
            cheapest_driver_price = price_for_driver
    return cheapest_driver_price, cheapest_driver

def calculate_money_made(**trips):
    total_money_made = 0
    for i in trips.values():
        trip_revenue = i.cost - i.driver.cost
        total_money_made += trip_revenue
    return total_money_made

test_function(calculate_money_made)






# Test the function by calling
# test_function(calculate_driver_cost)

# Define calculate_money_made() here


# Test the function by calling
# test_function(calculate_money_made)
