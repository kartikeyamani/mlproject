from setuptools import setup, find_packages
from typing import List
def get_requirements(filepath:str)-> List[str]:
    '''
    Here I'm mentioning how to extract packages required for the project
    from requirements.txt
    '''
    with open(filepath) as f:
        rerquirements=f.readlines()
        rerquirements=[req.replace("\n","") for req in rerquirements]
        if "-e ." in rerquirements:
            rerquirements.remove("-e .")

        return rerquirements


setup(
    name="simple ml project",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    author="Karthikeya Gangisetty",
    author_email="kartikeyamani0724@gmail.com"
)