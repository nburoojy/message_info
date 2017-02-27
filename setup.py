from setuptools import setup

setup(
    name='message_info',
    packages=['message_info'],
    include_package_data=True,
    install_requires=[
        'flask',
        'lxml',
        'grequests'
    ],
    tests_require=[
        'pytest',
    ],
)
