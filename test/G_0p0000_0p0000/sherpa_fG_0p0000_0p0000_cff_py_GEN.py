# Auto generated configuration file
# using: 
# Revision: 1.284.2.5 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: ZZ/Gen/sherpa_fG_0p0000_0p0000_cff.py -s GEN --conditions MC_41_v0::All --datatier GEN-SIM-RAW --eventcontent RAWSIM -n 100 --no_exec --fileout Sherpa_Gen.root
import FWCore.ParameterSet.Config as cms

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
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.284.2.5 $'),
    annotation = cms.untracked.string('ZZ/Gen/sherpa_fG_0p0000_0p0000_cff.py nevts:100'),
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
process.GlobalTag.globaltag = 'MC_41_v0::All'

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
            ' STABLE[15]            = 0', 
            ' # atgc parameters', 
            ' F4_Z     = 0.0', 
            ' F4_gamma = 0.0000', 
            ' F5_Z     = 0.0', 
            ' F5_gamma = 0.0000', 
            '}(model)', 
            '(beam)', 
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
            '(fragmentation){', 
            ' YFS_MODE = 2', 
            ' YFS_USE_ME = 1', 
            '}', 
            '(mi) {', 
            ' MI_HANDLER = Amisic', 
            '}')
    ),
    filterEfficiency = cms.untracked.double(1.0),
    Path = cms.untracked.string("./SherpaRun"),
    crossSection = cms.untracked.double(-1),
    maxEventsToPrint = cms.untracked.int32(0),
    PathPiece = cms.untracked.string("./SherpaRun")
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
