class ConfigurationMetadata(object):
    def __init__(self, configurationVersions: list = None, currentConfigurationVersions: list = None, clusterVersion: str = "") -> None:
        self._configurationVersions = configurationVersions
        self._type = type
        
    #region Properties
    @property
    def configurationVersions(self):
        return self._configurationVersions
    @configurationVersions.setter
    def configurationVersions(self, value):
        self._configurationVersions = value
    
    @property
    def currentConfigurationVersions(self):
        return self._currentConfigurationVersions
    @currentConfigurationVersions.setter
    def currentConfigurationVersions(self, value):
        self._currentConfigurationVersions = value
        
    @property
    def clusterVersion(self):
        return self._clusterVersion
    @clusterVersion.setter
    def clusterVersion(self, value):
        self._clusterVersion = value
    #endregion