from lark import Transformer, Token

class ConstructTransformer(Transformer):
    def message(self, args):
        return self._strip(args)

    def target(self, args):
        return self._strip(args)

    def _strip(self, token):
        if isinstance(token, Token):
            val = token.value
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            return val
        return str(token)

    def ping_stmt(self, args):
        msg = args[0]
        return ("PING", self.message(msg))