import requests
url='http://127.0.0.1:5000'
payload = {
  "bp": 1,
  "bp_limit": 2,
  "sg": "1.009 - 1.011",
  "al": "≥1.04",
  "rbc": 0,
  "su": "< 0",
  "pc": 1,
  "pcc": 1,
  "ba": 1,
  "bgr": "< 112",
  "bu": "< 48.1",
  "sod": "123 - 128",
  "sc": "< 3.65",
  "pot": "< 7.31",
  "hemo": "7.4 - 8.7",
  "pcv": "21.8 - 25.7",
  "rbcc": "3.87 - 4.46",
  "wbcc": "12120 - 14500",
  "htn": 0,
  "dm": 0,
  "cad": 0,
  "appet": 0,
  "pe": 0,
  "ane": 1,
  "grf": "51.7832 - 76.949",
  "stage": "s3",
  "affected": 1,
  "age": "20 - 27"
}


headers = {"Content-Type":"application/json"}

response = requests.post(url,json=payload, headers=headers)

print(response.text)