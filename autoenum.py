#!/usr/bin/env python3

import enum


__all__ = ['AutoEnum']


class AutoEnum(enum.Enum):
    """Enum type that automatically assigns incrementing integer values
    starting at 1 to members."""
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj
