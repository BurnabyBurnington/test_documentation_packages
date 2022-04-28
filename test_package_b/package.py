name = "test_package_b"

version = "1.0.0"

description = "A package containing reference documentation to another package."

authors = ["ColinKennedy"]

private_build_requires = ["rez_build_helper-1+<2"]

requires = ["dependency-1+<2", "python-2.7+<4"]

build_command = "python -m rez_build_helper --items python"


def commands():
    import os

    env.PYTHONPATH.append(os.path.join(root, "python"))
