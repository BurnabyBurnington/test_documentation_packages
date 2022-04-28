name = "downstream"

version = "1.0.0"

description = "A package containing reference documentation to another package."

authors = ["ColinKennedy"]

help = [["README", "README.rst"]]

private_build_requires = ["rez_build_helper-1+<2"]

requires = [
    "PySide2-5.15+<6",
    "Qt.py-1.3+<2",
    "dependency-1+<2",
    "python-2.7+<4",
    "qt_rez_core-1+<2",
    "test_package_a-1+<2",
    "test_package_b-1+<2",
]

build_command = "python -m rez_build_helper --items README.rst python"


def commands():
    import os

    env.PYTHONPATH.append(os.path.join(root, "python"))
