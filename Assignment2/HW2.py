import random
import os
import time
import uuid
import json
from azure.iot.device import IoTHubDeviceClient, Message

# The connection string for a device should never be stored in code. For the sake of simplicity we're using an environment variable here.
conn_str = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")
device_id = "IrisLaptop"
host_name = "IrisIoTHub"
# The client object is used to interact with your Azure IoT hub.
device_client = IoTHubDeviceClient.create_from_connection_string("HostName=IrisIoTHub.azure-devices.net;DeviceId=IrisLaptop;SharedAccessKey=1cm1aDa0Ys21D7ikFJoQAq4IDvxSToA7+d6ATC2/sRo=")

# Connect the client.
device_client.connect()

message2 = {}
message2['data1'] = random.randrange(10)
message2['data2'] = random.randrange(10)
message2['data3'] = random.randrange(10)

messageJson2 = json.dumps(message2)
device_client.send_message(messageJson2)
time.sleep(1)

device_client.disconnect()
