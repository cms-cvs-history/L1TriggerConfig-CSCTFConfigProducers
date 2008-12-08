import FWCore.ParameterSet.Config as cms

process = cms.Process("L1ConfigWritePayloadDummy")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cout.placeholder = cms.untracked.bool(False)
process.MessageLogger.cout.threshold = cms.untracked.string('INFO')
process.MessageLogger.debugModules = cms.untracked.vstring('*')

# Generate dummy L1TriggerKeyList
process.load("CondTools.L1Trigger.L1TriggerKeyListDummy_cff")


# Get configuration data from OMDS.  This is the subclass of =L1ConfigOnlineProdBase=.
process.load("L1TriggerConfig.CSCTFConfigProducers.CSCTFConfigOnline_cfi")

# ## For a known object key (MyObjectKey): 
# process.load("CondTools.L1Trigger.L1TriggerKeyDummy_cff")
# process.L1TriggerKeyDummy.objectKeys = cms.VPSet(cms.PSet(
#         record = cms.string('L1MuCSCTFConfigurationRcd'),
#         type = cms.string('L1MuCSCTFConfiguration'),
#         key = cms.string('1208080001')
# ))


# ## For a Run Settings key from MYSUBSYSTEM_RUN_SETTINGS_KEYS_CURRENT: 
# #process.load("L1TriggerConfig.CSCTFConfigProducers.CSCTFObjectKeysOnline_cff")

# process.load("CondTools.L1Trigger.L1TriggerKeyDummy_cff")
# process.L1TriggerKeyDummy.objectKeys = cms.VPSet()
# process.L1TriggerKeyDummy.label = cms.string('SubsystemKeysOnly')
# process.load("L1TriggerConfig.CSCTFConfigProducers.CSCTFObjectKeysOnline_cfi")


# ## For a known subsystem key (MySubsystemKey):
    
# process.load("CondTools.L1Trigger.L1TriggerKeyDummy_cff")
# process.L1TriggerKeyDummy.objectKeys = cms.VPSet()
# process.L1TriggerKeyDummy.label = cms.string('SubsystemKeysOnly')

# # xxxKey = csctfKey, dttfKey, rpcKey, gmtKey, rctKey, gctKey, gtKey, or tsp0Key
# process.L1TriggerKeyDummy.csctfKey = cms.string('120808')

# # Subclass of L1ObjectKeysOnlineProdBase.
# process.load("L1TriggerConfig.CSCTFConfigProducers.CSCTFObjectKeysOnline_cfi")
# process.CSCTFObjectKeysOnline.subsystemLabel = cms.string('')

# For a known TSC key (MyTSCKey): 
process.load("CondTools.L1Trigger.L1SubsystemKeysOnline_cfi")
process.L1SubsystemKeysOnline.tscKey = cms.string( 'TSC_000601_081114_CRAFT_GTgtstartupbase6tm2v2rand6hz_GMTstartupcscrpc_GCT_RCT_CSCTF_HCAL_MI' )

# Subclass of L1ObjectKeysOnlineProdBase.
process.load("L1TriggerConfig.CSCTFConfigProducers.CSCTFObjectKeysOnline_cfi")
process.CSCTFObjectKeysOnline.subsystemLabel = cms.string('')

# process.load("L1TriggerConfig.CSCTFConfigProducers.L1CSCTFConfig_cff")
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(1),
    lastValue = cms.uint64(1),
    interval = cms.uint64(1)
)

process.getter = cms.EDAnalyzer("EventSetupRecordDataGetter",
   toGet = cms.VPSet(cms.PSet(
   record = cms.string('L1MuCSCTFConfigurationRcd'),
   data = cms.vstring('L1MuCSCTFConfiguration')
   )),
   verbose = cms.untracked.bool(True)
)

process.p = cms.Path(process.getter)

# process.myanalyzer = cms.EDAnalyzer("CSCTFConfigTestAnalyzer")
# process.p = cms.Path(process.myanalyzer)

