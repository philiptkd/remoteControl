del_signal_button_name = data.get('value')
view_name = del_signal_button_name[len('script.delete_signal_button_'):]
input_select_name = 'input_select.delete_signal_select_'+view_name
#input_text = hass.states.get(input_select_name).state
input_text = hass.states.get('input_select.delete_device_select').state

logger.info('\n\nbutton name: '+del_signal_button_name+'\ninput select name: '+input_select_name+'\ninput text: '+input_text+'\n\n')

if(input_text != 'Select Signal to Delete'):
    container_name = 'script.'+view_name
    state = hass.states.get(container_name)
    attributes = state.attributes
    newAttributes = {}
    newAttributes['custom_ui_state_card'] = attributes['custom_ui_state_card']
    configDict = {}
    for configKey in attributes['config'].keys():
        if(configKey != 'entities'):
            configDict[configKey] = attributes['config'][configKey]
    entityList = attributes['config']['entities']
    for i in range(0,len(entityList)):
        if(entityList[i]['caption'] == input_text):
            del entityList[i]
            break
    configDict['entities'] = entityList
    newAttributes['config'] = configDict
    hass.states.set(container_name, state.state, attributes=newAttributes, force_update=True)

    selectAttr = hass.states.get(input_select_name).attributes
    selectAttr['options'].remove(input_text)
    hass.states.set(input_select_name, 'Select Signal to Delete', attributes=selectAttr, force_update=True)
