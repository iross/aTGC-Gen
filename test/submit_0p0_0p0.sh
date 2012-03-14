cp $CMSSW_BASE/src/ZZ/Gen/test/sherpa_0p0_0p0_cards.tgz .
bash $CMSSW_BASE/src/ZZ/Gen/test/MakeSherpaLibs.sh -i $PWD -p 0p0_0p0 -d /cvmfs/cms.hep.wisc.edu/osg/app/cmssoft/cms/slc5_amd64_gcc434/external/sherpa/1.3.0-cms/bin/Sherpa 
mv *.tgz $OUTPUT

