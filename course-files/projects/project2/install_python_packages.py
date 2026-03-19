import os
import sys
import subprocess
import os.path, ssl, stat


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def run_command(command):
    print("Running...", command)
    result = subprocess.run(command, stdout=subprocess.PIPE)
    print("***** SYSTEM OUT *****\n", result.stdout.decode(), "\n***** SYSTEM OUT *****")    

OPTIONS = [
    "install",
    "upgrade",
    "uninstall",
    "list",
    "debug",
    "exit",
    "fix-ssl-windows",
]
python_path = sys.executable

run_command([python_path, '-m', 'pip', 'install', '--upgrade', 'pip'])

while True:

    print("***************")
    for i in range(len(OPTIONS)):
        print(i, OPTIONS[i])
    print("***************")
    user_input = input(
        "What action [0-{}] would you like to perform? ".format(len(OPTIONS)-1))

    try:
        option = int(user_input.strip())

    except:
        print("Invalid input!")
        continue

    if OPTIONS[option] == "uninstall":
        user_input = input(
            "Enter the name of the package you want to uninstall: ")
        print("Running...", [python_path, '-m',
              'pip', 'uninstall', user_input.strip()])
        result = subprocess.Popen([python_path, '-m', 'pip', 'uninstall',
                                  user_input.strip()], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_data = result.communicate(input="Y".encode())[0]

        print("***** SYSTEM OUT *****\n",
              stdout_data.decode(), "\n***** SYSTEM OUT *****")
        print("Done. DO NOT HALT EXECUTION. Instead, use the EXIT command.")

    if OPTIONS[option] == "install":
        user_input = input(
            "Enter the name of the package you want to install: ")

        run_command([python_path, '-m', 'pip', 'install', user_input.strip()])

    if OPTIONS[option] == "upgrade":
        user_input = input(
            "Enter the name of the package you want to update: ")

        if user_input != "certifi" or sys.platform != "darwin":
            run_command([python_path, '-m', 'pip', 'install', '--upgrade', user_input.strip()])

        else:

            STAT_0o775 = ( stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
                        | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP
                        | stat.S_IROTH |                stat.S_IXOTH )

            openssl_dir, openssl_cafile = os.path.split(
                ssl.get_default_verify_paths().openssl_cafile)

            run_command([python_path, "-E", "-s", "-m", "pip", "install", "--upgrade", "certifi"])

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

    if OPTIONS[option] == "exit":
        restart_program()
        break

    if OPTIONS[option] == "debug":
        print("***** DEBUG OUT *****")
        print(python_path)
        print("***** DEBUG OUT *****")

    if OPTIONS[option] == "fix-ssl-windows":
        print(sys.platform)
        if sys.platform not in ["win32", "cygwin", "msys"]:
            print("ERROR: You don't seem to be on a windows computer.")
            continue
        
        run_command([python_path, '-m', 'pip', 'install', 'truststore'])

        result = subprocess.Popen([python_path, '-m', 'pip', 'uninstall',
                                  "sendgrid"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_data = result.communicate(input="Y".encode())[0]

        print("***** SYSTEM OUT *****\n",
              stdout_data.decode(), "\n***** SYSTEM OUT *****")

        run_command([python_path, '-m', 'pip', 'install', 'sendgrid', '--use-feature=truststore'])

        print("Done. DO NOT HALT EXECUTION. Instead, use the EXIT command.")

    if OPTIONS[option] == "list":
        result = subprocess.run(
            [python_path, '-m', 'pip', 'list'], stdout=subprocess.PIPE)
        print("***** PIP LIST   *****\n",
              result.stdout.decode(), "\n***** PIP LIST   *****")

        result = subprocess.run(
            [python_path, '-m', 'pip', 'list'], stdout=subprocess.PIPE)
        print("***** PIP FREEZE *****\n",
              result.stdout.decode(), "\n***** PIP FREEZE *****")
6