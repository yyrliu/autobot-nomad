from setuptools import setup, find_packages

setup(
    name='nomad_perovskite_schema',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A schema for Perovskite film synthesis processes using NOMAD.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Add your project dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)