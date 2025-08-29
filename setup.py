from setuptools import find_packages,setup 
from typing import List 

''' The setup.py file is an essential part of packaging and distributing python projects. it is used by setuptools to define the configuration

of your project,such as its metadata , dependencias and more
  '''

def get_requirements()->List[str]:
    '''This function will return list of requirements'''
    requirement_lst:List[str]=[]
    try: 
        with open('requirements.txt','r') as file: 
            lines  = file.readlines()
            for line in lines: 
                requirement =  line.strip()
                ## ignore the empty lines and -e 
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("Requirements.txt not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version='0.0.1',
    author="Dinesh Jangir",
    author_email="dineshjangir887766@gmail.com",
    packages=find_packages(),
    install_requares = get_requirements()

)