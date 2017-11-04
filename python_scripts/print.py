#state = hass.states.get('group.panel')
#attributes = state.attributes
#logger.info(attributes)

#entities = hass.states.entity_ids(domain_filter='group')
#logger.info(entities)

#state = hass.states.get('input_select.delete_device_list')
#attributes = state.attributes
#logger.info(state)

state = hass.states.get('group.remote0')
attributes = state.attributes
logger.info(attributes)

dummyPanel = attributes['entity_id'][0]
logger.info(dummyPanel)
