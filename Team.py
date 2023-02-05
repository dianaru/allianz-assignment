import typing

class Team(object):
    def __init__(self, name: str = "", cost_center: str = "", entity: str = "", host_group_prefixes: list = None) -> None:
        self._name = name
        self._cost_center = cost_center
        self._entity = entity
        self._host_group_prefixes = host_group_prefixes or []

    #region Properties
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cost_center(self):
        return self._cost_center
    @cost_center.setter
    def cost_center(self, value):
        self._cost_center = value

    @property
    def entity(self):
        return self._entity
    @entity.setter
    def entity(self, value):
        self._entity = value

    @property
    def host_group_prefixes(self):
        return self._host_group_prefixes
    @host_group_prefixes.setter
    def host_group_prefixes(self, value):
        self._host_group_prefixes = value
    #endregion

    def update_team(self, key: str, team_dict: dict) -> object:
        try:
            self.name = key
            self.entity = team_dict['entity']
            self.cost_center = team_dict['cost-center']
            self.host_group_prefixes = team_dict['host-group-prefixes']
        except KeyError:
            print("Dictionar key was not found!")
            pass

        # self.name = key
        # if self.hasKey(team_dict, 'entity'):
        #     self.entity = team_dict['entity']
        # else:
        #     pass
        # if self.hasKey(team_dict, 'cost-center'):
        #     self.cost_center = team_dict['cost-center']
        # else:
        #     pass
        # if self.hasKey(team_dict, 'host-group-prefixes'):
        #     self.host_group_prefixes = team_dict['host-group-prefixes']
        # else:
        #     pass
        return self


    # @staticmethod
    # def hasKey(dict: dict, key: str) -> bool:
    #     if key in dict.keys():
    #         return True
    #     else:
    #         return False