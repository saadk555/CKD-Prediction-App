from flask import Flask, request
import re

app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello():
    data = request.get_json()

    attributes = [
        'bp', 'bp_limit', 'sg', 'al', 'rbc', 'su', 'pc', 'pcc', 'ba', 'bgr',
        'bu', 'sod', 'sc', 'pot', 'hemo', 'pcv', 'rbcc', 'wbcc', 'htn', 'dm',
        'cad', 'appet', 'pe', 'ane', 'grf', 'stage', 'affected', 'age'
    ]

    data = {attr: data.get(attr) for attr in attributes}

    stage_mapping = {'s1': 1, 's2': 2, 's3': 3, 's4': 4, 's5': 5}
    data['stage'] = stage_mapping.get(data['stage'])

    def apply_transformations(value):
        value = str(value).replace(' ', '') if ' ' in str(value) else value

        if '-' in str(value):
            value = (float(str(value).split('-')[0]) + float(str(value).split('-')[1])) / 2
        else:
            value

        regexp = re.compile(r'≥|≤')
        if '<' in str(value):
            value = float(value[1:]) - 1
        elif regexp.search(str(value)):
            value = float(str(value).replace('≥', '').replace('≤', ''))
        elif '>' in str(value):
            value = float(value[1:]) + 1
     
        return value

    data = {key: apply_transformations(value) for key, value in data.items()}

    return data


if __name__ == "__main__":
    app.run()
