
class UDPMessage:
    def __init__(self, ip):
        self.ip = ip

    def send_udp_message(self, msg_id, payload):

        payload_str = payload.removeprefix("0x")

        return f"{self.ip}: {msg_id}{payload_str}"


udp_connection = UDPMessage("127.0.0.1")
udp_message = udp_connection.send_udp_message("0x123", "0x245334")

print(udp_message)