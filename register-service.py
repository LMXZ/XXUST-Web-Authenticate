import os, sys, shutil

currentPath = os.path.dirname(os.path.abspath(__file__))
servicePath = f'{currentPath}/service'
pythonPath = sys.executable

def escapeTemplate(dir: str, templateFile: str, **kwargs):
    with open(f'{dir}/template-{templateFile}', 'r') as file:
        template = file.read()

    with open(f'{dir}/{templateFile}', 'w') as file:
        file.write(template.format(**kwargs))

escapeTemplate(servicePath, 'start-service.sh', pythonPath=pythonPath, currentPath=currentPath)
escapeTemplate(servicePath, 'auto-auth.service', servicePath=servicePath)

try:
    os.system(f'sudo systemctl stop auto-auth.service')
except:
    pass

try:
    print('registering')
    os.system(f'chmod 755 {servicePath}/start-service.sh')
    os.system(f'sudo cp "{servicePath}/auto-auth.service" "/etc/systemd/system/"')
    os.system(f'sudo systemctl enable auto-auth.service')
    os.system(f'sudo systemctl daemon-reload')
except:
    print('register failed!')
