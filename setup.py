import pip
from setuptools import setup
from pip.req import parse_requirements
from awsclpy.version import VERSION

install_reqs = parse_requirements("./requirements.txt",
                                  session=pip.download.PipSession())
reqs = [str(ir.req) for ir in install_reqs]

setup(name='awsclpy',
      version=VERSION,
      description='Chain AWSCLI commands.',
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
      install_requires=reqs,
      zip_safe=False)
