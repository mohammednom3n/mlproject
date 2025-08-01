from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(path:str)-> list[str]:
    '''
        this function will return the list of requirements
    '''

    requirements = []
    with open(path) as obj:
        requirements=obj.readlines()
        requirements= [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name= 'mlproject',
    version= '0.0.1',
    author='Noman',
    author_email='mohammednom3n@gmial.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')

)