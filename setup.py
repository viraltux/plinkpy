from setuptools import setup, find_packages

setup(name='plinkpy',
      version='1.90.1 beta',
      description='Simple python wrapper for plink',
      url='',
      author='Fran Urbano',
      author_email='francisco.urbano_garcia@novartis.com',
      license='GPL3',
      #packages=['plinkpy'],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False)
