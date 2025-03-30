import json


def get_json_result_str(result_diff):
    return json.dumps(result_diff, indent=4, separators=(',', ': '))