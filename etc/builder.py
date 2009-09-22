from iocbuilder import Substitution
from iocbuilder.arginfo import *
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.modules.asyn import AsynOctetInterface

class mks937a(Substitution, AutoProtocol):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, device, port):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        device = Simple('Description for device', str),
        port   = Ident ('Asyn Port', AsynOctetInterface))

    # Substitution attributes
    TemplateFile = 'mks937a.template'
    Arguments = ArgInfo.Names()

    # AutoProtocol attributes
    ProtocolFiles = ['mks937a.protocol']


class mks937aPirg(Substitution, AutoProtocol):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, device, channel, port):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        device  = Simple('Description for device', str),
        channel = Simple('Description for channel', str),
        port    = Ident ('Asyn Port', AsynOctetInterface))

    # Substitution attributes
    TemplateFile = 'mks937aPirg.template'
    Arguments = ArgInfo.Names()

    # AutoProtocol attributes
    ProtocolFiles = ['mks937a.protocol']


class mks937aPirgGroup(Substitution):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, device, pirg1, pirg2, pirg3, pirg4, pirg5, pirg6, pirg7, pirg8):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        device = Simple('Description for device', str),
        pirg1  = Simple('Description for pirg1', str),
        pirg2  = Simple('Description for pirg2', str),
        pirg3  = Simple('Description for pirg3', str),
        pirg4  = Simple('Description for pirg4', str),
        pirg5  = Simple('Description for pirg5', str),
        pirg6  = Simple('Description for pirg6', str),
        pirg7  = Simple('Description for pirg7', str),
        pirg8  = Simple('Description for pirg8', str))

    # Substitution attributes
    TemplateFile = 'mks937aPirgGroup.template'
    Arguments = ArgInfo.Names()


class mks937aImg(Substitution, AutoProtocol):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, device, channel, port):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        device  = Simple('Description for device', str),
        channel = Simple('Description for channel', str),
        port    = Ident ('Asyn Port', AsynOctetInterface))

    # Substitution attributes
    TemplateFile = 'mks937aImg.template'
    Arguments = ArgInfo.Names()

    # AutoProtocol attributes
    ProtocolFiles = ['mks937a.protocol']


class mks937aImgGroup(Substitution):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, device, delay, img1, img2, img3, img4, img5, img6, img7, img8):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        device = Simple('Description for device', str),
        delay  = Simple('Description for delay', str),
        img1   = Simple('Description for img1', str),
        img2   = Simple('Description for img2', str),
        img3   = Simple('Description for img3', str),
        img4   = Simple('Description for img4', str),
        img5   = Simple('Description for img5', str),
        img6   = Simple('Description for img6', str),
        img7   = Simple('Description for img7', str),
        img8   = Simple('Description for img8', str))

    # Substitution attributes
    TemplateFile = 'mks937aImgGroup.template'
    Arguments = ArgInfo.Names()


class mks937aImgMean(Substitution):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, device, nimgs, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, current):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        device  = Simple('Description for device', str),
        nimgs   = Simple('Description for nimgs', str),
        img1    = Simple('Description for img1', str),
        img2    = Simple('Description for img2', str),
        img3    = Simple('Description for img3', str),
        img4    = Simple('Description for img4', str),
        img5    = Simple('Description for img5', str),
        img6    = Simple('Description for img6', str),
        img7    = Simple('Description for img7', str),
        img8    = Simple('Description for img8', str),
        img9    = Simple('Description for img9', str),
        img10   = Simple('Description for img10', str),
        current = Simple('Description for current', str))

    # Substitution attributes
    TemplateFile = 'mks937aImgMean.template'
    Arguments = ArgInfo.Names()


class mks937aImgDummy(Substitution):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, device):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        device = Simple('Description for device', str))

    # Substitution attributes
    TemplateFile = 'mks937aImgDummy.template'
    Arguments = ArgInfo.Names()


class mks937aGauge(Substitution):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, dom, id, c, s):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        dom = Simple('Description for dom', str),
        id  = Simple('Description for id', str),
        c   = Simple('Description for c', str),
        s   = Simple('Description for s', str))

    # Substitution attributes
    TemplateFile = 'mks937aGauge.template'
    Arguments = ArgInfo.Names()


class mks937aGaugeGroup(Substitution):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, device, gauge1, gauge2, gauge3, gauge4, gauge5, gauge6, gauge7, gauge8, dom, id):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        device = Simple('Description for device', str),
        gauge1 = Simple('Description for gauge1', str),
        gauge2 = Simple('Description for gauge2', str),
        gauge3 = Simple('Description for gauge3', str),
        gauge4 = Simple('Description for gauge4', str),
        gauge5 = Simple('Description for gauge5', str),
        gauge6 = Simple('Description for gauge6', str),
        gauge7 = Simple('Description for gauge7', str),
        gauge8 = Simple('Description for gauge8', str),
        dom    = Simple('Description for dom', str),
        id     = Simple('Description for id', str))

    # Substitution attributes
    TemplateFile = 'mks937aGaugeGroup.template'
    Arguments = ArgInfo.Names()


class mks937aInterlock(Substitution):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, interlock, name, high, low, level):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        interlock = Simple('Description for interlock', str),
        name      = Simple('Description for name', str),
        high      = Simple('Description for high', str),
        low       = Simple('Description for low', str),
        level     = Simple('Description for level', str))

    # Substitution attributes
    TemplateFile = 'mks937aInterlock.template'
    Arguments = ArgInfo.Names()


class simulation_mks937aGauge(Substitution):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, dom, id):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        dom = Simple('Description for dom', str),
        id  = Simple('Description for id', str))

    # Substitution attributes
    TemplateFile = 'simulation_mks937aGauge.template'
    Arguments = ArgInfo.Names()


class simulation_mks937aImg(Substitution, AutoProtocol):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, device, channel, port):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        device  = Simple('Description for device', str),
        channel = Simple('Description for channel', str),
        port    = Ident ('Asyn Port', AsynOctetInterface))

    # Substitution attributes
    TemplateFile = 'simulation_mks937aImg.template'
    Arguments = ArgInfo.Names()

    # AutoProtocol attributes
    ProtocolFiles = ['mks937a.protocol']


class simulation_mks937aPirg(Substitution, AutoProtocol):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, device, channel, port):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        device  = Simple('Description for device', str),
        channel = Simple('Description for channel', str),
        port    = Ident ('Asyn Port', AsynOctetInterface))

    # Substitution attributes
    TemplateFile = 'simulation_mks937aPirg.template'
    Arguments = ArgInfo.Names()

    # AutoProtocol attributes
    ProtocolFiles = ['mks937a.protocol']


class simulation_mks937a(Substitution, AutoProtocol):
    '''A brief description for this class goes here'''

    # The __init__ method specifies arguments and defaults
    def __init__(self, device, port):
        # Filter the list of local variables by the argument list,
        # then initialise the super class
        self.__super.__init__(**filter_dict(locals(), self.Arguments))

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        device = Simple('Description for device', str),
        port   = Ident ('Asyn Port', AsynOctetInterface))

    # Substitution attributes
    TemplateFile = 'simulation_mks937a.template'
    Arguments = ArgInfo.Names()

    # AutoProtocol attributes
    ProtocolFiles = ['mks937a.protocol']


