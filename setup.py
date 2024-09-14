# coding: utf-8

from setuptools import setup, find_packages

version = __import__('glo').get_version()

setup(
	name='glo',
	version=version,
	url='https://github.com/limoxi/glo.git',
	author='aix',
	author_email='asia-aixiang@163.com',
	long_description=open('README.md', encoding='utf-8').read(),
	long_description_content_type='text/markdown',
	packages=find_packages(),
	include_package_data=True,
	install_requires=['click'],
	python_requires='>=3.6',
	classifiers=[
        'Programming Language :: Python :: 3'
    ],
	entry_points='''
		[console_scripts]
		glo=glo.core.cli:cli
	''',
)