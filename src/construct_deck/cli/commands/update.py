from .command import Command, CommandType
from typing import Any, override
import construct_deck.construct_protocol.socket_messages_pb2 as smpb2

class UpdateCommand(Command):

    def __init__(self, key, value):
        self._key = key
        self._value = value

    @override
    @classmethod
    def command_type(cls) -> CommandType:
        return CommandType.CREATE
    
    @override
    @classmethod
    def help_syntax(cls) -> str:
        return "UPDATE PAIR <key> to VALUE <value>"
    
    @override
    def make_proto(self):
        key = self._key
        value = self._value
        
        update_message = smpb2.UpdateKVPairReq()
        update_pair = smpb2.KeyValuePair()

        update_pair.key = key
        update_pair.value = value
        update_message.pair.CopyFrom(update_pair)

        return update_message
    
    @override
    def generate_req_payload(self):
        return self.make_proto()
    
    @override
    @classmethod
    def parse_response(cls, payload: bytes):
        pass
