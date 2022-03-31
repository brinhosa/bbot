from pathlib import Path
from omegaconf import OmegaConf

root_dir = Path(__file__).parent.parent.parent.parent
config_filename = root_dir / "bbot.conf"
secrets_filename = root_dir / "secrets.conf"


def _get_config(filename):
    try:
        return OmegaConf.load(str(filename))
    except Exception:
        return OmegaConf.create()


def get_config():

    return OmegaConf.merge(
        _get_config(config_filename),
        _get_config(secrets_filename),
    )
