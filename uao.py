#!/usr/bin/env python

import os
import subprocess
import sys

if __name__ == '__main__':

    def run(c):
        print('running: %s' % c)
        return subprocess.check_call(c, shell=True)

    assert len(sys.argv) > 1 and sys.argv[1].endswith('.zip'), 'you must specify a .zip file to open.'
    zip_file = os.path.abspath(sys.argv[1])
    assert os.path.exists(zip_file), 'the zip file referenced must be valid.'
    folder_name = zip_file.split('.')[0]
    try:
        run('unzip -a %s -d %s' % (zip_file, os.path.dirname(folder_name)))
    except:
        print("non zero exist code but we proceed anyway..")

    gradle_build = os.path.join(folder_name, 'build.gradle')
    mvn_pom = os.path.join(folder_name, 'pom.xml')
    mvn_exists = os.path.exists(mvn_pom)
    gradle_exists = os.path.exists(gradle_build)
    assert gradle_exists or mvn_exists, 'missing build.gradle` or a `pom.xml` in root of folder %s.' % folder_name

    if gradle_exists:
        run('idea.bat  %s/build.gradle' % folder_name)
    else:
        run('idea.bat %s' % folder_name)
