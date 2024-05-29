import subprocess

if __name__ == '__main__':
    result = subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0:
        lst = out.split('\n')
        if 'PRETTY_NAME="Ubuntu 22.04.1 LTS"' in lst and 'VERSION="22.04.1 LTS (Jammy JellyFish)"' in lst:
            print('SUCCESS')
        else:
            print('FAIL')