value = data.get('value')
if(value == 'Select Device to Delete')
   return

#else
#get list of options
state = hass.states.get('input_select.delete_device')
attributes = state.attributes
options_list = attributes['options']

