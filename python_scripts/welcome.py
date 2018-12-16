hass.states.set('sensor.tts_input', 'willkommen zu hause', {'language':'de', 'entity': 'media_player.living_room'})
time.sleep(15)
hass.states.set('sensor.tts_input', '', {'language':'de', 'entity': 'media_player.living_room'})
