
value = data.get('value')

#creates entity on button press
#hass.states.set('group.panel3', value)

#create remote(script.dummy_panel) entity on button press
panelAttributes = {'entity_id': ('script.dummy_panel',), 'view': 'yes'}
hass.states.set('group.'+value,'hello', attributes=panelAttributes)

logger.info("Executing the {0} script.".format(value))
hass.bus.fire(value, { "wow": "from a Python script!" })


