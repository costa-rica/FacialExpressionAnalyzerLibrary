print("- in fea_models/config.py")
import os
from fea_config import ConfigDev, ConfigProd, ConfigWorkstation

if os.environ.get('fea_config_TYPE')=='workstation':
    config = ConfigWorkstation()
    print('- fea_models/config: Local')
elif os.environ.get('fea_config_TYPE')=='dev':
    config = ConfigDev()
    print('- fea_models/config: Development')
elif os.environ.get('fea_config_TYPE')=='prod':
    config = ConfigProd()
    print('- fea_models/config: Production')