"""
Main lambda function handler. The AWS Lambda function should point here to
lambda_function.lambda_handler. Acts on request and session information
through event_actions. Code for sessions is left for reference.
"""

import os
import events

alexa_id = os.environ.get('AWS_ALEXA_SKILLS_KIT_ID')

def lambda_handler(event, context):
    """
    Handles event and request from Alexa Skill by using methods form
    the event_actions module.

    Args:
        event: Python dict of event, request, and session data
        context: LambdaContext containing runtime data
    Returns:
        Python dict of response message
    Rasies:
        ValueError
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])
   
    if (event['session']['application']['applicationId'] !=
            alexa_id):

        print("amzn1.ask.skill.{0}".format(alexa_id))
        raise ValueError("Invalid Application ID")
    
    request_type = event['request']['type']

    if request_type == "LaunchRequest":
        return events.on_launch(event['request'], event['session'])
    elif request_type == "IntentRequest":
        return events.on_intent(event['request'], event['session'])

