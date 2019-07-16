from artifactory import ArtifactoryPath

"""
Downloads the list of numbers and puts them into old.txt
"""

def download():
    path = ArtifactoryPath(
        "http://artifactory.calormen.net:8040/artifactory/generic-local/test/numbers.txt",
        auth=('admin', 'f22-demo'))

    with path.open() as fd:
        with open("old.txt", "wb") as out:
            out.write(fd.read())

