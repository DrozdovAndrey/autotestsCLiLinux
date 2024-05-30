from checkers import checkout_negative

folder_in = '/home/ad/tst'
folder_out = '/home/ad/out'
folder_ext = '/home/ad/folder1'


def test_nstep1():
    assert checkout_negative('cd {}; 7z e arx3.7z -o{} -y'.format(folder_out, folder_ext), 'ERROR:'), \
        'test1 FAIL'


def test_nstep2():
    assert checkout_negative('cd {}; 7z t arx3.7z'.format(folder_out), 'ERROR:'), 'test1 FAIL'
