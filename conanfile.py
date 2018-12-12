from conans import ConanFile, CMake, tools


class LibConan(ConanFile):
    name = "lib"
    version = "version"

    scm = {"type": "git", "url": "auto", "revision": "auto"}

    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Lib here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    export_sources = "README.md"

