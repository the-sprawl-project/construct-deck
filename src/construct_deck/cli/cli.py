import construct_deck.construct_protocol.socket_messages_pb2 as smpb2
from construct_deck.toml_parser.toml_parser import load_config_toml
from .commands.ping import PingCommand
from .commands.create import CreateCommand
from .commands.update import UpdateCommand
from .commands.delete import DeleteCommand
from .commands.read import ReadCommand

CONFIG_PATH = "config.toml"

def inline_test():
    ping_request = PingCommand.generate_req_payload(message="hello")
    config = load_config_toml(CONFIG_PATH)
    print(f"Config: {config}")
    print(f"Ping message: {ping_request.ping_message}")

    create_request = CreateCommand.generate_req_payload(
        key="obiwan", value="kenobi")
    print("Create Request: "
        f"Key: {create_request.pair.key}, Value: {create_request.pair.value}")
    
    update_request = UpdateCommand.generate_req_payload(
        key="general", value="grievous")
    
    print("Update request: "
        f"Key: {update_request.pair.key}, Value: {update_request.pair.value}")
    
    delete_request = DeleteCommand.generate_req_payload(key="anakin")
    print(f"Delete request: key: {delete_request.key}")
    
    read_request = ReadCommand.generate_req_payload(key="skywalker")
    print(f"Read Request: Key: {read_request.key}")

def main():
    print("====Running inline test====")
    inline_test()
    print("====Inline test complete====")

if __name__ == "__main__":
    main()