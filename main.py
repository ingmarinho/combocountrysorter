from multiprocessing import Pool
import multiprocessing
import json
import time

countries = json.load(open('./countries.json', 'r', encoding='utf-8'))
combolist = set(open('./combos.txt', 'r', encoding='utf-8').read().splitlines())                            # By making it a set you automatically get rid of any duplicates

def sortCombos(combo):
    for domain in countries:
        if domain in combo.lower():
            with open("./combos/" + countries[domain] + "_COMBOS" + ".txt", 'a', encoding='utf-8') as file:
                file.write(combo + '\n')

if __name__ == '__main__':
    start = time.time()
    pool = Pool()
    pool.map(sortCombos, combolist)
    print('\nAll combos are sorted!\n')
    print(f'Time taken:\t{round(time.time() - start, 2)} seconds')
