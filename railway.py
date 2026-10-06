import random
import os


class Train:
    def __init__(self, train_number, train_name, source, destination, available_seats):
        self.train_number = train_number
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.available_seats = available_seats


class Booking:
    def __init__(self, pnr, passenger_name, age, train_number,
                 journey_date, number_of_seats, travel_class):
        self.pnr = pnr
        self.passenger_name = passenger_name
        self.age = age
        self.train_number = train_number
        self.journey_date = journey_date
        self.number_of_seats = number_of_seats
        self.travel_class = travel_class


print("===== RAILWAY TICKET RESERVATION SYSTEM =====")


trains = [
    Train(12723, "Telangana Express", "Hyderabad", "Delhi", 50),
    Train(12760, "Charminar Express", "Hyderabad", "Chennai", 40),
    Train(12727, "Godavari Express", "Hyderabad", "Visakhapatnam", 45)
]


def search_trains(trains):
    source = input("Enter source station: ").strip().lower()
    destination = input("Enter destination station: ").strip().lower()

    found = False

    for train in trains:
        if train.source.lower() == source and train.destination.lower() == destination:
            print("Train Number:", train.train_number)
            print("Train Name:", train.train_name)
            print("Source:", train.source)
            print("Destination:", train.destination)
            print("Available Seats:", train.available_seats)

            found = True

    if not found:
        print("No Trains Found for the given Route!")


def save_bookings(bookings):
    file = open("bookings.txt", "w")

    for booking in bookings:
        file.write("========================================\n")
        file.write("          RAILWAY BOOKING\n")
        file.write("========================================\n")
        file.write("PNR           : " + str(booking.pnr) + "\n")
        file.write("Passenger     : " + booking.passenger_name + "\n")
        file.write("Age           : " + str(booking.age) + "\n")
        file.write("Train Number  : " + str(booking.train_number) + "\n")
        file.write("Journey Date  : " + booking.journey_date + "\n")
        file.write("Seats         : " + str(booking.number_of_seats) + "\n")
        file.write("Travel Class  : " + booking.travel_class + "\n")
        file.write("========================================\n")
        file.write("\n")

    file.close()


def load_bookings():
    if not os.path.exists("bookings.txt"):
        return []

    file = open("bookings.txt", "r")
    lines = file.readlines()
    file.close()

    bookings = []

    i = 0

    while i < len(lines):

        if lines[i].startswith("PNR"):
            pnr = int(lines[i].split(":")[1].strip())
            passenger_name = lines[i + 1].split(":")[1].strip()
            age = int(lines[i + 2].split(":")[1].strip())
            train_number = int(lines[i + 3].split(":")[1].strip())
            journey_date = lines[i + 4].split(":")[1].strip()
            number_of_seats = int(lines[i + 5].split(":")[1].strip())
            travel_class = lines[i + 6].split(":")[1].strip()

            booking = Booking(
                pnr,
                passenger_name,
                age,
                train_number,
                journey_date,
                number_of_seats,
                travel_class
            )

            bookings.append(booking)

            i = i + 8

        else:
            i = i + 1

    return bookings


def update_available_seats(trains, bookings):
    for train in trains:
        for booking in bookings:
            if train.train_number == booking.train_number:
                train.available_seats -= booking.number_of_seats


def generate_pnr(bookings):
    while True:
        pnr = random.randint(100000, 999999)

        pnr_exists = False

        for booking in bookings:
            if booking.pnr == pnr:
                pnr_exists = True
                break

        if not pnr_exists:
            return pnr


def book_ticket(trains, bookings):

    try:
        train_number = int(input("Enter train number: "))
    except ValueError:
        print("Please enter a valid train number.")
        return

    selected_train = None

    for train in trains:
        if train.train_number == train_number:
            selected_train = train
            break

    if selected_train is None:
        print("Train Not Found.")
        return

    print("Train found:", selected_train.train_name)

    try:
        number_of_seats = int(input("Enter number of seats: "))
    except ValueError:
        print("Please enter a valid number of seats.")
        return

    if number_of_seats <= 0:
        print("Enter a valid number of seats greater than 0.")
        return

    if number_of_seats > selected_train.available_seats:
        print("Not enough seats available.")
        return

    print("Seats are Available.")

    passenger_name = input("Enter passenger name: ").strip()

    if passenger_name == "":
        print("Passenger name cannot be empty.")
        return

    try:
        age = int(input("Enter passenger age: "))
    except ValueError:
        print("Please enter a valid age.")
        return

    if age <= 0:
        print("Please enter a valid age.")
        return

    journey_date = input("Enter Journey date: ").strip()

    if journey_date == "":
        print("Journey date cannot be empty.")
        return

    print("1. General")
    print("2. Sleeper")
    print("3. AC")

    class_choice = input("Enter travel class: ")

    if class_choice == "1":
        travel_class = "General"
    elif class_choice == "2":
        travel_class = "Sleeper"
    elif class_choice == "3":
        travel_class = "AC"
    else:
        print("Invalid travel class.")
        return

    selected_train.available_seats -= number_of_seats

    pnr = generate_pnr(bookings)

    booking = Booking(
        pnr,
        passenger_name,
        age,
        train_number,
        journey_date,
        number_of_seats,
        travel_class
    )

    bookings.append(booking)

    save_bookings(bookings)

    print("Remaining Seats:", selected_train.available_seats)
    print("PNR:", pnr)


def view_bookings(bookings):

    if not bookings:
        print("No Bookings Found.")
        return

    for booking in bookings:
        print("========================================")
        print("          RAILWAY BOOKING")
        print("========================================")
        print("PNR           :", booking.pnr)
        print("Passenger     :", booking.passenger_name)
        print("Age           :", booking.age)
        print("Train Number  :", booking.train_number)
        print("Journey Date  :", booking.journey_date)
        print("Seats         :", booking.number_of_seats)
        print("Travel Class  :", booking.travel_class)
        print("========================================")


def cancel_ticket(bookings, trains):

    try:
        pnr = int(input("Enter PNR Number: "))
    except ValueError:
        print("Please enter a valid PNR number.")
        return

    for booking in bookings:

        if booking.pnr == pnr:

            print("Booking Found.")

            for train in trains:
                if train.train_number == booking.train_number:
                    train.available_seats += booking.number_of_seats
                    break

            bookings.remove(booking)

            save_bookings(bookings)

            print("Ticket Cancelled Successfully.")
            return

    print("PNR Not Found. Check the PNR Number and Try Again.")


bookings = load_bookings()

update_available_seats(trains, bookings)


choice = 0

while choice != 5:

    print("\n1. Search Trains")
    print("2. Book Ticket")
    print("3. View Bookings")
    print("4. Cancel Ticket")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        search_trains(trains)

    elif choice == 2:
        book_ticket(trains, bookings)

    elif choice == 3:
        view_bookings(bookings)

    elif choice == 4:
        cancel_ticket(bookings, trains)

    elif choice == 5:
        print("Thank you for using Railway Ticket Reservation System.")

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        