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
joined = ",".join(elements)
print(joined)
print(joined.split(","))
sorted_elements = sorted(elements)
print(sorted_elements)
nums_list = [1,4,2]
print(nums_list)
nums_list.sort()
print(nums_list)
nums_list.sort(reverse=True)
print(nums_list)
test_elements=elements
new_elements_list = elements.copy()
new_elements_list.insert(-1,"Lithium")
print(elements)
print(test_elements)
print(new_elements_list)
empty_tuple = ()
element_tuple = tuple(elements) #tuples cannot be modified after creation
print(element_tuple)
elements.insert(10, "Lithium")
print(elements, "\n",element_tuple)
a, b, c, d, e, f = element_tuple #tuple unpacking
print(b)
password = "test_password"
password_2 = "test_password_2"
password, password_2 = password_2, password #use tuple to exchange values
print(password, password_2)

empty_dict = {}
print(empty_dict)
elements_dict = {
    1:"Hydrogen",
    2:"Helium",
    3:"Lithium",
    4:"Beryllium",
    5:"Boron",
    6:"Carbon"
}
print(elements_dict)

element_list_2 = [[1,"Hydrogen"],
    [2,"Helium"],
    [3,"Lithium"],
    [4,"Beryllium"],
    [5,"Boron"],
    [6,"Carbon"]]

#Convert list to dictionary
print(element_list_2, dict(element_list_2))
elements_dict[7] = "Nitroge" #add element
print(elements_dict)
elements_dict[7] = "Nitrogen" #change 7th element
print(elements_dict)
add_elements = {
    8:"Oxygen",
    9:"Fluorine"
                }
elements_dict.update(add_elements)
print(elements_dict)
del elements_dict[9]
print(elements_dict)
add_elements.clear()
print(add_elements)
print(7 in elements_dict)