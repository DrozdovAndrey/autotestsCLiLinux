from checkers import checkout

folder_in = '/home/ad/tst'
folder_out = '/home/ad/out'
folder_ext = '/home/ad/folder1'


def test_step1():
    res1 = checkout('cd /home/ad/tst; 7z a ../out/arx2', 'Everything is Ok'), 'test1 failed'
    res2 = checkout('ls {}'.format(folder_out), 'arx2.7z')
    assert res1 and res2, 'test1 FAIL'

def test_step2():
    res1 =  checkout('cd /home/ad/out; 7z e arx2.7z -o/home/ad/folder1 -y', 'Everything is Ok'), 'test2 failed'
    res2 = checkout('ls {}'.format(folder_ext), 'test1')
    res3 = checkout('ls {}'.format(folder_ext), 'test2')
    assert res1 and res2 and res3, 'test2 FAIL'
