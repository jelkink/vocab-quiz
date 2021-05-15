from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='vocab-quiz',
    version='0.1.0',
    description='Python for Mac vocabulary quiz program',
    long_description=readme,
    author='Jos Elkink',
    author_email='jelkink@gmail.com',
    url='https://github.com/jelkink/vocab-quiz',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
