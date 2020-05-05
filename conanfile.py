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
        cmake = CMake(self, parallel=True)
        cmake.definitions['BUILD_SHARED_LIBS'] = self.options.shared

        cmake.configure()
        cmake.build(target='install')

    def package_info(self):
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths
        self.cpp_info.libdirs = ['lib']  # Directories where libs are located
        self.cpp_info.libs = ['zbar']
