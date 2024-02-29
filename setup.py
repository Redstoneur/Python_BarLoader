from setuptools import setup

setup(name='BarLoader',
      version='1.0.0',
      description='A simple package to display the loading of a process in percentage',
      long_description=open('README.md').read(),
      url='https://github.com/Redstoneur/Python_BarLoader',
      author='Redstoneur',
      author_email='',
      license='MIT License',
      packages=['Bar_Loader'],
      keywords='BarLoader',
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.8',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: BarLoader'
      ],
      install_requires=[],
      include_package_data=True
      )
