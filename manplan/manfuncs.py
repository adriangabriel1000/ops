from django.utils.timezone import utc
from .models import *
from datetime import datetime, timedelta
import string
import random
import random





# Populate Employee Model with Random Characters  ---------------- Run when required
def pop():
    employee = Employee.objects.all()
    for x in range(1, 30):
        name = ''.join(random.choices(string.ascii_letters, k=random.randint(6, 10)))
        surname = ''.join(random.choices(string.ascii_letters, k=random.randint(7, 15)))
        fullname = name + ' ' + surname
        Employee.objects.create(name=fullname, shift='O')
        print(fullname)
    return employee


# Populate Random Positions on Manplan ---------------- Run when required
def randPos():
    for x in range(1,100):
        rndDt = random.randint(-7, 41)
        rndDay = (datetime.today().date() + timedelta(rndDt)).day
        rndMnth = (datetime.today().date() + timedelta(rndDt)).month
        rndYr = 2024
        rndDate = datetime(rndYr, rndMnth, rndDay, 12, 0, 0)
        posi = ['T1M', 'N1M', '0M', 'SNM', 'T1A', 'N1A', '0A', 'SNA', 'T1N', 'N1N', '0N', 'SNN']
        rndPos = random.choice(posi)
        nms = []
        for a in Employee.objects.all():
            nms.append(a.pk)
        rndNme = random.choice(nms)
        Schedule.objects.create(date=rndDate, position=rndPos, employee_id=rndNme)