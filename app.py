from flask import *
import re
import models
from flask_restful import Resource, Api, reqparse
import werkzeug
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import requests

UPLOAD_FOLDER = "./UPLOAD_FOLDER"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=['POST'])
def hello():

    data = request.get_json()

    stage_mapping = {'s1': 1, 's2': 2, 's3': 3, 's4': 4, 's5': 5}
    data['stage'] = stage_mapping.get(data['stage'])

    def apply_transformations(value):
        value = str(value).replace(' ', '') if ' ' in str(value) else value

        if '-' in str(value):
            value = (float(str(value).split('-')
                     [0]) + float(str(value).split('-')[1])) / 2
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

    algo = data.get('algorithm')
    bp = data.get('bp')
    bp_limit = data.get('bp_limit')
    sg = data.get('sg')
    al = data.get('al')
    rbc = data.get('rbc')
    su = data.get('su')
    pc = data.get('pc')
    pcc = data.get('pcc')
    ba = data.get('ba')
    bgr = data.get('bgr')
    bu = data.get('bu')
    sod = data.get('sod')
    sc = data.get('sc')
    pot = data.get('pot')
    hemo = data.get('hemo')
    pcv = data.get('pcv')
    rbcc = data.get('rbcc')
    wbcc = data.get('wbcc')
    htn = data.get('htn')
    dm = data.get('dm')
    cad = data.get('cad')
    appet = data.get('appet')
    pe = data.get('pe')
    ane = data.get('ane')
    grf = data.get('grf')
    stage = data.get('stage')
    affected = data.get('affected')
    age = data.get('age')


    print("=====>")

    if algo == 'svc':
        svc_result = models.svc(bp, bp_limit, sg, al, rbc, su, pc, pcc, ba, bgr, bu, sod, sc,pot, hemo, pcv, rbcc, wbcc, htn, dm, cad, appet, pe, ane, grf, stage, affected, age)
        return f" {svc_result} "
    elif algo == 'rf':
        rf_result = models.rf(bp, bp_limit, sg, al, rbc, su, pc, pcc, ba, bgr, bu, sod, sc,pot, hemo, pcv, rbcc, wbcc, htn, dm, cad, appet, pe, ane, grf, stage, affected, age)
        return f" {rf_result} "
    elif algo == 'dt':
        dt_result = models.dt(bp, bp_limit, sg, al, rbc, su, pc, pcc, ba, bgr, bu, sod, sc, pot, hemo, pcv, rbcc, wbcc, htn, dm, cad, appet, pe, ane, grf, stage, affected, age)
        return f" {dt_result} "

@app.route("/image", methods=['POST'])
def upload_file():
    from main import mainf
    global value
    algo = request.form['algorithm']
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('success')
            result = mainf(filename,algo)
            return result

        




if __name__ == "__main__":
    app.run(debug=True)
