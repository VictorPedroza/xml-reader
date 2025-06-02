from config.settings import Config

settings = Config(__file__)

entry = settings.get_entry
output = settings.get_output
backup = settings.get_backup
