"""Setup"""
from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

with open('README') as f:
    readme = f.read()

with open('requirements.text') as f:
    requires = list(f.read().splitlines())

setup(name='Comm Tool',
      version='0.1',
      long_description=readme,
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: MacOS X',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 3.7',
                   'Topic :: Scientific/Engineering :: Information Analysis'],
       url='https://github.com/johnnymac0515/Commodity-Project',
       author='John Macnamara',
       author_email= 'john.macnamara.dev@gmail.com',
       license=license,
       packages=find_packages(),
       install_requires=requires,
       include_package_data=True,
                   )
       