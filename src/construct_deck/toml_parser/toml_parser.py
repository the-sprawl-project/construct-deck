import tomllib

def load_config_toml(path: str) -> dict:
    """
    Loads the config toml
    """
    with open(path) as pth:
        val = tomllib.loads(pth.read())
    return val
