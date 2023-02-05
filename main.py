import argparse
import sys, typing
import yaml
from ReqestAPICall import ReqestAPICall
from ManagementZone import ManagementZone
from MzRule import MzRule
from EntityRuleEngineCondition import EntityRuleEngineCondition
from ConditionKey import ContitionKey
from ComparisonBasic import ComparisonBasic
from Team import Team
import json

def read_yml_file(input_yml_path: str)  -> dict:
    my_dict= {}
    with open(input_yml_path) as f:
        my_dict = yaml.safe_load(f)
    
    return my_dict

def get_teams(yml_dict: dict) -> list:
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

def main():
    args = cli_arguments_parser(sys.argv[1:])
    
    input_yml_path = args.input
    yml_dict = read_yml_file(input_yml_path)
    teams = get_teams(yml_dict)
    
    dynatrace_access_token = args.accessToken
    dynatrace = ReqestAPICall("https://svg88186.live.dynatrace.com/")
    
    header = {
            'Authorization': "Api-Token " + dynatrace_access_token,
            'Content-Type' : 'application/json'
        }
    
    management_zones = dynatrace.get("api/config/v1/managementZones", headers=header).json()['values']
    
    for management_zone, team in zip(management_zones, teams): 
        if team.name == management_zone['name']:
            pass
        else:
            mz_rules = []
            for hot_group_prefix in team.host_group_prefixes:
                key = ContitionKey('HOST_GROUP_NAME')
                comparison_info = ComparisonBasic('BEGINS_WITH', hot_group_prefix, False, 'STRING', True)
                
                #TODO: I think this is not really correct.
                conditions = [EntityRuleEngineCondition(key, comparison_info)]
                mz_rules.append(MzRule(conditions=conditions))
                
            mz = ManagementZone(team.name, mz_rules)
            data = mz.to_json()
            
            #Post new management zones into Dynatrace
            post = dynatrace.post("api/config/v1/managementZones", headers=header, data=data)
            
    

    # data1 = json.dumps(data)
    # post = dynatrace.post("api/config/v1/managementZones", headers=header, data=data1)
    # delete = dynatrace.delete("api/config/v1/managementZones/" + get.json()['values'][0]['id'], headers = header)
    x=0

if __name__ == "__main__":
    main()