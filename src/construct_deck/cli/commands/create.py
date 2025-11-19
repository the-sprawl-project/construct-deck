from .command import Command, CommandType
from typing import override
import construct_deck.construct_protocol.socket_messages_pb2 as smpb2

class CreateCommand(Command):

    def __init__(self, key, value):
        self._key = key
        self._value = value

    
    @override
    def make_proto(self):
        create_message = smpb2.CreateKVPairReq()
        create_pair = smpb2.KeyValuePair()

        create_pair.key = self._key
        create_pair.value = self._value
        create_message.pair.CopyFrom(create_pair)

        return create_message

    @override
    @classmethod
    def command_type(cls) -> CommandType:
        return CommandType.CREATE
    
    @override
    @classmethod
    def help_syntax(cls) -> str:
        return "CREATE PAIR <key> WITH VALUE <value>"
    
    @override
    def generate_req_payload(self):
        return self.make_proto()    
    
    @override
    @classmethod
    def parse_response(cls, payload):
        pass
    