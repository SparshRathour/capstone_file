import json
import pytest

def additional_location_coverage(json_obj):
    if "coverage" not in json_obj or "limit" not in json_obj["coverage"]:
        return json_obj
    
    limit_amount = json_obj["coverage"]["limit"].get("amount")
    if limit_amount is None:
        return json_obj
    
    if limit_amount < 100000:
        json_obj["coverage"]["limit"]["amount"] = 100000
    
    return json_obj

def retention_wall_details(json_obj):
    if "coverage" not in json_obj or "deductible" not in json_obj["coverage"]:
        return json_obj
    
    deductible_amount = json_obj["coverage"]["deductible"].get("amount")
    if deductible_amount is None:
        return json_obj
    
    if deductible_amount < 6000:
        json_obj["coverage"]["deductible"]["amount"] = 6000
    
    return json_obj






def test_additional_location_coverage():
    json_str = '{"coverage": {"limit": {"amount": 75000}, "deductible": {"amount": 6000}}}'
    expected_result = '{"coverage": {"limit": {"amount": 100000}, "deductible": {"amount": 6000}}}'
    json_obj = json.loads(json_str)
    new_json_obj = additional_location_coverage(json_obj)
    assert json.dumps(new_json_obj) == expected_result
    
    json_str = '{"deductible": {"amount": 6000}}'
    expected_result = '{"deductible": {"amount": 6000}}'
    json_obj = json.loads(json_str)
    new_json_obj = additional_location_coverage(json_obj)
    assert json.dumps(new_json_obj) == expected_result

    json_str = '{}'
    expected_result = '{}'
    json_obj = json.loads(json_str)
    new_json_obj = additional_location_coverage(json_obj)
    assert json.dumps(new_json_obj) == expected_result

def test_retention_wall_details():
    json_str = '{"coverage": {"limit": {"amount": 75000}, "deductible": {"amount": 5000}}}'
    expected_result = '{"coverage": {"limit": {"amount": 75000}, "deductible": {"amount": 6000}}}'
    json_obj = json.loads(json_str)
    new_json_obj = retention_wall_details(json_obj)
    assert json.dumps(new_json_obj) == expected_result
    
    json_str = '{"coverage": {"limit": {"amount": 75000}}}'
    expected_result = '{"coverage": {"limit": {"amount": 75000}}}'
    json_obj = json.loads(json_str)
    new_json_obj = retention_wall_details(json_obj)
    assert json.dumps(new_json_obj) == expected_result

    json_str = '{}'
    expected_result = '{}'
    json_obj = json.loads(json_str)
    new_json_obj = retention_wall_details(json_obj)
    assert json.dumps(new_json_obj) == expected_result