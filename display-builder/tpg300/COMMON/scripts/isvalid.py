from org.csstudio.display.builder.runtime.script import PVUtil
from org.csstudio.display.builder.model.properties import NamedWidgetColor
from org.csstudio.display.builder.model.persist import WidgetColorService

try:
	if PVUtil.getSeverityString(pvs[0]) != "INVALID" and PVUtil.getLong(pvs[0]) == 1:
		color = WidgetColorService.getColor("Background")
	else:
		raise Exception()
except:
	color = WidgetColorService.getColor("INVALID")

widget.setPropertyValue('background_color', color)
