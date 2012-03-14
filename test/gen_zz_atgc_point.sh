#!/bin/bash

function usage
{
    echo "gen_point.sh --coupling Z/G --f4 value --f5 value"
}

f4=
f5=
couplType=
dryrun=false
postfix=""
while [ "$1" != "" ]; do
    case $1 in
        --f4 )           
	    shift
	    f4=$1
	    ;;
        --f5 )    
	    shift
	    f5=$1
	    ;;
	--coupling )
	    shift
	    couplType=$1
	    ;;
	--dryrun )
	    dryrun=true
	    ;;
	--postfix )
		shift
		echo $1
		postfix=_$1
		;;
        -h | --help )           
	    usage
	    exit
	    ;;
        * ) 
	    usage
	    exit 1
    esac
    shift
done
if [[ $couplType !=  "Z" && $couplType != "G" ]] ; then
echo "Invalid coupling type: " $couplType
exit
fi

if [ "$postfix" == "_" ] ; then
	postfix=""
fi
#specilize template
cp Run.dat_template Run.dat
if [[ $couplType == "Z" ]] ; then
    sed 's/#F4Z/'$f4'/' -i Run.dat
    sed 's/#F5Z/'$f5'/' -i Run.dat
    sed 's/#F4G/0.0/' -i Run.dat
    sed 's/#F5G/0.0/' -i Run.dat
elif [[ $couplType == "G" ]] ; then
    sed 's/#F4Z/0.0/' -i Run.dat
    sed 's/#F5Z/0.0/' -i Run.dat
    sed 's/#F4G/'$f4'/' -i Run.dat
    sed 's/#F5G/'$f5'/' -i Run.dat
fi

f4=${f4/./p}
f5=${f5/./p}
f4=${f4/-/m}
f5=${f5/-/m}

tar -czf sherpa\_f$couplType\_$f4\_$f5$postfix\_cards.tgz Run.dat
cp submitTemplate.sh submit\_$couplType\_$f4\_$f5$postfix.sh
#COUP_#F4_#F5
sed 's/#COUP/'$couplType'/' -i submit\_$couplType\_$f4\_$f5$postfix.sh
sed 's/#F4/'$f4'/' -i submit\_$couplType\_$f4\_$f5$postfix.sh
sed 's/#F5/'$f5'/' -i submit\_$couplType\_$f4\_$f5$postfix.sh
sed 's/#POSTFIX/'$postfix'/' -i submit\_$couplType\_$f4\_$f5$postfix.sh 
rm Run.dat

#have dryrun mode for testing
if ! $dryrun ; then
farmoutAnalysisJobs --quick-test --express-queue --input-dir=$PWD --fwklite \
    --output-dir=. --job-count=1 \
    --extra-inputs=$PWD/sherpa_f${couplType}_${f4}_${f5}$postfix\_cards.tgz,$PWD/MakeSherpaLibs.sh \
    sherpa_ZZ\_$couplType\_$f4\_$f5$postfix $CMSSW_BASE $PWD/submit\_$couplType\_$f4\_$f5$postfix.sh
else 
echo farmoutAnalysisJobs --quick-test --express-queue --input-dir=$PWD --fwklite \
    --output-dir=. --job-count=1 \
    --extra-inputs=$PWD/sherpa_f${couplType}_${f4}_${f5}$postfix\_cards.tgz,$PWD/MakeSherpaLibs.sh \
    sherpa_ZZ\_$couplType\_$f4\_$f5$postfix $CMSSW_BASE $PWD/submit\_$couplType\_$f4\_$f5$postfix.sh
fi
