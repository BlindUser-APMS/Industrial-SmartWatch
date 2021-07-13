import json
import paho.mqtt.client as mqtt
from smartwatch_server import SmartWatchServer



def main():

    f = open("\\resources\\smartwatch_messages.json")
    sw_msgs = json.load(f)
    sw_msgs = list(sw_msgs["event_messages"])
    f.close()

    sws = SmartWatchServer()

# The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("#")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        #print(msg.topic+" "+str(msg.payload))
        msg = json.loads(str(msg.payload.decode("utf-8")))
        msg = list(msg['Messages'])[0]
        station_name = msg["DataSetWriterId"]
        current_state = msg["Payload"]["state_current"]
        for sw_msg in sw_msgs:
            if station_name in sw_msg["stationName"]:
                if current_state in sw_msg["triggerState"]:
                    print("Creating new task with ", sw_msg["msg_taskOrigin"], sw_msg["msg_taskDescription"], sw_msg["msg_taskPriority"])
                    sws.new_task(sw_msg["msg_taskOrigin"], sw_msg["msg_taskDescription"], sw_msg["msg_taskPriority"])


    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message



    client.connect("192.168.144.1", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()
    
if __name__ == '__main__':

    main()
