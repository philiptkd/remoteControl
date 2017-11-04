#get list of group entity IDs
group_id_list = hass.states.entity_ids(domain_filter='group')

#get first unused remote# entity ID
i = 0
while('group.remote'+str(i) in group_id_list):
    i = i + 1
entity_id = 'remote'+str(i)

#get argument passed
value = data.get('value')

#create remote(script.dummy_panel) entity on button press
panelAttributes = {'entity_id': ('script.dummy_panel',), 'view': 'yes'}
hass.states.set('group.'+entity_id,'hello', attributes=panelAttributes)

#add option input select for deleting devices
state = hass.states.get('input_select.delete_device')
attributes = state.attributes
attributes['options'].append(entity_id)

#convert newAttributes to dict
hass.states.set('input_select.delete_device','Select Device to Delete', attributes=attributes)

#print to logger
logger.info("Executing the {0} script.".format(value))
hass.bus.fire(value, { "wow": "from a Python script!" })
