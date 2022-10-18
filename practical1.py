from ast import pattern
import random
words = ['tree','sun','ball','moonbbb','earthbbb','grassbbb','worldbbb','present','chipbbb','room','talk','route','hen','low','mars'] 

incorrect_pattern = ["|","|","|","|","o","-","|","-","/","\ "]

losed_que = []
count = 0
print("Enter Missing Value: ")
while count < 10:
    word = random.choice(words)
    underlined_word = word
    for j in range(len(word)//3):
        underlined_word = underlined_word.replace(underlined_word[random.randint(0,len(word)-1)],"_",1)
        # underlined_word = temp_underline_var2
    missing_char = input(f"{underlined_word} = ")
    if len(missing_char) == len(word)//3:
        for k in range(len(word)//3):
            current_word = underlined_word.replace("_",missing_char[k],1)
        if current_word != word:
            # print(" ",incorrect_pattern[count])
            losed_que.append(incorrect_pattern[count])
            count += 1
        # print(current_word)
    else:
        # print(" ",incorrect_pattern[count])
        losed_que.append(incorrect_pattern[count])
        count += 1

print("|----",end="")
for i in range(len(losed_que)):
    if i >= 5 and i <= 7:
        print(losed_que[i],end="")
    elif i == 8 or i == 9:
        if i == 8:
            print("\n|    ",end="")
        print(losed_que[i],end="")
    else:
        if i == 4:
            print(losed_que[i],end="\n|   ")
        else:
            print(losed_que[i])
            print("|",end="    ")
if i == 9:
    print("\n_______")


# |----|
# |	 |
# |	 |
# |    |
# |	 O
# |   -|-
# |	 /\
# |_________