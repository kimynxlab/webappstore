import configparser

config = configparser.ConfigParser() 
config.read('dbconfig.ini')

print(config['default']['dbname'])
