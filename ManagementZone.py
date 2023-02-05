
import json

class ManagementZone(object):
    def __init__(self, name: str = "", rules: list = None) -> None:
        self._name = name
        self._rules = rules
        
    #region Properties
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def rules(self):
        return self._rules
    @rules.setter
    def rules(self, value):
        self.rules = value
    #endregion
    
    def to_json(self):
        '''
        convert the instance of this class to json
        '''
        return json.dumps(self, indent = 4, default=lambda o: o.__dict__)