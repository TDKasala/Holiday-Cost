# Defining a function for the cost of the stay at the hotel
# Calculating the cost by multiplying the number of days by the price

def calculate_hotel_cost(total_days, price):
    total_cost = total_days * price
    return float(f"{total_cost}")

# Defining the function for the price of the ticket per city
# Using an if/else to display appropriate message to the user


def calculate_plane_ticket_cost(city):

    ticket = 0
    if city == 'Johannesburg':
        ticket += 1200

    elif city == 'Durban':
        ticket += 2800

    else:
        print(f"Sorry wrong choice. We do not fly to {city}")

    return ticket

# Defining a function for the cost of the car rental and calulating the cost


def calculate_car_rental_cost(number_days, rental_cost):
    total_rental_cost = number_days * rental_cost
    return float(f"{total_rental_cost}")


# Defining a function for the total cost of the holiday
# Calculating the cost by additioning the 3 amounts (hotel cost, flight ticket and car rental)
# Printing the amount to the user

def calculate_total_holiday_cost(nights_number, ticket_cost, rental_days):
    total_holiday_cost = nights_number + ticket_cost + rental_days
    print(f"\nThe overal cost of your holiday will be :", total_holiday_cost)


# Calling all for 4 functions and assigning values to the parameters

hotel_nights = calculate_hotel_cost(
    int(input("\nHow many days will you be staying at the hotel: ")), 800.99)
print("The total cost for the hotel is: ", hotel_nights)

city = input(
    "\nPlease choose a city from the option below:\nJohannesburg\nDurban\n: ").capitalize()
ticket_cost = calculate_plane_ticket_cost(city)
print(f"The ticket for {city} is:", ticket_cost)


car_rental_cost = calculate_car_rental_cost(int(input(
    "\nPlease enter the number of days you will be renting the car for: ", )), 400.99)
print("The total cost of the car rental is: ", car_rental_cost)

calculate_total_holiday_cost(hotel_nights, ticket_cost, car_rental_cost)
