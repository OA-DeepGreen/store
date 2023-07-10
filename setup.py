from setuptools import setup, find_packages

setup(
    name = 'store',
    version = '0.0.3',
    packages = find_packages(),
    install_requires = [
        "Flask==1.1.2",
        "Flask-Login==0.5.0",
        "Flask-WTF==0.14.3",
        "Werkzeug==1.0.1",
        "requests==2.25.1"
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
