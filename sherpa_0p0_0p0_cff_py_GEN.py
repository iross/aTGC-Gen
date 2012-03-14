# Auto generated configuration file
# using: 
# Revision: 1.284.2.5 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: ZZ/Gen/python/sherpa_0p0_0p0_cff.py -s GEN --conditions MC_41_V0::All --datatier GEN-SIM-RAW --eventcontent RAWSIM -n 1 --no_exec --fileout Sherpa_Gen.root
import FWCore.ParameterSet.Config as cms

# this is a tag test

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic7TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.284.2.5 $'),
    annotation = cms.untracked.string('ZZ/Gen/python/sherpa_0p0_0p0_cff.py nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('Sherpa_Gen.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RAW')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'MC_41_V0::All'

process.generator = cms.EDFilter("SherpaGeneratorFilter",
    ResultDir = cms.untracked.string('Result'),
    default_weight = cms.untracked.double(1.0),
    SherpaParameters = cms.PSet(
        parameterSets = cms.vstring('Run'),
        Run = cms.vstring('(run){', 
            ' QCUT:=20.0', 
            ' DCUT:=0.3', 
            ' NUM_JETS:=1', 
            ' EVENTS       = 1', 
            ' ANALYSIS     = 1', 
            ' EVENT_MODE   = HepMC', 
            ' # avoid comix re-init after runcard modification', 
            ' WRITE_MAPPING_FILE 3;', 
            '}(run)', 
            '(model){', 
            ' MASSIVE[15]           = 1', 
            ' MODEL                 = SM+AGC', 
            ' EW_SCHEME             = 0', 
            ' ALPHAS(MZ)            = 0.129783', 
            ' ALPHAS(default)       = 0.0800', 
            ' ORDER_ALPHAS          = 0', 
            ' 1/ALPHAQED(0)         = 137.036', 
            ' 1/ALPHAQED(default)   = 132.51', 
            ' SIN2THETAW            = 0.2222', 
            ' VEV                   = 246.', 
            ' LAMBDA                = 0.47591', 
            ' CKMORDER              = 0', 
            ' CABIBBO               = 0.22', 
            ' A                     = 0.85', 
            ' RHO                   = 0.50', 
            ' ETA                   = 0.50', 
            ' STABLE[15]            = 0', 
            ' # atgc parameters', 
            ' f4_Z     = 0.0', 
            ' f4_gamma = 0', 
            ' f5_Z     = 0.0', 
            ' f5_gamma = 0', 
            ' UNITARIZATION_N       = 0', 
            ' UNITARIZATION_SCALE   = 1500', 
            '}(model)', 
            '(beam){', 
            ' BEAM_1 = 2212; BEAM_ENERGY_1 = 3500;', 
            ' BEAM_2 = 2212; BEAM_ENERGY_2 = 3500;', 
            '}(beam)', 
            '(isr){', 
            ' PDF_LIBRARY\t= LHAPDFSherpa', 
            ' PDF_SET         = cteq6ll.LHpdf', 
            ' PDF_SET_VERSION = 1', 
            ' PDF_GRID_PATH   = PDFsets', 
            '}(isr)', 
            '(processes){', 
            ' Process 93 93 -> -90 90 -90 90 93{NUM_JETS}', 
            ' Order_EW          4', 
            ' CKKW              sqr(QCUT/E_CMS)|DCUT', 
            ' Print_Graphs      1', 
            ' Integration_Error 0.02', 
            ' End process', 
            '}(processes)', 
            '(selector){', 
            ' Mass -90 90 12 E_CMS', 
            '}(selector)', 
            '(me){', 
            ' ME_SIGNAL_GENERATOR = Amegic', 
            '}(me)', 
            '(mi) {', 
            ' MI_HANDLER = Amisic', 
            '}')
    ),
    filterEfficiency = cms.untracked.double(1.0),
    Path = cms.untracked.string('/afs/hep.wisc.edu/cms/iross/EWKZZ/CMSSW_4_1_8_patch7/src/ZZ/Gen/SherpaRun'),
    crossSection = cms.untracked.double(-1),
    maxEventsToPrint = cms.untracked.int32(0),
    PathPiece = cms.untracked.string('/afs/hep.wisc.edu/cms/iross/EWKZZ/CMSSW_4_1_8_patch7/src/ZZ/Gen/SherpaRun')
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 
