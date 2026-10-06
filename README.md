# Railway Ticket Reservation System

## 1. Project Description

The Railway Ticket Reservation System is a Python-based console application used to manage basic railway ticket reservation operations.

The system allows users to:

* Search for trains
* Book railway tickets
* Generate a unique PNR number
* View booked tickets
* Cancel tickets
* Store booking details in a text file

The project uses Object-Oriented Programming concepts, functions, conditional statements, loops, exception handling, and file handling.

---

## 2. Features

### 2.1 Search Trains

Users can search for available trains by entering the source and destination stations.

### 2.2 Book Ticket

Users can select a train, enter passenger details, select the number of seats and travel class, and book a ticket.

### 2.3 Generate PNR

A unique six-digit PNR number is generated automatically for every booking.

### 2.4 View Bookings

Users can view all the bookings stored in the system.

### 2.5 Cancel Ticket

Users can cancel a ticket using the PNR number.

### 2.6 File Storage

Booking details are stored in `bookings.txt` so that the bookings remain available even after closing the program.

---

## 3. Technologies Used

* Python
* Object-Oriented Programming
* File Handling
* Exception Handling
* Random Module
* OS Module

---

## 4. Python Concepts Used

The following Python concepts are used in this project:

* Variables
* Data Types
* Input and Output
* Type Conversion
* Conditional Statements
* `if`, `elif`, and `else`
* `for` loop
* `while` loop
* Functions
* Function Parameters
* Return Statements
* Classes and Objects
* Constructors
* Object Attributes
* Lists
* String Methods
* Exception Handling
* File Handling
* Modules
* `random`
* `os`

---

# 5. Classes Used

## 5.1 Train Class

The `Train` class is used to store the details of a train.

### Syntax

```python
class Train:
    def __init__(self, train_number, train_name, source, destination, available_seats):
```

### Attributes

* `train_number` - Stores the train number.
* `train_name` - Stores the train name.
* `source` - Stores the source station.
* `destination` - Stores the destination station.
* `available_seats` - Stores the number of available seats.

---

## 5.2 Booking Class

The `Booking` class is used to store the details of a railway ticket booking.

### Attributes

* `pnr` - Stores the unique PNR number.
* `passenger_name` - Stores the passenger name.
* `age` - Stores the passenger age.
* `train_number` - Stores the selected train number.
* `journey_date` - Stores the journey date.
* `number_of_seats` - Stores the number of seats booked.
* `travel_class` - Stores the selected travel class.

---

# 6. Objects Created

Three `Train` objects are created and stored inside the `trains` list.

### Train 1

```python
Train(12723, "Telangana Express", "Hyderabad", "Delhi", 50)
```

### Train 2

```python
Train(12760, "Charminar Express", "Hyderabad", "Chennai", 40)
```

### Train 3

```python
Train(12727, "Godavari Express", "Hyderabad", "Visakhapatnam", 45)
```

Each object stores the details of one train.

---

# 7. Functions Used

The project contains the following functions:

| Function                   | Purpose                                         |
| -------------------------- | ----------------------------------------------- |
| `search_trains()`          | Searches trains based on source and destination |
| `save_bookings()`          | Saves booking details into `bookings.txt`       |
| `load_bookings()`          | Loads existing bookings from `bookings.txt`     |
| `update_available_seats()` | Updates available seats using stored bookings   |
| `generate_pnr()`           | Generates a unique six-digit PNR                |
| `book_ticket()`            | Books a railway ticket                          |
| `view_bookings()`          | Displays all bookings                           |
| `cancel_ticket()`          | Cancels a booking using PNR                     |

---

# 8. Line-by-Line Code Documentation

## 8.1 Import Statements

```python
import random
import os
```

### `import random`

The `random` module is imported to generate a random six-digit PNR number.

It is used in the `generate_pnr()` function.

### `import os`

The `os` module is imported to work with the operating system.

In this project, it is used to check whether the `bookings.txt` file exists.

---

# 9. Train Class Documentation

```python
class Train:
```

Defines a class named `Train`.

The class is used as a blueprint for creating train objects.

```python
def __init__(self, train_number, train_name, source, destination, available_seats):
```

This is the constructor of the `Train` class.

