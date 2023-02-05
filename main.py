import argparse
import sys
import typing
import yaml
import json

from ReqestAPICall import ReqestAPICall
from ManagementZone import ManagementZone
from MzRule import MzRule
from EntityRuleEngineCondition import EntityRuleEngineCondition
from ConditionKey import ContitionKey
from ComparisonBasic import ComparisonBasic
from Team import Team

def read_yml_file(input_yml_path: str)  -> dict:
    """
    Read the input yml file and return the contents
    in dict format.
  
    Parameters:
    input_yml_file (str): input file yml
  
    Returns:
    input_dict (dict): content of yml file in dict format
  
    """
    input_dict= {}
    with open(input_yml_path) as f:
        input_dict = yaml.safe_load(f)
    
    return input_dict


def get_teams(yml_dict: dict) -> list:
    """
    Transfor the input dict in Team objects and
    puts them in list.
  
    Parameters:
    yml_dict (dict): input dict that was read
        from yml file 
  
    Returns:
    teams (list): list of Team objects
  
    """
    teams = []
    for key, value in yml_dict['teams'].items():
        team = Team()
        teams.append(team.update_team(key, value))
    
    return teams

 
def cli_arguments_parser(argv: typing.Sequence) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', type=str, required=True, default='./test_data.yml', help='Path to the input yml file.')
    parser.add_argument('-t', '--accessToken', type=str, required=True, default='', help='Acces tocken for Dynatrace')
    
    parsed_arguments = parser.parse_args(argv)
    
    
    return parsed_arguments


def update_rules(team: Team, management_zone: ManagementZone) -> str:
    """
    Update the rules from the Management Zone 
    objects.
  
    Parameters:
    team (Team): team object in scope 
    management_zone (ManagementZone): management zone in scope 
  
    Returns:
    data (str): management zone in JSON format
  
    """
    mz_rules = []
    
    # check if the management_zone is new or is already existing
    if management_zone.name != "":
        management_zone.name = team.name
    else:
        pass
    
    if len(team.host_group_prefixes) > 0 :
        for hot_group_prefix in team.host_group_prefixes:
            key = ContitionKey('HOST_GROUP_NAME')
            comparison_info = ComparisonBasic('BEGINS_WITH', hot_group_prefix, False, 'STRING', True)
            
            #TODO: I think this is not really correct.
            conditions = [EntityRuleEngineCondition(key, comparison_info)]
            mz_rules.append(MzRule(conditions=conditions))
    else:
        pass
    
    management_zone.rules = mz_rules
    
    return management_zone.to_json()


def main():
    args = cli_arguments_parser(sys.argv[1:])
    
    input_yml_path = args.input
    yml_dict = read_yml_file(input_yml_path)
    teams = get_teams(yml_dict)
    
    dynatrace_access_token = args.accessToken
    dynatrace = ReqestAPICall("https://svg88186.live.dynatrace.com/")
    
    header = {
            'Authorization': "Api-Token " + dynatrace_access_token,
            'Content-Type' : 'application/json',
            'Accept': 'application/json'
        }
    
    get_mz_response = dynatrace.get("api/config/v1/managementZones", headers=header)
    if  get_mz_response.ok:
        management_zones = get_mz_response.json()['values']
        for team, management_zone in zip(teams, management_zones):
            # check if management_zone is new or already exists
            if team.name == management_zone['name']:
                
                #if management_zone already exists take specific management_zone using the management zone ID
                get_single_mz_response = dynatrace.get("api/config/v1/managementZones/" + management_zone['id'], headers = header)
                
                if get_single_mz_response.ok:
                    # convert from JSON object to custom object
                    mz_json = json.loads(get_single_mz_response.text)
                    in_scope_management_zone = ManagementZone(**mz_json)
                    
                    # delete all existing rules
                    in_scope_management_zone.rules.clear()
                    
                    data = update_rules(team, in_scope_management_zone)
                    
                    #update data back into the specific management_zone into Dynatrace
                    update_mz_response = dynatrace.put("api/config/v1/managementZones/"+ management_zone['id'], headers = header, data = data)
                    if  update_mz_response.ok:
                        print("Update was successful!")
                    else:
                        print("API call failed with the following code:{0}. Reason of failing: {1}.".format(update_mz_response.status_code, update_mz_response.reason))
                else:
                    print("API call failed with the following code:{0}. Reason of failing: {1}.".format(get_single_mz_response.status_code, get_single_mz_response.reason))
            else:
                # if the management_zone is new, create a new ManagementZone object
                mz = ManagementZone()
                data = update_rules(team, mz)
                
                #create new management zones into Dynatrace
                create_mz_response = dynatrace.post("api/config/v1/managementZones", headers=header, data=data)
                if  create_mz_response.ok:
                        print("Update was successful!")
                else:
                    print("API call failed with the following code:{0}. Reason of failing: {1}.".format(create_mz_response.status_code, create_mz_response.reason))
    else:
        print("API call failed with the following code:{0}. Reason of failing: {1}.".format(get_mz_response.status_code, get_mz_response.reason))


if __name__ == "__main__":
    main()