import os, shutil

file_name = 'appshields.txt'

working_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(os.path.abspath(working_dir))

print('──────────────────────────────────────────────────────────')
print('Q2. appshields.txt 파일에 회사 주소를 입력하고')
print('    해당 파일을 상위 디렉토리로 이동 및 복사')
print('──────────────────────────────────────────────────────────')
print('회사 주소를 입력하세요.')
file_content = input('>> ')

with open(file_name, 'w') as file:
    file.writelines(file_content)
print('')
print('appshields.txt 파일이 생성되었습니다.')
print('- 현재 디렉터리:', working_dir)
for i in  os.listdir():
    print(' - ', i)
    
shutil.copy(file_name,  os.path.join("../", file_name))
print('')
print('appshields.txt 파일을 상위 디렉토리로 복사하였습니다.')
print('- 상위 디렉터리:', parent_dir)
for i in  os.listdir(parent_dir):
    print(' - ', i)