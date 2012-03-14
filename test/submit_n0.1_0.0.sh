cp $CMSSW_BASE/src/ZZ/Gen/test/sherpa_n0.1_0.0_cards.tgz .
bash $CMSSW_BASE/src/ZZ/Gen/test/MakeSherpaLibs.sh -i $PWD -p n0.1_0.0 -d /cvmfs/cms.hep.wisc.edu/osg/app/cmssoft/cms/slc5_amd64_gcc434/external/sherpa/1.3.0-cms/bin/Sherpa 
mv *.tgz $OUTPUT

