from org.csstudio.display.builder.runtime.script import PVUtil

tooltip = "$(pv_name)\n$(pv_value)"

try:
    pvStat   = PVUtil.getString(pvs[0]).upper()
    pvPrsStr = pvs[1]

    if pvStat != "ON" and pvStat != "OPEN": # and pvStat != "UNDER-RANGE" and pvStat != "OVER-RANGE":
        tooltip += "\n" + PVUtil.getString(pvPrsStr)
except:
    pass

widget.setPropertyValue("tooltip", tooltip)
