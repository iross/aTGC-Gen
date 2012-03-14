#!/bin/bash
if [ $# -lt 2 ]; then
	echo "Not enough arguments: try dumbScript.sh (F4_Z) (F5_Z)"
	exit
fi
voms-proxy-init --voms=cms --valid=48:00
cp Run.dat_template Run.dat
sed 's/#F4Z/'$1'/' -i Run.dat
sed 's/#F5Z/'$2'/' -i Run.dat
f4z=${1/./p}
f5z=${2/./p}
f4z=${f4z/-/n}
f5z=${f5z/-/n}
tar -czf sherpa\_$f4z\_$f5z\_cards.tgz Run.dat
cp submitTemplate.sh submit_$f4z\_$f5z.sh
sed 's/#F4Z/'$f4z'/' -i submit_$f4z\_$f5z.sh
sed 's/#F5Z/'$f5z'/' -i submit_$f4z\_$f5z.sh
rm Run.dat
farmoutAnalysisJobs --quick-test --express-queue --input-dir=$PWD --fwklite --output-dir=. --match-input-files="submit_$f4z\_$f5z.sh" sherpa_ZZ_$f4z\_$f5z\_uPow2 $CMSSW_BASE $PWD/submit_$f4z\_$f5z.sh
