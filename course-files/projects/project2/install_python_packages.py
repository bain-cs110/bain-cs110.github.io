import os
import sys
import subprocess
import os.path, ssl, stat


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


python_path = sys.executable

OPTIONS = ["install", "upgrade", "uninstall", "list", "debug", "exit"]

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
        print("Uninstalling package:", user_input)

        result = subprocess.Popen([python_path, '-m', 'pip', 'uninstall',
                                  user_input.strip()], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_data = result.communicate(input="Y".encode())[0]
        print("Running...", [python_path, '-m',
              'pip', 'uninstall', user_input.strip()])
        print("***** SYSTEM OUT *****\n",
              stdout_data.decode(), "\n***** SYSTEM OUT *****")
        print("Done. DO NOT HALT EXECUTION. Instead, use the EXIT command.")

    if OPTIONS[option] == "install":
        user_input = input(
            "Enter the name of the package you want to install: ")
        print("Installing package:", user_input)

        print("Running...", [python_path, '-m',
              'pip', 'install', user_input.strip()])
        result = subprocess.run(
            [python_path, '-m', 'pip', 'install', user_input.strip()], stdout=subprocess.PIPE)

        print("***** SYSTEM OUT *****\n",
              result.stdout.decode(), "\n***** SYSTEM OUT *****")
        print("Done. DO NOT HALT EXECUTION. Instead, use the EXIT command.")

    if OPTIONS[option] == "upgrade":
        user_input = input(
            "Enter the name of the package you want to update: ")
        print("Upgrading package:", user_input)
        
        if user_input != "certifi" or sys.platform != "darwin":
            print("Running...", [python_path, '-m', 'pip', 'install', '--upgrade', user_input.strip()])
            result = subprocess.run(
                [python_path, '-m', 'pip', 'install', '--upgrade', user_input.strip()], stdout=subprocess.PIPE)
        
        else:

            STAT_0o775 = ( stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
                        | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP
                        | stat.S_IROTH |                stat.S_IXOTH )

            openssl_dir, openssl_cafile = os.path.split(
                ssl.get_default_verify_paths().openssl_cafile)

            print("Running...", [python_path, "-E", "-s", "-m", "pip", "install", "--upgrade", "certifi"])
            result = subprocess.run([python_path,
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
        print("Done. DO NOT HALT EXECUTION. Instead, use the EXIT command.")

    if OPTIONS[option] == "exit":
        restart_program()
        break

    if OPTIONS[option] == "debug":
        print("***** DEBUG OUT *****")
        print(python_path)
        print("***** DEBUG OUT *****")

    if OPTIONS[option] == "list":
        result = subprocess.run(
            [python_path, '-m', 'pip', 'list'], stdout=subprocess.PIPE)
        print("***** PIP LIST   *****\n",
              result.stdout.decode(), "\n***** PIP LIST   *****")

        result = subprocess.run(
            [python_path, '-m', 'pip', 'list'], stdout=subprocess.PIPE)
        print("***** PIP FREEZE *****\n",
              result.stdout.decode(), "\n***** PIP FREEZE *****")
