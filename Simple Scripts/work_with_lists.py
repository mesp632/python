empty_list = []
elements = ["Iron", "Helium", "Oxygen", "Gold"]
empty_list_function = list()
print("convert string to list:",list("test"))
animal_tuple = ("cat", "dog", "bird")
print("convert tuple to list:", list(animal_tuple))
Date = "01/09/2024"
print(Date.split("/"))
print(elements[1], elements[-1])
list_of_lists = [elements,list(animal_tuple)]
print(list_of_lists)
print(list_of_lists[1][2]) #first offset is for first list second offset is for embedded list
print(elements[0:2])
elements.append("Hydrogen")
print(elements)
other_elements = ["Calcium", "Carbon"]
elements.extend(other_elements)
print(elements)
more_elements = ["Sodium", "Chlorine"]
elements += more_elements
print(elements)
append_elements = ["uranium", "plutonium"]
elements.append(append_elements)
print(elements)
elements.insert(4,"Lithium")
print(elements)
del elements[10]
print(elements)
del elements[3]
print(elements)
elements.remove("Lithium")
print(elements)
first_element = elements.pop(0)
print("removed:", first_element, elements)
last_element = elements.pop(-1)
print("removed:",last_element, elements)
print("Oxygen" in elements, elements.count("Oxygen"), elements.count("Plutonium"))
print(",".join(elements))