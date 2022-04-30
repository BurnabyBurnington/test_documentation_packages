name = "dependency"

version = "1.1.0"

description = "A package with a Python function."

authors = ["ColinKennedy"]

private_build_requires = ["rez_build_helper-1+<2"]

requires = ["python-2.7+<4"]

build_command = "python -m rez_build_helper --items python"


def commands():
    import os

    env.PYTHONPATH.append(os.path.join(root, "python"))


tests = {
    "build_documentation": {
        "command": "rez_sphinx build run",
        "requires": ["rez_sphinx-1"],
    },
}