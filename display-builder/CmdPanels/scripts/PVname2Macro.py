from org.csstudio.display.builder.runtime.script import PVUtil

channel = PVUtil.getString(pvs[0])

# Remove the last part of the name
channel = channel.replace(':sRdV','')

# Adding the macros on the widget that will consume this script
widget.getPropertyValue("macros").add("AI2Macro", channel)

widget.setPropertyValue("file", "")
widget.setPropertyValue("file", "./Cstat-AI-sim.bob")
