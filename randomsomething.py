import random
import time
def getRandomdate(startDate,endDate):
    print(" printing random date between", startDate,"and", endDate )
    random.Generater = random.random()
    dateFormat = '%m/%d/%Y'
    
    startTime = time.mktime(time.strptime(startDate , dateFormat))
    endTime = time.mktime(time.strptime(endDate , dateFormat))

    randomTime = startTime +  random.Generater * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate


print("Random Date = ", getRandomdate("1/1/2016","12/12/2018"))


