#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Usrp Echotimer Fmcw
# Generated: Sun Feb 12 08:41:58 2023
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import radar
import sip
import sys
import time
from gnuradio import qtgui


class usrp_echotimer_fmcw(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Usrp Echotimer Fmcw")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Usrp Echotimer Fmcw")
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

        self.settings = Qt.QSettings("GNU Radio", "usrp_echotimer_fmcw")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_up = samp_up = 2**14
        self.samp_rate = samp_rate = 50000000
        self.sweep_freq = sweep_freq = samp_rate/2
        self.samp_down = samp_down = samp_up
        self.samp_cw = samp_cw = 2**14
        self.center_freq = center_freq = 6.0e9
        self.wait_to_start = wait_to_start = 0.02
        self.v_res = v_res = samp_rate/samp_cw*3e8/2/center_freq
        self.tx_gain = tx_gain = 99
        self.threshold = threshold = -150
        self.rx_gain = rx_gain = 99
        self.range_res = range_res = 3e8/2/sweep_freq
        self.protect_samp = protect_samp = 0
        self.min_output_buffer = min_output_buffer = int((samp_up+samp_down+samp_cw)*2)
        self.meas_duration = meas_duration = (samp_cw+samp_up+samp_down)/float(samp_rate)
        self.max_output_buffer = max_output_buffer = 0
        self.freq_res_up = freq_res_up = samp_rate/samp_up
        self.freq_res_cw = freq_res_cw = samp_rate/samp_cw
        self.delay_samp = delay_samp = 24
        self.decim_fac = decim_fac = 2**3

        ##################################################
        # Blocks
        ##################################################
        self._tx_gain_range = Range(0, 100, 1, 99, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, 'TX Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_gain_win, 0,0)
        self._threshold_range = Range(-150, 0, 1, -150, 200)
        self._threshold_win = RangeWidget(self._threshold_range, self.set_threshold, "threshold", "counter_slider", float)
        self.top_grid_layout.addWidget(self._threshold_win, 1,0)
        self._rx_gain_range = Range(0, 100, 1, 99, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, 'RX Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_gain_win, 0,1)
        self._protect_samp_range = Range(0, 100, 1, 0, 200)
        self._protect_samp_win = RangeWidget(self._protect_samp_range, self.set_protect_samp, "protect_samp", "counter_slider", float)
        self.top_grid_layout.addWidget(self._protect_samp_win, 1,1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(('serial=315AF40', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_clock_source('gpsdo', 0)
        self.uhd_usrp_source_0.set_time_source('gpsdo', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        (self.uhd_usrp_source_0).set_min_output_buffer(98304)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(('serial=315AF6C', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        	"packet_len",
        )
        self.uhd_usrp_sink_0.set_clock_source('gpsdo', 0)
        self.uhd_usrp_sink_0.set_time_source('gpsdo', 0)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim_fac,
                taps=None,
                fractional_bw=None,
        )
        self.radar_ts_fft_cc_2 = radar.ts_fft_cc(samp_down/decim_fac,  "packet_len")
        self.radar_ts_fft_cc_1 = radar.ts_fft_cc(samp_up/decim_fac,  "packet_len")
        self.radar_ts_fft_cc_0 = radar.ts_fft_cc(samp_cw/decim_fac,  "packet_len")
        self.radar_split_cc_0_0_0 = radar.split_cc(2, ((samp_cw/decim_fac,samp_up/decim_fac,samp_down/decim_fac)), "packet_len")
        (self.radar_split_cc_0_0_0).set_min_output_buffer(98304)
        self.radar_split_cc_0_0 = radar.split_cc(1, ((samp_cw/decim_fac,samp_up/decim_fac,samp_down/decim_fac)), "packet_len")
        (self.radar_split_cc_0_0).set_min_output_buffer(98304)
        self.radar_split_cc_0 = radar.split_cc(0, ((samp_cw/decim_fac,samp_up/decim_fac,samp_down/decim_fac)), "packet_len")
        (self.radar_split_cc_0).set_min_output_buffer(98304)
        self.radar_signal_generator_fmcw_c_0 = radar.signal_generator_fmcw_c(samp_rate, samp_up, samp_down, samp_cw, -sweep_freq/2, sweep_freq, 1, "packet_len")
        (self.radar_signal_generator_fmcw_c_0).set_min_output_buffer(98304)
        self.radar_print_results_0 = radar.print_results(False, "")
        self.radar_find_max_peak_c_0_0_0 = radar.find_max_peak_c(samp_rate/decim_fac, threshold, int(protect_samp), (), False, "packet_len")
        (self.radar_find_max_peak_c_0_0_0).set_min_output_buffer(98304)
        self.radar_find_max_peak_c_0_0 = radar.find_max_peak_c(samp_rate/decim_fac, threshold, int(protect_samp), (), False, "packet_len")
        (self.radar_find_max_peak_c_0_0).set_min_output_buffer(98304)
        self.radar_find_max_peak_c_0 = radar.find_max_peak_c(samp_rate/decim_fac, threshold, int(protect_samp), (), False, "packet_len")
        (self.radar_find_max_peak_c_0).set_min_output_buffer(98304)
        self.radar_estimator_fmcw_0 = radar.estimator_fmcw(samp_rate/decim_fac, center_freq, sweep_freq, samp_up/decim_fac, samp_down/decim_fac, False)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	samp_cw/decim_fac, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim_fac, #bw
        	'CW', #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self._delay_samp_range = Range(0, 100, 1, 24, 200)
        self._delay_samp_win = RangeWidget(self._delay_samp_range, self.set_delay_samp, 'Number delay samples', "counter_slider", float)
        self.top_layout.addWidget(self._delay_samp_win)
        self.blocks_tagged_stream_multiply_length_0 = blocks.tagged_stream_multiply_length(gr.sizeof_gr_complex*1, "packet_len", 1.0/decim_fac)
        (self.blocks_tagged_stream_multiply_length_0).set_min_output_buffer(98304)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        (self.blocks_multiply_conjugate_cc_0).set_min_output_buffer(98304)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.radar_estimator_fmcw_0, 'Msg out'), (self.radar_print_results_0, 'Msg in'))
        self.msg_connect((self.radar_find_max_peak_c_0, 'Msg out'), (self.radar_estimator_fmcw_0, 'Msg in CW'))
        self.msg_connect((self.radar_find_max_peak_c_0_0, 'Msg out'), (self.radar_estimator_fmcw_0, 'Msg in UP'))
        self.msg_connect((self.radar_find_max_peak_c_0_0_0, 'Msg out'), (self.radar_estimator_fmcw_0, 'Msg in DOWN'))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.radar_split_cc_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.radar_split_cc_0_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.radar_split_cc_0_0_0, 0))
        self.connect((self.radar_signal_generator_fmcw_c_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.radar_signal_generator_fmcw_c_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.radar_split_cc_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.radar_split_cc_0, 0), (self.radar_ts_fft_cc_0, 0))
        self.connect((self.radar_split_cc_0_0, 0), (self.radar_ts_fft_cc_1, 0))
        self.connect((self.radar_split_cc_0_0_0, 0), (self.radar_ts_fft_cc_2, 0))
        self.connect((self.radar_ts_fft_cc_0, 0), (self.radar_find_max_peak_c_0, 0))
        self.connect((self.radar_ts_fft_cc_1, 0), (self.radar_find_max_peak_c_0_0, 0))
        self.connect((self.radar_ts_fft_cc_2, 0), (self.radar_find_max_peak_c_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_tagged_stream_multiply_length_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "usrp_echotimer_fmcw")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_up(self):
        return self.samp_up

    def set_samp_up(self, samp_up):
        self.samp_up = samp_up
        self.set_samp_down(self.samp_up)
        self.set_min_output_buffer(int((self.samp_up+self.samp_down+self.samp_cw)*2))
        self.set_meas_duration((self.samp_cw+self.samp_up+self.samp_down)/float(self.samp_rate))
        self.set_freq_res_up(self.samp_rate/self.samp_up)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sweep_freq(self.samp_rate/2)
        self.set_v_res(self.samp_rate/self.samp_cw*3e8/2/self.center_freq)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim_fac)
        self.set_meas_duration((self.samp_cw+self.samp_up+self.samp_down)/float(self.samp_rate))
        self.set_freq_res_up(self.samp_rate/self.samp_up)
        self.set_freq_res_cw(self.samp_rate/self.samp_cw)

    def get_sweep_freq(self):
        return self.sweep_freq

    def set_sweep_freq(self, sweep_freq):
        self.sweep_freq = sweep_freq
        self.set_range_res(3e8/2/self.sweep_freq)

    def get_samp_down(self):
        return self.samp_down

    def set_samp_down(self, samp_down):
        self.samp_down = samp_down
        self.set_min_output_buffer(int((self.samp_up+self.samp_down+self.samp_cw)*2))
        self.set_meas_duration((self.samp_cw+self.samp_up+self.samp_down)/float(self.samp_rate))

    def get_samp_cw(self):
        return self.samp_cw

    def set_samp_cw(self, samp_cw):
        self.samp_cw = samp_cw
        self.set_v_res(self.samp_rate/self.samp_cw*3e8/2/self.center_freq)
        self.set_min_output_buffer(int((self.samp_up+self.samp_down+self.samp_cw)*2))
        self.set_meas_duration((self.samp_cw+self.samp_up+self.samp_down)/float(self.samp_rate))
        self.set_freq_res_cw(self.samp_rate/self.samp_cw)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.set_v_res(self.samp_rate/self.samp_cw*3e8/2/self.center_freq)
        self.uhd_usrp_source_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.center_freq, 0)

    def get_wait_to_start(self):
        return self.wait_to_start

    def set_wait_to_start(self, wait_to_start):
        self.wait_to_start = wait_to_start

    def get_v_res(self):
        return self.v_res

    def set_v_res(self, v_res):
        self.v_res = v_res

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)


    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.radar_find_max_peak_c_0_0_0.set_threshold(self.threshold)
        self.radar_find_max_peak_c_0_0.set_threshold(self.threshold)
        self.radar_find_max_peak_c_0.set_threshold(self.threshold)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)


    def get_range_res(self):
        return self.range_res

    def set_range_res(self, range_res):
        self.range_res = range_res

    def get_protect_samp(self):
        return self.protect_samp

    def set_protect_samp(self, protect_samp):
        self.protect_samp = protect_samp
        self.radar_find_max_peak_c_0_0_0.set_samp_protect(int(self.protect_samp))
        self.radar_find_max_peak_c_0_0.set_samp_protect(int(self.protect_samp))
        self.radar_find_max_peak_c_0.set_samp_protect(int(self.protect_samp))

    def get_min_output_buffer(self):
        return self.min_output_buffer

    def set_min_output_buffer(self, min_output_buffer):
        self.min_output_buffer = min_output_buffer

    def get_meas_duration(self):
        return self.meas_duration

    def set_meas_duration(self, meas_duration):
        self.meas_duration = meas_duration

    def get_max_output_buffer(self):
        return self.max_output_buffer

    def set_max_output_buffer(self, max_output_buffer):
        self.max_output_buffer = max_output_buffer

    def get_freq_res_up(self):
        return self.freq_res_up

    def set_freq_res_up(self, freq_res_up):
        self.freq_res_up = freq_res_up

    def get_freq_res_cw(self):
        return self.freq_res_cw

    def set_freq_res_cw(self, freq_res_cw):
        self.freq_res_cw = freq_res_cw

    def get_delay_samp(self):
        return self.delay_samp

    def set_delay_samp(self, delay_samp):
        self.delay_samp = delay_samp

    def get_decim_fac(self):
        return self.decim_fac

    def set_decim_fac(self, decim_fac):
        self.decim_fac = decim_fac
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim_fac)
        self.blocks_tagged_stream_multiply_length_0.set_scalar(1.0/self.decim_fac)


def main(top_block_cls=usrp_echotimer_fmcw, options=None):

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
