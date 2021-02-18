#!/bin/bash
# 1 2 3 4 5传几个起几个
# 起不同的数量一样的负载，符合控制变量原则
# 选择负载类型 bzip2

BenchRootDir=/home/wcx/Downloads/cpu2006v99/
num=${1}
pwd=`pwd`
echo ${pwd}
cd ${BenchRootDir}
source shrc
cd ${pwd}
# echo ${num}
if [ ${num} -ge 1 ];
then        # bash ${BenchRootDir}/bindRunOne.sh 401.bzip2;\
    echo "--------------- Now start to run first bzip2. -----------------"
    for((;;)); do bash ${BenchRootDir}/bindRunOne.sh 401.bzip2; done &
fi
if [ ${num} -ge 2 ];
then 
    echo "--------------- Now start to run second bzip2. -----------------"
    for((;;)); do bash ${BenchRootDir}/bindRunOne.sh 401.bzip2; done &
    # echo 2
fi
if [ ${num} -ge 3 ];
then 
    echo "--------------- Now start to run third bzip2. -----------------"
    for((;;)); do bash ${BenchRootDir}/bindRunOne.sh 401.bzip2; done &
    # echo 3
fi
if [ ${num} -ge 4 ];
then
    echo "--------------- Now start to run fourth bzip2. -----------------"
    for((;;)); do bash ${BenchRootDir}/bindRunOne.sh 401.bzip2; done &
    # echo 4
fi
if [ ${num} -ge 5 ];
then 
    echo "--------------- Now start to run fifth bzip2. -----------------"
    for((;;)); do bash ${BenchRootDir}/bindRunOne.sh 401.bzip2; done &
    # echo 5
fi

