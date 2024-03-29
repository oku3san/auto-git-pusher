from setuptools import setup, find_packages

setup(
    name='auto-git-pusher',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'auto-git-pusher = auto_git_pusher.main:auto_git_pusher',
        ],
    },
    install_requires=[
        'GitPython',
    ],
)
