#! /usr/bin/env bash
#
# Create a Tkinter-enabled flavour of "Dockerfile.pyenv"

src="Dockerfile.pyenv"

sed -r <"${src}" >"${src}-tk" \
    -e 's/biopy3/biopy3-tk/g' \
    -e 's/\.pyenv/.pyenv-tk/g' \
    -e 's~^( +)lib/.+/_?tkinter.+(.)$~\1\2~' \
    -e 's/^#tk/   /'

$(which colordiff || echo diff) -U1 "${src}" "${src}-tk"
