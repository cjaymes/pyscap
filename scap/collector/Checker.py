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

import importlib
import logging
import sys
from scap.Collector import Collector

logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
class Checker(Collector):
    @staticmethod
    def load(host, content, parent, args={}):
        model_namespace = content.__class__.__module__.split('.')[2]
        collector_module = 'scap.collector.checker.' + model_namespace + '.' + content.__class__.__name__
        # try to load the collector's module
        if collector_module not in sys.modules:
            logger.debug('Loading module ' + collector_module)
            try:
                mod = importlib.import_module(collector_module)
            except Exception as e:
                logger.warning('Could not load module for ' + collector_module + ': ' + str(e))
                raise
        else:
            mod = sys.modules[collector_module]

        # instantiate an instance of the class & load it
        class_ = getattr(mod, content.__class__.__name__)
        inst = class_(host, content, parent, args)

        return inst

    def __init__(self, host, content, parent, args={}):
        super(Checker, self).__init__(host, args)
        self.content = content
        self.parent = parent
        self.ref_mapping = {}

    def resolve_reference(self, ref):
        if not self.parent:
            raise RuntimeError("Got to null parent without resolving reference")

        logger.debug('Reference ' + ref + ' not in ' + self.__class__.__name__ + ' continuing to parent ' + self.parent.__class__.__name__)
        return self.parent.resolve_reference(ref)
