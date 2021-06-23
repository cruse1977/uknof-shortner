# UKNOF URL Shortner

## Overview

This app provides a simple URL shortening service, other similar projects already exist, but did not meet all of our requirements.

This version is an update of the original Nat Morris code, 99.99% of this remains, changes are:

* update to python3
* add rudimentary (and it so, is) delete function
* add pagination

original readme below....

The below is out of date, need update this - see: requirements.txt ^CR

It is built using Python:

* Python3
* Flask 0.10.1
* Flask-Login 0.2.11
* sqlite3
* passlib
* ipaddr
* rfc3987
* unittest

HTML / JS / CSS:

* Bootstrap 3
* Bootbox.js 4.3.0
* Bootstrap-table 1.4.0
* BootstrapValidator 0.5.3
* jQuery 1.10.2

## Production deployment

TODO

## Development

### Setting up your environment

Clone the repo, then install the required Python modules:

```
$ git clone git@github.com:cruse1977/uknof-shortner.git
$ cd shortner
$ sudo pip install -r requirements.txt
```

Create an empty database:

```
python db
```

Running the local web server:

```
$ ./shortner.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader

```

Point your web browser at http://127.0.0.1:5000
