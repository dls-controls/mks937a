###########################################################
# Pete Owens 7/1/04 vxWorks/EPICS startup file, 
# Example to test simulated mks937a stream device application
#

mks937aTop = "/home/pho76/diamond/mks937a"
#mks937aTop = "/home/diamond/R3.13.9/work/support/mks937a/Rx-y"
diamondTop = "/home/diamond/R3.13.9/prod/support/superTop/Rx-y"

###########################################################

cd diamondTop
cd "bin/ppc604" 
ld < iocCore
ld < baseLib   
ld < pressArrLib
ld < genSubRecord.o

cd mks937aTop
cd "bin/ppc604"
ld < mks937aMean.o

###########################################################

cd diamondTop
cd "dbd" 
dbLoadDatabase "baseApp.dbd"
dbLoadDatabase "genSubRecord.dbd"

###########################################################
# Load the databses & start the IOC
#
cd mks937aTop
cd "example"

dbLoadTemplate "simulation_mks937a.substitutions"

iocInit

###########################################################
