from spack import *

class Kripke(Package):
    """Kripke is a simple, scalable, 3D Sn deterministic particle
       transport proxy/mini app.
    """
    homepage = "https://codesign.llnl.gov/kripke.php"
    url      = "https://codesign.llnl.gov/downloads/kripke-openmp-1.1.tar.gz"

    version('1.1', '7fe6f2b26ed983a6ce5495ab701f85bf')

    variant('mpi', default=True, description='Enable MPI support')

    depends_on('mpi', when="+mpi")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake('-DCMAKE_INSTALL_PREFIX:PATH=.',
                  '-DENABLE_OPENMP=1',
                  '-DENABLE_MPI=1',
                  '..',
                  *std_cmake_args)
            make()

            # Kripke does not provide install target, so we have to copy
            # things into place.
            mkdirp(prefix.bin)
            install('kripke', prefix.bin)