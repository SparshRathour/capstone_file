import json
import pytest

def update_json(json_str):
    data = json.loads(json_str)
    data['buliding']['areaOccupied']['unitCount'] = 0
    return json.dumps(data)

def test_update_json():
    input_json = '{"buliding": {"areaOccupied": {"unitCount": 75000}}}'
    expected_output = '{"buliding": {"areaOccupied": {"unitCount": 0}}}'

    updated_json = update_json(input_json)
    data1 = json.loads(updated_json)
    data2 = json.loads(expected_output)

    assert data1 == data2

if __name__ == "__main__":
    pytest.main([__file__])