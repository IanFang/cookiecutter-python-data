import setuptools

setuptools.setup(
    name="{{ cookiecutter.name }}",
    version="{{ cookiecutter.version }}",
    url="{{ cookiecutter.repo_url }}",

    author="{{ cookiecutter.author}}",
    author_email="{{ cookiecutter.email}}",

    description="{{ cookiecutter.description }}",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
