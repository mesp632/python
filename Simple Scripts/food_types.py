#will specify the type for one of the listed 
#fruits based on the value in the variable "food"
foodtypes={
    "apple" : "fruit",
    "potato" : "vegetable",
    "bread" : "grain",
    "yogurt" : "dairy",
    "steak" : "meat",
    "cake" : "dessert",
           }
food = "apple"
print(food, "is a", foodtypes[food])