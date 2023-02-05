import json

from ConditionKey import ContitionKey
from ComparisonBasic import ComparisonBasic

class EntityRuleEngineCondition(object):
    def __init__(self, key: ContitionKey = ContitionKey(), comparison_info: ComparisonBasic = ComparisonBasic()) -> None:
        self._key = key
        self._comparison_info = comparison_info
        
    #region Properties
    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, value):
        self._key = value
    
    @property
    def comparison_info(self):
        return self._comparison_info
    @comparison_info.setter
    def comparison_info(self, value):
        self.comparison_info = value
    #endregion
    
    def to_json(self):
        '''
        convert the instance of this class to json
        '''
        return json.dumps(self, indent = 4, default=lambda o: o.__dict__)