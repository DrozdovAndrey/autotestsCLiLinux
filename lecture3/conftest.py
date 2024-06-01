import random
import string
import yaml
import pytest
from datetime import datetime

from task1 import checkout

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return checkout(f"mkdir {data['folder_in']} {data['folder_out']} {data['folder_ext']} {data['folder_ext2']}",
                    "")


@pytest.fixture()
def clear_folders():
    return checkout(
        f"rm -rf {data['folder_in']}/* {data['folder_out']}/* {data['folder_ext']}/* {data['folder_ext2']}/*",
        "")


@pytest.fixture()
def make_files():
    list_of_files = list()
    for i in range(data['count']):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout(f"cd {data['folder_in']}; dd if=/dev/urandom of={filename} bs=1M count=1 iflag=fullblock",
                    ""):
            list_of_files.append(filename)
    return list_of_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout(f"cd {data['folder_in']}; mkdir {subfoldername}", ""):
        return None, None
    if not checkout(
            f"cd {data['folder_in']}/{subfoldername}; dd if=/dev/urandom of={testfilename} bs=1M count=1"
            f" iflag=fullblock", ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def print_time(autouse=True):
    print('start: {}'.format(datetime.now().strftime('%H:%M:%S.%f')))
    yield print('stop: {}'.format(datetime.now().strftime('%H:%M:%S.%f')))


@pytest.fixture()
def make_bad_arx():
    checkout(f"cd {data['folder_in']}; 7z a {data['folder_out']}/arxbad", 'Everything is Ok')
    checkout(f"truncate -s 1 {data['folder_out']}/arxbad.7z", 'Everything is Ok')
    yield 'arxbad'
    checkout(f"rm -f {data['folder_out']}/arxbad.7z", '')

