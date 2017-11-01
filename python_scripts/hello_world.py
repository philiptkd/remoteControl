value = data.get('value')
logger.info("Executing the {0} script.".format(value))
hass.bus.fire(value, { "wow": "from a Python script!" })


