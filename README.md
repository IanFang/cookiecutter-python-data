cookiecutter-python-data
========================

An minimal template for Python data science packages.

Usage
-----

    pip install cookiecutter
    git clone https://github.com/IanFang/cookiecutter-python-data.git
    cookiecutter cookiecutter-python-data/

Update the classifiers in `setup.py` to fit the need. [Reference](https://pypi.python.org/pypi?:action=list_classifiers).

Fill out the README, and add a license to the project.

### Features

* **git integration**
    git repository generated with initial commit and git remote url setup

### Notes

* **README should use reStructuredText format**
    This is the format used by most Python tools, i.e. [Sphinx](http://sphinx-doc.org/).

* **Additional files (AUTHORS, CHANGELOG, etc) may be added**.

### Testing

* **Uses [pytest](http://pytest.org/latest/) as the test runner**
    Can be changed. pytest is a powerful test library and runner than the standard library's unittest.

* **tox as test automation tool**

### TODO

* global change
	- change index files to readme file

* data folder:
	- add instruction in the top level readme about suggestions on how to organize file
	- metadata should be version controlled but data file should not (change gitignore)

* more git automation in fabfile, create dev branch in hook also
