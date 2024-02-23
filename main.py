from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from users_data import SheetyUsers

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
users_data = SheetyUsers()

print("Welcome to Flight Club.\n \
We find the best flight deals and email them to you.")

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email1 = "email1"
email2 = "email2"

while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" or email1.lower() == "exit":
        exit()
    email2 = input("Please verify your email : ")
    if email2.lower() == "quit" or email2.lower() == "exit":
        exit()
print("OK, You're in the Club!")
users_data.post_new_row(first_name, last_name, email1)


ORIGIN_CITY_IATA = "FRA"
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

seven_month_from_today = datetime.now() + timedelta(days=(7 * 30))
eight_month_from_today = datetime.now() + timedelta(days=(8 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=seven_month_from_today,
        to_time=eight_month_from_today
    )
    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:

        users = data_manager.get_customer_data()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)


        #------------------ to send sms ------------------#
        # notification_manager.send_sms(message)

        #send email to multiple customer------------------#
        notification_manager.send_emails(emails, message)


