'''
Author : Nandana Hasheed 
Date : 08-10-2024
python program to find date and time 
'''
from datetime import datetime
current_time=datetime.now()
print(current_time)
format1=current_time.strftime("%Y-%m-%d-%H:%M:%S")
print(format1)
format2=current_time.strftime("%m/%d/%Y")
print(format2)
format3=current_time.strftime("%A,%m,%d%Y")
print(format3)
format4=current_time.strftime("%A,%m,%d%Y %H:%M:%S %p")
print(format4)
format5=current_time.strftime("%A-%b-%d %H:%M:%S %Z IST %Y")
print(format5)
format6=current_time.strftime("%a-%b-%d %H:%M:%S IST %y")
print(format6)
format7=current_time.isoformat()
print(format7)
format8=current_time.strftime("%d")
print(format8)
format9=current_time.strftime("%H:%M:%S")
print(format9)
format10=current_time.strftime("%B")
print(format10)
format10=current_time.strftime("%Y")
print(format10)