It is automatically called when a new `Train` object is created.

The constructor accepts train number, train name, source, destination, and available seats.

```python
self.train_number = train_number
```

Stores the train number inside the object.

```python
self.train_name = train_name
```

Stores the train name inside the object.

```python
self.source = source
```

Stores the source station inside the object.

```python
self.destination = destination
```

Stores the destination station inside the object.

```python
self.available_seats = available_seats
```

Stores the number of available seats inside the object.

---

# 10. Booking Class Documentation

```python
class Booking:
```

Defines a class named `Booking`.

The class is used to create booking objects.

```python
def __init__(self, pnr, passenger_name, age, train_number,
             journey_date, number_of_seats, travel_class):
```

This is the constructor of the `Booking` class.

It accepts all the information required to store a passenger's booking.

```python
self.pnr = pnr
```

Stores the PNR number.

```python
self.passenger_name = passenger_name
```

Stores the passenger name.

```python
self.age = age
```

Stores the passenger age.

```python
self.train_number = train_number
```

Stores the train number selected by the passenger.

```python
self.journey_date = journey_date
```

Stores the journey date.

```python
self.number_of_seats = number_of_seats
```

Stores the number of seats booked.

```python
self.travel_class = travel_class
```

Stores the selected travel class.

---

# 11. Railway System Heading

```python
print("===== RAILWAY TICKET RESERVATION SYSTEM =====")
```

Displays the title of the Railway Ticket Reservation System when the program starts.

---

# 12. Creating Train Objects

```python
trains = [
    Train(12723, "Telangana Express", "Hyderabad", "Delhi", 50),
    Train(12760, "Charminar Express", "Hyderabad", "Chennai", 40),
    Train(12727, "Godavari Express", "Hyderabad", "Visakhapatnam", 45)
]
```

A list named `trains` is created.

Three `Train` objects are created and stored inside the list.

This allows the program to store and access details of multiple trains.

---

# 13. `search_trains()` Function

```python
def search_trains(trains):
```

Defines the `search_trains()` function.

The function receives the `trains` list as a parameter.

```python
source = input("Enter source station: ").strip().lower()
```

Takes the source station from the user.

* `input()` accepts user input.
* `.strip()` removes unnecessary spaces from the beginning and end.
* `.lower()` converts the input to lowercase.

```python
destination = input("Enter destination station: ").strip().lower()
```

Takes the destination station from the user and converts it into lowercase after removing extra spaces.

```python
found = False
```

Creates a Boolean variable to track whether a matching train is found.

Initially, it is set to `False`.

```python
for train in trains:
```

Loops through every train object in the `trains` list.

```python
if train.source.lower() == source and train.destination.lower() == destination:
```

Checks whether the source and destination entered by the user match the train's source and destination.

The `and` operator ensures that both conditions must be true.

```python
print("Train Number:", train.train_number)
print("Train Name:", train.train_name)
print("Source:", train.source)
print("Destination:", train.destination)
print("Available Seats:", train.available_seats)
```

Displays the details of the matching train.

```python
found = True
```

Changes the value of `found` to `True` because a matching train has been found.

```python
if not found:
```

Checks whether no matching train was found.

```python
print("No Trains Found for the given Route!")
```

Displays a message when there is no train for the requested route.

---

# 14. `save_bookings()` Function

```python
def save_bookings(bookings):
```

Defines a function to save booking details into a file.

```python
file = open("bookings.txt", "w")
```

Opens `bookings.txt` in write mode.

The `"w"` mode allows the program to write booking information to the file.

```python
for booking in bookings:
```

Loops through every booking object in the bookings list.

The following `file.write()` statements write the booking information into the file in a structured format.

```python
file.write("========================================\n")
```

Writes a separator line.

```python
file.write("          RAILWAY BOOKING\n")
```

Writes the booking heading.

```python
file.write("PNR           : " + str(booking.pnr) + "\n")
```

Writes the PNR number.

`str()` converts the PNR number into a string before joining it with other strings.

```python
file.write("Passenger     : " + booking.passenger_name + "\n")
```

Writes the passenger name.

```python
file.write("Age           : " + str(booking.age) + "\n")
```

Writes the passenger age.

