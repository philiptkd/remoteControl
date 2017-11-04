entity_id = data.get('entity_id')
view_name = data.get('view_name')

#get state
state = hass.states.get(entity_id)
attributes = state.attributes
stateStr = state.state

#if entity is group
if(entity_id[:6] == 'group.'):
    members = attributes['entity_id']   #possibly a tuple
    membersList = []
    #for each entity
    for i in range(0,len(members)):
        service_data = {'entity_id': members[i], 'view_name': view_name}
        hass.services.call('python_script', 'rename', service_data=service_data, blocking=True)
        membersList.append(members[i]+'_'+view_name)
    #make new attributes
    newAttributes = {}
    for key in attributes.keys():
        if(key != 'entity_id'):
            newAttributes[key] = attributes[key]
    newAttributes['entity_id'] = membersList
else:
    newAttributes = attributes

#create new entity with edited name/attributes
newName = entity_id+'_'+view_name
hass.states.set(newName, stateStr, attributes=newAttributes)

