#!/usr/bin/env python

"""Tests for `ankh_slam` package."""

import pytest

import numpy as np
from ankh_slam import ankh_slam
from ankh_slam.pose import R2Pose


class TestPose:
    def test_one(self):
        pose = R2Pose([15, 20])
        assert pose.position[0] == 15

    def test_add_r2pose(self):
        pose1 = R2Pose([15, 1])
        pose2 = R2Pose([1, 15])
        expcted = R2Pose([16, 16])
        assert np.linalg.norm(pose1 + pose2 - expcted) == 0

    def test_subtract_r2pose(self):
        pose1 = R2Pose([15, 1])
        pose2 = R2Pose([1, 15])
        expcted = R2Pose([14, -14])
        assert np.linalg.norm(pose1 - pose2 - expcted) == 0
