from setuptools import find_packages
from setuptools import setup

# with open('requirements.txt') as f:
#     content = f.readlines()
# requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='sizer',
      version="1.0.0",
      description="automation tool for checking file and directory size",
      packages=["sizer"],
      #install_requires=requirements,
      #test_suite= 'tests',
      # include_package_data: to install data from MANIFEST.in
      #include_package_data=True,
      scripts=['scripts/sizer', "scripts/sizel"],
      zip_safe=False)
