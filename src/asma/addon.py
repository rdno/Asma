# -*- coding: utf-8 -*-
"""Asma addon module

AsmaAddon - Asma Addon Model
AddonManager - Asma Addon Manager

"""
#
# Rıdvan Örsvuran (C) 2010
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import glob
import re

class AsmaAddon(object):
    """Asma Addon Model"""
    def __init__(self):
        """init variables"""
        super(AsmaAddon, self).__init__()
        self._uuid = "" #create via str(uuid.uuid4())
        self._icon_name = ""
        self._label = ""
        self._widget = None
    def _get_uuid(self):
        return self._uuid
    uuid = property(fget=_get_uuid,
                    doc="Unique ID")
    def _get_icon_name(self):
        return self._icon_name
    icon_name = property(fget=_get_icon_name,
                         doc="icon name for load")
    def _get_label(self):
        return self._label
    label = property(fget=_get_label,
                     doc="label for asma")
    def _get_widget(self):
        return self._widget
    widget = property(fget=_get_widget,
                      doc="widget to add asma")

class AddonManager(object):
    """Asma Addon Manager"""
    def __init__(self):
        """init"""
        super(AddonManager, self).__init__()
        self.search()
    def search(self):
        """search asma.addons package for addons"""
        from asma import addons
        addons_dir = os.path.split(addons.__file__)[0]
        pys = glob.glob(addons_dir+"/*.py")
        #delete __init__.py
        pys = filter(lambda x: not x.endswith("__init__.py"), pys)
        exp = re.compile(".*(asma/addons/.*)[.]py")
        to_module = lambda x: exp.match(x).group(1).replace("/", ".")
        modules =  map(to_module, pys)
        self._load_modules(modules)
        self._get_addons()
    def _load_modules(self, modules):
        #imports modules in list
        for module in modules:
            __import__(module, level=0)
    def _get_addons(self):
        #gets addons from imported modules
        addon_objs = [x() for x in AsmaAddon.__subclasses__()]
        self._addons = {}
        for addon in addon_objs:
            self._addons[addon.uuid] = {"icon_name":addon.icon_name,
                                        "label":addon.label,
                                        "widget":addon.widget}
    def create_widget(self, uuid):
        """creates addon's widget and returns it
        
        Arguments:
        - `uuid`:addon's uuid
        """
        return self._addons[uuid]["widget"]()
    def list_addons(self):
        """return addons list for adding ManagerList(IconView)
        """
        return [(uuid, self._addons[uuid]["label"],
                 self._addons[uuid]["icon_name"])
                for uuid in self._addons.keys()]
    
    
