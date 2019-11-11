import greengrasssdk
import logging
import platform
import boto3




client = greengrasssdk.client('iot-data')
my_platform = platform.platform()

OUTPUT_TOPIC = 'test/topic_results'

def get_input_topic(context):
    try:
        topic = context.client_context.custom['subject']
    except Exception as e:
        logging.error('Topic could not be parsed. ' + repr(e))
    return topic
    
def get_input_message(event):
    try:
        message = event['test-key']
    except Exception as e:
        logging.error('Message could not be parsed. ' + repr(e))
    return message

def function_handler(event, context):
    try:
        input_topic = get_input_topic(context)
        input_message = get_input_message(event)
        response = 'Invoked on topic "%s" with message "%s"' % (input_topic, input_message)
        response = response + my_platform
        logging.info(response)
    except Exception as e:
        logging.error(e)
        
    client.publish(topic=OUTPUT_TOPIC, payload=response)
    
    storeData = {}
    storeData['weatherRecord'] = event['test-key']
    jsonData = json.dumps(storeData)
    s3 = boto3.resource('s3')
    object = s3.Object('lambdatestdata', 'recordData.json')
    object.put(Body=some_binary_data)
    
   
    

    return
