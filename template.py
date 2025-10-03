import os 
from pathlib import  Path

PROJECT_NAME="ml_project"

files = [
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    'notebook/.gitkeep',
    f'src/{PROJECT_NAME}/__init__.py',
    f'src/{PROJECT_NAME}/utils/.gitkeep',
    f'src/{PROJECT_NAME}/constant/.gitkeep',
    f'src/{PROJECT_NAME}/pipeline/data/.gitkeep',
    f'src/{PROJECT_NAME}/pipeline/features/.gitkeep',
    f'src/{PROJECT_NAME}/pipeline/model/.gitkeep',
    'setup.py',
    'main.py',
    'dvc.yaml',
    'app.py',
    'README.md',
    '.gitignore',
    'template.py',
    'requirements.txt',
    "Dockerfile",
    '.dockerignore'
]

for file in files:
    file = Path(file)
    print(file)
    dirs,_=os.path.split(file)
    if dirs != '':
        
        os.makedirs(dirs,exist_ok=True)
    if not os.path.exists(file) or os.path.getsize(file)==0 :
        with open(file,'w') as f :
            pass