#state = hass.states.get('group.panel')
#attributes = state.attributes
#logger.info(attributes)

#entities = hass.states.entity_ids(domain_filter='group')
#logger.info(entities)

state = hass.states.get('input_select.delete_device')
#attributes = state.attributes
logger.info(state)
