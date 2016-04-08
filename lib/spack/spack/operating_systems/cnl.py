from spack.architecture import OperatingSystem

class Cnl(OperatingSystem):
    """ Compute Node Linux (CNL) is the operating system used for the Cray XC
    series super computers. It is a very stripped down version of GNU/Linux.
    Any compilers found through this operating system will be used with
    modules. If updated, user must make sure that version and name are 
    updated to indicate that OS has been upgraded (or downgraded)
    """
    def __init__(self):
        name = 'CNL'
        version = '10'
        super(Cnl, self).__init__(name, version, "MODULES")