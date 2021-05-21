#!/usr/bin/python3
import pathlib as pl
import abc
import pexpect
import os



class Gpg(abc.ABC):
    @abc.abstractmethod
    def sign(self, file: pl.Path) -> None:
        pass


class FsGpg(Gpg):
    def __init__(self, gpgh: str):
        self._gpgh = gpgh


    def sign(self, file: pl.Path) -> None:
        os.environ['GPGH'] = self._gpgh
        child = pexpect.spawn(f'/home/yulia/devel/tasks/sb/gpg.sh --sign {file}')
        child.interact()
        child.close()
        if child.exitstatus != 0:
            exit(1)
        print("Sign from FsGpg")

class YuGpg(Gpg):
    def sign(self, file: pl.Path) -> None:
        print("Sign from YuGpg")


def main() -> None:
    import argparse
    my_parser = argparse.ArgumentParser(description='Script to sign files. Supports file system '
                                                    'as well as Yubikeys')
    my_parser.add_argument('--engine', type=str, required=True, choices=['fs', 'yu'], help='Engine')
    my_parser.add_argument('--gpgh', type=str, help='Path to GPG keys')
    my_parser.add_argument('--file-to-sign', type=str, required=True, help='Path to file for signing')

    args = my_parser.parse_args()


    # if args['engine'] == 'fs':
    if args.engine == 'fs':
        gpg: FsGpg = FsGpg(args.gpgh)
        # gpg.init(args.gpgh)
        # gpg._gpgh = args.gpgh
    else:
        gpg: YuGpg = YuGpg()


    gpg.sign(pl.Path("asdf"))



main()

