# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Power
# Author: Erik and Mohsin
# Description: A block for calculating average power of a signal.
# GNU Radio version: 3.10.1.1

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal







class power(gr.hier_block2):
    def __init__(self):
        gr.hier_block2.__init__(
            self, "Power",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.blocks_rms_xx_0 = blocks.rms_ff(0.0001)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_xx_0, 0), (self, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self, 0), (self.blocks_rms_xx_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

