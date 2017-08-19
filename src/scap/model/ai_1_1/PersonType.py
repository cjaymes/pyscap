# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

import logging

from scap.decorators import *
from scap.model.ai_1_1.AssetType import AssetType

logger = logging.getLogger(__name__)

@element('urn:oasis:names:tc:ciq:xsdschema:xNL:2.0', 'PersonName', cls='PersonNameType', min=0)
@element(None, 'email-address', list='email_addresses', cls='EmailAddressType', min=0, max=None)
@element(None, 'telephone-number', list='telephone_numbers', cls='TelephoneNumberType', min=0, max=None)
@element(None, 'birthdate', cls='BirthdateType', min=0)
class PersonType(AssetType):
    pass
