#!/usr/bin/env python

from distutils.core import setup

setup(name='StepperControl',
      version='1.0',
      description='Python library for using stepper motors with the Raspberry Pi',
      author='Stefan Biermann',
      author_email='sb@ems-solutions.com',
      url='https://github.com/sbiermann/steppercontrol',
      license = 'GPL v2',
      long_description=open('README.md').read(),
      packages=['StepperControl'],
)