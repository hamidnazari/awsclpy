import pip
from setuptools import setup

setup(name='awsclpy',
      version='0.3.1',
      description='Chain AWSCLI commands in Python.',
      long_description='Run AWSCLI commands and use their outputs in next ' +
      'commands.',
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Development Status :: 4 - Beta',
      ],
      keywords=[
          'awsclpy',
          'awscli',
          'aws',
          'amazon web services',
          'command line interface',
      ],
      author='Hamid Nazari',
      author_email='hn@linux.com',
      maintainer='Hamid Nazari',
      maintainer_email='hn@linux.com',
      url='http://github.com/hamidnazari/awsclpy',
      license='MIT',
      packages=['awsclpy'],
      install_requires=[
        'awscli==1.7.36',
        'six==1.9.0'
      ],
      zip_safe=False)
