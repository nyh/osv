import os
from osv.modules.api import *
from osv.modules.filemap import FileMap
from osv.modules import api

_module = '${OSV_BASE}/modules/jolokia-agent'


usr_files = FileMap()
usr_files.add(os.path.join(_module, 'target/jolokia-agent.jar')).to('/usr/mgmt/jolokia-agent.jar')
