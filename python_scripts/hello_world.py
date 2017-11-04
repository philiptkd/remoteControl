value = data.get('value')

#get input text for new entity id
entity_id = hass.states.get('input_text.add_device_name').state
entity_id = entity_id.lower()

#get list of group entity IDs
group_id_list = hass.states.entity_ids(domain_filter='group')

#if the input text was empty
if(entity_id == ''):
    #get first unused remote# entity ID
    i = 0
    while('group.remote'+str(i) in group_id_list):
        i = i + 1
    entity_id = 'remote'+str(i)

logger.info(group_id_list)
logger.info(entity_id)

#if there is not already a device with this name
if('group.' + entity_id not in group_id_list):
    #create remote(script.dummy_panel) entity on button press
    #panelAttributes = {'entity_id': ('script.dummy_panel',), 'view': 'yes'}
    panelAttributes = {'entity_id': 'group.'+entity_id, 'entities': ['script.'+entity_id], 'view': 'yes'}
    hass.states.set('group.'+entity_id,'hello', attributes=panelAttributes)

    #add option input select for deleting devices
    state = hass.states.get('input_select.delete_device_select')
    attributes = state.attributes
    attributes['options'].append(entity_id)

    #set the new state of the input select
    hass.states.set('input_select.delete_device_select', state.state, attributes=attributes, force_update=True)

#print to logger
logger.info("Executing the {0} script.".format(value))
hass.bus.fire(value, { "wow": "from a Python script!" })
