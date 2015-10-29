from setuptools import setup, find_packages

setup(
    name = 'ijson',
    version = '2.3-celect',
    author = 'Ying-zong Huang',
    author_email = 'yingzong@celectengine.com',
    url = 'https://github.com/yingzong/ijson',
    license = 'BSD',
    description = 'Iterative JSON parser with a standard Python iterator interface',
    long_description = open('README.rst').read(),

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    packages = find_packages(),
)
