#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 11
# Problem 1
# 204113 Sec 02A

import math

def readfile(fname):
    with open(fname, "rt") as f:
        data = f.read()
    data = data.split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(",")
    return data

def information_gain(aspect,suscess_rate,p_all):
    choice = set(aspect) # เพื่อไม่ให้ซ้ำ
    ent = []
    count = []
    for name in choice:
        e,c = entropy(name,aspect,suscess_rate)
        ent.append(e)
        count.append(c)

    gain = 0
    total = len(aspect)
    for i in range(len(choice)):
        gain += ((count[i] / total) * ent[i])

    return p_all-gain

def entropy(name,aspect,suscess_rate):
    c = 0 # จน. name ที่มีอยู่ใน aspect
    suscess = 0
    not_suscess = 0
    for i in range(len(aspect)):
        if aspect[i] == name:
            c = c + 1
            if suscess_rate[i] == "true":
                suscess = suscess + 1
            else:
                not_suscess = not_suscess + 1

    p1 = (suscess / c) # ความน่าจะดป็นที่จะเจอ suscess ใน c (ทั้งหมด)
    p2 = (not_suscess / c)
    if p1 != 0 and p2 != 0:
        ent = -(p1) * math.log(p1,2) - (p2) * math.log(p2,2)
    elif p1 != 0:
        ent = -p1 * math.log(p1,2)
    elif p2 != 0:
        ent = -p2 * math.log(p2,2)
    else:
        ent = 0

    return(ent,c)

def factor_list(first_factor, next_factor_USA, next_factor_Europe):
    print("First factor is %s"%first_factor)
    print("The next factor of USA is %s"%next_factor_USA)
    print("The next factor of Europe is %s"%next_factor_Europe)

def main():
    filename = "input.txt"
    data = readfile(filename)
    id, country, big_star, genre, suscess = zip(*data)
    gain_country = information_gain(country, list(suscess), 1)
    gain_big = information_gain(list(big_star), list(suscess), 1)
    gain_genre = information_gain(list(genre), list(suscess), 1)

    max_ = max(gain_country, gain_big, gain_genre)
    list_of_gain = {gain_country:"Country of origin", gain_big:"Big star", gain_genre:"Genre"}

    big_star_USA = []
    genre_USA = []
    suscess_USA = []
    for i in range(len(country)):
        if country[i] == "USA":
            big_star_USA.append(big_star[i])
            genre_USA.append(genre[i])
            suscess_USA.append(suscess[i])
    gain_big_USA = information_gain(list(big_star_USA), list(suscess_USA), entropy("USA", country, suscess)[0])
    gain_genre_USA = information_gain(list(genre_USA), list(suscess_USA), entropy("USA", country, suscess)[0])
    
    max_2 = max(gain_big_USA, gain_genre_USA)
    list_of_gain_next_USA = {gain_big_USA:"Big star", gain_genre_USA:"Genre"}

    big_star_Europe = []
    genre_Europe = []
    suscess_Europe = []
    for i in range(len(country)):
        if country[i] == "Europe":
            big_star_Europe.append(big_star[i])
            genre_Europe.append(genre[i])
            suscess_Europe.append(suscess[i])
    gain_big_Europe = information_gain(list(big_star_Europe), list(suscess_Europe), entropy("Europe", country, suscess)[0])
    gain_genre_Europe = information_gain(list(genre_Europe), list(suscess_Europe), entropy("Europe", country, suscess)[0])
    
    max_3 = max(gain_big_Europe, gain_genre_Europe)
    list_of_gain_next_Europe = {gain_big_Europe:"Big star", gain_genre_Europe:"Genre"}

    factor_list(list_of_gain[max_], list_of_gain_next_USA[max_2], list_of_gain_next_Europe[max_3])

if __name__ == '__main__':
    main()
