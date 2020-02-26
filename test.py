import os
your_data = {"Purchase Amount": 'TotalAmount'}
print('Current Dir:'+os.getcwd())
files = os.listdir(os.getcwd())
print('-----')
print(*files, sep = "\n") 
print('-----')
print(your_data,  file=open('/my-vol2/log.txt', 'w'))
print('Done!')