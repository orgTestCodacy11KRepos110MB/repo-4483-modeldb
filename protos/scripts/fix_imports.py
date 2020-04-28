# -*- coding: utf-8 -*-

"""
Fixes the import paths in generated Python Protobuf files.

This has apparently been a problem for years:
https://github.com/protocolbuffers/protobuf/issues/1491

"""

import argparse
import os


def fix_imports(python_output_dir):
    known_dirs = set()
    for parent_dir, dirnames, filenames in os.walk(python_output_dir):
        if parent_dir != python_output_dir:
            known_dirs.add(parent_dir.replace(python_output_dir+'/', '').replace('/','.'))

    for parent_dir, dirnames, filenames in os.walk(python_output_dir):
        filepaths = (
            os.path.join(parent_dir, filename)
            for filename
            in filenames
            if filename.endswith('.py')
        )
        for filepath in filter(os.path.isfile, filepaths):
            depth = os.path.relpath(filepath, python_output_dir).count('/')+1
            with open(filepath, 'r+') as f:
                contents = f.read()
                f.seek(0)

                for d in known_dirs:
                    contents = contents.replace("from {0} ".format(d), "from {1}{0} ".format(d, '.'*depth))

                f.write(contents)
                f.truncate()

    for dirpath in (dirpath for dirpath, _, _ in os.walk(python_output_dir)):
        open(os.path.join(dirpath, "__init__.py"), 'a').close()

    # TODO: chdir and import proto modules to validate


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--python-output-dir", required=True,
        metavar='',
        help="directory where generated Python protos were output",
    )
    args = parser.parse_args()

    fix_imports(args.python_output_dir)
