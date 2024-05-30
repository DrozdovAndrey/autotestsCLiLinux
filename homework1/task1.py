import subprocess


def check_returncode_and_text(coman_text: str) -> bool:
    result = subprocess.run(coman_text, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0:
        lst = out.split('\n')
        if 'PRETTY_NAME="Ubuntu 22.04.1 LTS"' in lst and 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in lst:
            return True
        else:
            return False


print(check_returncode_and_text('cat /etc/os-release'))
