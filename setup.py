from setuptools import setup, find_packages

setup(
    name='auto_git_pusher',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'auto_git_pusher = main:auto_git_pusher',
        ],
    },
)
