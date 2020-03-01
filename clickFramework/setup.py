from setuptools import setup


setup(
    name='v',
    version='0.1',
    py_modules=['v'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        v=ventas:cli
    ''',
)