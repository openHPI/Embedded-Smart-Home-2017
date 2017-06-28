"""
Helper classes and functions
"""

class PageContext():
    """ Context class to be passed to a template for rendering the navbar """

    def __init__(self, title="", active_site="", super_sites=[]):
        self.title = title

        self.active_site = active_site  # navbar current site (not clickable)
        self.super_sites = super_sites  # mavbar super sites ( tuple: link, text )
