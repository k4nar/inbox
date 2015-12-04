from setuptools import setup, find_packages

import inbox

requirements = [
    "click",
    "github3.py",
]

setup(
    name="inbox",
    version=inbox.__version__,
    url='TODO',
    description=inbox.__doc__,
    author=inbox.__author__,
    license=inbox.__license__,
    long_description="TODO",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'inbox = inbox.__main__:inbox'
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Customer Service",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet",
        "Topic :: Office/Business",
        "Topic :: Utilities",
    ],
    keywords='inbox github notifications',
)
