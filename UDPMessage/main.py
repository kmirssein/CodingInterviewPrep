from xml.sax import default_parser_list


class UDPMessage:
    def __init__(self, ip, msg_id, payload):
        self.ip = ip
        self.msg_id = msg_id
        self.payload = payload.removeprefix("0x")

    def send_udp_message(self):
        return f"{self.ip}: {self.msg_id}{self.payload}"


udp_connection = UDPMessage("127.0.0.1", "0x123", "0x245334")
udp_message = udp_connection.send_udp_message()

#print(udp_message)

'''
Quetion 2: Send a cyclic UDP Message with a specified cycle time in ms and a 
specified duration in ms. 
'''
def send_udp_message_cyclic(udp_msg, cycle_time_ms, duration_ms):
    num_cycles = duration_ms // cycle_time_ms
    for _ in range(num_cycles):
        print(udp_msg.send_udp_message())

#send_udp_message_cyclic(udp_connection, 1000, 5000)


'''
Question 3: Send multiple UDP messages with varying payloads  
'''
payload_list = [
"0x245331",
"0x245332",
"0x245333",
"0x245334",
"0x245335",
"0x245336"
]

def send_udp_message_multi_payload(msg_class, payloads):
    for p in payloads:
        udp_conn = msg_class("127.0.0.1", "0x123", p)
        print(udp_conn.send_udp_message())

#send_udp_message_multi_payload(UDPMessage,payload_list)





payload_cycles = [
    {
        "payload": "PING",
        "cycle_time_ms": 1000
    },
    {
        "payload": "PONG",
        "cycle_time_ms": 2000
    },
    {
        "payload": "PING",
        "cycle_time_ms": 3000
    },
    {
        "payload": "PONG",
        "cycle_time_ms": 4000
    },
    {
        "payload": "PING",
        "cycle_time_ms": 5000
    },
    {
        "payload": "PONG",
        "cycle_time_ms": 6000
    }
]
'''
Question 4: Cyclic messages with different payloads and different cycle times
'''
def send_udp_message_multi_payload_cycles(msg_class, ip, msg_id,
                                             duration_ms, payload_cycle_pairs):

    if duration_ms <= 0:
        return

    for payload_cfg in payload_cycle_pairs:
        if payload_cfg["cycle_time_ms"] <= 0:
            continue
        num_cycles = duration_ms // payload_cfg["cycle_time_ms"]

        udp_connect = msg_class(ip, msg_id, payload_cfg["payload"])
        for _ in range(num_cycles):
            print(udp_connect.send_udp_message())

#send_udp_message_multi_payload_cycles(UDPMessage, "127.0.0.1", "0x123", 10000,
#                                      payload_cycles)



from typing import List

logs = [
    "127.0.0.1: 123PING",
    "127.0.0.1: 123PING",
    "127.0.0.1: 123PONG",
    "127.0.0.1: 123PING",
    "127.0.0.1: 123PONG",
]

'''
Question: Owner-Driven Mode (Interview Style)
Problem: UDP Message Deduplication + Ordering (Tooling / SDET-style)

This is very realistic for Tesla / Rivian tooling roles.

Scenario

You are receiving formatted UDP messages (strings) from logs.
Each message represents something that would have been sent.

Example messages:

127.0.0.1: 123PING
127.0.0.1: 123PING
127.0.0.1: 123PONG
127.0.0.1: 123PING
127.0.0.1: 123PONG

Task

Write a function that:

Deduplicates messages

Preserves first-seen order

Returns the result as a list of strings

Expected behavior

Input:

[
    "127.0.0.1: 123PING",
    "127.0.0.1: 123PING",
    "127.0.0.1: 123PONG",
    "127.0.0.1: 123PING",
    "127.0.0.1: 123PONG",
]


Output:

[
    "127.0.0.1: 123PING",
    "127.0.0.1: 123PONG",
]

Constraints (important)

Do not sort

Do not use external libraries

Preserve first appearance order

O(n) time expected
'''
def deduplicate_messages(udp_messages: List[str]) -> List[str]:
    """Return messages with duplicates removed, preserving original order."""
    seen = set()
    result = []

    for message in udp_messages:
        if message not in seen:
            seen.add(message)
            result.append(message)

    return result

msgs = deduplicate_messages(logs)
print(msgs)
