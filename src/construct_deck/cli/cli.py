import construct_deck.construct_protocol.socket_messages_pb2 as smpb2
from construct_deck.toml_parser.toml_parser import load_config_toml
from .commands.ping import PingCommand
from .commands.create import CreateCommand
from .commands.update import UpdateCommand
from .commands.delete import DeleteCommand
from .commands.read import ReadCommand

from .parser.parser import parser
from .parser.transformer import ConstructTransformer

CONFIG_PATH = "config.toml"

def inline_test():
    ping_request = PingCommand("hello").generate_req_payload()
    config = load_config_toml(CONFIG_PATH)
    print(f"Config: {config}")
    print(f"Ping message: {ping_request.ping_message}")

    create_request = CreateCommand("obiwan", "kenobi").generate_req_payload()
    print("Create Request: "
        f"Key: {create_request.pair.key}, Value: {create_request.pair.value}")
    
    update_request = UpdateCommand("general", "grievous").generate_req_payload()
    
    print("Update request: "
        f"Key: {update_request.pair.key}, Value: {update_request.pair.value}")
    
    delete_request = DeleteCommand("anakin").generate_req_payload()
    print(f"Delete request: key: {delete_request.key}")
    
    read_request = ReadCommand("skywalker").generate_req_payload()
    print(f"Read Request: Key: {read_request.key}")


def parser_test():
    examples = [
        'PING hello',
        'PING "Hello World"',
        "PING \"Hello There\""
    ]

    transformer = ConstructTransformer()
    for text in examples:
        tree = parser.parse(text, start='start')
        result = transformer.transform(tree)
        print(f"\nInput: {text}\nParsed: {result}")
    print("")


def create_test():
    examples = [
        'CREATE PAIR hello WITH VALUE goodbye',
        'CREATE PAIR buenos WITH VALUE "dias"',
        'CREATE PAIR greeting WITH VALUE "hello world!"'
    ]

    transformer = ConstructTransformer()
    for text in examples:
        tree = parser.parse(text, start='start')
        result = transformer.transform(tree)
        print(f"\nInput: {text}\nParsed: {result}")
    print("")
   

def main():
    print("====Running inline test====")
    inline_test()
    print("====Inline test complete====")
    print("====Running parser test====")
    parser_test()
    print("====Parser test complete===")
    print("====Running create test====")
    create_test()
    print("====Create test complete===")


if __name__ == "__main__":
    main()