class ContitionKey(object):
    def __init__(self, attribute: str = "", type: list = None) -> None:
        self._attribute = attribute
        self._type = type
        
    #region Properties
    @property
    def attribute(self):
        return self._attribute
    @attribute.setter
    def attribute(self, value):
        self._attribute = value
    
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, value):
        self.type = value
    #endregion