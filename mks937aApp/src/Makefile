TOP=../..

ifdef EPICS_HOST_ARCH

include $(TOP)/configure/CONFIG

USR_CFLAGS += -DEPICS_R3_14

#==================================================
# build a mks937a library
#

LIBRARY_IOC_vxWorks += mks937a

# install support.dbd into <top>/dbd
DBD += mks937a.dbd

mks937a_DBD += base.dbd
mks937a_DBD += genSubRecord.dbd
mks937a_DBD += mks937aRegister.dbd

# specify all source files to be compiled and added to the library
mks937a_SRCS += mks937aMean.c

mks937a_LIBS += $(EPICS_BASE_IOC_LIBS)

DATA += mks937a_sim.py

include $(TOP)/configure/RULES

else

#===========================
#Build 3.13 stuff

include $(TOP)/config/CONFIG_APP
include $(TOP)/config/RULES_ARCHS

endif


#===========================

