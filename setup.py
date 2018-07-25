from setuptools import setup, find_packages

setup(name='pipinstalltestingv1',
      version='0.1',
      description='pipinstalltesting',
      url='http://github.com/storborg/funniest',
      author='Nikunj',
      author_email='nikunjaggarwal08@gmail.com',
      license='Edge',
      packages=find_packages(exclude=['test', 'test.*']),
      install_requires=[
          'requests',
      ],
      zip_safe=False)
