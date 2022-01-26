from org.csstudio.display.builder.runtime.script import PVUtil, ScriptUtil

valid = pvs[0]
type  = pvs[1]
chan  = pvs[2]

if PVUtil.getLong(valid):
    widget.setPropertyValue("text", PVUtil.getString(chan))
    widget.setPropertyValue("transparent", "true")
else:
    widget.setPropertyValue("text", PVUtil.getString(type) + " @ " + PVUtil.getString(chan))
    widget.setPropertyValue("transparent", "false")

widget.setPropertyValue("tooltip", "Gauge " + PVUtil.getString(type) + " @ channel " + PVUtil.getString(chan))
