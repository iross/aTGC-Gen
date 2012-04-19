#!/bin/bash
echo "--------------------start script here------------------"
echo "pwd"
pwd
echo "ls"
ls
#get tag for numbering
echo "now get the right tag tagging:"
echo "first less report.log"
less report.log
TAG=`less report.log | grep SENDING | cut -f3 -d":" | cut -f1 -d"_"| head -n 1 |tail -n 1`
echo $TAG
CRABFILE=crab_fjr_$TAG.xml
echo "CRABFILE=crab_fjr_$TAG.xml"

echo "tar -xzf sherpa_*_MASTER.tgz"
tar -xzf sherpa_*_MASTER.tgz
echo "ls again to check if the files are correctly unpacked"
ls
echo "Runtime area"
echo $RUNTIME_AREA
echo "cmsRun -j $RUNTIME_AREA/$CRABFILE -p pset.py"
cmsRun -j $RUNTIME_AREA/$CRABFILE -p pset.py
# cmsRun -j crab_fjr.xml pset.py
