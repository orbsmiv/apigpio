from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    README = f.read()


setup(name='apigpio',
      version='0.0.1',
      description='asyncio-based python client for pigpiod',
      long_description=README,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers"

          "License :: OSI Approved :: Apache Software License",

          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3.4",

          "Topic :: System :: Hardware :: Hardware Drivers",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      author='Pierre Rust',
      author_email='pierre.rust@gmail.com',
      url='https://github.com/PierreRust/apigpio',

      keywords=['gpio', 'pigpio', 'asyncio', 'raspberry'],
      packages=find_packages()
      )
