import math

def TimeToInt(time):
    a, b = map(int, time.split(':'))
    return 60 * a + b

class Car:
    def __init__(self):
        self.start = 0
        self.isOut = False
        self.total = 0
        
    def In(self, start):
        self.start = start
        self.isOut = False
        
    def Out(self, end):
        if not self.isOut:
            self.total += end - self.start
            self.isOut = True

def solution(fees, records):
    parking = {}
    
    for record in records:
        t, n, io = record.split()
        
        if io == "IN":
            if n not in parking:
                parking[n] = Car()
                
            parking[n].In(TimeToInt(t))
            
        else:
            parking[n].Out(TimeToInt(t))
            
    answer = []

    for num in sorted(parking.keys()):
        parking[num].Out(1439)
        time = parking[num].total
        
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3])
            
    return answer