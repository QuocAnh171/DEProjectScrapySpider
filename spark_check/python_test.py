import copy

dict_data = dict()
dict_data["main_number"] = "00"
dict_data["number_00"] = 0
for i in range(0,100):
    if i in range(0,10):
        dict_data["number_0" + str(i)] = 0
    else:
        dict_data["number_" + str(i)] = 0

list_data_xs = list()
list_data_xs.append(dict_data)
for i in range(1,100):
    dict_copy = copy.deepcopy(dict_data)  
    if i in range(0,10):
        dict_copy["main_number"] = "0" + str(i)
    else:
        dict_copy["main_number"] = str(i)
    list_data_xs.append(dict_copy)
    
for i in list_data_xs:
    print(i['main_number'])

print(list_data_xs[3])