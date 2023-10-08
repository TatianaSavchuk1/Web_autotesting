import pytest
import yaml
from module import Site
import time

# with open ('./testdata.yaml') as f:
#     testdata = yaml.safe_load(f)
#
# @pytest.fixture()
# def site():
#     site_1 = Site(testdata['address'])
#     yield site_1
#     site_1.driver.quit
#