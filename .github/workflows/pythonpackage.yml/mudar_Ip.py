import os
ip = str(list(input('ips com virgula e ponto:')))
os.sytem('ifconfig wlan0 ip')
print('seu ip: ', os.system('ifconfig wlan0'))
