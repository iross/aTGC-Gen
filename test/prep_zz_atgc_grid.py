#!/usr/bin/env python

import subprocess
import os
from optparse import OptionParser

def prep_grid(options):
    fzmax = options.fzMax
    fgmax = options.fgMax
    coupling = options.coupling
    side = options.side
    dryrun = options.dryrun
    postfix = options.postfix
    if postfix != "":
        postfix="_"+postfix
    print fzmax,fgmax

    fzs = [-fzmax + 2*fzmax/(side - 1.0)*i for i in range(side)]
    fgs = [-fgmax + 2*fgmax/(side - 1.0)*i for i in range(side)]

    home=os.getcwd()
    for fz in fzs:
        fzstr = ('%.4f'%fz).replace('.','p').replace('-','m')
        for fg in fgs:
            fgstr =('%.4f'%fg).replace('.','p').replace('-','m')
            print fzstr,fgstr
            #mkdir for this grid point, prep libraries
            subprocess.call("mkdir %s_%s_%s%s"%(coupling,fzstr,fgstr,postfix),executable="bash",shell=True)
            cur=os.getcwd()
            os.chdir("%s_%s_%s%s"%(coupling,fzstr,fgstr,postfix))
            subprocess.call("../PrepareSherpaLibs.sh -i /scratch/iross/sherpa_ZZ_%s_%s_%s%s-submit_%s_%s_%s%s/submit_%s_%s_%s%s* -p f%s_%s_%s%s -m PROD"%
                    (coupling,fzstr,fgstr,postfix,
                        coupling,fzstr,fgstr,postfix,
                        coupling,fzstr,fgstr,postfix,
                        coupling,fzstr,fgstr,postfix),
                    executable="bash",shell=True)
            subprocess.call("tar -xzf sherpa_f%s_%s_%s%s_MASTER.tgz"%(coupling,fzstr,fgstr,postfix),executable="bash",shell=True)
            subprocess.call("cp sherpa_f%s_%s_%s%s_cff.py ../../python"%(coupling,fzstr,fgstr,postfix),executable="bash",shell=True)
            os.chdir(cur)
    os.chdir(home)
    os.chdir("..")
    subprocess.call("scramv1 b",executable="bash",shell=True)
    os.chdir(home)
    print "now go back into the gridpoint dirs and cmsDrive around"
    for fz in fzs:
        fzstr = ('%.4f'%fz).replace('.','p').replace('-','m')
        for fg in fgs:
            fgstr =('%.4f'%fg).replace('.','p').replace('-','m')
            cur=os.getcwd()
            os.chdir("%s_%s_%s%s"%(coupling,fzstr,fgstr,postfix))
            subprocess.call("cmsDriver.py ZZ/Gen/sherpa_f%s_%s_%s%s_cff.py -s GEN --conditions MC_41_v0::All --datatier GEN-SIM-RAW --eventcontent RAWSIM -n 100 --no_exec --fileout Sherpa_Gen.root"%(coupling,fzstr,fgstr,postfix),executable="bash",shell=True)
            #hack the path so that it runs from ./SherpaRun
            subprocess.call("sed -i 's/Path = .*/Path = cms.untracked.string\(\".\/SherpaRun\"\),/' sherpa_f%s_%s_%s%s_cff_py_GEN.py"%(coupling,fzstr,fgstr,postfix),executable="bash",shell=True)
            subprocess.call("sed -i 's/PathPiece = .*/PathPiece = cms.untracked.string\(\".\/SherpaRun\"\)/' sherpa_f%s_%s_%s%s_cff_py_GEN.py"%(coupling,fzstr,fgstr,postfix),executable="bash",shell=True)
            #todo: cp crab.cfg, script.sh, submit crab jobs
            subprocess.call("sed -e 's/#coupling/%s/' ../crab.cfg > crab.cfg"%(coupling),executable="bash",shell=True)
            subprocess.call("sed -i 's/#F4/%s/' crab.cfg"%(fzstr),executable="bash",shell=True)
            subprocess.call("sed -i 's/#F5/%s%s/' crab.cfg"%(fgstr,postfix),executable="bash",shell=True)
            subprocess.call("cp ../script.sh .",executable="bash",shell=True)
            os.chdir(cur)
    os.chdir(home)
if __name__ == '__main__':
    parser = OptionParser(description="%prog : atgc sherpack prepper.",usage="%prog --h4Max 0.1 --h5Max 0.1 --coupling Z --NPointsSide 3 --postfix TOTHEMAX")

    parser.add_option("--fzMax",dest="fzMax",type="float")
    parser.add_option("--fgMax",dest="fgMax",type="float")
    parser.add_option("--coupling",dest="coupling",type="string")
    parser.add_option("--NPointsSide",dest="side",type="int")
    parser.add_option("--dryrun",dest="dryrun",action="store_true",default=True)
    parser.add_option("--postfix",dest="postfix",type="string",default="")

    (options,args) = parser.parse_args()

    prep_grid(options)
