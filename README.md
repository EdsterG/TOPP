TOPP
====

This is TOPP, the Time-Optimal Path Parameterization library by Quang-Cuong
Pham (cuong.pham@normalesup.org)

Requirements 
------------

The library comes in two versions: "standalone" and "full". Both version need
the following software:

- Boost (1.47 or above) with Boost.Python
- Python (2.7 or above)

The full version furthermore requires:

- OpenRAVE (0.9 or above) with Python bindings
- LAPACK (3.5.0 or above)

Installation
------------

From the top folder:
  
    ./configure

Then, either:

    make standalone

for the standalone verison, or:

    make full

for the full version. Finally, install with:

    sudo make install

Notes on OpenRAVE integration
-----------------------------

We will suppose here that you are installing OpenRAVE from source. Let
OPENRAVE_DIR denote your OpenRAVE source folder, for instance:
    
    export OPENRAVE_DIR=~/openrave
    git clone https://github.com/rdiankov/openrave.git OPENRAVE_DIR

Install OpenRAVE (Linux instructions here:
http://openrave.org/docs/latest_stable/coreapihtml/installation_linux.html).
Supposing you kept the default installation path (i.e. /usr/local/), make
a symbolic link:

    /usr/local/include/openrave-0.9/openrave/python -> OPENRAVE_DIR/python

Add the Python bindings folder to your library path by exporting it to
LD_LIBRARY_PATH (you can put the following line in your .bashrc or .zshrc for
persistence):

    export LD_LIBRARY_PATH=$(openrave-config --python-dir)/openravepy/_openravepy_:$LD_LIBRARY_PATH
