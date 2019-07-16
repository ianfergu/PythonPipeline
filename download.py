import sys
import requests
from artifactory import ArtifactoryPath
import random


def download():
    path = ArtifactoryPath(
        "http://artifactory.calormen.net:8040/artifactory/generic-local/test/old.txt",
        auth=('admin', 'f22-demo'))

    with path.open() as fd:
        with open("old.txt", "wb") as out:
            out.write(fd.read())
