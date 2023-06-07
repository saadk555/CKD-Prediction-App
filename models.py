import joblib
import os

a  =  os.getcwd()
print(a)
# Load the saved models
svc_model = joblib.load("./models/support_vector_classifier.pkl")
random_forest_model = joblib.load("./models/random_forest_classifier.pkl")
decision_tree_model = joblib.load("./models/decision_tree_classifier.pkl")

'''mo
bp=1
bp_limit=1
sg=1
al=1
rbc=1
su=1
pc=1
pcc=1
ba=1
bgr=1
bu=1
sod=1
sc=1
pot=1
hemo=1
pcv=1
rbcc=1
wbcc=1
htn=1
dm=1
cad=1
appet=1
pe=1
ane=1
grf=1
stage=1
affected=1
age=1
'''

def svc(bp,bp_limit,sg,al,rbc,su,pc,pcc,ba,bgr,bu,sod,sc,pot,hemo,pcv,rbcc,wbcc,htn,dm,cad,appet,pe,ane,grf,stage,affected,age):
    input = [[bp,bp_limit,sg,al,rbc,su,pc,pcc,ba,bgr,bu,sod,sc,pot,hemo,pcv,rbcc,wbcc,htn,dm,cad,appet,pe,ane,grf,stage,affected,age]]
    output = svc_model.predict(input)
    final_output=int(output)
    print(output)
    return final_output



def rf(bp,bp_limit,sg,al,rbc,su,pc,pcc,ba,bgr,bu,sod,sc,pot,hemo,pcv,rbcc,wbcc,htn,dm,cad,appet,pe,ane,grf,stage,affected,age):
    input = [[bp,bp_limit,sg,al,rbc,su,pc,pcc,ba,bgr,bu,sod,sc,pot,hemo,pcv,rbcc,wbcc,htn,dm,cad,appet,pe,ane,grf,stage,affected,age]]
    output = random_forest_model.predict(input)
    final_output=int(output)
    print(output)
    return final_output

def dt(bp,bp_limit,sg,al,rbc,su,pc,pcc,ba,bgr,bu,sod,sc,pot,hemo,pcv,rbcc,wbcc,htn,dm,cad,appet,pe,ane,grf,stage,affected,age):
    input = [[bp,bp_limit,sg,al,rbc,su,pc,pcc,ba,bgr,bu,sod,sc,pot,hemo,pcv,rbcc,wbcc,htn,dm,cad,appet,pe,ane,grf,stage,affected,age]]
    output = decision_tree_model.predict(input)
    final_output=int(output)
    print(output)
    return final_output


