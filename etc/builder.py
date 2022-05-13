from iocbuilder import SetSimulation, AutoSubstitution, Substitution, Device
from iocbuilder.arginfo import *
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.modules.calc import Calc
from iocbuilder.modules.genSub import GenSub

class mks937aLib(Device):
    LibFileList = ['mks937a']
    DbdFileList = ['mks937a']
    AutoInstantiate = True
class mks937a(AutoSubstitution, AutoProtocol):
    Dependencies = (Calc,GenSub,mks937aLib)
    TemplateFile = 'mks937a.template'
    ProtocolFiles = ['mks937a.protocol']

class _mks937aImg_template(AutoSubstitution):
    TemplateFile = 'mks937aImg.template'

class _mks937aPirg_template(AutoSubstitution):
    TemplateFile = 'mks937aPirg.template'

class _mks937aGauge_template(AutoSubstitution):
    TemplateFile = 'mks937aGauge.template'
class _mks937aPlogEGU_template(AutoSubstitution):
    TemplateFile = 'mks937aPlogEGU.template'


class mks937aImg(_mks937aImg_template):
    def __init__(self, GCTLR, **args):
        # get port from GCTLR
        args['port'] = GCTLR.args['port']
        self.__super.__init__(**args)

    # construct the ArgInfo
    ArgInfo = makeArgInfo(__init__,
        GCTLR = Ident('Parent mks937a object', mks937a)) + \
        _mks937aImg_template.ArgInfo.filtered(without = ('port'))
        

class mks937aPirg(_mks937aPirg_template):
    def __init__(self, GCTLR, **args):
        # get port from GCTLR
        args['port'] = GCTLR.args['port']
        self.__super.__init__(**args)

    # construct the ArgInfo
    ArgInfo = makeArgInfo(__init__,
        GCTLR = Ident('Parent mks937a object', mks937a)) + \
        _mks937aPirg_template.ArgInfo.filtered(without = ('port'))

class mks937aGauge(AutoSubstitution):

    def __init__(self, id, **args):
        # make sure the id is a 2 digit int
        args['id'] = "%02d" % int(id)
        self.__super.__init__(**args)

    TemplateFile = 'mks937aGauge.template'

class mks937aGaugeEGU(Device,):

    def __init__(self,name, dom,id,input):
        self.__super.__init__()
        self.name = name
        self.dom = dom
        self.id = "%02d" % int(id)
        self.input = input
    
        self.eguInputPV = "{}-VA-GAUGE-{}:PLOG_CALC".format(self.dom,self.id)

        _mks937aPlogEGU_template(device=self.eguInputPV,p_egu_pv=self.input)
        _mks937aGauge_template(GCTLR="",c="",s="", dom=self.dom,id=self.id,aitype="Soft Channel",aiinp="{} CP".format(self.eguInputPV))
    
    ArgInfo = makeArgInfo(__init__,
        name = Simple("Device name", str),
        dom = Simple("Domain 5 char string (e.g. BL11I)", str),
        id = Simple("ID number as 2 digit string (e.g. 01)",int),
        input = Simple("PV providing gauge reading in mbar",str)
    )

class mks937aGauge_sim(AutoSubstitution):
    WarnMacros = False
    TemplateFile = 'simulation_mks937aGauge.template'
SetSimulation(mks937aGauge, mks937aGauge_sim) 

# The following create groups that can be used in vacuum spaces
class mks937aGaugeGroup(AutoSubstitution):
    TemplateFile = 'mks937aGaugeGroup.template'

class mks937aImgGroup(AutoSubstitution):
    TemplateFile = 'mks937aImgGroup.template'

class mks937aPirgGroup(AutoSubstitution):
    TemplateFile = 'mks937aPirgGroup.template'

class mks937aImgDummy(AutoSubstitution):
    TemplateFile = 'mks937aImgDummy.template'

class mks937aPirgDummy(AutoSubstitution):
    TemplateFile = 'mks937aPirgDummy.template'
    
