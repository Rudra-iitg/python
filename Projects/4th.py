# **************************Dictionary**************************

bio = {
    "name" : "Rudra",
    "age" : 22,
    "marks" : [99.23, 100.0, 98.0, 97.0],
    "subjects" : ["Maths", "Physics", "Chemistry", "English"],
    "is_passed" : True
    }
print(bio) 
print (type(bio)) # <class 'dict'>
print(bio["age"])
# ***********************We can change the data of a dictionary***********************
bio["name"] = "Rudra Pratap Singh"
print(bio["name"])

# ***********************Nested Dictionary************************

data = {
    "fields" : {
        "DSA" : 100,
        "Algo" : 100,
        "DBMS" : 100,
        "OS" : 100
        },
    }
print(data["fields"]["DSA"])

# ***********************Dictionary Methods************************

print(bio.keys()) # dict_keys(['name', 'age', 'marks', 'subjects', 'is_passed'])
print(bio.values()) # dict_values(['Rudra Pratap Singh', 22, [99.23, 100.0, 98.0, 97.0], ['Maths', 'Physics', 'Chemistry', 'English'], True])
print(bio.items()) # dict_items([('name', 'Rudra Pratap Singh'), ('age', 22), ('marks', [99.23, 100.0, 98.0, 97.0]), ('subjects', ['Maths', 'Physics', 'Chemistry', 'English']), ('is_passed', True)])
print(bio.get("name")) # Rudra Pratap Singh

Food = {
    "veg" : {
        "Spices" : "Chillies",
        "Grains" : "Rice",
        "Vegetables" : "Potato"
        },
    "non-veg" : {
        "Spices" : {
            "sweet" : "Cinnamon",
            "sour" : "Lemon",
            "bitter" : {
                "strong" : "Neem",
                "mild" : {
                    "leafy" : "Spinach",
                    "non-leafy" : "Bitter Gourd"
                                }
            }
        },
        "Meat" : {"Chicken",
                  "Mutton",
                  "Fish"},
        "Fish" : "Salmon"
        }
    }
print(Food["non-veg"]["Fish"]) # Salmon
print(Food.keys()) # dict_keys(['veg', 'non-veg'])
print(Food.get("non-veg")["Spices"]) #Pepper
print(Food.get("non-veg")["Spices"]["sour"])
print(Food.get("non-veg")["Spices"]["bitter"]["mild"]["non-leafy"]) # Bitter Gourd

