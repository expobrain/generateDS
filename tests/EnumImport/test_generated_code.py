#!/usr/bin/env python

from __future__ import print_function
import sys

from enum_import00 import Type00_2

def test():
    success = True
    try:
        from enum_import00 import EnumType01_1
        print("the 'enum_import00' file should not have 'EnumType01_1'")
        success = False
    except:
        pass

    testType = Type00_2()
    if type(testType.get_attr1()) != int:
        print("the default value of 'Type00_2.attr1' should be of int type")
        success = False

    if not success:
        print("test failed")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    test()
