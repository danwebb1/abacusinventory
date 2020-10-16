import subprocess
from abacusinventory.settings import STATIC_URL_DEV, STATIC_URL_QA, STATIC_URL_STAGING, STATIC_URL_PROD


class InventoryDeploymentManager():
    _valid_projects = ['abacus_inventory', 'abacus_inventory-qa', 'abacus_inventory-staging']
    _gcloud_project_id = 'abacus-app'
    _django_static_urls = {
        'DEV': STATIC_URL_DEV,
        'QA': STATIC_URL_QA,
        'STAGING': STATIC_URL_STAGING,
        'PRODUCTION': STATIC_URL_PROD,
    }

    def cleanup(self):
        subprocess.call('rm -rf static', shell=True)


deployment_manager = InventoryDeploymentManager()
deployment_manager.deploy()
