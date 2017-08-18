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
import os
import pathlib
import pytest

from scap.Host import Host
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

filename = str(pathlib.Path(os.path.expanduser('~')) / '.pyscap' / 'inventory.ini')
try:
    with open(filename, 'r') as fp:
        logger.debug('Loading inventory from ' + filename)
        Inventory().readfp(fp)
except IOError:
    logger.error('Could not read from inventory file ' + filename)

host = Host.load('localhost')

def setup_module(module):
    if host.facts['oval_family'] != 'linux':
        pytest.skip('Does not apply to platform')
    host.load_collector('VirtualMachineDetectionCollector', {}).collect()
    if host.facts['in_virtual_machine'] and host.facts['hosting_hypervisor'] == 'docker':
        pytest.skip('Does not apply to platform')

def test_rootfsuuid():
    host.load_collector('RootFsUuidCollector', {}).collect()

    assert 'root_filesystem_uuid' in host.facts
