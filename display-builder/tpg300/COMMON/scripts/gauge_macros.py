from org.csstudio.display.builder.runtime.script import PVUtil
from org.csstudio.display.builder.runtime.script import ScriptUtil

################################################################################
#
# This script sets macros based on PV values:
# * `CONTROLLER` and `CONTROLLERNAME` to the ESS name of the gauge controller
# * `CONTROLLER_TYPE` to the UI type of the gauge controller
# * `MODULE` to the name of the measurement board the gauge is connected to
#
# Input PVs:
# * pvs[0] - CtrlNameR
# * pvs[1] - CtrlUITypeR
# * pvs[2] - ModuleNameR
#
################################################################################
macros = widget.getEffectiveMacros()
macros.expandValues(macros)

try:
    controllername = PVUtil.getString(pvs[0])
    macros.add("CONTROLLER", controllername)
    macros.add("CONTROLLERNAME", controllername)
except Exception as e:
    ScriptUtil.getLogger().severe("{}: {}".format(pvs[0], e))

try:
    uitype = PVUtil.getString(pvs[1])
    macros.add("CONTROLLER_TYPE", uitype)
except Exception as e:
    ScriptUtil.getLogger().severe("{}: {}".format(pvs[1], e))

try:
    modulename = PVUtil.getString(pvs[2])
    macros.add("MODULE", modulename)
except Exception as e:
    ScriptUtil.getLogger().severe("{}: {}".format(pvs[2], e))

widget.propMacros().setValue(macros)
