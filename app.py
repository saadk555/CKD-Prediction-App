from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello():
    import models
    data = request.get_json()
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

    models.svc()


    return ...


if __name__ == "__main__":
    app.run()
