import argparse
import sys, typing
import yaml
from dynatrace_api_call import DynatraceAPICall
from team_class import Team
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
    dynatrace = DynatraceAPICall("https://svg88186.live.dynatrace.com/")
    
    
    data = {
            "name": "sampleManagementZone",
            "description": "sampleDescription"
        }
    data1 = json.dumps(data)
    header = {
            'Authorization': "Api-Token " + dynatrace_access_token,
            'Content-Type' : 'application/json'
        }
    
    get = dynatrace.get("api/config/v1/managementZones", headers=header)    
    post = dynatrace.post("api/config/v1/managementZones", headers=header, data=data1)
    x=0

if __name__ == "__main__":
    main()