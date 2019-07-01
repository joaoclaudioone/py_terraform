from setuptools import setup

setup(
    name='pyform',
    version='0.1',
    py_modules=['pyform'],
    install_requires=[
        'python-terraform',
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pyform=pyform:cli
    ''',
)