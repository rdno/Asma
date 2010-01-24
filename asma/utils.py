# -*- coding: utf-8 -*-
"""includes some useful methods

get_icon - gets icon from gtk.IconTheme return Pixbuf

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

def get_icon(name, size=48, flags=0):
    """gets icon from gtk.IconTheme return Pixbuf
    
    Arguments:
    - `name`: icon name
    - `size`: icon size
    - `flags`: the flags modifying the behavior of the icon lookup
    """
    return gtk.IconTheme().load_icon(name, size, flags)
