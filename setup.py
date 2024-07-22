from setuptools import setup,find_packages
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        This function will return the list of requirements
    '''
    requriments=[]
    with open(file_path) as file:
        
        requriments=file.readlines()
        requriments=[req.replace('\n','') for req in requriments]

        if HYPHEN_E_DOT in requriments:
            requriments.remove(HYPHEN_E_DOT)
    return requriments


setup(
    name='mlproject',
    version='0.0.1',
    author='Luvya',
    author_email='luvyagoswami@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)