DOMAIN = 'button'

def setup(hass,config):
   hass.states.set('group.remote','on',{'entity_id': ['button_1']})
   return True
