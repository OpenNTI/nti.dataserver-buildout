#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id: interfaces.py 82800 2016-02-12 15:27:12Z carlos.sanchez $
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.field import ValidTextLine

class IConsumer(interface.Interface):
    key = ValidTextLine(title="Consumer key", required=True)
    secret = ValidTextLine(title="Consumer secret", required=True)
