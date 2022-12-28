"""
Test suite for Post-Build Tests
"""
import os
import unittest
from pre_build import ZIP_ARTIFACTS


TESTS_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(TESTS_DIR_PATH)


class PostBuildTest(unittest.TestCase):
    """
    PostBuildTest TestCase Class
    """

    def test_zip_artifacts_exist(self) -> None:
        """
        Test that all the artifacts have been created
        """
        for artifact in ZIP_ARTIFACTS:
            artifact_path = os.path.join(ROOT_DIR, artifact["name"])
            self.assertIs(
                os.path.exists(artifact_path),
                True,
                msg=f"The '{artifact_path}' doesn't exist",
            )


if __name__ == "__main__":
    unittest.main()
