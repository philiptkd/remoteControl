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
    #create empty script entity to hold signal buttons
    scriptAttr = {}
    scriptAttr['custom_ui_state_card'] = 'state-card-button-panel'
    configDict = {'columns': 3, 'cell_height': '75px', 'cell_width': '75px', 'entities': []}
    scriptAttr['config'] = configDict
    hass.states.set('script.'+entity_id, 'on', attributes=scriptAttr, force_update=True)

    #create group
    panelAttributes = {'entity_id': ['script.'+entity_id, 'group.add_signal'], 'view': 'yes'}
    hass.states.set('group.'+entity_id,'hello', attributes=panelAttributes, force_update=True)

    #rename group.add_signal and its parts,
      # input_text.add_signal_name and script.add_signal_button
    service_data = {'entity_id': 'group.add_signal', 'view_name': entity_id}
    hass.services.call('python_script', 'rename', service_data=service_data, blocking=True)
    newGroupEntityId = 'group.add_signal'+'_'+entity_id

    #put the new group into the view
    panelAttributes = {'entity_id': ['script.'+entity_id, newGroupEntityId], 'view': 'yes'}
    hass.states.set('group.'+entity_id, 'hello', attributes=panelAttributes, force_update=True)

    #add option input select for deleting devices
    state = hass.states.get('input_select.delete_device_select')
    attributes = state.attributes
    attributes['options'].append(entity_id)

    #set the new state of the input select
    hass.states.set('input_select.delete_device_select', state.state, attributes=attributes, force_update=True)

#print to logger
logger.info("Executing the {0} script.".format(value))
hass.bus.fire(value, { "wow": "from a Python script!" })
