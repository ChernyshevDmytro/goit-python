from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.0.1',
    entry_points = {
          'console_scripts' : ['clean-folder=clean_folder.clean:clean'],
          },
    description='Sorting trash into cathegories',
    url='https://github.com/Shakal1985/Shakal1985/tree/main/clean%20folder',
    author='Dmytro Chernyshev',
    author_email='shakal1985@i.ua',
    license='MIT',
    packages=find_packages(),
)