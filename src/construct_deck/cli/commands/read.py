from .command import Command, CommandType
from typing import Any, override
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
    def make_proto(self):
        key = self._key
        if key is None:
            raise Exception("Syntax Error: READ expects a key")
        
        read_message = smpb2.ReadKVPairReq()
        read_message.key = key

        return read_message
    
    @override
    def generate_req_payload(self):
        return self.make_proto()
    
    @override
    @classmethod
    def parse_response(cls, payload: bytes):
        pass