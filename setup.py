from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    req=[]
    with open('requirements.txt') as obj:
        req=obj.readlines()
        req=[r.replace("\n","") for r in req]
        
        if HYPHEN_E_DOT in req:
            req.remove(HYPHEN_E_DOT)
    return req


setup(
    name='MLPROJECT',
    version='0.0.1',
    author='Kumar Ashutosh',
    author_email='kumarashutoshbtech2023@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)