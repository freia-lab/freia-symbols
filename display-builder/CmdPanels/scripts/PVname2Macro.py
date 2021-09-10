from org.csstudio.display.builder.runtime.script import PVUtil

channel = PVUtil.getString(pvs[0])

# Remove the last part of the name
if ":sRdV" in channel:
#    print("Analog")
    channel = channel.replace(':sRdV','')
# Adding the macros on the widget that will consume this script
    widget.getPropertyValue("macros").add("AI2Macro", channel)
    widget.setPropertyValue("file", "")
    widget.setPropertyValue("file", "./Cstat-AI-sim.bob")
elif ":sInp" in channel or ":sProcInp" in channel:
#    print("Digital")
    channel = channel.replace(':sInp','')
    channel = channel.replace(':sProcInp','')
    widget.getPropertyValue("macros").add("DI2Macro", channel)
    widget.setPropertyValue("file", "")
    widget.setPropertyValue("file", "./Cstat-DI-sim.bob")
else:
    widget.getPropertyValue("macros").add("AI2Macro", "")
    widget.getPropertyValue("macros").add("DI2Macro", "")
#    print("Unsupported PV name")
# Adding the macros on the widget that will consume this script
#widget.getPropertyValue("macros").add("AI2Macro", channel)

#widget.setPropertyValue("file", "")
#widget.setPropertyValue("file", "./Cstat-AI-sim.bob")
