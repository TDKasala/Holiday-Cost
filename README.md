# Holiday Cost Calculator

This program is designed to help you calculate the total cost of your holiday, including hotel stay, flight ticket, and car rental.

## Table of Contents

- [Description](#description)
- [Functions](#functions)
- [Usage](#usage)
- [Example](#example)

## Description

When planning a holiday, it's important to have an estimate of the total cost. This program provides functions to calculate the cost of hotel stay, flight tickets, car rental, and the overall holiday cost.

## Functions

1. **`hotel_cost(total_days, price)`**

   This function calculates the cost of staying at a hotel based on the number of days and the price per night.

   - `total_days` (int): Number of days you'll be staying at the hotel.
   - `price` (float): Price per night at the hotel.

   Returns the total cost of the hotel stay.

2. **`plane_cost(city)`**

   This function calculates the cost of a plane ticket based on the destination city.

   - `city` (str): The destination city for the flight.

   Returns the cost of the flight ticket to the specified city. If the city is not recognized, it provides an error message.

3. **`car_rental(number_days, rental_cost)`**

   This function calculates the cost of renting a car for a certain number of days.

   - `number_days` (int): Number of days you'll be renting the car.
   - `rental_cost` (float): Daily cost of renting the car.

   Returns the total cost of car rental.

4. **`holiday_cost(nights_number, ticket_cost, rental_days)`**

   This function calculates the total cost of the holiday by adding the costs of the hotel stay, flight ticket, and car rental.

   - `nights_number` (float): Cost of the hotel stay.
   - `ticket_cost` (float): Cost of the flight ticket.
   - `rental_days` (float): Cost of the car rental.

   Prints the overall cost of the holiday to the user.

## Usage

1. Define the number of days you'll be staying at the hotel and the price per night.
2. Choose a destination city for the flight.
3. Enter the number of days you'll be renting a car and the daily rental cost.
4. The program will calculate and display the total cost of your holiday.

## Example

```python
# Calling all four functions and assigning values to the parameters

nights_number = hotel_cost(int(input("\nHow many days will you be staying at the hotel: ")), 800.99)
print("The total cost for the hotel is:", nights_number)

city = input("\nPlease choose a city from the options below:\n- Johannesburg\n- Durban\n: ").capitalize()
ticket_cost = plane_cost(city)
print(f"The ticket for {city} is: {ticket_cost}")

rental_days = car_rental(int(input("\nPlease enter the number of days you will be renting the car for: ")), 400.99)
print("The total cost of car rental is:", rental_days)

holiday_cost(nights_number, ticket_cost, rental_days)
```
