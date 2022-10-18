random_puzzle = [
    ["$", "#", "#", "$", "#"], 
    ["%", "%", "%", "#", "#"], 
    ["$", "$", "%", "$", "%"]
    ]



# random_puzzle = [
#     ["$", "$", "$", "$", "%"], 
#     ["%", "%", "%", "%", "$"], 
#     ["#", "#", "#", "#", "#"]
#     ]

# get unique ele from random_puzzle
unique_eles = []
for i in random_puzzle:
    for j in i:
        if j not in unique_eles:
            unique_eles.append(j)

main_count = 0
temp_k = []
temp_l = []
counter = False
# loop repeat from 0 to length of unique_eles
for i in range(len(unique_eles)):
    #loop repeat from 0 to length of random_puzzle
    for k in range(len(random_puzzle)):
        #loop repeat from 0 to legth of random_puzzle[k] (sublist of random puzzle)
        for l in range(len(random_puzzle[k])):
            #check unique element is equalto current element or not
            if unique_eles[i] != random_puzzle[k][l]:
                # get the index of all element who are not eqaul to unique_element[i]
                temp_k.append(k)
                temp_l.append(l)

            # if current element is equal to unique_element[i] then check it is in right sublist or not(k = i)
            # where i represent correct sublist(i.e index) and k represent current element's sublist(i.e index)
            elif unique_eles[i] == random_puzzle[k][l] and k != i:
                # is temp_l or temp_k are empty or not 
                if temp_l != [] or temp_k != []:
                    # run a for loop on length of temp_k or temp_l (any one)
                    for m in range(len(temp_k)):
                        # check current element is equal to element who is in unique_eles[temp_k[forloop index]]
                        if unique_eles[temp_k[m]] == random_puzzle[k][l]:
                            # if yes then swap it from current element
                            temp_var = random_puzzle[temp_k[m]][temp_l[m]]
                            random_puzzle[temp_k[m]][temp_l[m]] = random_puzzle[k][l]
                            random_puzzle[k][l] = temp_var
                            main_count += 2
                            # counter = True
                            # remove that swaped element index form the temp_k and temp_l
                            temp_k.remove(temp_k[m])
                            temp_l.remove(temp_l[m])
                            break
                
        

print(random_puzzle)
print("Count is ",main_count)






# -----------EXTRA CODE LOGIC--------

# random_puzzle = [
#     ["$", "#", "#", "$", "#"], 
#     ["%", "%", "%", "#", "#"], 
#     ["$", "$", "%", "$", "%"]
#     ]

# unique_ele = {""}
# for i in random_puzzle:
#     for j in i:
#         unique_ele.add(j)
        
# unique_ele.remove("")
# unique_eles = list(unique_ele)
# main_count = 0

# for i in range(len(unique_eles)):
#     count = 0
#     for k in range(len(random_puzzle)):
#         for l in range(len(random_puzzle[k])):
#             if unique_eles[i] == random_puzzle[k][l]:
#                 temp_var = random_puzzle[i][count]
#                 random_puzzle[i][count] = random_puzzle[k][l]
#                 random_puzzle[k][l] = temp_var
#                 count += 1
#                 main_count += 2
#             else:
#                 count += 0
        

# print(random_puzzle)
# print("Count is ",main_count)
