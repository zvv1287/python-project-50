import json


def get_file_date(file_path):
    with open(file_path) as file:
        return file.read()


def get_date_from_file(file_path):
    from pathlib import Path

    import yaml

    suffix = Path(file_path).suffix
    file_date = get_file_date(file_path)

    if suffix == '.json':
        data = json.loads(file_date)
    elif suffix == '.yml' or suffix == '.yaml':
        data = yaml.safe_load(file_date)
    else:
        return
    return data
