from setuptools import find_packages, setup
from typing import List

HYPHEN_DOT_E = "-e ."

def get_requirements(file_path: str)->List[str]:
    '''
    Docstring for get_requirements
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: List[str]
    '''
    requirements = []

    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)
    return requirements

setup(
    name="ML Project 1",
    version="0.0.1",
    author="Divyanshu",
    author_email="divyanshusoni.iitr@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)

