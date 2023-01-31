# allianz-assignment
Repo use for allianz technical assignment. 


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