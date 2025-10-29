import construct_protocol.socket_messages_pb2 as smpb2


def main():
    ping_request = smpb2.PingRequest()
    ping_request.ping_message = "Hello"
    print(f"Ping message: {ping_request.ping_message}")

if __name__ == "__main__":
    main()