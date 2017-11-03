DOMAIN = 'hello_state'

panelAttributes = {'assumed_state': False, 'entity_id': ('script.dummy_panel',), 'friendly_name': 'Button Panel', 'order': 0}

def setup(hass,config):
   hass.states.set('group.world','hello', attributes=panelAttributes)
   return True


