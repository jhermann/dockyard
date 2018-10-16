#! /bin/sh
#
# Helper script to build wheels ONCE

pip_cache="/build/pip-cache"
wheel_dir="$pip_cache/repo"

pip_wheel() {
    python3 -m pip wheel \
            --cache-dir "$pip_cache" \
            --wheel-dir "$wheel_dir" \
            --find-links "$wheel_dir" \
            "$@"
}

sed -ne '1,/need NumPy/p' requirements.txt >no-numpy.txt
pip_wheel -r no-numpy.txt
# SciPy's "setup.py" needs numpy installed!
sudo python3 -m pip install --no-cache --find-links "$wheel_dir" numpy
pip_wheel -r requirements.txt