```python
file.write("Train Number  : " + str(booking.train_number) + "\n")
```

Writes the train number.

```python
file.write("Journey Date  : " + booking.journey_date + "\n")
```

Writes the journey date.

```python
file.write("Seats         : " + str(booking.number_of_seats) + "\n")
```

Writes the number of booked seats.

```python
file.write("Travel Class  : " + booking.travel_class + "\n")
```

Writes the selected travel class.

```python
file.write("========================================\n")
file.write("\n")
```

Writes the closing separator and a blank line between bookings.

```python
file.close()
```

Closes the file after writing the booking information.

---

# 15. `load_bookings()` Function

```python
def load_bookings():
```

Defines a function to load previously stored bookings from `bookings.txt`.

```python
if not os.path.exists("bookings.txt"):
```

Checks whether the `bookings.txt` file does not exist.

```python
return []
```

Returns an empty list if the file does not exist.

```python
file = open("bookings.txt", "r")
```

Opens the file in read mode.

```python
lines = file.readlines()
```

Reads all lines from the file and stores them in the `lines` list.

```python
file.close()
```

Closes the file.

```python
bookings = []
```

Creates an empty list to store the booking objects.

```python
i = 0
```

Creates a counter variable to start reading the file from the first line.

```python
while i < len(lines):
```

Runs the loop while there are still lines left to process.

```python
if lines[i].startswith("PNR"):
```

Checks whether the current line starts with `"PNR"`.

This identifies the beginning of a booking record.

```python
pnr = int(lines[i].split(":")[1].strip())
```

Extracts the PNR from the line.

* `split(":")` separates the label and value.
* `[1]` selects the value.
* `.strip()` removes extra spaces.
* `int()` converts the value into an integer.

The same approach is used to extract passenger name, age, train number, journey date, number of seats, and travel class.

```python
booking = Booking(
    pnr,
    passenger_name,
    age,
    train_number,
    journey_date,
    number_of_seats,
    travel_class
)
```

Creates a `Booking` object using the extracted information.

```python
bookings.append(booking)
```

Adds the booking object to the `bookings` list.

```python
i = i + 8
```

Moves the counter forward through the booking record.

```python
else:
    i = i + 1
```

If the current line does not contain a PNR, the counter moves to the next line.

```python
return bookings
```

Returns the list of loaded booking objects.

---

# 16. `update_available_seats()` Function

```python
def update_available_seats(trains, bookings):
```

Defines a function to update the available seats of trains based on existing bookings.

```python
for train in trains:
```

Loops through all trains.

```python
for booking in bookings:
```

Loops through all bookings.

```python
if train.train_number == booking.train_number:
```

Checks whether the booking belongs to the current train.

```python
train.available_seats -= booking.number_of_seats
```

Subtracts the booked seats from the train's available seats.

---

# 17. `generate_pnr()` Function

```python
def generate_pnr(bookings):
```

Defines a function to generate a unique PNR.

```python
while True:
```

Creates a loop that continues until a unique PNR is generated.

```python
pnr = random.randint(100000, 999999)
```

Generates a random six-digit number.

```python
pnr_exists = False
```

Initially assumes that the generated PNR does not already exist.

```python
for booking in bookings:
```

Checks all existing bookings.

```python
if booking.pnr == pnr:
```

Checks whether the generated PNR matches an existing PNR.

```python
pnr_exists = True
break
```

If the PNR already exists, the variable is changed to `True` and the loop stops checking further bookings.

```python
if not pnr_exists:
    return pnr
```

If the generated PNR is not already present, it is returned.

---

# 18. `book_ticket()` Function

```python
def book_ticket(trains, bookings):
```

Defines the function used to book a railway ticket.

### Train Number

```python
try:
    train_number = int(input("Enter train number: "))
except ValueError:
```

The program accepts the train number and converts it into an integer.

`try` and `except` prevent the program from stopping when the user enters invalid input.

```python
print("Please enter a valid train number.")
return
```

Displays an error message and exits the function if the input cannot be converted to an integer.

### Finding the Train

```python
selected_train = None
```

Initially no train is selected.

```python
for train in trains:
```

Loops through the train list.

```python
if train.train_number == train_number:
```

