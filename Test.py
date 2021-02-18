import os
import time
from concurrent.futures import ThreadPoolExecutor
RandPerfDir = "/home/wcx/MyBin/ForCephBench/Data/Rand/Perf/"
RandTopDir = "/home/wcx/MyBin/ForCephBench/Data/Rand/Top/"
WritePerfDir = "/home/wcx/MyBin/ForCephBench/Data/Write/Perf/"
WriteTopDir = "/home/wcx/MyBin/ForCephBench/Data/Write/Top/"
# os.system('''sudo perf stat -e cache-misses,instructions,cycles,LLC-load-misses --time 20000  -p  17434 1>>perfdata.txt 2>>perfdata.txt''')
num = 1
# os.system(' top -d 2 -n 20  -b -p 17434|grep  --line-buffered -i  "17434"  >> %s.txt&'%(RandTopDir+str(num)) )
os.system("sudo perf stat -e cache-misses,instructions,cycles,LLC-load-misses --time 20000  -p  17434 1>>%s.txt 2>>%s.txt"%(WritePerfDir+str(num), WritePerfDir+str(num)  ))
os.system("sudo perf stat -e cache-misses,instructions,cycles,LLC-load-misses --time 20000  -p  17434 1>>%s.txt 2>>%s.txt"%(WritePerfDir+str(num), WritePerfDir+str(num)  ))
executor = ThreadPoolExecutor(2)
def run(num):
    time.sleep(3)
    print(1)
executor.submit(run, 1)
print(1)
time.sleep(10)
