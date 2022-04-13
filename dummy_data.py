from random import randint


def getData():
    names = ['Amal', 'Amani', 'Amira', 'Arwa', 'Aya', 'Abbas', 'Abdul', 'Abid', 'Adil', 'Adam', 'Adib', 'Adnan', 'Afif',
             'Ahsan', 'Ajmal', 'Aladdin', 'Basma', 'Bayan', 'Bushra', 'Dalal', 'Dalia', 'Dalila', 'Dana', 'Tala',
             'Tamara', 'Tara', 'Tamanna', 'Tasnim', 'Umm Kulthoum', 'Wafaa', 'Yara', 'Yasmin', 'Yumna', 'Yusra', 'Zayn',
             'Zaynab', 'Hatem', 'Haydar', 'Hazem', 'Hisham', 'Hussein', 'Abu Hurayrah', 'Ibrahim', 'Idrees', 'Iqbal',
             'Iyad', 'Jafar', 'Jalal', 'Jaleel', 'Jawad']
    data = []
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
        data.append(ap)
    return data
