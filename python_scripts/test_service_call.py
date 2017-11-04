service_data = {'value1': '{{value1}}', 'value2': '{{value2}}'}
hass.services.call('python_script', 'test_service', service_data=service_data)
