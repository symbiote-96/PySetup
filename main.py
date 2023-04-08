import argparse
from commands import install


def main():
    parser = argparse.ArgumentParser(description='MyApp CLI')
    subparsers = parser.add_subparsers(help='commands')

    # Install command
    install_parser = subparsers.add_parser('install', help='Install programs')
    install_parser.set_defaults(func=install.install)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
