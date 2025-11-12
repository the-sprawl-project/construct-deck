import construct_deck.construct_protocol.socket_messages_pb2 as smpb2
from construct_deck.toml_parser.toml_parser import load_config_toml
from .commands.ping import PingCommand
from .commands.create import CreateCommand
from .commands.update import UpdateCommand

CONFIG_PATH = "config.toml"

def main():
    ping_request = PingCommand.generate_req_payload(message="hello")
    config = load_config_toml(CONFIG_PATH)
    print(f"Config: {config}")
    print(f"Ping message: {ping_request.ping_message}")

    create_request = CreateCommand.generate_req_payload(
        key="obiwan", value="kenobi")
    print(
        f"Key: {create_request.pair.key}, Value: {create_request.pair.value}")
    
    update_request = UpdateCommand.generate_req_payload(
        key="general", value="grievous")
    
    print("Update request: "
        f"Key: {update_request.pair.key}, Value: {update_request.pair.value}")

if __name__ == "__main__":
    main()