[![PyPI version](https://badge.fury.io/py/justin_furuness.svg)](https://badge.fury.io/py/justin_furuness)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/justin_furuness)](https://pypi.org/project/justin_furuness/)
![Tests](https://github.com/jfuruness/justin_furuness/actions/workflows/tests.yml/badge.svg)
![Linux](https://img.shields.io/badge/os-Linux-blue.svg)
![macOS Intel](https://img.shields.io/badge/os-macOS_Intel-lightgrey.svg)
![macOS ARM](https://img.shields.io/badge/os-macOS_ARM-lightgrey.svg)

# justin\_furuness


### If you like the repo, it would be awesome if you could add a star to it! It really helps out the visibility. Also for any questions at all we'd love to hear from you at jfuruness@gmail.com

* [Description](#package-description)
* [Usage](#usage)
* [Installation](#installation)
* [Development/Contributing](#developmentcontributing)
* [License](#license)

## Package Description

Prints my name, and it my first package!

## Usage
* [justin\_furuness](#justin\_furuness)

from a script:

```python
from justin_furuness import Justin

Justin().print_name()
```

From the command lind:

```bash
justin_furuness
```

## Installation
* [justin\_furuness](#justin\_furuness)

Install python and pip if you have not already.

Then run:

```bash
pip3 install pip --upgrade
pip3 install wheel
```

For production:

```bash
pip3 install justin_furuness
```

This will install the package and all of it's python dependencies.

If you want to install the project for development:
```bash
git clone https://github.com/jfuruness/justin_furuness.git
cd justin_furuness
pip3 install -e .[dev]
```

To test the development package: [Testing](#testing)


## Development/Contributing
* [justin\_furuness](#justin\_furuness)

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Test it
5. Run tox
6. Commit your changes: `git commit -am 'Add some feature'`
7. Push to the branch: `git push origin my-new-feature`
8. Ensure github actions are passing tests
9. Email me at jfuruness@gmail.com if it's been a while and I haven't seen it

## License
* [justin\_furuness](#justin\_furuness)

BSD License (see license file)
