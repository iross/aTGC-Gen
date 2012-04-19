import FWCore.ParameterSet.Config as cms
import os

source = cms.Source("EmptySource")

generator = cms.EDFilter("SherpaGeneratorFilter",
  maxEventsToPrint = cms.untracked.int32(0),
  filterEfficiency = cms.untracked.double(1.0),
  crossSection = cms.untracked.double(-1),
  Path = cms.untracked.string(os.getcwd()+'/SherpaRun'),
  PathPiece = cms.untracked.string(os.getcwd()+'/SherpaRun'),
  ResultDir = cms.untracked.string('Result'),
  default_weight = cms.untracked.double(1.0),
  SherpaParameters = cms.PSet(parameterSets = cms.vstring(
                             "Run"),
                              Run = cms.vstring(
				"(run){",
				" QCUT:=20.0",
				" DCUT:=0.3",
				" NUM_JETS:=1",
				" EVENTS       = 1",
				" ANALYSIS     = 1",
				" EVENT_MODE   = HepMC",
				" # avoid comix re-init after runcard modification",
				" WRITE_MAPPING_FILE 3;",
				"}(run)",
				"(model){",
				" MASSIVE[15]           = 1",
				" MODEL                 = SM+AGC",
				" STABLE[15]            = 0",
				" # atgc parameters",
				" F4_Z     = 0.0",
				" F4_gamma = 0.0600",
				" F5_Z     = 0.0",
				" F5_gamma = -0.0600",
				"}(model)",
				"(beam)",
				" BEAM_1 = 2212; BEAM_ENERGY_1 = 3500;",
				" BEAM_2 = 2212; BEAM_ENERGY_2 = 3500;",
				"}(beam)",
				"(isr){",
				" PDF_LIBRARY	= LHAPDFSherpa",
				" PDF_SET         = cteq6ll.LHpdf",
				" PDF_SET_VERSION = 1",
				" PDF_GRID_PATH   = PDFsets",
				"}(isr)",
				"(processes){",
				" Process 93 93 -> -90 90 -90 90 93{NUM_JETS}",
				" Order_EW          4",
				" CKKW              sqr(QCUT/E_CMS)|DCUT",
				" Print_Graphs      1",
				" Integration_Error 0.02",
				" End process",
				"}(processes)",
				"(selector){",
				" Mass -90 90 12 E_CMS",
				"}(selector)",
				"(me){",
				" ME_SIGNAL_GENERATOR = Amegic",
				"}(me)",
				"(fragmentation){",
				" YFS_MODE = 2",
				" YFS_USE_ME = 1",
				"}",
				"(mi) {",
				" MI_HANDLER = Amisic",
				"}"
                                                  ),
                             )
)

ProductionFilterSequence = cms.Sequence(generator)

