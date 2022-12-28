"""
Script that creates all the artifacts for the GitHub release.
"""
import os
import zipfile

from tests.pre_build import ZIP_ARTIFACTS


def main():
    """Creates all the artifacts for the GitHub release."""
    create_zip_artifacts(artifacts=ZIP_ARTIFACTS)


def create_zip_artifacts(*, artifacts: list[dict]):
    """Create zip artifacts for the GitHub release."""
    for artifact in artifacts:
        with zipfile.ZipFile(artifact["name"], "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
            for path in artifact["paths"]:
                root_name = os.path.basename(path)
                if root_name == "*":
                    path = os.path.dirname(path)

                for root, _, files in os.walk(path):
                    for file in files:
                        filename = os.path.join(root, file)
                        rel_filename = os.path.relpath(filename, start=path)
                        if root_name != "*":
                            rel_filename = os.path.join(root_name, rel_filename)
                        zip_file.write(filename=filename, arcname=rel_filename)


if __name__ == "__main__":
    main()
