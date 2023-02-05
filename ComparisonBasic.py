class ComparisonBasic(object):
    def __init__(self, operator: str = "", value: object = None, negate: bool = False, comparison_basic_type: str = "", case_sensitive: bool = True) -> None:
        self._operator = operator
        self._value = value
        self._negate = negate
        self._comparison_basic_type = comparison_basic_type
        self._case_sensitive = case_sensitive
        
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
    def comparison_basic_type(self):
        return self._comparison_basic_type
    @comparison_basic_type.setter
    def comparison_basic_type(self, value):
        self._comparison_basic_type = value
        
    @property
    def case_sensitive(self):
        return self._case_sensitive
    @case_sensitive.setter
    def case_sensitive(self, value):
        self._case_sensitive = value
    #endregion