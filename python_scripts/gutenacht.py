hass.states.set('sensor.tts_input', 'gute nacht grosse', {'language':'de', 'entity': 'media_player.lara'})
time.sleep(15)
hass.states.set('sensor.tts_input', '', {'language':'de', 'entity': 'media_player.lara'})
