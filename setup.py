from setuptools import setup, find_packages

setup(
    name='preaudio',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'librosa'
    ],
    author='Nirvik Goswami',
    author_email='nirvikgoswami689@gmail.com',
    description='A small audio visualization library built from Jupyter Notebook code.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Nirvik34/preaudio',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
