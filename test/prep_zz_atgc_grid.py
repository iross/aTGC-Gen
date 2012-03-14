#!/usr/bin/env python

import subprocess
import os
from optparse import OptionParser

def prep_grid(options):
	f4max = options.f4Max
	f5max = options.f5Max
	coupling = options.coupling
	side = options.side
	dryrun = options.dryrun
	postfix = options.postfix
	if postfix != "":
		postfix="_"+postfix
	print f4max,f5max

	f4s = [-f4max + 2*f4max/(side - 1.0)*i for i in range(side)]
	f5s = [-f5max + 2*f5max/(side - 1.0)*i for i in range(side)]
	home=os.getcwd()
	for f4 in f4s:
		f4str = ('%.3f'%f4).replace('.','p').replace('-','m')
		for f5 in f5s:
			f5str =('%.3f'%f5).replace('.','p').replace('-','m')
			print f4str,f5str
			#mkdir for this grid point, prep libraries
			subprocess.call("mkdir %s_%s_%s%s"%(coupling,f4str,f5str,postfix),executable="bash",shell=True) 
			cur=os.getcwd()
			os.chdir("%s_%s_%s%s"%(coupling,f4str,f5str,postfix))
#			sherpa_ZZ_Z_0p060_0p000_l1000-submit_Z_0p060_0p000_l1000
			subprocess.call("../PrepareSherpaLibs.sh -i /scratch/iross/sherpa_ZZ_%s_%s_%s%s-submit_%s_%s_%s%s/submit_%s_%s_%s%s-Sherpa_Gen -p f%s_%s_%s%s -m PROD"%
					(coupling,f4str,f5str,postfix,
						coupling,f4str,f5str,postfix,
						coupling,f4str,f5str,postfix,
						coupling,f4str,f5str,postfix),
					executable="bash",shell=True)
			subprocess.call("tar -xzf sherpa_f%s_%s_%s%s_MASTER.tgz"%(coupling,f4str,f5str,postfix),executable="bash",shell=True)
			#sherpa_fZ_0p100_0p100_cff.py
			subprocess.call("cp sherpa_f%s_%s_%s%s_cff.py ../../python"%(coupling,f4str,f5str,postfix),executable="bash",shell=True)
			#do stuff
			os.chdir(cur)
	os.chdir(home)
	os.chdir("..")
	subprocess.call("scramv1 b",executable="bash",shell=True)
	os.chdir(home)
	print "now go back into the gridpoint dirs and cmsDrive around"
	for f4 in f4s:
		f4str = ('%.3f'%f4).replace('.','p').replace('-','m')
		for f5 in f5s:
			f5str =('%.3f'%f5).replace('.','p').replace('-','m')
			cur=os.getcwd()
			os.chdir("%s_%s_%s%s"%(coupling,f4str,f5str,postfix))
			subprocess.call("cmsDriver.py ZZ/Gen/sherpa_f%s_%s_%s%s_cff.py -s GEN --conditions MC_41_v0::All --datatier GEN-SIM-RAW --eventcontent RAWSIM -n 100 --no_exec --fileout Sherpa_Gen.root"%(coupling,f4str,f5str,postfix),executable="bash",shell=True)
			#hack the path so that it runs from ./SherpaRun
			subprocess.call("sed -i 's/Path = .*/Path = cms.untracked.string\(\".\/SherpaRun\"\),/' sherpa_f%s_%s_%s%s_cff_py_GEN.py"%(coupling,f4str,f5str,postfix),executable="bash",shell=True)
			subprocess.call("sed -i 's/PathPiece = .*/PathPiece = cms.untracked.string\(\".\/SherpaRun\"\)/' sherpa_f%s_%s_%s%s_cff_py_GEN.py"%(coupling,f4str,f5str,postfix),executable="bash",shell=True)
			#todo: cp crab.cfg, script.sh, submit crab jobs
			subprocess.call("sed -e 's/#coupling/%s/' ../crab.cfg > crab.cfg"%(coupling),executable="bash",shell=True)
			subprocess.call("sed -i 's/#F4/%s/' crab.cfg"%(f4str),executable="bash",shell=True)
			subprocess.call("sed -i 's/#F5/%s%s/' crab.cfg"%(f5str,postfix),executable="bash",shell=True)
			subprocess.call("cp ../script.sh .",executable="bash",shell=True)
			os.chdir(cur)
	os.chdir(home)
if __name__ == '__main__':
	parser = OptionParser(description="%prog : atgc sherpack prepper.",usage="%prog --h4Max 0.1 --h5Max 0.1 --coupling Z --NPointsSide 3 --postfix TOTHEMAX")

	parser.add_option("--f4Max",dest="f4Max",type="float")
	parser.add_option("--f5Max",dest="f5Max",type="float")
	parser.add_option("--coupling",dest="coupling",type="string")
	parser.add_option("--NPointsSide",dest="side",type="int")
	parser.add_option("--dryrun",dest="dryrun",action="store_true",default=True)
	parser.add_option("--postfix",dest="postfix",type="string",default="")

	(options,args) = parser.parse_args()

	prep_grid(options)
