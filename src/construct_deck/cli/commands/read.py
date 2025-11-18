from .command import Command, CommandType
from typing import override
import construct_deck.construct_protocol.socket_messages_pb2 as smpb2

class ReadCommand(Command):

    def __init__(self, key):
        self._key = key

    @override
    @classmethod
    def command_type(cls) -> CommandType:
        return CommandType.READ
    
    @override
    @classmethod
    def help_syntax(cls) -> str:
        return "READ PAIR {key}"
    
    @override
    @classmethod
    def generate_req_payload(cls, **kwargs):
        # Expect a key to read
        key = kwargs.get("key", None)
        if key is None:
            raise Exception("Syntax Error: READ expects a key")
        
        read_message = smpb2.ReadKVPairReq()
        read_message.key = key

        return read_message
    
    @override
    @classmethod
    def parse_response(cls, payload: bytes):
        pass