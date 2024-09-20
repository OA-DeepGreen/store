from setuptools import setup, find_packages

setup(
    name = 'store',
    version = '1.1',
    packages = find_packages(),
    install_requires = [
        "Flask~=3.0",
        "Flask-Login~=0.6",
        "Flask-WTF~=1.2",
        "Werkzeug~=3.0",
        "requests~=2.32"
    ],
    url = 'http://cottagelabs.com/',
    author = 'Cottage Labs',
    author_email = 'us@cottagelabs.com',
    description = 'Provision of a web API wrapper for storage system',
    license = 'MIT',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Copyheart',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
