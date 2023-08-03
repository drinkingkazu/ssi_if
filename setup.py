from setuptools import setup, find_packages

setup(
    name='iftools',
    version='0.1',
    author='drinkingkazu',
    description='utils for IF projects',
    packages=find_packages(),
    url='https://github.com/drinkingkazu/ssi_if',
    scripts=['bin/download_if_dataset.py'],
    install_requires=['gdown','fire','h5py','torch','torch_geometric','plotly','matplotlib'],
)
