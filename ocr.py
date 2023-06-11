import platform
from pathlib import Path
from tempfile import TemporaryDirectory
from flask import jsonify
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import re
import requests




if platform.system() == "Windows":
	pytesseract.pytesseract.tesseract_cmd = (r"D:\\Tesseract-OCR\\tesseract.exe")
 

pe_path = Path(r"C:\\Program Files\\poppler-0.68.0\bin")
		

def main(PDF_file,algo):
	bp=''
	bp_limit=''
	sg=''
	al=''
	rbc=''
	su=''
	pc=''
	pcc=''
	ba=''
	bgr=''
	bu=''
	sod=''
	sc=''
	pot=''
	hemo=''
	pcv=''
	rbcc=''
	wbcc=''
	htn=''
	dm=''
	cad=''
	appet=''
	pe=''
	ane=''
	grf=''
	stage=''
	affected=''
	age=''

	image_file_list = []
	final_text = ""

	if platform.system() == "Windows":
		pdf_pages = convert_from_path(
			PDF_file, 500, poppler_path=pe_path
		)
	else:
		pdf_pages = convert_from_path(PDF_file, 500)


	for page_enumeration, page in enumerate(pdf_pages, start=1):
		filename = f"./{page_enumeration}.jpg"
		page.save(filename, "JPEG")
		image_file_list.append(filename)

#change this one
	for image_file in image_file_list:
		text = str(((pytesseract.image_to_string(Image.open(image_file)))))
		#text = text.replace("-\n", "")
		final_text += text
		if bp=='':
			print('true')
			bp+=str(re.search(r'BP: (.*)\n',final_text).group(1)).replace('O', '0')
			bp_limit+=str(re.search(r'BP_ LIMIT: (.*)\n',final_text).group(1)).replace('O', '0')
			sg+=str(re.search(r'OG: (.*)\n',final_text).group(1)).replace('O', '0')
			al+=str(re.search(r'AL: (.*)\n',final_text).group(1)).replace('O', '0').replace('2', '≥')
			rbc+=str(re.search(r'RBC: (.*)\n',final_text).group(1)).replace('O', '0')
			su+=str(re.search(r'SU: (.*)\n',final_text).group(1)).replace('O', '0')
			pc+=str(re.search(r'PC: (.*)\n',final_text).group(1)).replace('O', '0')
			pcc+=str(re.search(r'PCC: (.*)\n',final_text).group(1)).replace('O', '0')
			ba+=str(re.search(r'BA: (.*)\n',final_text).group(1)).replace('O', '0')
			bgr+=str(re.search(r'BGR: (.*)\n',final_text).group(1)).replace('O', '0')
			bu+=str(re.search(r'BU: (.*)\n',final_text).group(1)).replace('O', '0')
			sod+=str(re.search(r'SOD: (.*)\n',final_text).group(1)).replace('O', '0')
			sc+=str(re.search(r'SC: (.*)\n',final_text).group(1)).replace('O', '0')
			pot+=str(re.search(r'POT: (.*)\n',final_text).group(1)).replace('O', '0')
			hemo+=str(re.search(r'HEMO: (.*)\n',final_text).group(1)).replace('O', '0')
			pcv+=str(re.search(r'PCV: (.*)\n',final_text).group(1)).replace('O', '0')
			rbcc+=str(re.search(r'RBCC: (.*)\n',final_text).group(1)).replace('O', '0')
		elif bp=='1':
			wbcc=str(re.search(r'WBCC: (.*)\n',final_text).group(1)).replace('O', '0')
			htn=str(re.search(r'HTN: (.*)\n',final_text).group(1)).replace('O', '0')
			dm=str(re.search(r'DM: (.*)\n',final_text).group(1)).replace('O', '0')
			cad=str(re.search(r'CAD: (.*)\n',final_text).group(1)).replace('O', '0')
			appet=str(re.search(r'APPET: (.*)\n',final_text).group(1)).replace('O', '0')
			pe=str(re.search(r'PE: (.*)\n',final_text).group(1)).replace('O', '0')
			ane=str(re.search(r'ANE: (.*)\n',final_text).group(1)).replace('O', '0')
			grf=str(re.search(r'GRF: (.*)\n',final_text).group(1)).replace('O', '0')
			stage=str(re.search(r'STAGE: (.*)\n',final_text).group(1)).replace('$', 's')
			affected=str(re.search(r'AFFECTED: (.*)\n',final_text).group(1)).replace('O', '0')
			age=str(re.search(r'^AGE: (.*)\n',final_text,flags=re.MULTILINE).group(1)).replace('/', '7')
		
	
	
	url = 'http://127.0.0.1:5000'
	headers = {"Content-Type": "application/json"}
	payload = {
        "algorithm": algo,
        "bp": bp,
        "bp_limit": bp_limit,
        "sg": sg,
        "al": al,
        "rbc": rbc,
        "su": su,
        "pc": pc,
        "pcc": pcc,
        "ba": ba,
        "bgr": bgr,
        "bu": bu,
        "sod": sod,
        "sc": sc,
        "pot": pot,
        "hemo": hemo,
        "pcv": pcv,
        "rbcc": rbcc,
        "wbcc": wbcc,
        "htn": htn,
        "dm": dm,
        "cad": cad,
        "appet": appet,
        "pe": pe,
        "ane": ane,
        "grf": grf,
        "stage": stage,
        "affected": affected,
        "age": age
    }
	response = requests.post(url, json=payload, headers=headers)
	print(response.text)
	return response.text



if __name__ == "__main__":
	main()
