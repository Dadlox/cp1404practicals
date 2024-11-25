from Codes.Practical.Week9.Assessment.silver_service_taxi import SilverServiceTaxi

new_taxi = SilverServiceTaxi("Hummer", 200, 2)
print(new_taxi)
new_taxi.start_fare()
new_taxi.drive(10)
print(new_taxi.get_fare())

