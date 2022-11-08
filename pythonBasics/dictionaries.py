
hotel_records = {101 : "John", 304 : "Paul", 403 : "Mia"}

print(hotel_records)

print(hotel_records[304])

print(hotel_records[403])

#print(hotel_records.get(109)) # Return null if object not available

    # While using the get method, we do not get an error when
# the key is missing from the Python dictionary, but direct access does

hotel_records[505] = 'Russell'

print(hotel_records)

d = {1: 'Jimmy', 2: 'Alex', 3: 'john', 4: 'mike'}

# Printing dictionary
print(d)

# Accesing value using keys
print("1st name is " + d[1])
print("2nd name is " + d[4])

print(d.keys())
print(d.values())

