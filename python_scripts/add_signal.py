add_signal_button_name = data.get('value')
view_name = add_signal_button_name[len('script.add_signal_button_'):]
input_text_name = 'input_text.add_signal_name_'+view_name
#input_text = hass.states.get('input_text.add_device_name').state
input_text = hass.states.get(input_text_name).state

container_name = 'script.'+view_name
attributes = hass.states.get(container_name).attributes

logger.info('input_text_name: ' + input_text_name + '\ninput_text: ' + input_text + '\ncontainer_name: ' + container_name)

#don't do anything if this signal button already exists on this device
found_flag = 0
for entity in attributes['config']['entities']:
    if(entity['caption'] == input_text):
        logger.info('button '+input_text+' already exists on '+view_name)
        found_flag = 1

if(found_flag == 0):
    newAttributes = {}
    newAttributes['custom_ui_state_card'] = attributes['custom_ui_state_card']
    configDict = {}
    for configKey in attributes['config'].keys():
        if(configKey != 'entities'):
            configDict[configKey] = attributes['config'][configKey]
    entitiesList = attributes['config']['entities']
    entitiesList.append({'entity': 'script.signal_button', 'caption': input_text, 'data': {'value': view_name+'_'+input_text}})
    configDict['entities'] = entitiesList
    newAttributes['config'] = configDict

    hass.states.set(container_name, 'on', attributes=newAttributes, force_update=True)

    #add option in input_select.delete_signal_select
    delState = hass.states.get('input_select.delete_signal_select_'+view_name)
    delAttributes = delState.attributes
    delAttributes['options'].append(input_text)
    hass.states.set('input_select.delete_signal_select_'+view_name, delState.state, attributes=delAttributes, force_update=True)
