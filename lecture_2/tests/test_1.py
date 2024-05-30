import subprocess
import pytest


def checkout(cmd: str, text: str) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    assert checkout('cd /home/ad/tst; 7z a ../out/arx2', 'Everything is Ok'), 'test1 failed'


def test_step2():
    assert checkout('cd /home/ad/out; 7z e arx2.7z -o/home/ad/folder1 -y', 'Everything is Ok'), 'test2 failed'


def test_step3():
    assert checkout('cd /home/ad/out; 7z t arx2.7z', 'Everything is Ok'), 'test2 failed'


def test_step4():
    assert checkout('cd /home/ad/tst; 7z u arx2.7z', 'Everything is Ok'), 'test2 failed'


def test_step5():
    assert checkout('cd /home/ad/out; 7z d arx2.7z', 'Everything is Ok'), 'test2 failed'
