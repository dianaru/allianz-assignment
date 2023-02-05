
import json

from ConfigurationMetadata import ConfigurationMetadata
class ManagementZone(object):
    def __init__(self, metadata = ConfigurationMetadata(), id: str = "", name: str = "", description: str = "", rules: list = None, dimensionalRules: list = None, entitySelectorBasedRules: list = None) -> None:
        self._metadata = metadata
        self._id = id
        self._name = name
        self._description = description
        self._rules = rules
        self._dimensionalRules = dimensionalRules
        self._entitySelectorBasedRules = entitySelectorBasedRules
        
    #region Properties
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def metadata(self):
        return self._metadata
    @metadata.setter
    def metadata(self, value):
        self._metadata = value
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        self._description = value
    
    @property
    def rules(self):
        return self._rules
    @rules.setter
    def rules(self, value):
        self._rules = value
    
    @property
    def dimensionalRules(self):
        return self._dimensionalRules
    @dimensionalRules.setter
    def dimensionalRules(self, value):
        self._dimensionalRules = value
    
    @property
    def entitySelectorBasedRules(self):
        return self._entitySelectorBasedRules
    @entitySelectorBasedRules.setter
    def entitySelectorBasedRules(self, value):
        self._entitySelectorBasedRules = value
    #endregion
    
    def to_json(self):
        """
            convert the instance of this class to json
        """
        object_dict = lambda o: {key.lstrip('_'): value for key, value in o.__dict__.items()}
        return json.dumps(self, default=object_dict, allow_nan=False, sort_keys=False, indent=4)
