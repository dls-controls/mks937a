#!/dls_sw/tools/bin/python2.4

# Test suite to use with pyUnit

import sys
sys.path.insert(0,'/dls_sw/work/common/python/autotestframework/dist/dls.autotestframework-0.0-py2.4.egg')
from pkg_resources import require
#require('dls.autotestframework==1.13')
from dls.autotestframework import *

################################################
# Test suite for the MKS 937A Gauge Controller
    
class mks937aTestSuite(TestSuite):

    def createTests(self):
        # Define the targets for this test suite
        Target("simulation", self,
            iocDirectory="iocs/simulation",
            iocBootCmd="bin/linux-x86/stsimulation.boot",
            runIocInScreenUnderHudson=True,
            epicsDbFiles="db/simulation.db",
            simDevices=[SimDevice("mks937a", 9001, rpc=True)],
            environment=[('EPICS_CA_REPEATER_PORT','6065'),
                ('EPICS_CA_SERVER_PORT','6064')],
            guiCmds=[r'edm -x -eolc -m "P=MKS937ASIM-01" data/mks937a.edl'])

        # The tests
        CaseGetFrequency(self)
        
################################################
# Intermediate test case class that provides some utility functions
# for this suite

class mks937aCase(TestCase):
    base_pvname = "MKS937ASIM-01"
    pv_getfreq  = base_pvname+":F"
        
        
################################################
# Test cases
    
class CaseGetFrequency(mks937aCase):
    def runTest(self):
        print "mks937aTestSuite - CaseGetFrequency()"
        '''The GetFrequency test'''
        if self.simulationDevicePresent("mks937a"):
            self.diagnostic("frequency read = %s" % (self.getPv(self.pv_getfreq)),1)
            f = self.getPv(self.pv_getfreq)
            self.verifyInRange(f, 50, 60)

            
################################################
# Main entry point

if __name__ == "__main__":
    # Create and run the test sequence
    mks937aTestSuite()

    
