'''
/*
CSS 532 HW1  Std Name: IrisZheng

Iris Zheng made change on the original code provided by AWS IoT SDK, October,2019. 
The original code is cied as the followings.

 * Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json


## Setting variables
received = False
host = "a2gimuu85fro8a-ats.iot.us-west-2.amazonaws.com"
rootCAPath = "AmazonRootCA1.pem"
certificatePath = "03b24b58f8-certificate.pem.crt"
privateKeyPath = "03b24b58f8-private.pem.key" 
port = 8883
useWebsocket = False
clientId = "Laptop"


topic3 = "hello/world"



# Custom callback function

def customCallback1(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

def customCallback2(client, userdata, message):
    global received
    received = True

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


#Configure AWSIotMQTTCLIent, connect and subscribe laptop to AWS IoT
myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1) 
myAWSIoTMQTTClient.configureDrainingFrequency(2) 
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  
myAWSIoTMQTTClient.configureMQTTOperationTimeout(30)  
myAWSIoTMQTTClient.connect()


#Send message to the console.
while True:
    message = {}
    message['test-key'] = "Current weather: Raining"
    message['sequence'] = loopCount
    messageJson = json.dumps(message)
    myAWSIoTMQTTClient.publish(topic, messageJson, 0)
    print('Published topic %s: %s\n' % (topic, messageJson))
    loopCount += 1
    time.sleep(5)



