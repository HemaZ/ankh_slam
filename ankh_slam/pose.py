import numpy as np


class BasePose(np.ndarray):
    @property
    def position(self):
        """Abstract method

        Raises
        ------
        NotImplementedError

        """
        raise NotImplementedError

    @property
    def orientation(self):
        """Abstract method

        Raises
        ------
        NotImplementedError

        """
        raise NotImplementedError


class R2Pose(BasePose):
    """ Class representing a point in 2D space.
    """
    def __new__(cls, position):
        obj = np.asarray(position, dtype=np.float64).view(cls)
        return obj

    @property
    def position(self):
        """position of this pose

        Returns
        -------
        numpy.array
            the 2d position of this pose
        """

        return np.array(self)

    @property
    def orientation(self):
        """the orientation of this pose

        Returns
        -------
        int
            0
        """
        return 0

    def __add__(self, other):
        """Add two R2Pose

        Parameters
        ----------
        other : R2Pose
            the other pose to be added

        Returns
        -------
        R2Pose
            the result of the addition
        """
        return R2Pose(np.add(self, other))

    def __sub__(self, other):
        """subtracts two R2Poses

        Parameters
        ----------
        other : R2Pose
            the second other post to subtract

        Returns
        -------
        R2Pose
            the resultant pose
        """
        return R2Pose(np.subtract(self, other))
