import os
import sys
import subprocess
import os.path, ssl, stat

python_path = sys.executable


user_input = "pip-system-certs"
print("Installing package:", user_input)

print("Running...", [python_path, '-m',
        'pip', 'install', user_input.strip()])
result = subprocess.run(
    [python_path, '-m', 'pip', 'install', user_input.strip()], stdout=subprocess.PIPE)

print("***** SYSTEM OUT *****\n",
        result.stdout.decode(), "\n***** SYSTEM OUT *****")
print("Done. DO NOT HALT EXECUTION. ")


user_input = "requests"
print("Installing package:", user_input)

print("Running...", [python_path, '-m',
        'pip', 'install', user_input.strip()])
result = subprocess.run(
    [python_path, '-m', 'pip', 'install', user_input.strip()], stdout=subprocess.PIPE)

print("***** SYSTEM OUT *****\n",
        result.stdout.decode(), "\n***** SYSTEM OUT *****")
print("Done. DO NOT HALT EXECUTION. ")

user_input = "customtkinter"
print("Installing package:", user_input)

print("Running...", [python_path, '-m',
        'pip', 'install', user_input.strip()])
result = subprocess.run(
    [python_path, '-m', 'pip', 'install', user_input.strip()], stdout=subprocess.PIPE)

print("***** SYSTEM OUT *****\n",
        result.stdout.decode(), "\n***** SYSTEM OUT *****")
print("Done. DO NOT HALT EXECUTION.")

user_input = "sendgrid"
print("Installing package:", user_input)

print("Running...", [python_path, '-m',
        'pip', 'install', user_input.strip()])
result = subprocess.run(
    [python_path, '-m', 'pip', 'install', user_input.strip()], stdout=subprocess.PIPE)

print("***** SYSTEM OUT *****\n",
        result.stdout.decode(), "\n***** SYSTEM OUT *****")
print("Done. DO NOT HALT EXECUTION.")

user_input = "certifi"
print("Running...", [python_path, '-m', 'pip',
        'install', '--upgrade', user_input])

if sys.platform != "darwin":
    result = subprocess.run(
        [python_path, '-m', 'pip', 'install', '--upgrade', user_input.strip()], stdout=subprocess.PIPE)

else:
    STAT_0o775 = ( stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
                | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP
                | stat.S_IROTH |                stat.S_IXOTH )

    openssl_dir, openssl_cafile = os.path.split(
        ssl.get_default_verify_paths().openssl_cafile)

    result = subprocess.run([sys.executable,
        "-E", "-s", "-m", "pip", "install", "--upgrade", "certifi"], stdout=subprocess.PIPE)

    import certifi
    # change working directory to the default SSL directory
    os.chdir(openssl_dir)
    relpath_to_certifi_cafile = os.path.relpath(certifi.where())
    print(" -- removing any existing file or link")
    try:
        os.remove(openssl_cafile)
    except FileNotFoundError:
        pass
    print(" -- creating symlink to certifi certificate bundle")
    os.symlink(relpath_to_certifi_cafile, openssl_cafile)
    print(" -- setting permissions")
    os.chmod(openssl_cafile, STAT_0o775)
    print(" -- update complete")

print("***** SYSTEM OUT *****\n",
        result.stdout.decode(), "\n***** SYSTEM OUT *****")
print("Done. DO NOT HALT EXECUTION.")

os.execl(sys.executable, sys.executable, * sys.argv)
