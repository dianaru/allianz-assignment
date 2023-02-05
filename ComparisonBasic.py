class ComparisonBasic(object):
    def __init__(self, operator: str = "", value: object = None, negate: bool = False, type: str = "", caseSensitive: bool = True) -> None:
        self._operator = operator
        self._value = value
        self._negate = negate
        self._type = type
        self._caseSensitive = caseSensitive
        
    #region Properties
    @property
    def operator(self):
        return self._operator
    @operator.setter
    def operator(self, value):
        self._operator = value
    
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self.value = value
        
    @property
    def negate(self):
        return self._negate
    @negate.setter
    def negate(self, value):
        self._negate = value
        
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, value):
        self._type = value
        
    @property
    def caseSensitive(self):
        return self._caseSensitive
    @caseSensitive.setter
    def caseSensitive(self, value):
        self._caseSensitive = value
    #endregion