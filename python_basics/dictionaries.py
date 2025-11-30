# Dictionaries store data in key-value pairs

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"]) # November
print(monthConversions.get("Abp")) # None
print(monthConversions.get("Abp" ,"Not a valid key")) # Not a valid key

# Add new key-value pair
monthConversions["Mon"] = "Monday"
print(monthConversions)

# Update value
monthConversions["Jan"] = "JANUARY"
print(monthConversions)

# Check if key exists
print("Feb" in monthConversions)   # True

# Remove a key
monthConversions.pop("Mon")
print(monthConversions)

# Loop through dictionary
for key in monthConversions:
    print(key, ":", monthConversions[key])