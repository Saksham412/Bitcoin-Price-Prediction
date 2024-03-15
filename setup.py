from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

# This function will be called when pip is installing the package.
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # As it is geting readed as line we are replacing the /n
        requirements=[req.replace("\n","") for req in requirements] 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='BitcoinPricePrediction',
version='0.0.1',
author='Saksham',
author_email='sakshamshinde412@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)