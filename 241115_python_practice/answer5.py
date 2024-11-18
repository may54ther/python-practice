import json

print('──────────────────────────────────────────────────────────')
print('Q5. test.json 파일 인코딩 및 디코딩')
print('──────────────────────────────────────────────────────────')

with open('test.json', 'r') as file:
	encoded_json = json.load(file)
	decoded_json = json.dumps(encoded_json, ensure_ascii=False, indent="\t")
	print("- 인코딩 결과 = ", encoded_json)
	print("- 디코딩 결과 = ", decoded_json)