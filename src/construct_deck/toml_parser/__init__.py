import tomllib


def parse_toml_file(path: str) -> dict:
    """
    Reads a toml file and returns it as a dict.
    """
    with open(path) as pth:
        val = tomllib.loads(pth.read())
    
    return val
