"""
  Project: Search System by set and dictionary
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Mar. 29, 2021
"""

# define count value and list
num = 0
L_nation_capital = []

#start loop
while True:
    # get input data while count is lower than 10
    if num < 10:
        #input data
        raw_str = input("Input nation and its capital (. to quit) : ")
        # quit check
        if(raw_str == "."):
            break
        # append raw data to list
        L_temp = raw_str.split(sep=' ')
        L_nation_capital.append(L_temp)

        num += 1

    elif num ==10:
        # list to dictionary
        dict_nation_capital = dict(L_nation_capital)
        # print list
        print("dict_nation_capital : {}".format(dict_nation_capital))
        num += 1

    else:
        # start search function
        nation = input("Input nation to find its capital(. to quit) : ")
        # quit check
        if(nation == "."):
            break
        # print valid nation and capital
        print("The capital of {} is {}".format(nation, dict_nation_capital[nation]))
        
