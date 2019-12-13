import response_builders
import shadow_updater

session_attributes = {}
should_end_session = False
reprompt_text = None

def get_help_response():
    card_title = "Bienvenido"
    speech_output = "Dime, ¿Qué necesitas?"
    response = response_builders.build_response(session_attributes,
        response_builders.build_speechlet_response(card_title,
        speech_output, reprompt_text, should_end_session))
    return response

def movement(intent):
    card_title = "Movimiendose"

    movimiento = intent.get('slots',{}).get('move',{}).get('value')
    if movimiento and (movimiento.lower() == 'adelante' or movimiento.lower() == 'atras' or movimiento.lower() == 'derecha' \
     or movimiento.lower() == 'izquierda' or movimiento.lower() == 'parar'):
        speech_output = "Entendido."
        new_value_dict = {"movimiento":movimiento.lower()}
        shadow_updater.update_shadow(new_value_dict)
    else:
        speech_output = "No entendi lo que quisiste decir, ¿puedes repetirlo?"

    response = response_builders.build_response(session_attributes,
        response_builders.build_speechlet_response(card_title,
        speech_output, reprompt_text, should_end_session))
    return response



