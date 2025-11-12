from abc import ABC, abstractmethod
from enum import IntEnum

class CommandType(IntEnum):
    SENTINEL = -1
    PING = 0
    CREATE = 1
    GET = 2
    UPDATE = 3
    DELETE = 4


class Command(ABC):

    # Must be overridden by all inheritors of this class
    @classmethod
    @abstractmethod
    def command_type(cls) -> CommandType:
        return CommandType.SENTINEL
    
    # Basic syntax help, must be overridden as well
    @classmethod
    @abstractmethod
    def help_syntax(cls) -> str:
        return "Override Me"
    
    # Generate request payload for this command. Must be overridden by all
    # inheritors of this class to generate a request payload based on the
    # values in kwargs
    @classmethod
    @abstractmethod
    def generate_req_payload(cls, **kwargs):
        pass

    # Parse response for this command. Expects a byte array as input, parses
    # the response for downstream use
    @classmethod
    @abstractmethod
    def parse_response(cls, payload: bytes):
        pass