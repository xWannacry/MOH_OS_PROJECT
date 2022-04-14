from random import randint
import numpy as np

dummydata = [{'tid': '', 'name': 'Amal', 'doi': 2, 'estime': 18, 'type': 1, 'status': '', 'resources': [4, 3, 10]},
             {'tid': '', 'name': 'Amani', 'doi': 7, 'estime': 16, 'type': 1, 'status': '', 'resources': [1, 1, 5]},
             {'tid': '', 'name': 'Amira', 'doi': 6, 'estime': 20, 'type': 0, 'status': '', 'review': 'c'},
             {'tid': '', 'name': 'Arwa', 'doi': 3, 'estime': 12, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Aya', 'doi': 7, 'estime': 18, 'type': 1, 'status': '', 'resources': [7, 7, 6]},
             {'tid': '', 'name': 'Abbas', 'doi': 3, 'estime': 17, 'type': 1, 'status': '', 'resources': [8, 7, 5]},
             {'tid': '', 'name': 'Abdul', 'doi': 1, 'estime': 14, 'type': 1, 'status': '', 'resources': [3, 0, 2]},
             {'tid': '', 'name': 'Abid', 'doi': 9, 'estime': 13, 'type': 1, 'status': '', 'resources': [3, 0, 5]},
             {'tid': '', 'name': 'Adil', 'doi': 3, 'estime': 17, 'type': 0, 'status': '', 'review': 'd'},
             {'tid': '', 'name': 'Adam', 'doi': 6, 'estime': 15, 'type': 1, 'status': '', 'resources': [7, 1, 10]},
             {'tid': '', 'name': 'Adib', 'doi': 6, 'estime': 13, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Adnan', 'doi': 5, 'estime': 13, 'type': 1, 'status': '', 'resources': [4, 3, 11]},
             {'tid': '', 'name': 'Afif', 'doi': 6, 'estime': 18, 'type': 0, 'status': '', 'review': 'd'},
             {'tid': '', 'name': 'Ahsan', 'doi': 3, 'estime': 11, 'type': 0, 'status': '', 'review': 'd'},
             {'tid': '', 'name': 'Ajmal', 'doi': 7, 'estime': 15, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Aladdin', 'doi': 5, 'estime': 14, 'type': 1, 'status': '', 'resources': [10, 5, 6]},
             {'tid': '', 'name': 'Basma', 'doi': 8, 'estime': 16, 'type': 0, 'status': '', 'review': 'c'},
             {'tid': '', 'name': 'Bayan', 'doi': 5, 'estime': 19, 'type': 0, 'status': '', 'review': 'd'},
             {'tid': '', 'name': 'Bushra', 'doi': 5, 'estime': 12, 'type': 0, 'status': '', 'review': 'c'},
             {'tid': '', 'name': 'Dalal', 'doi': 7, 'estime': 18, 'type': 1, 'status': '', 'resources': [3, 1, 5]},
             {'tid': '', 'name': 'Dalia', 'doi': 2, 'estime': 15, 'type': 0, 'status': '', 'review': 'd'},
             {'tid': '', 'name': 'Dalila', 'doi': 4, 'estime': 20, 'type': 1, 'status': '', 'resources': [5, 4, 11]},
             {'tid': '', 'name': 'Dana', 'doi': 9, 'estime': 10, 'type': 1, 'status': '', 'resources': [4, 7, 0]},
             {'tid': '', 'name': 'Tala', 'doi': 8, 'estime': 13, 'type': 1, 'status': '', 'resources': [8, 2, 7]},
             {'tid': '', 'name': 'Tamara', 'doi': 6, 'estime': 15, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Tara', 'doi': 8, 'estime': 19, 'type': 1, 'status': '', 'resources': [4, 3, 10]},
             {'tid': '', 'name': 'Tamanna', 'doi': 3, 'estime': 17, 'type': 0, 'status': '', 'review': 'c'},
             {'tid': '', 'name': 'Tasnim', 'doi': 6, 'estime': 20, 'type': 1, 'status': '', 'resources': [4, 5, 6]},
             {'tid': '', 'name': 'Umm Kulthoum', 'doi': 2, 'estime': 15, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Wafaa', 'doi': 2, 'estime': 10, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Yara', 'doi': 1, 'estime': 14, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Yasmin', 'doi': 6, 'estime': 16, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Yumna', 'doi': 0, 'estime': 15, 'type': 0, 'status': '', 'review': 'd'},
             {'tid': '', 'name': 'Yusra', 'doi': 1, 'estime': 19, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Zayn', 'doi': 6, 'estime': 19, 'type': 1, 'status': '', 'resources': [8, 0, 7]},
             {'tid': '', 'name': 'Zaynab', 'doi': 5, 'estime': 20, 'type': 0, 'status': '', 'review': 'c'},
             {'tid': '', 'name': 'Hatem', 'doi': 4, 'estime': 20, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Haydar', 'doi': 3, 'estime': 18, 'type': 1, 'status': '', 'resources': [2, 2, 1]},
             {'tid': '', 'name': 'Hazem', 'doi': 6, 'estime': 16, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Hisham', 'doi': 4, 'estime': 11, 'type': 1, 'status': '', 'resources': [8, 2, 5]},
             {'tid': '', 'name': 'Hussein', 'doi': 3, 'estime': 16, 'type': 1, 'status': '', 'resources': [0, 6, 7]},
             {'tid': '', 'name': 'Abu Hurayrah', 'doi': 6, 'estime': 13, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Ibrahim', 'doi': 7, 'estime': 14, 'type': 0, 'status': '', 'review': 'd'},
             {'tid': '', 'name': 'Idrees', 'doi': 0, 'estime': 13, 'type': 1, 'status': '', 'resources': [3, 5, 3]},
             {'tid': '', 'name': 'Iqbal', 'doi': 9, 'estime': 15, 'type': 1, 'status': '', 'resources': [9, 1, 6]},
             {'tid': '', 'name': 'Iyad', 'doi': 5, 'estime': 10, 'type': 0, 'status': '', 'review': 'o'},
             {'tid': '', 'name': 'Jafar', 'doi': 1, 'estime': 20, 'type': 1, 'status': '', 'resources': [10, 6, 2]},
             {'tid': '', 'name': 'Jalal', 'doi': 0, 'estime': 14, 'type': 0, 'status': '', 'review': 'd'},
             {'tid': '', 'name': 'Jaleel', 'doi': 5, 'estime': 19, 'type': 1, 'status': '', 'resources': [9, 0, 0]},
             {'tid': '', 'name': 'Jawad', 'doi': 2, 'estime': 18, 'type': 1, 'status': '', 'resources': [2, 3, 4]}]


def getData():
    names = ['Amal', 'Amani', 'Amira', 'Arwa', 'Aya', 'Abbas', 'Abdul', 'Abid', 'Adil', 'Adam', 'Adib', 'Adnan', 'Afif',
             'Ahsan', 'Ajmal', 'Aladdin', 'Basma', 'Bayan', 'Bushra', 'Dalal', 'Dalia', 'Dalila', 'Dana', 'Tala',
             'Tamara', 'Tara', 'Tamanna', 'Tasnim', 'Umm Kulthoum', 'Wafaa', 'Yara', 'Yasmin', 'Yumna', 'Yusra', 'Zayn',
             'Zaynab', 'Hatem', 'Haydar', 'Hazem', 'Hisham', 'Hussein', 'Abu Hurayrah', 'Ibrahim', 'Idrees', 'Iqbal',
             'Iyad', 'Jafar', 'Jalal', 'Jaleel', 'Jawad']
    data = [[], [[], [], []], [0, 0, 0]]
    for i in range(50):
        ap = {}
        typep = randint(0, 1)
        extime = randint(10, 20)
        DOI = randint(0, 9)
        ap["tid"] = ""
        ap["name"] = names[i]
        ap["doi"] = DOI
        ap["estime"] = extime
        ap["type"] = typep
        ap["status"] = ""
        if typep == 0:
            li = ["o", "c", "d"]
            tt = li[randint(0, 2)]
            ap["review"] = tt
        else:
            meNU = randint(0, 10)
            stD = randint(0, 7)
            inj = randint(0, 11)
            ap["resources"] = [meNU, stD, inj]
            ap["allocated"] = [0, 0, 0]
        data[0].append(ap)
    for x in data[0]:
        if x['type'] == 1:
            for p, y in enumerate(x['resources']):
                data[1][p].append(y)
    op = 0
    for m in data[1]:
        rsum = 0
        for n in m:
            rsum += n
        data[2][op] = abs(round(rsum / len(m)))
        op += 1
    return data
