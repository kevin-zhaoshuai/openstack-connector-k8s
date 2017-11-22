# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sys

from openstack_connector_k8s import version
from oslo_log import log as logging
from openstack_connector_k8s.conf import CONF

LOG = logging.getLogger(__name__)

def init(args, **kwargs):
    version_connector = version.version_info.version_string()
    CONF(args=args, project='openstack-connector-k8s', version=version_connector, **kwargs)


def setup_logging():
    logging.setup(CONF, 'openstack-connector-k8s')
    logging.set_defaults(default_log_levels=logging.get_default_log_levels())
    version_connector = version.version_info.version_string()
    LOG.info("Logging enabled!")
    LOG.info("%(prog)s version %(version)s",
             {'prog': sys.argv[0], 'version': version_connector})
