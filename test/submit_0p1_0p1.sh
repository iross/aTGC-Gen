cp $CMSSW_BASE/src/ZZ/Gen/test/sherpa_0p1_0p1_cards.tgz .
bash $CMSSW_BASE/src/ZZ/Gen/test/MakeSherpaLibs.sh -i $PWD -p 0p1_0p1 -d /cvmfs/cms.hep.wisc.edu/osg/app/cmssoft/cms/slc5_amd64_gcc434/external/sherpa/1.3.0-cms/bin/Sherpa 
mv *.tgz $OUTPUT

