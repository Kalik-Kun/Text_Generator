import os
import re
# import time
data_list = []


def clear(): return os.system('cls')


def Tokenization_file(name_file, der):
    os.chdir(der)
    f = open(name_file + '.txt', 'r')
    file = f.read()
    file = file.lower()
    file = re.findall(r'\w+', file)
    print()
    return file


def fit(data, perc):
    for i in range(0, len(data) - 1):
        word = data[i]
        will_word = data[i + 1]
        was = True
        ind = 0
        for elm_id in range(len(data_list)):
                # elm = data_list[elm_id]
            if data_list[elm_id][0] == word:
                was = False
                ind = elm_id
                break

        if was:
            data_list.append([])
            data_list[len(data_list) - 1].append('')
            data_list[len(data_list) - 1].append([])
            data_list[len(data_list) - 1].append([])
            data_list[len(data_list) - 1][0] = word
            ind = len(data_list) - 1

        if data_list[ind][1].count(will_word) == 0:
            data_list[ind][1].append(will_word)
            data_list[ind][2].append(1.0)
        else:
            id2 = data_list[ind][1].index(will_word)
            data_list[ind][2][id2] += 1.0
    for par in data_list:
        Sum = 0.0
        for quan in par[2]:
            Sum += quan
        for i in range(len(par[2])):
            par[2][i] = par[2][i] / Sum
    print('\n')
    print('____________LEARNING COMPLETED_____________')
    return data_list
