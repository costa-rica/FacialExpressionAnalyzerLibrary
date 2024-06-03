from setuptools import setup

setup (
    name="fea-modules",
    version = "0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description = "fea stands for Facial Expression Analyzer. These are the core packages for this app.",
    packages=['fea_config','fea_models'],
    python_requires=">=3.10",
    )