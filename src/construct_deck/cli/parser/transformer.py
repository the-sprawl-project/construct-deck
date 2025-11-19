from lark import Transformer
from lark.lexer import Token

# command imports
from construct_deck.cli.commands.command import CommandType
from construct_deck.cli.commands.ping import PingCommand
from construct_deck.cli.commands.create import CreateCommand
from construct_deck.cli.commands.delete import DeleteCommand
from construct_deck.cli.commands.read import ReadCommand
from construct_deck.cli.commands.update import UpdateCommand

class ConstructTransformer(Transformer):

    def _strip(self, token):
        if isinstance(token, Token):
            val = token.value
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            return val
        return str(token)

    ### Each rule type and token type requires a parse ###

    # Rules for PING go below
    def ping__CNAME(self, args):
        return self._strip(args)
    
    def ping__ESCAPED_STRING(self, args):
        return self._strip(args)

    def ping_stmt(self, args):
        '''
        The expected syntax for PING is PING <stmt>, which can be either
        a single word or an escaped string.
        '''
        msg = args[0]
        return (CommandType.PING, PingCommand(msg))
    
    # Rules for CREATE go below
    def create__CNAME(self, args):
        return self._strip(args)
    
    def create__ESCAPED_STRING(self, args):
        return self._strip(args)
    
    def create_stmt(self, args):
        '''
        We expect the create statement to contain two entities: The key of the
        create statement and the value associated with the key. The key is
        expected to be a single word, while the value may be an escaped string
        '''
        key = args[0]
        val = args[1]
        return (CommandType.CREATE, CreateCommand(key, val))