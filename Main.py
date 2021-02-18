#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 搭建flask框架收到number然后开始开始跑并写到对应指标
from flask import Flask,request
from concurrent.futures import ThreadPoolExecutor
import subprocess
import os
import time
app = Flask("bench")
pid = 37347
# 需要用root来执行这个,不然需要一直sudo
RandPerfDir = "/home/wcx/MyBin/ForCephBench/Mix2Data/Rand/Perf/"
RandTopDir = "/home/wcx/MyBin/ForCephBench/Mix2Data/Rand/Top/"
WritePerfDir = "/home/wcx/MyBin/ForCephBench/Mix2Data/Write/Perf/"
WriteTopDir = "/home/wcx/MyBin/ForCephBench/Mix2Data/Write/Top/"
executor = ThreadPoolExecutor(3)

def runRand(num):
    time.sleep(10)
    # 1.top运行40s    关于设定时间
    # top -b -p 17434|grep  --line-buffered -i  "17434"  >> top.txt&
    ## 1.1 perf写到数据文件中
    ## /home/wcx/MyBin/ForCephBench/Data/Write 
    os.system(' top -d 2 -n 20  -b -p 38600|grep  --line-buffered -i  "38600"  >> %s.txt&'%(RandTopDir+str(num)) )
    # 2.perf运行20s
    ## 2.1 perf写到数据文件中
    ## /home/wcx/MyBin/ForCephBench/Data/Rand
    os.system("sudo perf stat -e cache-misses,instructions,cycles,LLC-load-misses --time 20000  -p  38600 1>>%s.txt 2>>%s.txt"%(RandPerfDir+str(num), RandPerfDir+str(num)  ))
    os.system("sudo perf stat -e cache-misses,instructions,cycles,LLC-load-misses --time 20000  -p  38600 1>>%s.txt 2>>%s.txt"%(RandPerfDir+str(num), RandPerfDir+str(num)  ))
    

def runWrite(num):
    time.sleep(10)
    # 1.top运行40s    关于设定时间
    # top -b -p 18005|grep  --line-buffered -i  "17434"  >> top.txt&
    ## 1.1 perf写到数据文件中
    ## /home/wcx/MyBin/ForCephBench/Data/Write 
    os.system(' top -d 2 -n 20  -b -p 38600|grep  --line-buffered -i  "38600"  >> %s.txt&'%(WriteTopDir+str(num)) )
    # 2.perf运行20s
    ## 2.1 perf写到数据文件中
    ## /home/wcx/MyBin/ForCephBench/Data/Rand
    os.system("sudo perf stat -e cache-misses,instructions,cycles,LLC-load-misses --time 20000  -p  38600 1>>%s.txt 2>>%s.txt"%(WritePerfDir+str(num), WritePerfDir+str(num)  ))
    os.system("sudo perf stat -e cache-misses,instructions,cycles,LLC-load-misses --time 20000  -p  38600 1>>%s.txt 2>>%s.txt"%(WritePerfDir+str(num), WritePerfDir+str(num)  ))
    

# curl 10.118.0.224:5000?type=1\&num=1   1是随机读 2是写
@app.route("/")
def getRandNum():
    type = request.args.get("type")
    num = request.args.get("num")
    print(type)
    print(num)
    if type == "1":
        print("here")
        executor.submit(runRand, num)
        # runRand(num)
    else:
        print("there")
        executor.submit(runWrite, num)
        # runWrite(num)
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0")