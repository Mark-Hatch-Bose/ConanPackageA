from conans import ConanFile
import os.path

class PackageA(ConanFile):
    name = "PackageA"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    scm = {
        "type": "git",
        "url": "git@github.com:Mark-Hatch-Bose/ConanPackageA.git",
        "revision": "auto"
    }
        
    def package(self):
        self.copy("*")

    def package_id(self):
        self.info.requires.full_package_mode()