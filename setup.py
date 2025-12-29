from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requires(file_path:str)->list[str]:
    requires=[]
    with open(file_path) as f:
        requires = f.readlines()
    requires = [req.replace("\n", "") for req in requires]
    if HYPEN_E_DOT in requires:
        requires.remove(HYPEN_E_DOT)
    
    return requires


setup(    
    name="my_package",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requires("requirement.txt"),
    author="Pabitra",
    author_email="pm.pabitra.mondal.2003@gmail.com",
    
)