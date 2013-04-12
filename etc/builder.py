from iocbuilder import SetSimulation, AutoSubstitution, Substitution
from iocbuilder.arginfo import *
from iocbuilder.modules.streamDevice import AutoProtocol

class mks937a(AutoSubstitution, AutoProtocol):
    TemplateFile = 'mks937a.template'
    ProtocolFiles = ['mks937a.protocol']

class _mks937aImg_template(AutoSubstitution):
    TemplateFile = 'mks937aImg.template'

class _mks937aPirg_template(AutoSubstitution):
    TemplateFile = 'mks937aPirg.template'

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
    
