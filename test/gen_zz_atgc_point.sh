#!/bin/bash

function usage
{
    echo "gen_point.sh --coupling Z/G --fz value --fg value"
}

fz=
fg=
couplType=
dryrun=false
postfix=""
while [ "$1" != "" ]; do
    case $1 in
        --fz )           
	    shift
	    fz=$1
	    ;;
        --fg )    
	    shift
	    fg=$1
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
if [[ $couplType !=  "4" && $couplType != "5" ]] ; then
echo "Invalid coupling type: " $couplType
exit
fi

if [ "$postfix" == "_" ] ; then
	postfix=""
fi
#specilize template
#temp
cp Run.dat_template Run.dat
#cp Run.dat_david Run.dat
if [[ $couplType == "4" ]] ; then
    sed 's/#F4Z/'$fz'/' -i Run.dat
    sed 's/#F4G/'$fg'/' -i Run.dat
    sed 's/#F5Z/0.0/' -i Run.dat
    sed 's/#F5G/0.0/' -i Run.dat
elif [[ $couplType == "5" ]] ; then
    sed 's/#F4Z/0.0/' -i Run.dat
    sed 's/#F4G/0.0/' -i Run.dat
    sed 's/#F5Z/'$fz'/' -i Run.dat
    sed 's/#F5G/'$fg'/' -i Run.dat
fi

fz=${fz/./p}
fg=${fg/./p}
fz=${fz/-/m}
fg=${fg/-/m}

tar -czf sherpa\_f$couplType\_$fz\_$fg$postfix\_cards.tgz Run.dat
cp submitTemplate.sh submit\_$couplType\_$fz\_$fg$postfix.sh
#COUP_#F4_#F5
sed 's/#COUP/'$couplType'/' -i submit\_$couplType\_$fz\_$fg$postfix.sh
sed 's/#F4/'$fz'/' -i submit\_$couplType\_$fz\_$fg$postfix.sh
sed 's/#F5/'$fg'/' -i submit\_$couplType\_$fz\_$fg$postfix.sh
sed 's/#POSTFIX/'$postfix'/' -i submit\_$couplType\_$fz\_$fg$postfix.sh 
rm Run.dat

#have dryrun mode for testing
if ! $dryrun ; then
farmoutAnalysisJobs --quick-test --express-queue --input-dir=$PWD --fwklite \
    --output-dir=. --job-count=1 --shared-fs\
	--match-input-files=submit\_$couplType\_$fz\_$fg$postfix.sh \
    --extra-inputs=$PWD/sherpa_f${couplType}_${fz}_${fg}$postfix\_cards.tgz,$PWD/MakeSherpaLibs.sh \
    sherpa_ZZ\_$couplType\_$fz\_$fg$postfix $CMSSW_BASE $PWD/submit\_$couplType\_$fz\_$fg$postfix.sh
else 
echo farmoutAnalysisJobs --quick-test --express-queue --input-dir=$PWD --fwklite \
    --output-dir=. --job-count=1 --shared-fs\
	--match-input-files=submit\_$couplType\_$fz\_$fg$postfix.sh \
    --extra-inputs=$PWD/sherpa_f${couplType}_${fz}_${fg}$postfix\_cards.tgz,$PWD/MakeSherpaLibs.sh \
    sherpa_ZZ\_$couplType\_$fz\_$fg$postfix $CMSSW_BASE $PWD/submit\_$couplType\_$fz\_$fg$postfix.sh
fi
