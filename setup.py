from setuptools import setup, find_packages

def get_requirements(file_path:str)->list:
    """"This function will return the list of requirements
    mentioned in the requirements.txt file
    """
    with open(file_path) as requirement_file:
        requirements = requirement_file.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
    if '-e .' in requirements:
        requirements.remove('-e .')
    return requirements

print(get_requirements('requirements.txt'))
setup(
    name="StudentPerformance",
    version="1.0.0",
    author="Bishal",
    author_email="bisalpandey9@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)