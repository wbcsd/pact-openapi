import sys
import json
import yaml
#from jsonschema import validate
#from jsonschema.validators import Draft202012Validator
from openapi_schema_validator import validate, OAS30Validator, OAS31Validator
# from openapi_core import OpenAPI, validate_response

# raises error if response is invalid
#openapi = OpenAPI('openapi-2.2.1-wip.json')
#openapi.validate_response()
#openapi.validate_response(request, response)
#exit()

# load yaml file openapi-2.2.1-wip.yaml:
#with open('openapi-2.2.1-wip.yaml') as file:
#    schema = yaml.safe_load(file)

with open('openapi-2.2.1-wip.json') as file:
    schema = json.load(file)
#print(json.dumps(schema, indent=2))
#exit()

yaml.dump(schema, sys.stdout, sort_keys=False)
exit()

yaml.dump(schema["components"]["schemas"]["PositiveNonZeroDecimal"], sys.stdout, indent=2)
yaml.dump(schema["components"]["schemas"]["PositiveOrZeroDecimal"], sys.stdout, indent=2)
yaml.dump(schema["components"]["schemas"]["Decimal"], sys.stdout, indent=2)
yaml.dump(schema["components"]["schemas"]["NegativeOrZeroDecimal"], sys.stdout, indent=2)
yaml.dump(schema["components"]["schemas"]["NegativeNonZeroDecimal"], sys.stdout, indent=2)

validator = OAS31Validator(schema)
OAS31Validator.check_schema(schema)
#validator = Draft202012Validator(schema)
#validator.check_schema(schema)

carbonFootprint = schema["components"]["schemas"]["CarbonFootprint"]
#json.dump(carbonFootprint, sys.stdout, indent=2)

validator.validate({
        "biogenicCarbonContent": "11234",
        "boundaryProcessesDescription": "Description of boundary processes",
        "characterizationFactors": "AR6",
        "crossSectoralStandardsUsed": ["ISO Standard 14044"],
        "declaredUnit": "liter",
        "exemptedEmissionsDescription": "AR5",
        "exemptedEmissionsPercent": 5.0,
        "fossilCarbonContent": "123.456",
        "fossilGhgEmissions": "123.456",
        "ipccCharacterizationFactorsSources": ["AR6"],
        "pCfExcludingBiogenic": "+123.456",
        "pCfIncludingBiogenic": None,
        "dLucGhgEmissions": None,
        "packagingEmissionsIncluded": True,
        "productOrSectorSpecificRules": [
            { "operator": "PEF", "ruleNames": ["xx", "yy"] }
        ],
        "referencePeriodEnd": "X21-12-31",
        "referencePeriodStart": "2021-01-01",
        "unitaryProductAmount": "-0.1",
        "geographyRegionOrSubregion": "Africa",
        "landManagementGhgEmissions": "123.456",
        "uncertaintyAssessmentDescription": None,
    },
    carbonFootprint)

print("Validation successful")

#validator.validate({"name": "John", "age": 30, "address": {"street":"xx","city":"yy","postalCode":"1234"}}, schema["components"]["schemas"]["User"])
#validator.is_type({"name": "John", "age": 30}, "User")
##validate({"name": "John", "aged": 30}, schema)