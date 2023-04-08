import subprocess


def install(args):
    programs = ['neofetch', 'neovim', 'zsh']

    print("Installing packages...")
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'install', '-y'] + programs)
