import subprocess


def checkout(cmd: str, *args) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if args[0] is None:
        return False
    if result.returncode != 0:
        return False
    else:
        for i in args:
            if i not in result.stdout:
                return False
    return True


def hash_crc32(cmd: str):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0 and result.stdout != '':
        # lst_stdout = result.stdout.split(\n)
        return result.stdout.split('\n')[0]
    else:
        return None




# result = subprocess.run('cd /home/ad/tst/archive_folder; crc32 archive_folder.7z', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
# lst = result.stdout.split('\n')
# print(lst)
# print('19215973' in result.stdout)
#
# print(checkout('cd /home/ad/tst/archive_folder; crc32 archive_folder.7z', '19215973'))
# folder_in = '/home/ad/tst/archive_folder'
# folder_out = '/home/ad/out'
# folder_ext = '/home/ad/folder1'
# dir1 = 'folder1'
# dir2 = 'folder2'
# f1 = 'test_apx1'
# f2 = 'test_apx2'
# f3 = 'test_apx3'
# f4 = 'test_apx4'
# _hash_crc32 = hash_crc32(f'cd {folder_in}; crc32 archive_folder.7z')
# print(_hash_crc32)