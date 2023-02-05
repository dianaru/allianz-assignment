import json

class MzRule(object):
    def __init__(self, rule_type: str = "PROCESS_GROUP", enabled: bool = True, propagation_types: list = ['PROCESS_GROUP_TO_SERVICE',
'PROCESS_GROUP_TO_HOST'] , conditions: list = None) -> None:
        self._rule_type = rule_type
        self._enabled = enabled
        self._propagation_types = propagation_types
        self._conditions = conditions or {}
        
    #region Properties
    @property
    def rule_type(self):
        return self._rule_type
    @rule_type.setter
    def name(self, value):
        self._rule_type = value
    
    @property
    def enabled(self):
        return self._enabled
    @enabled.setter
    def enabled(self, value):
        self._enabled = value
    
    @property
    def propagation_types(self):
        return self._propagation_types
    @propagation_types.setter
    def propagation_types(self, value):
        self._propagation_types = value
    
    @property
    def conditions(self):
        return self._conditions
    @conditions.setter
    def conditions(self, value):
        self._conditions = value
    #endregion
    
    def to_json(self):
        '''
        convert the instance of this class to json
        '''
        return json.dumps(self, indent = 4, default=lambda o: o.__dict__)