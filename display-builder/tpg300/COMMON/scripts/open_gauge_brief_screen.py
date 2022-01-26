from org.csstudio.display.builder.runtime.script import PVUtil
from org.csstudio.display.builder.runtime.script import ScriptUtil
from org.csstudio.display.builder.runtime.pv import PVFactory

################################################################################
#
# This script checks the `CONTROLLER_TYPE` macro and based on its value
# determines the path to the correct faceplate, sets up the `DEVICENAME` macro
# and opens the faceplate OPI
#
# Input PVs:
# -none-
#
################################################################################
macros = widget.getEffectiveMacros()
macros.expandValues(macros)

mks = macros.getValue("FACEPLATE_MKS")
tpg = macros.getValue("FACEPLATE_TPG")

def bob_path(typ):
    if "tpg" in typ.lower():
        path = tpg
    elif "mks" in typ.lower():
        path = mks
    else:
        path = mks
        ScriptUtil.getLogger().severe("Cannot determine controller type: '{}', Falling back to MKS faceplate".format(typ))

    return path


controller_type = macros.getValue("CONTROLLER_TYPE")
if controller_type:
    path = bob_path(controller_type)
else:
    path = mks
    ScriptUtil.getLogger().severe("Falling back to mks faceplate")


devicename = macros.getValue("vacPREFIX")
macros.add("DEVICENAME", devicename)
dmacros = dict()
for k in macros.getNames():
    dmacros[k] = macros.getValue(k)

ScriptUtil.openDisplay(widget, path, "STANDALONE", dmacros)
