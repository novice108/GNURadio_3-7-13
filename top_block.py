#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Spectrum HackRF transmit - recieve
# Author: icyb180
# Description: Transmit and receive aes256
# Generated: Tue Jun 28 16:20:35 2022
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import cryptography
import epy_block_2_0
import epy_block_2_0_0
import numpy
import os
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, hdr_format=digital.header_format_default(digital.packet_utils.default_access_code, 0), my_const=digital.constellation_calcdist((digital.psk_2()[0]), (digital.psk_2()[1]), 2, 1).base()):
        gr.top_block.__init__(self, "Spectrum HackRF transmit - recieve")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Spectrum HackRF transmit - recieve")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.hdr_format = hdr_format
        self.my_const = my_const

        ##################################################
        # Variables
        ##################################################
        self.sps_TX = sps_TX = 40
        self.nfilts = nfilts = 32
        self.EBW = EBW = .35
        self.svar32 = svar32 = "12345678123456781234567812345678"
        self.sps_RX = sps_RX = 40/10
        self.samp_rate = samp_rate = 240E3
        self.center_freq = center_freq = 430E6

        self.RRC_filter_taps = RRC_filter_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, EBW, 5*sps_TX*nfilts)


        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=int(sps_TX/sps_RX),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0_0_1 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	samp_rate, #bw
        	"transmitter", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_0_1.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0_1.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_1_win)
        self.qtgui_waterfall_sink_x_0_0_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	samp_rate, #bw
        	"reciever", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_0_win)
        self.qtgui_edit_box_msg_0_0_0_0 = qtgui.edit_box_msg(qtgui.STRING, svar32, 'Input', False, True, '')
        self._qtgui_edit_box_msg_0_0_0_0_win = sip.wrapinstance(self.qtgui_edit_box_msg_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_edit_box_msg_0_0_0_0_win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps_TX,
                  taps=(RRC_filter_taps),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)

        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'hackrf=17c467dc2d1445c3' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(True, 0)
        self.osmosdr_source_0.set_gain(15, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.osmosdr_sink_0_0 = osmosdr.sink( args="numchan=" + str(1) + " " + 'hackrf=17c467dc2967a2c3' )
        self.osmosdr_sink_0_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0_0.set_center_freq(center_freq, 0)
        self.osmosdr_sink_0_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0_0.set_gain(1, 0)
        self.osmosdr_sink_0_0.set_if_gain(10, 0)
        self.osmosdr_sink_0_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0_0.set_antenna('', 0)
        self.osmosdr_sink_0_0.set_bandwidth(0, 0)

        self.epy_block_2_0_0 = epy_block_2_0_0.msg_block()
        self.epy_block_2_0 = epy_block_2_0.msg_block()
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, 'len_key')
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps_RX, 6.28/400.0*2, (RRC_filter_taps), nfilts, nfilts/2, 1.5, 1)
        self.digital_fll_band_edge_cc_0 = digital.fll_band_edge_cc(sps_RX, EBW, 45, .02)
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(2)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.digital_crc32_async_bb_1 = digital.crc32_async_bb(False)
        self.digital_crc32_async_bb_0 = digital.crc32_async_bb(True)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(.01, 2, False)
        self.digital_correlate_access_code_xx_ts_1_0 = digital.correlate_access_code_bb_ts(digital.packet_utils.default_access_code,
          2, 'len_key2')
        self.digital_constellation_soft_decoder_cf_0 = digital.constellation_soft_decoder_cf(my_const)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(11, 1, .01, 1)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((my_const.points()), 1)
        self.digital_burst_shaper_xx_0 = digital.burst_shaper_cc((numpy.ones(500)), 4000, 4000, True, 'len_key')
        (self.digital_burst_shaper_xx_0).set_block_alias("burst_shaper0")
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.byte_t, 'len_key2')
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'len_key', 0)
        self.blocks_tagged_stream_multiply_length_0 = blocks.tagged_stream_multiply_length(gr.sizeof_gr_complex*1, 'len_key', sps_TX)
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(1, 8, 'len_key2', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, my_const.bits_per_symbol(), 'len_key', False, gr.GR_MSB_FIRST)
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'len_key')
        self.blocks_message_debug_0_0 = blocks.message_debug()
        self.blocks_message_debug_0 = blocks.message_debug()
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-20, .01, 0, True)
        self.analog_feedforward_agc_cc_0 = analog.feedforward_agc_cc(1024/2, 1.0)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.digital_crc32_async_bb_0, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.epy_block_2_0_0, 'pdu_in'))
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))
        self.msg_connect((self.epy_block_2_0, 'out'), (self.blocks_message_debug_0_0, 'print_pdu'))
        self.msg_connect((self.epy_block_2_0, 'out'), (self.digital_crc32_async_bb_1, 'in'))
        self.msg_connect((self.epy_block_2_0, 'out'), (self.qtgui_edit_box_msg_0_0_0_0, 'val'))
        self.msg_connect((self.epy_block_2_0_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.qtgui_edit_box_msg_0_0_0_0, 'msg'), (self.epy_block_2_0, 'msg_in'))
        self.connect((self.analog_feedforward_agc_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.digital_fll_band_edge_cc_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.osmosdr_sink_0_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.qtgui_waterfall_sink_x_0_0_1, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_burst_shaper_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.digital_burst_shaper_xx_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_constellation_soft_decoder_cf_0, 0))
        self.connect((self.digital_constellation_soft_decoder_cf_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_1_0, 0), (self.blocks_repack_bits_bb_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_cma_equalizer_cc_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.digital_correlate_access_code_xx_ts_1_0, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.analog_feedforward_agc_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_waterfall_sink_x_0_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_tagged_stream_multiply_length_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_pwr_squelch_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_my_const(self):
        return self.my_const

    def set_my_const(self, my_const):
        self.my_const = my_const

    def get_sps_TX(self):
        return self.sps_TX

    def set_sps_TX(self, sps_TX):
        self.sps_TX = sps_TX
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps_TX)
        self.blocks_tagged_stream_multiply_length_0.set_scalar(self.sps_TX)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts

    def get_EBW(self):
        return self.EBW

    def set_EBW(self, EBW):
        self.EBW = EBW

    def get_svar32(self):
        return self.svar32

    def set_svar32(self, svar32):
        self.svar32 = svar32

    def get_sps_RX(self):
        return self.sps_RX

    def set_sps_RX(self, sps_RX):
        self.sps_RX = sps_RX

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0_0_1.set_frequency_range(self.center_freq, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0_0.set_sample_rate(self.samp_rate)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.qtgui_waterfall_sink_x_0_0_1.set_frequency_range(self.center_freq, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)
        self.osmosdr_sink_0_0.set_center_freq(self.center_freq, 0)

    def get_RRC_filter_taps(self):
        return self.RRC_filter_taps

    def set_RRC_filter_taps(self, RRC_filter_taps):
        self.RRC_filter_taps = RRC_filter_taps
        self.pfb_arb_resampler_xxx_0.set_taps((self.RRC_filter_taps))
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.RRC_filter_taps))


def argument_parser():
    description = 'Transmit and receive aes256'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
