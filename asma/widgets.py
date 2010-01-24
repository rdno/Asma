# -*- coding: utf-8 -*-
"""Asma widgets module

Container - container of ManagerList & managers
ManagerList - List managers as icons

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

import gtk
import gobject

from asma.translation import _
from asma.utils import get_icon

from asma.addon import AddonManager

class Container(gtk.ScrolledWindow):
    """container of ManagerList & managers"""
    def __init__(self):
        """init"""
        gtk.ScrolledWindow.__init__(self)
        self._set_style()
        self.addon_manager = AddonManager()
    def _set_style(self):
        #sets style of ScrolledWindow
        self.set_shadow_type(gtk.SHADOW_IN)
        self.set_policy(gtk.POLICY_NEVER,
                        gtk.POLICY_AUTOMATIC)
    def _remove_child(self, child):
        """removes widget"""
        self.get_child().remove(child)
        del child
    def _add_child(self, child):
        """add widget

        Arguments:
        - `child`: widget to add
        """
        if self.get_child():
            if type(child) == ManagerList:
                self._remove_child(self.manager)
            else:
                self._remove_child(self.manlist)
        self.add_with_viewport(child)
        child.show_all()
    def set_mode(self, mode):
        """sets view mode
        
        Arguments:
        - `mode`: 'list' | 'manager'
        """
        if mode == "list":
            self.manlist = ManagerList()
            self.manlist.show_list(self.addon_manager.list_addons())
            self.manlist.listen_on_item(self._add_manager)
            self._add_child(self.manlist)
            self.parent.back_btn.hide()
        elif mode == "manager":
            self.parent.back_btn.show()
            self._add_child(self.manager)
    def _add_manager(self, uuid):
        #add manager
        self.manager = self.addon_manager.create_widget(uuid)
        self.set_mode("manager")

gobject.type_register(Container)

class ManagerList(gtk.IconView):
    """List managers as icons"""
    def __init__(self):
        """init"""
        self.store = gtk.ListStore(str, str, gtk.gdk.Pixbuf)
        gtk.IconView.__init__(self, self.store)
        self._set_style()
    def _set_style(self):
        #sets style of IconView
        self.set_text_column(1)
        self.set_pixbuf_column(2)
    def show_list(self, mlist):
        """shows managers 
        
        Arguments:
        - `mlist`: manager list [(uuid, label, icon_name),
                                 (uuid, label, icon_name),
                                             ...         ]
        """
        for uuid, label, icon_name in mlist:
            self.store.append([uuid, label, get_icon(icon_name)])
    def listen_on_item(self, func):
        """on item activate func will be called
        with argument uuid"""
        self._func = func
        self.connect("item-activated",
                           self._on_item_activated)
    def _on_item_activated(self, widget, item):
        self._func.__call__(self.store[item][0])

gobject.type_register(ManagerList)
