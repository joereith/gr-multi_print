#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2021 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
import time

class printer(gr.sync_block):
    """
    docstring for block printer
    """
    def __init__(self, in_sig):
        mapper = type(in_sig).__name__
        if in_sig == 4:
            if isinstance(in_sig, int):
                self.mapper2 = 'int32'
        if in_sig == 1:
            if isinstance(in_sig, int):
                self.mapper2 = 'int8'
        if in_sig == 2:
            if isinstance(in_sig, int):
                self.mapper2 = 'int16'
        gr.sync_block.__init__(self,
            name="printer",
            in_sig = [mapper],
            out_sig=None)


    def work(self, input_items, output_items):
        #print("In the work function!!!")
        in0 = input_items[0]
        #out = output_items[0]
        # <+signal processing here+>
        #out[:] = in0
        print("{}".format(in0))
        return len(input_items[0])

