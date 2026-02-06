#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.1.1

from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation




class psk8(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_calcdist([0.924+0.382j, .382+.924j, -.924+.382j, -0.382+0.924j, 0.924-0.382j, 0.382-0.924j, -0.924-0.382j, -0.382-0.924j], [0, 1, 10, 11, 100, 101, 110, 111],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.sps = sps = 3
        self.samp_rate = samp_rate = 250000
        self.interp = interp = 16
        self.freq = freq = 700000000
        self.filter_coeff = filter_coeff = [0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625]

        ##################################################
        # Blocks
        ##################################################
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(interp, filter_coeff)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(1, filter_coeff)
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(2**sps, digital.DIFF_DIFFERENTIAL)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2**sps, digital.DIFF_DIFFERENTIAL)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc((6.28)/50, 8, False)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(variable_constellation_0)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_cc(16, 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(variable_constellation_0.points() , 1)
        self.blocks_repack_bits_bb_1 = blocks.repack_bits_bb(3, 8, "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 3, "", False, gr.GR_LSB_FIRST)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/shay/a/ekocinar/ECE440/Lab7/random_stream.txt', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/shay/a/ekocinar/ECE440/Lab7/rx_8psk.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0, 0)
        self.analog_agc_xx_0 = analog.agc_cc(0.01, 1.0, 1)
        self.analog_agc_xx_0.set_max_gain(5000)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_repack_bits_bb_1, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.analog_agc_xx_0, 0))


    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_filter_coeff(self):
        return self.filter_coeff

    def set_filter_coeff(self, filter_coeff):
        self.filter_coeff = filter_coeff
        self.fir_filter_xxx_0.set_taps(self.filter_coeff)
        self.interp_fir_filter_xxx_0.set_taps(self.filter_coeff)




def main(top_block_cls=psk8, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    main()
