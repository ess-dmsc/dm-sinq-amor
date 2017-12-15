#!/usr/bin/python

import time
import json
import kafka


cmd = {
  "cmd": "add",
  "streams": [
    {
      "channel": "SQ:AMOR:DIMETIX:DIST",
      "channel_provider_type": "ca",
      "converter": {
        "schema": "f142",
        "topic": "amor"
      }
    }
  ]
}

p = kafka.KafkaProducer(bootstrap_servers="localhost:9092")
p.send("forward-epics-cmds", json.dumps(cmd))
time.sleep(1)
