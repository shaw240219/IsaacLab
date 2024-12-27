# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for the Mujoco Limx robot."""

from __future__ import annotations

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import ImplicitActuatorCfg
from omni.isaac.lab.assets import ArticulationCfg
import os

##
# Configuration
##
assets_dir = os.path.dirname(os.path.abspath(__file__))

L2_CFG = ArticulationCfg(
    prim_path="{ENV_REGEX_NS}/Robot",
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{assets_dir}/limx_usd/HU_B04_01.usd",
        activate_contact_sensors=True,

        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.9),
        joint_pos={
            "shoulder_pitch_joint_L": -0.0655,
            "shoulder_roll_joint_L": -0.261,
            "shoulder_yaw_joint_L": -0.609,
            "elbow_joint_L": 0.338,
            "hip_roll_joint_L": 0.0,
            "hip_yaw_joint_L": 0.0,
            "hip_pitch_joint_L": 0.0,
            "knee_joint_L": 0.0,
            "ankle_pitch_joint_L": 0.0,
            "ankle_roll_joint_L": 0.0,
            "shoulder_pitch_joint_R": -0.0655,
            "shoulder_roll_joint_R": 0.261,
            "shoulder_yaw_joint_R": 0.609,
            "elbow_joint_R": -0.338,
            "hip_roll_joint_R": 0.0,
            "hip_yaw_joint_R": 0.0,
            "hip_pitch_joint_R": 0.0,
            "knee_joint_R": 0.0,
            "ankle_pitch_joint_R": 0.0,
            "ankle_roll_joint_R": 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    actuators={
        "body": ImplicitActuatorCfg(
            joint_names_expr=[".*"],
            stiffness={
                ".*shoulder_pitch.*": 20,
                ".*shoulder_roll.*": 20,
                ".*shoulder_yaw.*": 20,
                ".*elbow.*": 20,
                ".*hip_roll.*": 70.0,
                ".*hip_yaw.*": 70.0,
                ".*hip_pitch.*": 70.0,
                ".*knee.*": 60.0,
                ".*ankle.*": 20.0,
            },
            damping={
                ".*shoulder_pitch.*": 0.5,
                ".*shoulder_roll.*": 0.5,
                ".*shoulder_yaw.*": 0.5,
                ".*elbo.*": 0.5,
                ".*hip_roll.*": 0.625,
                ".*hip_yaw.*": 0.625,
                ".*hip_pitch.*": 0.625,
                ".*knee.*": 0.5,
                ".*ankle.*": 0.5,
            },
            effort_limit={
                ".*shoulder_pitch.*": 40.0,
                ".*shoulder_roll.*": 40.0,
                ".*shoulder_yaw.*": 40.0,
                ".*elbo.*": 40.0,
                ".*hip_roll.*": 120.0,
                ".*hip_yaw.*": 120.0,
                ".*hip_pitch.*": 120.0,
                ".*knee.*": 80.0,
                ".*ankle.*": 40.0,
            },
            velocity_limit={
                ".*shoulder_pitch.*": 10.0,
                ".*shoulder_roll.*": 10.0,
                ".*shoulder_yaw.*": 10.0,
                ".*elbo.*": 10.0,
                ".*hip_roll.*": 20.0,
                ".*hip_yaw.*": 20.0,
                ".*hip_pitch.*": 20.0,
                ".*knee.*": 10.0,
                ".*ankle.*": 20.0,
            },
        ),
    },
)
"""Configuration for the Mujoco Humanoid robot."""
