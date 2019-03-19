from setuptools import setup, find_packages

setup(
    name='AnalyseHackathon',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Analyse Hackathon python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Mangethe/AnalyseHackathon',
    author='Nqobile Shabangu',
    author_email='Nqobile.ZwaneShabangu@gmail.com'
)
