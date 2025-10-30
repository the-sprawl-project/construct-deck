import construct_protocol.socket_messages_pb2 as smpb2
from toml_parser.toml_parser import load_config_toml

CONFIG_PATH = "config.toml"

def main():
    ping_request = smpb2.PingRequest()
    config = load_config_toml(CONFIG_PATH)
    ping_request.ping_message = "Hello"
    print(f"Config: {config}")
    print(f"Ping message: {ping_request.ping_message}")

if __name__ == "__main__":
    main()