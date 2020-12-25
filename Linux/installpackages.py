import time
import os
try:
    os.system("apt install python3-pip")
except:
    pass
os.system("pip3 install -r requirements.txt")
time.sleep(1)
