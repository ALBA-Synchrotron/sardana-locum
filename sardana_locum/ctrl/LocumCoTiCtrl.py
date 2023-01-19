import logging
import numpy
import PyTango
from sardana.pool.controller import (CounterTimerController, Type, Access,
                                     Description, DefaultValue)
from sardana.tango.core.util import from_tango_state_to_state

from sardana_adlink.ctrl.AdlinkAICoTiCtrl import AdlinkAICoTiCtrl

def evalState(state):
    """This function converts Adlink device states into counters state."""
    if state == PyTango.DevState.RUNNING:
        return State.Moving
    elif state == PyTango.DevState.STANDBY:
        return State.On
    else:
        return from_tango_state_to_state(state)
    

class LocumCoTiCtrl(AdlinkAICoTiCtrl):
    """This class is the Sardana CounterTimer controller for the LoCum4.
    """
    
    MaxDevice = 5
    ctrl_properties = {
        'AdlinkAIDeviceName': {
            Description: 'AdlinkAI Tango device',
            Type: 'PyTango.DevString'
        },
        'LoCum4DeviceName': {
            Description: 'LoCum4 Tango device',
            Type: 'PyTango.DevString'
        },
        'SampleRate': {
            Description: 'SampleRate set for AIDevice',
            Type: 'PyTango.DevLong'
        },
        'SkipStart': {
            Description: 'Flag to skip if DS does not start',
            Type: str,
            DefaultValue: 'true'
        }
    }
    
    def __init__(self, inst, props, *args, **kwargs):

        AdlinkAICoTiCtrl.__init__(self,inst,props, *args, **kwargs)

        try:
            self.Locum = PyTango.DeviceProxy(self.LoCum4DeviceName)
        except PyTango.DevFailed as e:
            pass
            self._log.error("__init__(): Could not create a device proxy from following device name: %s.\nException: %s",
                            self.LoCum4DeviceName, e)
            raise
        
    def ReadOne(self, axis):
        stateLoc = self.Locum.state() 
        mean = 1e-100
        if axis == 1:
            return self.intTime
        if stateLoc == PyTango.DevState.ON: 
            mean = self.Locum["I%s"%(axis-1)].value
        return mean
            
        