Checks whether the train number matches.

```python
selected_train = train
break
```

Stores the matching train object and stops the loop.

```python
if selected_train is None:
```

Checks whether no matching train was found.

```python
print("Train Not Found.")
return
```

Displays an error message and exits the function.

### Number of Seats

```python
try:
    number_of_seats = int(input("Enter number of seats: "))
except ValueError:
```

Accepts the number of seats and converts it into an integer.

```python
if number_of_seats <= 0:
```

Checks whether the entered number is zero or negative.

```python
print("Enter a valid number of seats greater than 0.")
return
```

Prevents invalid seat booking.

```python
if number_of_seats > selected_train.available_seats:
```

Checks whether the requested number of seats is greater than the available seats.

```python
print("Not enough seats available.")
return
```

Stops the booking if enough seats are not available.

### Passenger Details

```python
passenger_name = input("Enter passenger name: ").strip()
```

Accepts the passenger name and removes unnecessary spaces.

```python
if passenger_name == "":
```

Checks whether the passenger name is empty.

```python
print("Passenger name cannot be empty.")
return
```

Prevents booking without a passenger name.

```python
try:
    age = int(input("Enter passenger age: "))
except ValueError:
```

Accepts the passenger age and converts it into an integer.

```python
if age <= 0:
```

Checks whether the age is valid.

```python
print("Please enter a valid age.")
return
```

Displays an error message for invalid age.

### Journey Date

```python
journey_date = input("Enter Journey date: ").strip()
```

Accepts the journey date.

```python
if journey_date == "":
```

Checks whether the date is empty.

```python
print("Journey date cannot be empty.")
return
```

Prevents booking without a journey date.

### Travel Class

```python
print("1. General")
print("2. Sleeper")
print("3. AC")
```

Displays the available travel class options.

```python
class_choice = input("Enter travel class: ")
```

Accepts the user's travel class choice.

```python
if class_choice == "1":
    travel_class = "General"
```

Selects General class when the user enters `1`.

```python
elif class_choice == "2":
    travel_class = "Sleeper"
```

Selects Sleeper class when the user enters `2`.

```python
elif class_choice == "3":
    travel_class = "AC"
```

Selects AC class when the user enters `3`.

```python
else:
    print("Invalid travel class.")
    return
```

Rejects any other travel class choice.

### Creating the Booking

```python
selected_train.available_seats -= number_of_seats
```

Reduces the available seats after successful validation.

```python
pnr = generate_pnr(bookings)
```

Generates a unique PNR.

```python
booking = Booking(
    pnr,
    passenger_name,
    age,
    train_number,
    journey_date,
    number_of_seats,
    travel_class
)
```

Creates a new `Booking` object.

```python
bookings.append(booking)
```

Adds the new booking to the bookings list.

```python
save_bookings(bookings)
```

Saves all bookings into `bookings.txt`.

```python
print("Remaining Seats:", selected_train.available_seats)
print("PNR:", pnr)
```

Displays the remaining seats and generated PNR.

---

# 19. `view_bookings()` Function

```python
def view_bookings(bookings):
```

Defines a function to display all existing bookings.

```python
if not bookings:
```

Checks whether the bookings list is empty.

```python
print("No Bookings Found.")
return
```

Displays a message and exits if there are no bookings.

```python
for booking in bookings:
```

Loops through every booking.

The following statements display the details of each booking:

```python
print("PNR           :", booking.pnr)
print("Passenger     :", booking.passenger_name)
print("Age           :", booking.age)
print("Train Number  :", booking.train_number)
print("Journey Date  :", booking.journey_date)
print("Seats         :", booking.number_of_seats)
print("Travel Class  :", booking.travel_class)
```

Each booking attribute is displayed in a structured format.

---

# 20. `cancel_ticket()` Function

```python
def cancel_ticket(bookings, trains):
```

Defines a function to cancel an existing booking.

```python
try:
    pnr = int(input("Enter PNR Number: "))
except ValueError:
```

Accepts the PNR number and converts it into an integer.

If the input is invalid, `ValueError` is handled.

```python
for booking in bookings:
```

Loops through all existing bookings.

```python
if booking.pnr == pnr:
```

Checks whether the entered PNR matches a booking.

