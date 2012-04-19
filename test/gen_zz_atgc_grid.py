#!/usr/bin/env python

import subprocess
from optparse import OptionParser

def gen_grid(options):

    f4max = options.f4Max
    f5max = options.f5Max
    coupling = options.coupling
    side = options.side
    dryrun = options.dryrun
    postfix = options.postfix
    print postfix
    f4s = [-f4max + 2*f4max/(side - 1.0)*i for i in range(side)]
    f5s = [-f5max + 2*f5max/(side - 1.0)*i for i in range(side)]

    for f4 in f4s:
        for f5 in f5s:
            if dryrun:
                subprocess.call("./gen_zz_atgc_point.sh --dryrun --f4 %.4f --f5 %.4f --coupling %s --postfix %s"%(f4,f5,coupling,postfix),
                                executable="bash",shell=True)
            else:
                subprocess.call("./gen_zz_atgc_point.sh  --f4 %.4f --f5 %.4f --coupling %s --postfix %s"%(f4,f5,coupling,postfix),
                                executable="bash",shell=True)

if __name__ == '__main__':
    parser = OptionParser(description="%prog : atgc grid producer.",
                          usage="%prog --h4Max 0.1 --h5Max 0.1 --coupling Z --NPointsSide 3")

    parser.add_option("--f4Max",dest="f4Max",type="float")
    parser.add_option("--f5Max",dest="f5Max",type="float")
    parser.add_option("--coupling",dest="coupling",type="string")
    parser.add_option("--NPointsSide",dest="side",type="int")
    parser.add_option("--dryrun",dest="dryrun",action="store_true",default=False)
    parser.add_option("--postfix",dest="postfix",type="string",default="")
    (options,args) = parser.parse_args()

    gen_grid(options)
