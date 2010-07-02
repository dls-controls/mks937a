from pkg_resources import require
require('dls_serial_sim')
from dls_serial_sim import serial_device

class Mks937aChannel(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.pressure = 1.0
        self.controlSetPoint = 0.0
        self.relaySetPoint = 0.0
        self.protectionSetPoint = 0.0
        self.coldCathodeEnable = False

    def getPressure(self):
        result = '%.1E' % self.pressure
        if self.type == 'img':
            if not self.coldCathodeEnable:
                result = 'HV_OFF'
            elif self.pressure > 0.01:
                result = 'HI'
        elif self.type == 'pirani':
            if self.pressure < 0.001:
                result = 'LO'
        else:
            result = 'NOGAUGE!'
        return result

class Mks937aCrate(serial_device):

    def __init__(self, name='', tcpPort=9100):
        print "Create MKS937A crate %s" % name
        serial_device.__init__(self)
        self.name = name
        self.gauges = {}
        self.gauges[1] = mks937aChannel(name+':1', 'img')
        self.gauges[2] = mks937aChannel(name+':2', 'img')
        self.gauges[3] = mks937aChannel(name+':3', '')
        self.gauges[4] = mks937aChannel(name+':4', 'pirani')
        self.gauges[5] = mks937aChannel(name+':5', 'pirani')
        self.start_ip(tcpPort)

    def getInterlock(self, signal):
        result = False
        gauge = self.gauges[signal[0]]
        if signal[1] == 1:
            result = gauge.pressure <= gauge.relaySetPoint
        return result

    def getGauge(self, number):
        result = None
        if number in self.gauges:
            result = self.gauges[number]
        return result

    def reply(self, command):
        result = None
        param = None
        printMessage = True
        cmd = command.strip()
        if '=' in cmd:
            parts = cmd.split('=')
            cmd = parts[0]
            param = parts[1]
        if len(cmd) > 1:
            n = None
            if cmd[-1] in '12345':
                n = int(cmd[-1])
                cmd = cmd[:-1]
            if cmd == 'R' and n is not None and param is None:
                result = "%s" % self.gauges[n].getPressure()
                printMessage = False
            elif cmd == 'CTL' and n is not None:
                if param is None:
                    result = "%s" % self.gauges[n].controlSetPoint
                    printMessage = False
                else:
                    self.gauges[n].controlSetPoint = float(param)
                    result = "OK"
            elif cmd == 'PRO' and n is not None:
                if param is None:
                    result = "%s" % self.gauges[n].protectionSetPoint
                    printMessage = False
                else:
                    self.gauges[n].protectionSetPoint = float(param)
                    result = "OK"
            elif cmd == 'RLY' and n is not None:
                if param is None:
                    result = "%s" % self.gauges[n].relaySetPoint
                    printMessage = False
                else:
                    self.gauges[n].relaySetPoint = float(param)
                    result = "OK"
            elif cmd == 'ECC' and n is not None and param is None:
                self.gauges[n].coldCathodeEnable = True
                result = "OK"
            elif cmd == 'XCC' and n is not None and param is None:
                self.gauges[n].coldCathodeEnable = False
                result = "OK"
            elif cmd == 'VER' and n is None and param is None:
                result = "1.00,1.10"
                printMessage = False
            elif cmd == 'FREQ' and n is None and param is None:
                result = "50Hz"
                printMessage = False
            elif cmd == 'UNIT' and n is None and param is None:
                result = "mbar"
                printMessage = False
            elif cmd == 'GAUGES' and n is None and param is None:
                result = "CcCcCv"
                printMessage = False
        if printMessage:
            print "%s==>%s" % (repr(command), repr(result))
        return result

