import yaml

def load_yaml(path):
    try:
        with open(path,"r",encoding="utf-8") as f:
            file=yaml.safe_load(
                stream=f
            )
        return file
    except FileNotFoundError:
        pass