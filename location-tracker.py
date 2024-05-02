import phonenumbers
from phonenumbers
from api import number


Key = "6d6f9676srg753gh89jk68091385fde957f0c86a5ba"

number = input("Enter phone number with country code:")
check_number = phonenumbers.parse(number)
number_location = "en")
print(number_location)
from phonenumbers import carrier 
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
 import phoneAPIKEY
query = str(number_location)
results = (query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

map_location = google.Map(location = [lat,lng], zoom_start=9)
google.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")
