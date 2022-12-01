car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}


keys = ["series","P Or D" , "Tire" , "Body"]

values = [123 , "petrol", "Tubeless", "Metallic"]

def cars(keys,values):
    for i , j in zip(keys,values):
        print(f'{i}:{j}')

        ret = car[i] = j
    return ret
cars(keys,values)

# def nest(keys,values):
#     for i in keys:
#         for j in values:
#             ret = car[i] = j

#         return ret
# nest(keys,values)

print(car)

# //how to iterate two list at same time in python?

# for lat, long in zip(Latitudes, Longitudes):
#     print(lat, long)








