from setuptools import find_packages , setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_name : str)->List[str]:
    requirements = []
    with open(file_name,"r") as f :
        requirements =  f.readlines()
        if HYPEN_E_DOT in requirements :
            requirements.remove(HYPEN_E_DOT)
        requirements = [req.replace("/n","") for req in requirements]
        return requirements

setup(
    name = "DiamondPricePrediction",
    version = "0.0.1",
    author = "Bhavesh",
    author_email="aswanib133@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")

)
