#cp $CMSSW_BASE/src/ZZ/Gen/test/sherpa_f#COUP_#F4_#F5_cards.tgz .
bash MakeSherpaLibs.sh -i $PWD -p f#COUP_#F4_#F5#POSTFIX -d /cvmfs/cms.hep.wisc.edu/osg/app/cmssoft/cms/slc5_amd64_gcc434/external/sherpa/1.3.0-cms/
mv *.tgz $OUTPUT
touch submit_#COUP_#F4_#F5-Sherpa_Gen.root

