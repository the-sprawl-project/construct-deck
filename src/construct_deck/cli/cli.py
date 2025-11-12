import construct_deck.construct_protocol.socket_messages_pb2 as smpb2
from construct_deck.toml_parser.toml_parser import load_config_toml
from .commands.ping import PingCommand

CONFIG_PATH = "config.toml"

def main():
    ping_request = PingCommand.generate_req_payload(message="hello")
    config = load_config_toml(CONFIG_PATH)
    print(f"Config: {config}")
    print(f"Ping message: {ping_request.ping_message}")

if __name__ == "__main__":
    main()