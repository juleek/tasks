#!/usr/bin/python3
import pathlib as pl
import abc
import pexpect
import os
import tempfile


def execute(command: str) -> None:
    child = pexpect.spawn(command)
    child.interact()
    child.close()
    if child.exitstatus != 0:
        exit(1)


class Gpg(abc.ABC):
    @abc.abstractmethod
    def sign(self, file: pl.Path) -> None:
        pass


class FsGpg(Gpg):
    def __init__(self, gpgh: str):
        self._gpgh = gpgh

    def sign(self, file: pl.Path) -> None:
        os.environ['GPGH'] = self._gpgh
        path_to_gpg: pl.Path = FsGpg.get_gpg_sh()
        execute(f'{path_to_gpg} --sign {file}')
        print("Sign from FsGpg")

    @staticmethod
    def get_gpg_sh() -> pl.Path:
        return pl.Path(__file__).parent / 'gpg.sh'


class YuGpg(Gpg):
    def sign(self, file: pl.Path) -> None:
        with tempfile.TemporaryDirectory() as fd:
            os.environ['GPGH'] = fd
            path_to_gpg: pl.Path = FsGpg.get_gpg_sh()
            execute(f'{path_to_gpg} --import')
            # FsGpg(fd).sign(file)
            fs_gpg: FsGpg = FsGpg(fd)
            fs_gpg.sign(file)
        print("Sign from YuGpg")



def main() -> None:
    import argparse
    my_parser = argparse.ArgumentParser(description='Script to sign files. Supports file system '
                                                    'as well as Yubikeys')
    my_parser.add_argument('--engine', type=str, required=True, choices=['fs', 'yu'], help='Engine')
    my_parser.add_argument('--gpgh', type=str, help='Path to GPG keys')
    my_parser.add_argument('--file-to-sign', type=str, required=True, help='Path to file for signing')

    args = my_parser.parse_args()

    if args.engine == 'fs':
        gpg: FsGpg = FsGpg(args.gpgh)
    else:
        gpg: YuGpg = YuGpg()

    gpg.sign(pl.Path(args.file_to_sign))


main()
