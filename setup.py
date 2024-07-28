from setuptools import setup, find_packages

setup(
    name='print_r',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description='A simple module to print iterable data with colors',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/print_r',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'colorama>=0.4.4'
    ],
)
