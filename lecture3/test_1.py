import yaml

from task1 import checkout, hash_crc32

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestPositive:
    def test_step1(self, make_folders, clear_folders, make_files):
        # test1
        res1 = checkout(f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx", "Everything is Ok")
        res2 = checkout(f"ls {data['folder_out']}", "arx.7z")
        assert res1 and res2, "test1 FAIL"

    def test_step2(self, clear_folders, make_files):
        # test2
        res = list()
        res.append(checkout(f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx", "Everything is Ok"))
        res.append(
            checkout(f"cd {data['folder_out']}; 7z e arx.7z -o{data['folder_ext']} -y", "Everything is Ok"))
        for item in make_files:
            res.append(checkout(f"ls {data['folder_ext']}", item))
        assert all(res)

    def test_step3(self):
        # test3
        assert checkout(f"cd {data['folder_out']}; 7z t arx.7z", "Everything is Ok"), "test3 FAIL"

    def test_step4(self):
        # test4
        assert checkout(f"cd {data['folder_in']}; 7z u arx2.7z", "Everything is Ok"), "test4 FAIL"

    def test_step5(self, clear_folders, make_files):
        # test5
        res = list()
        res.append(checkout(f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx", "Everything is Ok"))
        for i in make_files:
            res.append(checkout(f"cd {data['folder_out']}; 7z l arx.7z", i))
        assert all(res), "test5 FAIL"

    def test_step6(self, clear_folders, make_files, make_subfolder):
        # test6
        res = list()
        res.append(checkout(f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx", "Everything is Ok"))
        res.append(
            checkout(f"cd {data['folder_out']}; 7z x arx.7z -o{data['folder_ext2']} -y", "Everything is Ok"))
        for i in make_files:
            res.append(checkout(f"ls {data['folder_ext2']}", i))
        res.append(checkout(f"ls {data['folder_ext2']}", make_subfolder[0]))
        res.append(checkout(f"ls {data['folder_ext2']}/{make_subfolder[0]}", make_subfolder[1]))
        assert all(res), "test6 FAIL"

    def test_step7(self):
        # test7
        assert checkout(f"cd {data['folder_out']}; 7z d arx.7z", "Everything is Ok"), "test7 FAIL"

    def test_step8(self, clear_folders, make_files):
        # test8
        res = list()
        for i in make_files:
            _hash = hash_crc32(f"cd {data['folder_in']}; crc32 {i}")
            res.append(checkout(f"cd {data['folder_in']}; 7z h {i}", _hash.upper()))
        assert all(res), "test8 FAIL"
