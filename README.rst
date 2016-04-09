AutoEnum - Auto-numbered Enumerations
=====================================

.. image:: https://travis-ci.org/johnthagen/autoenum.svg
    :target: https://travis-ci.org/johnthagen/autoenum

.. image:: https://codeclimate.com/github/johnthagen/autoenum/badges/gpa.svg
   :target: https://codeclimate.com/github/johnthagen/autoenum

.. image:: https://codeclimate.com/github/johnthagen/autoenum/badges/issue_count.svg
   :target: https://codeclimate.com/github/johnthagen/autoenum

.. image:: https://codecov.io/github/johnthagen/autoenum/coverage.svg
    :target: https://codecov.io/github/johnthagen/autoenum

.. image:: https://img.shields.io/pypi/v/autoenum.svg
    :target: https://pypi.python.org/pypi/autoenum

.. image:: https://img.shields.io/pypi/status/autoenum.svg
    :target: https://pypi.python.org/pypi/autoenum

.. image:: https://img.shields.io/pypi/pyversions/autoenum.svg
    :target: https://pypi.python.org/pypi/autoenum/

.. image:: https://img.shields.io/pypi/dm/autoenum.svg
    :target: https://pypi.python.org/pypi/autoenum/

Auto-numbered enumeration based upon the
`Python 3.4+ enum documentation <https://docs.python.org/3/library/enum.html#autonumber>`_.

Installation
------------

You can install, upgrade, and uninstall ``autoenum`` with these commands:

.. code:: shell-session

    $ pip install autoenum
    $ pip install --upgrade autoenum
    $ pip uninstall autoenum

Usage
-----
``AutoEnum``'s are useful for distinguishing between ``Enum``'s whose members have meaningful
values and those that are abstract.  For abstract enumerations, manually assigning values (such
as an incrementing integer) can be misleading and also a maintenance problem for ``Enum``'s with
many members.

Declare an ``AutoEnum`` just like an ``Enum`` except use black ``tuple``s for each of the
member values.

.. code:: python

    import autoenum


    class Color(autoenum.AutoEnum):
        red = ()
        blue = ()
        green = ()

Then access members and their attributes  just like an ``Enum``.

.. code:: python

    >>> member = Color.red
    >>> member.name
    'red'
    >>> member.value
    1

Releases
--------

1.0.0 - 2016-04-09
^^^^^^^^^^^^^^^^^^

First release.
