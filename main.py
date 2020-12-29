# Imports all necessary modules
from multiprocessing import Pool
import multiprocessing
from os import path
import os
import json
import time

# Put file name of your combos here
comboFileName = 'combos.txt' # For example: 'combos.txt'

# |      |
# | CODE |
# v      v

# Loading domains dictionairy containing preset domain names (to exclude countries simply comment them out)
domains = json.load(open('./domains.json', 'r', encoding='utf-8'))
# Loading combolist (by making a set you get rid of any duplicates)
comboList = set(open('./' + comboFileName, 'r', encoding='utf-8').read().splitlines())

# Make sure combos folder exists
if not path.exists(os.path.dirname(__file__) + '\\combos'):
    os.mkdir(os.path.dirname(__file__) + '\\combos')

# Sorting all combos by comparing each combo to every domain in the domains dictionairy, then writes them into their respective txt files
def sortCombos(combo):
    for domain in domains:
        if domain in combo.lower():
            with open("./combos/" + domains[domain] + "_COMBOS" + ".txt", 'a', encoding='utf-8') as file:
                file.write(combo + '\n')

# Runs main function with multiprocessing (+ shows how long it took)
if __name__ == '__main__':
    start = time.time()
    pool = Pool()
    pool.map(sortCombos, comboList)
    print('\nAll combos are sorted!\n')
    print(f'Time taken:\t{round(time.time() - start, 2)} seconds')
