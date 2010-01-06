from iocbuilder import SetSimulation, AutoSubstitution, Substitution
from iocbuilder.modules.streamDevice import AutoProtocol

class mks937a(AutoSubstitution, AutoProtocol):    
    TemplateFile = 'mks937a.template'    
    ProtocolFiles = ['mks937a.protocol']
                   
class mks937a_sim(Substitution):
    TemplateFile = 'simulation_mks937a.template'    
    
SetSimulation(mks937a, mks937a_sim)     

class mks937aImg(AutoSubstitution):
    TemplateFile = 'mks937aImg.template'

class mks937aPirg(AutoSubstitution):
    TemplateFile = 'mks937aPirg.template'

try:
    # try to make some simulations, but need pressArr
    from iocbuilder.modules.pressArr_subrec import pressArr
    
    class mks937aImg_sim(Substitution):
        Dependencies = (pressArr,)
        TemplateFile = 'simulation_mks937aImg.template'        
    SetSimulation(mks937aImg, mks937aImg_sim)         

    class mks937aPirg_sim(Substitution):
        Dependencies = (pressArr,)
        TemplateFile = 'simulation_mks937aPirg.template'        
    SetSimulation(mks937aPirg, mks937aPirg_sim)         

except ImportError:
    print "# pressarr not included, cannot make mks937a simulations"

                                                                                                            
class mks937aGauge(AutoSubstitution):

    def __init__(self, id, **args):
        # make sure the id is a 2 digit int
        args['id'] = "%02d" % int(id)
        self.__super.__init__(**args)
        
    TemplateFile = 'mks937aGauge.template'    

class mks937aGauge_sim(Substitution):
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

