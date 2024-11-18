import os, subprocess


file_name = 'appshields.txt'

working_dir = os.path.dirname(__file__)

print('──────────────────────────────────────────────────────────')
print('Q4. appshields.txt 파일 권한 설정을 변경하고')
print('    설정 앱이 실행되도록 설정')
print('──────────────────────────────────────────────────────────')
print('- appshield.txt 권한')
file_mode = oct(os.stat(file_name).st_mode)[-3:]
if os.access(file_name, os.R_OK) is True:
    print('appshield.txt 파일의 권한은', file_mode, '입니다.')
else:
    os.chmod(file_name, 0o700)
    print('appshield.txt 파일의 권한을', file_mode, '→ 700 으로 변경하였습니다.')

print('')
print('- 설정(gnome-control-center) 실행')
subprocess.run('gnome-control-center')

