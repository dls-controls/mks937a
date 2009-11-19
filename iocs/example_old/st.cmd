###########################################################
# Pete Owens 28/8/03 vxWorks/EPICS startup file, 
# Example to test mks937a stream device application
# This IOC is configured for :
#       Hytec IP Carrier 8002 card in slot 7 - 
#       Hytec 8515 Octal serial module in slot B
#	MKS 937A units on ports 0 & 1
#

mks937aTop = "/home/pho76/diamond/mks937a"
#mks937aTop = "/home/diamond/R3.13.9/work/support/mks937a/Rx-y"
diamondTop = "/home/diamond/R3.13.9/prod/support/superTop/Rx-y"

IPSLOTA = 0
IPSLOTB = 1
IPSLOTC = 2
IPSLOTD = 3

###########################################################
# Configure serial port number here
#  
TYVMESLOT = 7
TYIPSLOT  = IPSLOTB
TYPORTNUM = 0
TYCARDNUM = (10 * TYVMESLOT) + TYIPSLOT

AIVMESLOT = 5
AIIPSLOT  = IPSLOTA
AICARDNUM = (10 * AIVMESLOT) + AIIPSLOT

###########################################################

cd diamondTop
cd "bin/ppc604" 
ld < iocCore
ld < baseLib   
ld < streamLib
ld < utilityLib
ld < streamTty.o
ld < ipacLib
ld < drvHy8515.o
ld < tyGSOctal.o
ld < Hy8401ipLib

###########################################################

cd diamondTop
cd "dbd" 
dbLoadDatabase "baseApp.dbd"
dbLoadDatabase "drvIpac.dbd" 
dbLoadDatabase "stream.dbd" 
dbLoadDatabase "Hy8401ip.dbd" 

###########################################################
# Configure a Hytec 8002 carrier VME slot 4 for the ADC
# and another one in slot 4 for the octal serial card
#
#                        vmeslotnum, IPintlevel, HSintnum
ARGS = malloc (10)
IVEC = newInterruptVector ()
sprintf (ARGS, "%d %d %d", AIVMESLOT, 2, IVEC)
AICARRIER = ipacEXTAddCarrier (&EXTHy8002, ARGS)

IVEC = newInterruptVector ()
sprintf (ARGS, "%d %d %d", TYVMESLOT, 2, IVEC)
TYCARRIER = ipacEXTAddCarrier (&EXTHy8002, ARGS)

###########################################################
# Hytec 8401 ADC in slot C of the IP carrier card. 
#
# Configure module on carrier 4, slot 2
# Params are : 
#	cardnum, 
#	vmeslotnum, 
#	ipslotnum, 
#	vectornum,   (0: find a vector)
#	itrState,    (enable interupts at init) 
#	aiType,	     (0: differential)
#	clockSource, (0: internal)
#	clockRate,   (15: 100000Hz)
#	inhibit,     (0: disables front panel inhibit ) 
#	samples,     (1: no averaging -use registers)
#	spacing,     (spacing between samples to average for ai) 
#	trigger	     (0: continuous)

IVEC = newInterruptVector ()
Hy8401ipConfigure (AICARDNUM, AICARRIER, AIIPSLOT, IVEC, 0, 0, 0, 15, 0, 1, 1, 0)

###########################################################
# Hytec 8515 IPOctal serial module in slot B on the IP carrier card. 
#
# Configure module on carrier 7, slot 1
# Params are : 
#	cardnum, 
#	vmeslotnum, 
#	ipslotnum, 
#	vectornum, 
#	intdelay (-ve => FIFO interrupt), 
#	halfduplexmode, 
#	delay845
#
IVEC = newInterruptVector ()
TYMODNUM = Hy8515Configure (TYCARDNUM, TYCARRIER, TYIPSLOT, IVEC, -32, 0, 0)

# Create devices
# Params are :
#	name
#	card number
#	port number
#	read buffer size
#	write buffer size
#
MKSPORT = tyHYOctalDevCreate("/ty/mks/0", TYMODNUM, TYPORTNUM, 2500, 250)

tyHYOctalConfig (MKSPORT, 9600, 'E', 1, 8, 'N')

###########################################################
# Configure stream device
#
STREAM_PROTOCOL_DIR = malloc (100)
strcpy (STREAM_PROTOCOL_DIR, mks937aTop)
strcat (STREAM_PROTOCOL_DIR, "/mks937aApp/protocol")

ty_mks_0_streamBus = "Tty"

###########################################################
# Load the databses & start the IOC
#
cd mks937aTop
cd "example"

dbLoadTemplate "mks937a.substitutions"

iocInit

###########################################################
