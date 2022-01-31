from setuptools import setup, find_packages

setup(
    name="hikvision-configure",
    version="0.0.1",
    url="https://github.com/synweap15/hikvision-configure",
    author="qb60",
    description="Hikvision/HiWatch camera configuring script",
    packages=find_packages(),
    install_requires=[
        "certifi>=2020.11.8",
        "chardet==3.0.4",
        "idna==2.10",
        "pycryptodomex>=3.9.9",
        "requests>=2.25.0",
        "urllib3>=1.26.2",
    ],
)
