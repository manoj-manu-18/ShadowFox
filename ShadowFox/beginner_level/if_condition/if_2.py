#2. WAP to determine which country a city belongs to Given List of Cities per Countries
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city_name = input("Enter the Name of the City: ")

if city_name in Australia:
    print(f"{city_name} is in Australia")
elif city_name in UAE:
    print(f"{city_name} is in the United Arab Emirates")
elif city_name in India:
    print(f"{city_name} is in India")
else:
    print(f"{city_name} is not in any of the mentioned countries")