```python
print("Booking Found.")
```

Displays a confirmation that the booking exists.

```python
for train in trains:
```

Loops through the available trains.

```python
if train.train_number == booking.train_number:
```

Finds the train associated with the booking.

```python
train.available_seats += booking.number_of_seats
```

Adds the cancelled seats back to the train's available seats.

```python
break
```

Stops searching for the train.

```python
bookings.remove(booking)
```

Removes the cancelled booking from the bookings list.

```python
save_bookings(bookings)
```

Updates the `bookings.txt` file after cancellation.

```python
print("Ticket Cancelled Successfully.")
return
```

Displays a successful cancellation message and exits the function.

```python
print("PNR Not Found. Check the PNR Number and Try Again.")
```

Displays an error message when the entered PNR does not exist.

---

# 21. Loading Existing Bookings

```python
bookings = load_bookings()
```

Loads previously saved bookings from `bookings.txt` when the program starts.

```python
update_available_seats(trains, bookings)
```

Updates the available seats of each train based on the loaded bookings.

This ensures that previously booked seats are considered when the program starts again.

---

# 22. Main Menu

```python
choice = 0
```

Initializes the menu choice.

```python
while choice != 5:
```

Runs the main menu until the user selects option `5`.

```python
print("\n1. Search Trains")
print("2. Book Ticket")
print("3. View Bookings")
print("4. Cancel Ticket")
print("5. Exit")
```

Displays the available menu options.

```python
try:
    choice = int(input("Enter your choice: "))
except ValueError:
```

Accepts the user's menu choice and converts it into an integer.

Invalid input is handled using `try` and `except`.

```python
if choice == 1:
    search_trains(trains)
```

Calls `search_trains()` when the user selects option 1.

```python
elif choice == 2:
    book_ticket(trains, bookings)
```

Calls `book_ticket()` when the user selects option 2.

```python
elif choice == 3:
    view_bookings(bookings)
```

Calls `view_bookings()` when the user selects option 3.

```python
elif choice == 4:
    cancel_ticket(bookings, trains)
```

Calls `cancel_ticket()` when the user selects option 4.

```python
elif choice == 5:
    print("Thank you for using Railway Ticket Reservation System.")
```

Displays a thank-you message and ends the program.

```python
else:
    print("Invalid choice. Please enter a number between 1 and 5.")
```

Displays an error message when the user enters an invalid menu option.

---

# 23. File Handling

The project uses a text file named `bookings.txt` to store booking information.

### Write Mode

```python
open("bookings.txt", "w")
```

The `"w"` mode is used to write booking information into the file.

### Read Mode

```python
open("bookings.txt", "r")
```

The `"r"` mode is used to read previously stored booking information.

### File Existence Check

```python
os.path.exists("bookings.txt")
```

Checks whether the booking file exists before trying to read it.

---

# 24. Project Execution Flow

The overall execution flow of the project is:

1. Import required modules.
2. Define the `Train` class.
3. Define the `Booking` class.
4. Create train objects.
5. Load previously stored bookings.
6. Update available train seats.
7. Display the main menu.
8. Accept the user's choice.
9. Perform the selected operation.
10. Continue displaying the menu until the user selects Exit.

---

# 25. Menu Flow

```text
Start
  |
  v
Load Existing Bookings
  |
  v
Update Available Seats
  |
  v
Display Main Menu
  |
  +----> 1. Search Trains
  |
  +----> 2. Book Ticket
  |
  +----> 3. View Bookings
  |
  +----> 4. Cancel Ticket
  |
  +----> 5. Exit
  |
  v
End
```

---

# 26. OOP Concepts Used

### Classes and Objects

The project uses two classes:

* `Train`
* `Booking`

Objects are created from these classes to store train and booking information.

### Encapsulation

The data and related structure are grouped inside classes using object attributes such as:

```python
self.train_number
self.train_name
self.pnr
self.passenger_name

---

# 27. Conclusion

The Railway Ticket Reservation System demonstrates the use of basic Python programming concepts along with Object-Oriented Programming and file handling.

The project provides basic railway reservation operations such as searching trains, booking tickets, viewing bookings, generating PNR numbers, and cancelling tickets.