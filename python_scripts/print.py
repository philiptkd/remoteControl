#state = hass.states.get('group.panel')
#attributes = state.attributes
#logger.info(attributes)

entities = hass.states.entity_ids(domain_filter='group')
logger.info(entities)
