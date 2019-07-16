from artifactory import ArtifactoryPath

"""
Uploads test.txt to the artifactory server.
"""

def upload():
    path = ArtifactoryPath(
        "http://artifactory.calormen.net:8040/artifactory/generic-local/test",
        auth=('admin', 'f22-demo'))

    path.deploy_file("test.txt")
