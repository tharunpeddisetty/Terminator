#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terminator-pkg-tharunpeddisetty5", # Replace with your own username
    version="0.0.1",
    author="Tharun Peddisetty",
    author_email="tharunpeddisetty5@gmail.com",
    description="This package implements multiple linear and logistic regressions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tharunpeddisetty/Terminator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


# In[ ]:





# In[ ]:



