from org.csstudio.display.builder.runtime.script import PVUtil
from org.csstudio.display.builder.runtime.script import ScriptUtil
from org.csstudio.display.builder.runtime.pv import PVFactory

macros = widget.getEffectiveMacros()
macros.expandValues(macros)

tpg300 = macros.getValue("FACEPLATE_300")
tpg500 = macros.getValue("FACEPLATE_500")

def bob_path(typ):
    typ = typ.lower()
    if "tpg" not in typ:
        return None

    if "500" in typ:
        path = tpg500
    elif "300" in typ:
        path = tpg300
    else:
        path = tpg300
        ScriptUtil.getLogger().severe("Cannot determine controller type: '{}', Falling back to TPG-300 faceplate".format(typ))

    return path


controller      = macros.getValue("CONTROLLER")
controller_type = macros.getValue("CONTROLLER_TYPE")
try:
    gaugePV = PVFactory.getPV("{}:iUITypeR".format(controller))
    gauge = gaugePV.read()
    PVFactory.releasePV(gaugePV)
    gauge = gauge.value
    path = bob_path(gauge)
except Exception as e:
    ScriptUtil.getLogger().severe(str(e))
    if controller_type:
        path = bob_path(controller_type)
    else:
        path = tpg300
        ScriptUtil.getLogger().severe("Falling back to TPG-300 faceplate")


macros.add("DEVICENAME", controller)
dmacros = dict()
for k in macros.getNames():
    dmacros[k] = macros.getValue(k)

ScriptUtil.openDisplay(widget, path, "STANDALONE", dmacros)
