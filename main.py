import upload as u
import download as d
import helpers as h

"""
This simply downloads, calculates, and then uploads the results in one fell swoop.
"""


def main():
    d.download()
    h.calculate()
    u.upload()

