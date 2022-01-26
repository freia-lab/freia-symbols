from org.csstudio.display.builder.runtime.script import PVUtil
from org.csstudio.display.builder.runtime.script import ScriptUtil
from org.phoebus.ui.vtype import FormatOption, FormatOptionHandler

################################################################################
#
# This script takes the pressure and pressure status and displays them as the
# widget's tooltip
#
# Input PVs:
# * pvs[0] - PrsStatR
# * pvs[1] - PrsR
# * pvs[2] - PrR-STR
#
################################################################################

tooltip  = "N/A"

# Compatibility with 4.6.3
try:
    PVUtil.PVHasNoValueException
except:
    setattr(PVUtil, 'PVHasNoValueException', Exception)

try:
    pvStat   = PVUtil.getString(pvs[0]).upper()

    if pvStat == "ON" or pvStat == "OVER-RANGE" or pvStat == "UNDER-RANGE":
        vtype = PVUtil.getVType(pvs[1])
        tooltip = FormatOptionHandler.format(vtype, FormatOption.EXPONENTIAL, 2, True)
    else:
        tooltip = PVUtil.getString(pvs[2])
except PVUtil.PVHasNoValueException:
    pass
except Exception as e:
    ScriptUtil.getLogger().severe(str(e))

widget.setPropertyValue("tooltip", tooltip)
