import json

from ConditionKey import ContitionKey
from ComparisonBasic import ComparisonBasic

class EntityRuleEngineCondition(object):
    def __init__(self, key: ContitionKey = ContitionKey(), comparisonInfo: ComparisonBasic = ComparisonBasic()) -> None:
        self._key = key
        self._comparisonInfo = comparisonInfo
        
    #region Properties
    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, value):
        self._key = value
    
    @property
    def comparisonInfo(self):
        return self._comparisonInfo
    @comparisonInfo.setter
    def comparisonInfo(self, value):
        self.comparisonInfo = value
    #endregion
    
    def to_json(self):
        '''
        convert the instance of this class to json
        '''
        return json.dumps(self, indent = 4, default=lambda o: o.__dict__)