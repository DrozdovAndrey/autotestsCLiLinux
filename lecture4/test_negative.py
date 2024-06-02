import yaml

from ssh_checkers import ssh_checkout_negative

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestNegative:
    def test_nstep1(self, make_folders, clear_folders, make_files, make_bad_arx):
        assert ssh_checkout_negative(data["ip"], data["user"], data["passwd"],
                                     'cd {}; 7z e {}.7z -o{} -y'.format(data['folder_out'],
                                                                        make_bad_arx, data['folder_ext']),
                                     'ERROR:'), 'test1 FAIL'

    def test_nstep2(self, clear_folders, make_files, make_bad_arx):
        assert ssh_checkout_negative(data["ip"], data["user"], data["passwd"],
                                     'cd {}; 7z t {}.7z'.format(data['folder_out'], make_bad_arx),
                                     'ERROR:'), 'test1 FAIL'
