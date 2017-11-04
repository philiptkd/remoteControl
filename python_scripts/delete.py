value = data.get('value')

logger.info(value)

if(value != 'Select Device to Delete'):
    hass.states.remove('group.'+value)
    dict = hass.states.get('input_select.delete_device_select').attributes
    dict['options'].remove(value)
    hass.states.set('input_select.delete_device_select', 'Select Device to Delete', attributes=dict, force_update=True)
