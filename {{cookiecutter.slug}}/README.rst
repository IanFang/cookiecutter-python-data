{{ cookiecutter.name }}
{{ cookiecutter.name|count * "=" }}


{{ cookiecutter.description }}

Usage
-----

Installation
------------
poetry install

Requirements
------------
python 3.6+
poetry

License
-------

Directory
---------

- **src** Source codes
- **data/raw:** Immutable original datasets
- **data/processed:** Processed datasets
- **data/interim:** Temporary and interim datasets
- **docs:** Package documentation (Sphinx)
- **tests** Unit tests
- **reports** Scientific reports
- **references** Reference documents

Authors
-------

`{{ cookiecutter.name }}` was written by `{{ cookiecutter.author}} <{{ cookiecutter.email }}>`_.
