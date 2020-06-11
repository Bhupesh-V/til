# Publishing a Package on PyPI
<!-- 31 Oct 2019 -->
I just published my first package on pypi 😍
I used the following steps to do it :

1. Put your python files/classes inside the folder `package-name`.Also make sure your main class file has the same name `package-name`.

2. Add the `__init__.py` file in the same folder. Use the init file like this.
```python
from coderunner.coderunner import Run
```

3. Now make a file `setup.py` inside the root of your github folder.
Add the following contents in it:
```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plagcheck",
    version="0.1",
    author="Bhupesh Varshney",
    author_email="varshneybhupesh@gmail.com",
    description="A Powerful Moss results scrapper",
    keywords='mosspy moss plagiarism cheat',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeclassroom/PlagCheck",
    project_urls={
        "Documentation": "https://github.com/codeclassroom/PlagCheck/blob/master/docs/docs.md",
        "Source Code": "https://github.com/codeclassroom/PlagCheck",
        "Funding": "https://www.patreon.com/bePatron?u=18082750",
        "Say Thanks!": "https://github.com/codeclassroom/PlagCheck/issues/new?assignees=&labels=&template=---say-thank-you.md&title=",
    },
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'mosspy',
        'beautifulsoup4',
        'lxml',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Topic :: Software Development :: Build Tools',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```

4. Now make a file `setup.cfg`. 
It is used for displaying project description on PyPi.
```txt
[metadata]
description-file = README.md
```

5. Install the followig libraries.
```bash
pip3 install setuptools wheel twine
```

6. Run the following command.
```bash
python3 setup.py sdist bdist_wheel
```

7. Finally upload it to PyPi.
```bash
twine upload dist/*
```
This will prompt for your PyPi username and password.

## Resources
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [How to upload your python package to PyPi](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)
