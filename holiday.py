# Define a function to calculate the cost of hotel stay
def calculate_hotel_cost(total_days, price_per_night):
    total_cost = total_days * price_per_night
    return total_cost

# Define a function to calculate the cost of plane ticket
def calculate_plane_ticket_cost(city):
    ticket_cost = 0
    if city == 'Johannesburg':
        ticket_cost += 1200
    elif city == 'Durban':
        ticket_cost += 2800
    else:
        print(f"Sorry wrong choice. We do not fly to {city}")
        ticket_cost = None  # Set a default value for invalid city choice
    return ticket_cost

# Define a function to calculate the cost of car rental
def calculate_car_rental_cost(number_of_days, rental_cost_per_day):
    total_rental_cost = number_of_days * rental_cost_per_day
    return total_rental_cost

# Define a function to calculate the total holiday cost
def calculate_total_holiday_cost(hotel_cost, ticket_cost, rental_cost):
    total_holiday_cost = hotel_cost + ticket_cost + rental_cost
    return total_holiday_cost

# User input section for hotel stay
hotel_nights = int(input("How many nights will you be staying at the hotel: "))

# User input section for plane ticket
plane_city = input("Please choose a city: Johannesburg or Durban: ").capitalize()
while plane_city not in ['Johannesburg', 'Durban']:
    print("Invalid city choice. Please choose either Johannesburg or Durban.")
    plane_city = input("Please choose a city: Johannesburg or Durban: ").capitalize()

# User input section for car rental
rental_days = int(input("Please enter the number of days you will be renting the car for: "))
while rental_days <= 0:
    print("Invalid number of rental days. Please enter a positive value.")
    rental_days = int(input("Please enter the number of days you will be renting the car for: "))

# Calculate hotel cost and display
hotel_cost = calculate_hotel_cost(hotel_nights, 800.99)
print("The total cost for the hotel is:", hotel_cost)

# Calculate plane ticket cost and display
ticket_cost = calculate_plane_ticket_cost(plane_city)
if ticket_cost is not None:
    print(f"The ticket for {plane_city} is:", ticket_cost)

# Calculate car rental cost and display
car_rental_cost = calculate_car_rental_cost(rental_days, 400.99)
print("The total cost of the car rental is:", car_rental_cost)

# Calculate total holiday cost and display
total_holiday_cost = calculate_total_holiday_cost(hotel_cost, ticket_cost, car_rental_cost)
print("The overall cost of your holiday will be:", total_holiday_cost)
