# allianz-assignment
Repo use for allianz technical assignment. 

# Introduction
This project main job is to assist in the creation and updating the **Management Zone** area from Dynatrace.

It does so by using an input file of *yml* type, transforming the data into JSON objects and transfering that into Dynatrace.

# Prerequisites
 - Python istallation
 - Python version >= 3.9
 - Packages: *requests*, *pyyml*
 - Dynatrace access

 *Note1: if some of the packages are missing use ```pip install <name_of_the_package>```*

 *Note2: set environment variable %PYTHON_PATH% to the desired python path.*

# Usage
Script calling:
```
 ./main.py -i <input_yml_file> -t <dynatrace_access_token>
```
Options:
 - -i input yml file
 - -t dynatrace access token (*see [documentation](https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication) on how to generate the access token for synatrace)

# Architectural details
Classes were constructed based on the [Dynatrace Management Zone documentation](https://www.dynatrace.com/support/help/dynatrace-api/configuration-api/management-zones-api). 

# Task
In Dynatrace, so-called Management Zones shall be configured via the API in a configuration-ascode approach. 

Provide a: 
* Python3 CLI-application that 

* accepts a filename as input and expects a YAML-file in the  style of the provided example .yml file

* uses the Dynatrace API such that for each team as specified by the yaml file and creates a Management Zone in Dynatrace with the team 's entry's dictionary key as name if no such MZ already exists 

* or updates the respective Management Zone if it already exists and deletes all existing rules and creates a Rule (cf. https://www.dynatrace.com/support/help/how-to-use-dynatrace/management-zones/set-up-management-zones/; see also the rules property of management zones in the DT API documentation) 

* for each entry in the host-group-prefixes List (if provided) of the team dictionary with the
following payload scheme:

```yml
{'type': 'PROCESS_GROUP',
 'enabled': True,
 'propagationTypes': ['PROCESS_GROUP_TO_SERVICE',
'PROCESS_GROUP_TO_HOST'],
 'conditions': [{'key': {'attribute': 'HOST_GROUP_NAME'},
 'comparisonInfo': {'type': 'STRING',
 'operator': 'BEGINS_WITH',
 'value': <hostgroup-prefix>,
 'negate': False,
 'caseSensitive': True}}]}
 ```

where is to be replaced by the respective list entry.
# Resources
You should first get yourself a trial Dynatrace tenant: https://www.dynatrace.com/trial/
In you trial tenant you will need to generate an Access Token for API usage (check official
Dynatrace docs for more details)

The example yaml file has the following content:
```yml
tenant_id: zxf97648
teams:
 global-pcf-a:
 cost-center: ct-4291
 entity: ab-3
 host-group-prefixes:
- global-pcf-a-Z
- global-pcf-a-Y
 global-pcf-b:
 cost-center: ct-4291
 entity: ab-3
 ```