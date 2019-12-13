import os
import time
import json

import boto3


thingName = os.environ.get("AWS_IOT_MY_THING_NAME")
host = os.environ.get("AWS_IOT_MQTT_HOST")
port = os.environ.get("AWS_IOT_MQTT_PORT_UPDATE")
topic = "$aws/things/{}/shadow/update".format(thingName)

def update_shadow(new_value_dict):
    payload_dict = {
        "state": {
            "desired" : new_value_dict
        }
    }
    JSON_payload = json.dumps(payload_dict)
    shadow_client = boto3.client('iot-data', 'us-east-1')
    response = shadow_client.update_thing_shadow(thingName=thingName,
                                                 payload=JSON_payload)
    res_payload = json.loads(response['payload'].read().decode('utf-8'))
    print("Move: {0}".format(res_payload.get("state").get("desired").get("movimiento")))

