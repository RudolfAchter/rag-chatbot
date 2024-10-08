# Install CUDA Toolkit first: https://developer.nvidia.com/cuda-12-3-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=runfile_local
# sudo ln -s /usr/bin/python3 /usr/local/bin/python

curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.7.0 python3 -
alias python='python3'

# .bashrc
export PATH=/usr/local/cuda-12.3/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-12.3/lib64:$LD_LIBRARY_PATH

# Zwei Versuche benötigt. Es musste mein Keyring entsperrt werden?
make setup_cuda
