# -*- coding: utf-8 -*-
# Copyright (C) 2013 Stéphane Caron <caron@ynl.t.u-tokyo.ac.jp>
#
# This file is part of the Time-Optimal Path Parameterization (TOPP) library.
# TOPP is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import TOPPpy
import TOPPbindings

from Utilities import vect2str


class RaveInstance(TOPPpy.RaveInstance):
    def __init__(self, robot, traj, taumin, taumax, vmax, **kwargs):
        super(RaveInstance, self).__init__(robot, **kwargs)
        self.taumin = taumin
        self.taumax = taumax
        self.vmax = vmax
        constring = str(self.discrtimestep) + "\n"
        constring += vect2str(taumin) + "\n"
        constring += vect2str(taumax) + "\n"
        constring += vect2str([0, 0])  # TODO: non-zero vmax
        self.solver = TOPPbindings.TOPPInstance(
            robot, "TorqueLimitsRave", constring, str(traj))


def AVP(robot, traj, sdbegmin, sdbegmax, taumin, taumax, vmax, **kwargs):
    rave_instance = RaveInstance(robot, traj, taumin, taumax, vmax, **kwargs)
    return rave_instance.GetAVP(sdbegmin, sdbegmax)


def Reparameterize(robot, traj, sdbegmin, sdbegmax, taumin, taumax, vmax,
                   **kwargs):
    rave_instance = RaveInstance(robot, traj, taumin, taumax, vmax, **kwargs)
    return rave_instance.GetTrajectory(sdbegmin, sdbegmax)
