TOP=../..

ifdef EPICS_HOST_ARCH

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# In a Diamond Support Module, install
# templates like this
#
DB += mks937a.template
DB += mks937aPirg.template
DB += mks937aPirgGroup.template
DB += mks937aImg.template
DB += mks937aImgGroup.template
DB += mks937aImgMean.template
DB += mks937aGauge.template
DB += mks937aGaugeGroup.template

#----------------------------------------------------
# In a Diamond IOC Application, build db files from
# template files like this
#
#DB += BL06I-MO-IOC-01.db
#DB += BL06I-MO-IOC-01_sim.db

#USES_TEMPLATE += $(MOTOR)/db/motor.template
#USES_TEMPLATE += $(MOTOR)/db/basic_motor.template

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

else

include $(TOP)/config/CONFIG_APP
include $(TOP)/config/RULES_ARCHS

endif
