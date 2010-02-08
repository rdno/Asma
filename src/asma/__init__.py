# -*- coding: utf-8 -*-
"""Asma main module"""
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

__all__ = ["addon", "widgets", "utils", "Asma"]

import gtk
import gobject

from asma.translation import _
from asma.widgets import Container

class Asma(gtk.VBox):
    """lol
    """
    def __init__(self):
        """init"""
        gtk.VBox.__init__(self, homogeneous=False, spacing=5)
        self.back_btn = gtk.Button(_("Back"))
        self.container = Container()
        self._create_ui()
        self._listen_signals()
    def _create_ui(self):
        self.pack_end(self.container, expand=True, fill=True)
        self.container.set_mode("list")
        self.container.show()
        hbox = gtk.HBox()
        hbox.pack_start(self.back_btn, expand=False, fill=False)
        self.pack_start(hbox, expand=False, fill=False)
        hbox.show()
        self.show()
    def _listen_signals(self):
        to_list = lambda x:self.container.set_mode("list")
        self.back_btn.connect("clicked", to_list)
