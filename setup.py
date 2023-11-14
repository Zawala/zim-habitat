from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in zim_habitat/__init__.py
from zim_habitat import __version__ as version

setup(
	name="zim_habitat",
	version=version,
	description="find long term and short term accommodation for a visit.",
	author="durihub",
	author_email="technical@durihub.cozw",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
