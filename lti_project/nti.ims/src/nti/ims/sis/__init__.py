#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id: __init__.py 81721 2016-01-25 23:49:39Z carlos.sanchez $
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from nti.common.iterables import isorted

from nti.ims.sis.interfaces import STUDENT
from nti.ims.sis.interfaces import INSTRUCTOR
from nti.ims.sis.interfaces import STUDENT_ROLE
from nti.ims.sis.interfaces import INSTRUCTOR_ROLE

from nti.ims.sis.utils import get_text
from nti.ims.sis.utils import get_fileobj

def to_legacy_role(role):
	if role:
		role = role.upper()
		if role == STUDENT:
			role = STUDENT_ROLE
		elif role == INSTRUCTOR:
			role = INSTRUCTOR_ROLE
	return role
