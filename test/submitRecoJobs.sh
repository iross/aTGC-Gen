#!/bin/bash
voms-proxy-init --voms cms --valid 100:00
rm -r /scratch/iross/test-temp
cat sherpa_0p0_0p0_cff_py_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_RECO.py > temp.py
cat CONDOR.py >> temp.py

farmoutAnalysisJobs --skip-existing-output --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/iross/Sherpa_ZZ_0p0_0p0/ test $CMSSW_BASE $CMSSW_BASE/src/ZZ/Gen/test/temp.py

