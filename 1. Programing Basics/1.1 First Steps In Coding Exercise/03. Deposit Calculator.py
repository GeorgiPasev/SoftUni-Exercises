# input float deposisted sum
# input int period in months
# input float yearly per cent
#сума = депозирана сума  + срок на депозита * 
# ((депозирана сума * годишен лихвен процент ) / 12)
# print sum at the end of period

deposit = float(input())
months_period = int(input())
yearly_percent = float(input())
monthly_interest = deposit * yearly_percent / 100 / 12
sum = deposit + months_period * monthly_interest
print(sum)