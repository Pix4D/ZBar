from conans import ConanFile, CMake, tools
import os
import pathlib

class ZBarTestConan(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake'

    def build(self):
        cmake = CMake(self)
        cmake.configure(defs={'CMAKE_INSTALL_PREFIX': 'install'})
        cmake.build(target='install')

    def imports(self):
        # Cache to simplify installation of libraries and resources
        imports_dir = 'conanLibs'
        self.copy('*.dll', src='bin', dst=imports_dir)
        self.copy('*.so*', src='lib', dst=imports_dir)
        self.copy('*.dylib*', src='lib', dst=imports_dir)

    def test(self):
        if not tools.cross_building(self.settings):
            executable = os.path.join(pathlib.Path().absolute(), 'install', 'bin', 'testApp')
            qr_code_sample_path = os.path.join(pathlib.Path().absolute(), '..', '..', 'sample_matrix.bin')
            self.run(executable + ' ' + qr_code_sample_path)
