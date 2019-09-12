from conans import ConanFile, CMake, tools
import os

class ZBarTestConan(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake'

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            qr_code_sample_path = '../../sample_matrix.bin'
            self.run(os.path.join(os.curdir, 'bin', 'testApp') + ' ' + qr_code_sample_path)
