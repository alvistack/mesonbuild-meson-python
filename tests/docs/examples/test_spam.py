import subprocess
import sys

import pytest

import mesonpy

from .conftest import build_project_wheel, examples_dir


def test_build_and_import(venv, tmp_dir_session):
    """Test that the wheel for the spam example builds, installs, and imports."""

    if sys.version_info < (3, 8):
        # The test project requires Python >= 3.8.
        with pytest.raises(mesonpy.MesonBuilderError, match=r'Unsupported Python version `3.7.\d+`'):
            build_project_wheel(package=examples_dir / 'spam', outdir=tmp_dir_session)

    else:
        wheel = build_project_wheel(package=examples_dir / 'spam', outdir=tmp_dir_session)

        subprocess.check_call([
            venv.executable, '-m', 'pip', '--disable-pip-version-check', 'install', wheel
        ])
        output = subprocess.check_output([
            venv.executable, '-c', 'import spam; print(spam.add(1, 2))'
        ])

        assert int(output) == 3
