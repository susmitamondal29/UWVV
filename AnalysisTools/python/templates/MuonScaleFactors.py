from UWVV.AnalysisTools.AnalysisFlowBase import AnalysisFlowBase
from UWVV.Utilities.helpers import UWVV_BASE_PATH

from os import path

import FWCore.ParameterSet.Config as cms

class MuonScaleFactors(AnalysisFlowBase):
    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'isMC'):
            self.isMC = kwargs.get('isMC', True)
        super(MuonScaleFactors, self).__init__(*args, **kwargs)

    def makeAnalysisStep(self, stepName, **inputs):
        step = super(MuonScaleFactors, self).makeAnalysisStep(stepName, **inputs)

        if stepName == 'embedding' and self.isMC:

            sfFile = path.join(UWVV_BASE_PATH, 'data', 'LeptonScaleFactors',
                               'muEfficiencySF_HZZ_ICHEP16_prelim.root')
            sfName = 'FINAL'

            scaleFactorEmbedder = cms.EDProducer(
                "PATMuonScaleFactorEmbedder",
                src = step.getObjTag('m'),
                fileName = cms.string(sfFile),
                histName = cms.string(sfName),
                label = cms.string("effScaleFactor"),
                )
            step.addModule('scaleFactorEmbedder', scaleFactorEmbedder, 'm')

            sfErrName = 'ERROR'

            scaleFactorErrorEmbedder = cms.EDProducer(
                "PATMuonScaleFactorEmbedder",
                src = step.getObjTag('m'),
                fileName = cms.string(sfFile),
                histName = cms.string(sfErrName),
                label = cms.string("effScaleFactorError"),
                )
            step.addModule('scaleFactorErrorEmbedder', 
                           scaleFactorErrorEmbedder, 'm')

        return step


    




