import FWCore.ParameterSet.Config as cms

hcalClient = cms.EDAnalyzer("HcalMonitorClient",
    runningStandalone = cms.untracked.bool(False),
    digiErrorFrac = cms.untracked.double(0.05),
    TrigPrimMonitor = cms.untracked.bool(True),
    CapIdMEAN_ErrThresh = cms.untracked.double(1.5),
    MonitorDaemon = cms.untracked.bool(True),
    deadcellErrorFrac = cms.untracked.double(0.05),
    showTiming = cms.untracked.bool(False),
    plotPedRAW = cms.untracked.bool(False),
    resetFreqEvents = cms.untracked.int32(-1),
    DeadCellClient = cms.untracked.bool(False),
    resetFreqLS = cms.untracked.int32(-1),
    PedestalMean_ErrThresh = cms.untracked.double(2.0),
    DataFormatClient = cms.untracked.bool(True),
    CapIdRMS_ErrThresh = cms.untracked.double(0.25),
    HotCellClient = cms.untracked.bool(False),
    processName = cms.untracked.string(''),
    LEDRMS_ErrThresh = cms.untracked.double(0.8),
    SummaryClient = cms.untracked.bool(True),                          
    DigiClient = cms.untracked.bool(True),
    diagnosticPrescaleUpdate = cms.untracked.int32(-1),
    inputFile = cms.untracked.string(''),
    hotcellErrorFrac = cms.untracked.double(0.05),
    LEDClient = cms.untracked.bool(False),
    resetFreqTime = cms.untracked.int32(-1),
    PedestalClient = cms.untracked.bool(False),
    LEDMEAN_ErrThresh = cms.untracked.double(2.25),
    diagnosticPrescaleLS = cms.untracked.int32(-1),
    subDetsOn = cms.untracked.vstring('HB', 
        'HE', 
        'HF', 
        'HO'),
    RecHitClient = cms.untracked.bool(False),
    CaloTowerClient = cms.untracked.bool(False),
    resetFreqUpdates = cms.untracked.int32(-1),
    baseHtmlDir = cms.untracked.string('.'),
    DoPerChanTests = cms.untracked.bool(True),
    PedestalRMS_ErrThresh = cms.untracked.double(1.0),
    diagnosticPrescaleTime = cms.untracked.int32(-1),
    diagnosticPrescaleEvt = cms.untracked.int32(200),
    debug = cms.untracked.bool(False)
)

