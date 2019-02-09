import file
import random
import time
import os


def clear(): return os.system('cls')


clear()
der = 'data'
name = 'town'

#print("please write name file and derective")
#name = str(input())
#der = str(input())

random.seed()

f = open('GENout.txt', 'w')

data = file.Tokenization_file(name, der)
clean_data = file.fit(data, 0.0)

print(' \n How long text you want see my king?')
size = len(clean_data)
LEN = int(input())
word = "башня"
for time in range(LEN):
    print(word, end=' ')
    f.write(word + ' ')
    if time % 18 == 0:
        print('\n', end='')
        f.write('\n')

    index_key = random.randint(0, size - 1)
    for i in range(size):
        if clean_data[i][0] == word:
            index_key = i
            break
    perc = 0.0
    index_val = -1
    rand = random.random()
    for i in range(len(clean_data[index_key][2])):
        if rand >= perc and rand <= perc + clean_data[index_key][2][i]:
            index_val = i
            break
        perc += clean_data[index_key][2][i]
    if index_val == -1:
        index_val = random.randint(0, size - 1)
        word = clean_data[index_val][0]
    else:
        word = clean_data[index_key][1][index_val]
print('\n', end='')
print("my txt")
f.close()
goto = bool(input())
