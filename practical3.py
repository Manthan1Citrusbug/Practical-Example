random_number = [
    [0, 0, 0, 1, 1, 1, 0, 0, 0], 
    [1, 0, 1, 0, 1, 1, 5, 6, 7], 
    [7, 7, 7, 9, 9, 9, 0, 0, 0], 
    [0, 0, 0, 1, 1, 5, 0, 0, 7], 
    [1, 2, 3, 4, 5, 6, 7, 8, 9], 
    [1, 1, 0, 0, 0, 0, 3, 7, 8], 
    [7, 7, 7, 6, 7, 0, 0, 0, 8], 
    [6, 5, 1, 1, 0, 0, 0, 3, 3], 
    [1, 1, 4, 0, 0, 0, 2, 2, 200]]

answered_array = []
answered_sum = 0
count = 0
for i in range(len(random_number)-2):
    for j in range(len(random_number[i])-2):
        temp_array = [
            random_number[i][j],random_number[i][j+1],random_number[i][j+2],
            random_number[i+1][j+1],
            random_number[i+2][j],random_number[i+2][j+1],random_number[i+2][j+2]
        ]
        temp_sum = sum(temp_array)
        count += 1
        if answered_sum < temp_sum:
            answered_sum = temp_sum
            answered_array = temp_array

print(f"""
{answered_array[0]} {answered_array[1]} {answered_array[2]} 
  {answered_array[3]} 
{answered_array[4]} {answered_array[5]} {answered_array[6]}""",end="   =  ")

print(answered_sum)
print(count)