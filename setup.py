

from distutils.core import setup, Extension

mod = Extension('evilframe', sources = ['frame_evil.c'])

setup(
    name='EvilFrames',
    version='1.0',
    description='make your own frames.',
    ext_modules=[mod]
    )


