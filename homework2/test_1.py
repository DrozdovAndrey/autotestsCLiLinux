from task1 import checkout, hash_crc32

folder_in = '/home/ad/tst/archive_folder'
folder_out = '/home/ad/out'
folder_ext = '/home/ad/folder1'
dir1 = 'folder1'
dir2 = 'folder2'
f1 = 'test_apx1'
f2 = 'test_apx2'
f3 = 'test_apx3'
f4 = 'test_apx4'
_hash_crc32 = hash_crc32(f'cd {folder_in}; crc32 archive_folder.7z')


def test_step1():
    assert checkout(f'cd {folder_in}; 7z l archive_folder.7z', 'Listing archive: archive_folder.7z'), \
        'test1 FAIL'


def test_step2():
    res1 = checkout(f'cd {folder_in}; 7z x archive_folder.7z -o/home/ad/out', 'Everything is Ok'), 'test1 FAIL'
    res2 = checkout(f'ls {folder_out}/{dir1}', f1, f2), 'test1 FAIL'
    res3 = checkout(f'ls {folder_out}/{dir2}', f3, f4), 'test1 FAIL'
    assert res1 and res2 and res3, 'test2 FAIL'


def test_step3():
    assert checkout(f'cd {folder_in}; 7z h archive_folder.7z', _hash_crc32), 'test1 FAIL'

