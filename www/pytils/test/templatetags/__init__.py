# -*- coding: utf-8 -*-
# pytils - russian-specific string utils
# Copyright (C) 2006-2008  Yury Yurevich
#
# http://www.pyobject.ru/projects/pytils/
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, version 2
# of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
"""
Unit tests for pytils' templatetags for Django web framework
"""

__all__ = ["test_common", "test_numeral", "test_dt", "test_translit"]

import unittest

def get_suite():
    """Return TestSuite for all unit-test of pytils' templatetags"""
    suite = unittest.TestSuite()
    for module_name in __all__:
        imported_module = __import__("pytils.test.templatetags."+module_name,
                                       globals(),
                                       locals(),
                                       ["pytils.test.templatetags"])
        
        getter = getattr(imported_module, 'get_suite', False)
        if getter:
            suite.addTest(getter())
        
        loader = unittest.defaultTestLoader
        suite.addTest(loader.loadTestsFromModule(imported_module))

    return suite

def run(verbosity=1):
    """Run all unit-test of pytils' templatetags"""
    suite = get_suite()
    unittest.TextTestRunner(verbosity=verbosity).run(suite)

if __name__ == '__main__':
    run(2)
