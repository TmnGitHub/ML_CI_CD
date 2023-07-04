# Find all the packages automitically for intire ML application
from setuptools import find_packages,setup
from typing import List

const = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    THis function will return the list of requirements
    """

    requirements = []

    with open(file_path) as file_obj:

        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if const in requirements:
            requirements.remove(const)

    #with open('requirements.txt') as f:
    #    requirements = f.readlines()

    return requirements


setup(
    name='ML_CICD_pipeline',
    version='0.0.1',
    author='Taman',
    author_email='tamanupadhaya@gmail.com',
    packages=find_packages(), # how many folder there are __init__.py and try to build it can you can import anywhere
    #install_require=['pandas','numpy','seaborn'] #100 packages in project and not able to write here
    install_require=get_requirements('requirements.txt')
)
