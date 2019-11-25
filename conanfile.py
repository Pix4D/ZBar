from conans import ConanFile, CMake, tools


class ZBarConan(ConanFile):
    name = 'zbar'
    lib_version = '0.23.0'
    revision = '0'
    version = '{}-{}'.format(lib_version, revision)
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'ZBar QR Code Reader'
    url = 'git@github.com:Pix4D/ZBar.git'
    license = 'LGPL LICENSE'
    generators = 'cmake'
    exports_sources = [
            'zbar/*',
            'include/*',
            'cmake/*',
            'CMakeLists.txt',
            ]
    options = {
            'shared' : [True, False],
            }
    default_options = 'shared=True'

    def build(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_SHARED_LIBS'] = 'ON' if self.options.shared else 'OFF'

        cmake.configure()
        cmake.build(target='install')

    def package_info(self):
        self.cpp_info.libs = ['zbar']

        if self.settings.os == 'Linux' and not self.options.shared:
            self.cpp_info.libs.append('pthread')

