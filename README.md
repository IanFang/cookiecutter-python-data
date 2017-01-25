cookiecutter-python-data
========================

An minimal template for Python data science packages.

Usage
-----

    pip install cookiecutter
    git clone https://github.com/IanFang/cookiecutter-python-data.git
    cookiecutter cookiecutter-python-data/

Update the classifiers in `{{ cookiecutter.name }}/setup.py` to fit the need [Ref](https://pypi.python.org/pypi?:action=list_classifiers).

Fill out the README, and add a license to the project.

### README and other files

* **README should use reStructuredText format**
  This is the format used by most Python tools, i.e. [Sphinx](http://sphinx-doc.org/).
* **Additional files (AUTHORS, CHANGELOG, etc) may be added**.

### Testing

* **Uses [pytest](http://pytest.org/latest/) as the test runner**
  Can be changed. pytest is a powerful test library and runner than the standard library's unittest.
* **tox as test automation tool**
