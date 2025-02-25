# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Eztrace(Package):
    """EZTrace is a tool to automatically generate execution traces
       of HPC applications."""

    homepage = "https://gitlab.com/eztrace"
    maintainers = ['trahay']
    git = "https://gitlab.com/eztrace/eztrace.git"

    version('master',  branch='master')
    version('2.0-rc1', sha256='2ad322df5aeb0c668ebadbfeb3b21c8841831b2c15944d86d1d217f738fee74e')
    version('1.1-13', sha256='6144d04fb62b3ccad41af0268cd921161f168d0cca3f6c210c448bb0b07be7e0')
    version('1.1-10', sha256='63d1af2db38b04efa817614574f381e7536e12db06a2c75375d1795adda3d1d8')

    # dependencies for eztrace 1.x and 2.x
    depends_on('mpi')
    depends_on('opari2')
    depends_on('binutils')

    # eztrace 1.x dependencies
    depends_on('autoconf@2.71', type='build', when="@:1")
    depends_on('automake', type='build', when="@:1")
    depends_on('libtool', type='build', when="@:1")
    # Does not work on Darwin due to MAP_POPULATE
    conflicts('platform=darwin', when='@:1')

    # eztrace 2.x dependencies
    depends_on('cmake@3.1:', type='build', when="@2.0:")
    depends_on('otf2', when="@2.0:")

    def url_for_version(self, version):
        url = "https://gitlab.com/eztrace/eztrace/-/archive/{0}/eztrace-{1}.tar.gz"
        return url.format(version, version)

    @when('@2.0:')
    def install(self, spec, prefix):
        # Since eztrace 2.0, the build system uses CMake
        spec = self.spec
        args = [
            "-DCMAKE_INSTALL_PREFIX=$prefix",
            "-DEZTRACE_ENABLE_MEMORY=ON",
            "-DEZTRACE_ENABLE_MPI=ON",
            "-DEZTRACE_ENABLE_OPENMP=ON",
            "-DEZTRACE_ENABLE_POSIXIO=ON",
            "-DEZTRACE_ENABLE_PTHREAD=ON",
            "-DOTF2_INCLUDE_PATH=%s" % spec['otf2'].prefix.include,
            "-DOTF2_LIBRARY_PATH=%s" % spec['otf2'].libs,
        ]

        if(spec.satisfies('%llvm-openmp-ompt')):
            args.append("-DEZTRACE_ENABLE_OMPT=ON")

        args.extend(std_cmake_args)

        with working_dir('spack-build', create=True):
            cmake('..', *args)
            make()
            make('install')

    # Until eztrace 2.0, the build system uses autoconf
    @when('@:1')
    def install(self, spec, prefix):
        if self.spec.satisfies('%fj'):
            env.set('LDFLAGS', '--linkfortran')
        self.patch()
        which('bash')('bootstrap')
        configure("--prefix=" + prefix,
                  "--with-mpi={0}".format(self.spec["mpi"].prefix))
        self.fix_libtool()
        make()
        make("install")

    @when('@:1')
    def patch(self):
        filter_file(
            '"DEFAULT_OUTFILE"',
            '" DEFAULT_OUTFILE "',
            'extlib/gtg/extlib/otf/tools/otfshrink/otfshrink.cpp',
            string=True
        )

    @when('@:1')
    def fix_libtool(self):
        if self.spec.satisfies('%fj'):
            libtools = ['extlib/gtg/libtool',
                        'extlib/opari2/build-frontend/libtool']
            for f in libtools:
                filter_file('wl=""', 'wl="-Wl,"', f, string=True)
