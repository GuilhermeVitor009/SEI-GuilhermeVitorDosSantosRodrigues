import os

print(dir(os))
print(os.getcwd())
os.chdir(r'C:\\Users\pexim\Desktop\SEI-GuilhermeVitorDosSantosRodrigues\Semana04')

print(os.getcwd())
print(os.listdir())
#os.mkdir('Arquivos-Video')
#os.rename('module09.py', 'modulo09.py')
for dirpath, dirnames, filenames in os.walk(r'C:\\Users\pexim\Desktop\SEI-GuilhermeVitorDosSantosRodrigues\Semana04'):
    print('Current-Path:', dirpath)
    print('Directories:', dirnames)
    print('Files', filenames)