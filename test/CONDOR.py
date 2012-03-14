process.source = cms.Source("PoolSource",
		fileNames = cms.untracked.vstring(
			$inputFileNames
			)
		)

process.maxEvents = cms.untracked.PSet(
		input = cms.untracked.int32(200)
		)

process.TFileService.fileName=cms.string("$outputFileName")
