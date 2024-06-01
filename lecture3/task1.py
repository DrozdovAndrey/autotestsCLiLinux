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


def checkout_negative(cmd: str, text: str) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False
