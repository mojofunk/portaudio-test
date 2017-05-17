#!/usr/bin/env python

import os

from waflib import Options, Logs

APPNAME = 'portaudio'
VERSION = '2.0'

out = 'waf-build'

def options(opt):
    opt.load('compiler_c')
    opt.load('compiler_cxx')
    opt.load('gnu_dirs')
    opt.load('toolset')
    opt.load('compiler_flags')
    opt.load('pkgconfig')

def define_compiler_flags(conf):
    if not conf.env.CFLAGS:
        # TODO check compiler and use appropriate flags
        conf.env.CFLAGS = '-g'

def print_configuration(conf):
    Logs.info('Host System               : %s' % conf.env.HOST_SYSTEM)
    Logs.info('Toolset                   : %s' % conf.env.TOOLSET)
    Logs.info('C compiler flags          : %s' % conf.env.CFLAGS)
    Logs.info('C++ compiler flags        : %s' % conf.env.CXXFLAGS)
    Logs.info('Linker flags              : %s' % conf.env.LINKFLAGS)

def configure(conf):
    conf.load('gnu_dirs')
    conf.load('toolset')
    conf.load('host_system')
    conf.load('compiler_flags')
    conf.load('pkgconfig')

    deps = { 'portaudio-2.0': '19' }

    conf.pkgconfig_check_required_deps (deps)

    define_compiler_flags(conf)

    print_configuration(conf)

def build(bld):

    # detect and possibly use
    #use_defines = ['PA_USE_C99_LRINTF']
    use_defines = []
    uselibs = ['PORTAUDIO-2.0']

    example_sources = '''
        examples/pa_devs.c
        '''.split()

    for example_src in example_sources:
       bld.program(
           uselibs=uselibs,
           source=example_src,
           uselib=uselibs,
           install_path='${BINDIR}',
           target=os.path.splitext(example_src)[0]
       )
