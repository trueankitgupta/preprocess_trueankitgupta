import setuptools

with open('README.md','r') as file:
	long_description=file.read()

setuptools.setup(
	name='preprocess_trueankitgupta', # this should be uniqure
	version='0,0,1',
	author='Ankit Gupta',
	author_email='trueankitgupta@gmail.com',
	description='This is preprocessing',
	long_description=long_description,
	long_description_content_type='text/markdown',
	package=setuptools.find_packages(),
	classifiers=[
	'Programming Language :: 3',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=')