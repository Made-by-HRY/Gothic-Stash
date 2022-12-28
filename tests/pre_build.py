"""
Test suite for Pre-Build Tests
"""
import os
import unittest
import filecmp


TESTS_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(TESTS_DIR_PATH)
SOURCES_DIR = os.path.join(ROOT_DIR, "docs", "assets", "sources")

ZIP_ARTIFACTS = [
    {
        "name": "TheChroniclesOfMyrtana-All.zip",
        "paths": [
            os.path.join(SOURCES_DIR, "archolos", "*"),
        ],
    },
    {
        "name": "TheChroniclesOfMyrtana-GD3D11.zip",
        "paths": [
            os.path.join(SOURCES_DIR, "archolos", "system", "GD3D11"),
        ],
    },
]
"""
A list of dicts, where each has `name` and `paths` keys.\n
`name` represents the name of the artifact file\n
`paths` is a list of str paths to files that will be included in the zip
the path can end with a `/*` to include only the files within the directory without creating the directory itself   
"""


class PreBuildTest(unittest.TestCase):
    """
    PreBuildTest TestCase Class
    """

    archolos_root = os.path.join(ROOT_DIR, "docs", "assets", "sources", "archolos")

    def test_archolos_gd3d11(self) -> None:
        """
        Test that all the zen_.ini files in subsequent language directories are the same
        """
        gd3d11_root = os.path.join(self.archolos_root, "system", "GD3D11")
        zen_root = os.path.join(gd3d11_root, "ZENResources")
        ini_files = [p for p in os.listdir(zen_root) if p.upper().endswith("INI")]
        lang_dirs = [p for p in os.listdir(zen_root) if os.path.isdir(os.path.join(zen_root, p))]
        for ini_file in ini_files:
            root_file = os.path.join(zen_root, ini_file)
            for lang_dir in lang_dirs:
                lang_file = os.path.join(zen_root, lang_dir, ini_file)
                self.assertIs(
                    filecmp.cmp(root_file, lang_file, shallow=False),
                    True,
                    msg=f"Files aren't equal:\nFile1: {root_file}\nFile2: {lang_file}",
                )

    def test_valid_artifacts(self):
        self.assertIs(len(ZIP_ARTIFACTS) > 0, True, msg="ZIP Artifacts cannot be empty")
        for artifact in ZIP_ARTIFACTS:
            self.assertIs(artifact.get("name") is not None, True, msg="Name key cannot be None")
            self.assertIs(artifact.get("paths") is not None, True, msg="Paths key cannot be None")


if __name__ == "__main__":
    unittest.main()
