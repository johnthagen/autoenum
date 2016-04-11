AutoEnum - Auto-numbered Enumerations
=====================================

.. image:: https://travis-ci.org/johnthagen/autoenum.svg
    :target: https://travis-ci.org/johnthagen/autoenum/

.. image:: https://codeclimate.com/github/johnthagen/autoenum/badges/gpa.svg
   :target: https://codeclimate.com/github/johnthagen/autoenum/

.. image:: https://codeclimate.com/github/johnthagen/autoenum/badges/issue_count.svg
   :target: https://codeclimate.com/github/johnthagen/autoenum/

.. image:: https://codecov.io/github/johnthagen/autoenum/coverage.svg
    :target: https://codecov.io/github/johnthagen/autoenum/

.. image:: https://img.shields.io/pypi/v/autoenum.svg
    :target: https://pypi.python.org/pypi/autoenum/

.. image:: https://img.shields.io/pypi/status/autoenum.svg
    :target: https://pypi.python.org/pypi/autoenum/

.. image:: https://img.shields.io/pypi/pyversions/autoenum.svg
    :target: https://pypi.python.org/pypi/autoenum/

.. image:: https://img.shields.io/pypi/dm/autoenum.svg
    :target: https://pypi.python.org/pypi/autoenum/

.. note::

    This package was removed from PyPI because it was found to be a duplicate of
     `aenum.AutoNumberEnum <https://pypi.python.org/pypi/aenum>`__ which existed first
     and will likely be better supported.

Auto-numbered enumeration based upon the
`Python 3.4+ enum documentation <https://docs.python.org/3/library/enum.html#autonumber>`__.

Installation
------------

You can install, upgrade, and uninstall ``autoenum`` with these commands:

.. code:: shell-session

    $ pip install autoenum
    $ pip install --upgrade autoenum
    $ pip uninstall autoenum

On Python 3.4+, the standard library
`enum <https://docs.python.org/3/library/enum.html>`__ is used, on older versions
`enum34 <https://pypi.python.org/pypi/enum34>`__ is installed as a dependency.

Usage
-----
``AutoEnum``'s are useful for distinguishing between ``Enum``'s whose members have meaningful
values and those that are abstract.  For abstract enumerations, *manually* assigning values (such
as an incrementing integer) can be misunderstood and can also become a maintenance problem for
``Enum``'s with many members.

Declare an ``AutoEnum`` just like an
`Enum <https://docs.python.org/3/library/enum.html#creating-an-enum>`__ except use empty
``tuple``'s (``()``) for each of the member values.  ``AutoEnum`` will automatically assign
incrementing integer values for each member, starting at ``1``.

.. code:: python

    >>> import autoenum
    >>> class Color(autoenum.AutoEnum):
    ...     red = ()
    ...     blue = ()
    ...     green = ()

Then access members and their attributes just like an ``Enum``.

.. code:: python

    >>> member = Color.red
    >>> member.name
    'red'
    >>> member.value
    1
    >>> import enum
    >>> isinstance(member, enum.Enum)
    True

There is no need to use the
`@enum.unique <https://docs.python.org/3/library/enum.html#ensuring-unique-enumeration-values>`__
decorator, as ``AutoEnum`` ensures that each member has a unique value.

Attempting to manually assign values to ``AutoEnum`` members will raise a
`TypeError <https://docs.python.org/3/library/exceptions.html#TypeError>`__.

.. code:: python

    >>> import autoenum
    >>> class Color(autoenum.AutoEnum):
    ...     red = 1
    TypeError: __new__() takes 1 positional argument but 2 were given

Releases
--------

1.0.1 - 2016-04-10
^^^^^^^^^^^^^^^^^^

Fix README rendering on PyPI and include ``autoenum`` module in ``setup.py``.
