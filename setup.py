from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import sys

setup_options = dict(
    name="seqlearn",
    version="0.0.0",
    description="Sequence learning toolkit",
    maintainer="Lars Buitinck",
    maintainer_email="L.J.Buitinck@uva.nl",
    license="MIT",
    url="https://github.com/larsmans/seqlearn",
    packages=["seqlearn", "seqlearn._utils", "seqlearn._decode", "seqlearn.datasets", "seqlearn._inference"],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing",
    ],
    cmdclass={'build_ext': build_ext},
    ext_modules=[
        Extension("seqlearn._decode.bestfirst",
                  ["seqlearn/_decode/bestfirst.c"]),
        Extension("seqlearn._decode.viterbi", ["seqlearn/_decode/viterbi.c"]),
        Extension("seqlearn._utils.ctrans", ["seqlearn/_utils/ctrans.c"]),
        Extension("seqlearn._utils.safeadd", ["seqlearn/_utils/safeadd.c"]),
        Extension("seqlearn._inference.forward_backward",
                  ["seqlearn/_inference/forward_backward.c"],
                  libraries=["m"]),
    ],
)

# For these actions, NumPy is not required. We want them to succeed without,
# for example when pip is used to install seqlearn without NumPy present.
NO_NUMPY_ACTIONS = ('--help-commands', 'egg_info', '--version', 'clean')
if not (len(sys.argv) >= 2 and ('--help' in sys.argv[1:]
                                or sys.argv[1] in NO_NUMPY_ACTIONS)):
    import numpy
    setup_options['include_dirs'] = [numpy.get_include()]

setup(**setup_options)
