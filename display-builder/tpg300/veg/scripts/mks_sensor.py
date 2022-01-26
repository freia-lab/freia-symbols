from org.csstudio.display.builder.runtime.script import PVUtil, ScriptUtil

tooltip    = "$(pv_name)\n$(pv_value)"
visible    = True
width      = 49

sensor_type = pvs[0]
sensor_name = pvs[1]

try:
    sensor_x2 = pvs[2]
except IndexError:
    sensor_x2 = None


# Add sensor name to tooltip
try:
    name    = PVUtil.getString(sensor_name)
    tooltip = tooltip + "\n{}".format(name)
except:
    pass


# Hide the A2, B2, C2 sensor if type is ''
if sensor_x2 is None:
    try:
        if PVUtil.getString(sensor_type) == "":
            visible = False
    except:
        pass

# Hide the A1, B1, C1 sensor if x2 is '' and x1 is 'NC'
# Enlarge A1, B1, C1 sensor if x2 is ''
else:
    try:
        if PVUtil.getString(sensor_x2) == '':
            if PVUtil.getString(sensor_type) == "NC":
                visible = False
            else:
                width = 104
    except:
        pass


widget.setPropertyValue("tooltip", tooltip)
widget.setPropertyValue("visible", visible)
widget.setPropertyValue("width",   width)
