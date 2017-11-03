#TODO
#use numbered naming convention for remote entities
#increment the largest group name number, use to create unique entity id
#give unique entity id to new remote entity

#get list of group entity IDs
group_id_list = hass.states.entity_ids(domain_filter='group')

#get first unused remote# entity ID
i = 0
while('group.remote'+str(i) in group_id_list):
    i = i + 1
entity_id = 'remote'+str(i)

value = data.get('value')
#creates entity on button press
#hass.states.set('group.panel3', value)

#create remote(script.dummy_panel) entity on button press
panelAttributes = {'entity_id': ('script.dummy_panel',), 'view': 'yes'}
hass.states.set('group.'+entity_id,'hello', attributes=panelAttributes)

logger.info("Executing the {0} script.".format(value))
hass.bus.fire(value, { "wow": "from a Python script!" })


