hass.states.set('sensor.tts_input', 'gute nacht grosse', {'language':'de', 'entity': 'media_player.bathroom'})
time.sleep(25)
hass.states.set('sensor.tts_input', '', {'language':'de', 'entity': 'media_player.bathroom'})
