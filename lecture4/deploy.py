from ssh_checkers import ssh_checkout, upload_files


def deploy():
    res = list()
    upload_files('o.o.o.o', 'user2', '11', 'p7zip-full.deb',
                 '/home/user2/p7zip=full.deb')
    res.append(ssh_checkout('0.0.0.0', 'user2',
                            '11', 'echo "11" | sudo -S dpkg -i /home/user2/p7zip-full.deb',
                            'Status: install ok installed'))
    return all(res)


if deploy():
    print('Deploy success')
else:
    print('Deploy failed')
