from mylib.module import baz


def foo():
    print("foo")


def bar():
    print("bar")


__all__ = ["foo", "bar", "baz"]
