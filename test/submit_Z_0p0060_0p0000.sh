#cp $CMSSW_BASE/src/ZZ/Gen/test/sherpa_fZ_0p0060_0p0000_cards.tgz .
bash MakeSherpaLibs.sh -i $PWD -p fZ_0p0060_0p0000 -d /cvmfs/cms.hep.wisc.edu/osg/app/cmssoft/cms/slc5_amd64_gcc434/external/sherpa/1.3.0-cms/
mv *.tgz $OUTPUT
touch submit_Z_0p0060_0p0000-Sherpa_Gen.root

