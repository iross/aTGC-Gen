#!/usr/bin/env python

import subprocess
from optparse import OptionParser

def gen_grid(options):

    fzmax = options.fzMax
    fgmax = options.fgMax
    coupling = options.coupling
    side = options.side
    dryrun = options.dryrun
    postfix = options.postfix
    print postfix
    fzs = [-fzmax + 2*fzmax/(side - 1.0)*i for i in range(side)]
    fgs = [-fgmax + 2*fgmax/(side - 1.0)*i for i in range(side)]
    for fz in fzs:
        for fg in fgs:
            if dryrun:
                subprocess.call("./gen_zz_atgc_point.sh --dryrun --fz %.4f --fg %.4f --coupling %s --postfix %s"%(fz,fg,coupling,postfix),
                                executable="bash",shell=True)
            else:
                subprocess.call("./gen_zz_atgc_point.sh  --fz %.4f --fg %.4f --coupling %s --postfix %s"%(fz,fg,coupling,postfix),
                                executable="bash",shell=True)

if __name__ == '__main__':
    parser = OptionParser(description="%prog : atgc grid producer.",
                          usage="%prog --h4Max 0.1 --h5Max 0.1 --coupling Z --NPointsSide 3")

    parser.add_option("--fzMax",dest="fzMax",type="float")
    parser.add_option("--fgMax",dest="fgMax",type="float")
    parser.add_option("--coupling",dest="coupling",type="string")
    parser.add_option("--NPointsSide",dest="side",type="int")
    parser.add_option("--dryrun",dest="dryrun",action="store_true",default=False)
    parser.add_option("--postfix",dest="postfix",type="string",default="")
    (options,args) = parser.parse_args()

    gen_grid(options)
