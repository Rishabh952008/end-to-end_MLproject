from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        for req in requirements:
            req.replace("\n","")
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements        

setup(
    name="End_to_EndMLproject",
    version="0.0.1",
    author="Rishabh Agrawal",
    author_email="rishabh16048@gmail.com",
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
    
)