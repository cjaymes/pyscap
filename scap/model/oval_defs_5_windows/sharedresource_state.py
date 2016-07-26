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

from scap.model.oval_defs_5_windows.State import State
import logging

logger = logging.getLogger(__name__)
class sharedresource_state(State)
    def __init__(self):
        super(sharedresource_state, self).__init__()    # {http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresource_state

        self.ignore_sub_elements.extend([
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}netname',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}shared_type',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}max_uses',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}current_uses',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}local_path',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}access_read_permission',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}access_write_permission',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}access_create_permission',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}access_exec_permission',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}access_delete_permission',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}access_atrib_permission',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}access_perm_permission',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}access_all_permission',
        ])