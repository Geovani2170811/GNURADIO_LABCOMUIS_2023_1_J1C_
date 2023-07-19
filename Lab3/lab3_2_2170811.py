#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: TransmisorAM
# Author: 2170811
# Copyright: 2170811
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from CalculoPotenciaComu_2170811 import CalculoPotenciaComu_2170811  # grc-generated hier_block
from ModuladorAM_2170811 import ModuladorAM_2170811  # grc-generated hier_block
from gnuradio import analog
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class lab3_2_2170811(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "TransmisorAM", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("TransmisorAM")
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

        self.settings = Qt.QSettings("GNU Radio", "lab3_2_2170811")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000
        self.ka = ka = 1
        self.fc = fc = 50e6
        self.GTX = GTX = 0
        self.Fm = Fm = 1000
        self.Am = Am = 1
        self.Ac = Ac = 125e-3

        ##################################################
        # Blocks
        ##################################################
        self._ka_range = Range(0, 4, 100e-3, 1, 200)
        self._ka_win = RangeWidget(self._ka_range, self.set_ka, "Coeficiente Ka", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._ka_win)
        self._fc_range = Range(50e6, 2.2e9, 1e6, 50e6, 200)
        self._fc_win = RangeWidget(self._fc_range, self.set_fc, "Frecuencia portadora", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fc_win)
        self._GTX_range = Range(0, 30, 1, 0, 200)
        self._GTX_win = RangeWidget(self._GTX_range, self.set_GTX, "Ganancia del TX", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._GTX_win)
        self._Fm_range = Range(300, 21000, 100, 1000, 200)
        self._Fm_win = RangeWidget(self._Fm_range, self.set_Fm, "Frecuencia Mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Fm_win)
        self._Am_range = Range(0, 4, 100e-3, 1, 200)
        self._Am_win = RangeWidget(self._Am_range, self.set_Am, "Amplitud mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Am_win)
        self._Ac_range = Range(0, 1, 1e-3, 125e-3, 200)
        self._Ac_win = RangeWidget(self._Ac_range, self.set_Ac, "Amplitud portadora", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Ac_win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            "",
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)

        self.uhd_usrp_sink_0.set_center_freq(fc, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_gain(GTX, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, Fm, Am, 0, 0)
        self.ModuladorAM_2170811_0 = ModuladorAM_2170811(
            Ac=Ac,
            ka=ka,
        )
        self.CalculoPotenciaComu_2170811_0 = CalculoPotenciaComu_2170811(
            I_vect=1024,
        )

        self.top_layout.addWidget(self.CalculoPotenciaComu_2170811_0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ModuladorAM_2170811_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.CalculoPotenciaComu_2170811_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.ModuladorAM_2170811_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lab3_2_2170811")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_ka(self):
        return self.ka

    def set_ka(self, ka):
        self.ka = ka
        self.ModuladorAM_2170811_0.set_ka(self.ka)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.uhd_usrp_sink_0.set_center_freq(self.fc, 0)

    def get_GTX(self):
        return self.GTX

    def set_GTX(self, GTX):
        self.GTX = GTX
        self.uhd_usrp_sink_0.set_gain(self.GTX, 0)

    def get_Fm(self):
        return self.Fm

    def set_Fm(self, Fm):
        self.Fm = Fm
        self.analog_sig_source_x_0.set_frequency(self.Fm)

    def get_Am(self):
        return self.Am

    def set_Am(self, Am):
        self.Am = Am
        self.analog_sig_source_x_0.set_amplitude(self.Am)

    def get_Ac(self):
        return self.Ac

    def set_Ac(self, Ac):
        self.Ac = Ac
        self.ModuladorAM_2170811_0.set_Ac(self.Ac)




def main(top_block_cls=lab3_2_2170811, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
