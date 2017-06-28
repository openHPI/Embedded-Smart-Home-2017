"""
Module to manage tiles that should later be rendered on a webpage in python
"""


class TileItem():
    """ Base class for tile items """

    def html(self):
        """ Should be overriden by the derived classes """
        return ""


class TileItemImage(TileItem):
    def __init__(self, location=""):
        self.location = location

    def html(self):
        return '<img src="' + self.location + '" class="img-responsive"/>'


class TileItemText(TileItem):
    def __init__(self, text="", css_class="", level=3):
        self.level = level
        self.text = text
        self.css_class = css_class

    def html(self):
        return ('<h' + str(self.level)
                + ' class="' + self.css_class + '">'
                + self.text
                + '</h' + str(self.level) + '>')


class Tile:
    def __init__(self):
        self.width = 1                   # relative
        self.items = []                  # list of TileItem objects
        self.bg = "#000000"              # background color
        self.identifier = ""             # html id, used to identify the smallest tile
        self.link = ""                   # href
        self.bootstrap_multiplier = 3    # multiplier width -> col-sm-X

    def bootstrap_width(self):
        return self.bootstrap_multiplier * self.width

    def columnclass(self):
        return "col-sm-" + str(self.bootstrap_width())

    def style(self):
        return "background: " + self.bg

    def id(self):
        return self.identifier

    def active_item(self):
        return self.items[0] if self.items else TileItem()

    def non_active_items(self):
        return self.items[1:] if len(self.items) > 1 else []


class SimpleTile(Tile):
    """ Simplified generator for tile objects """

    def __init__(self, text, background, link):
        super().__init__()

        item = TileItemText(text, "caption")
        self.items = [item]
        self.bg = background
        self.link = link


class TileManager:
    """
    Manager for a list of tiles that is to be displayed on a webpage.
    Can be iterated just like a list of rows of tiles
    """

    def __init__(self, tiles = []):
        self.tiles = tiles

        self._rows = [] # needed for iterating over the manager later

    def _split_tile_list(self):
        BOOTSTRAP_ROW_WIDTH = 12
        rows = []
        row_length = 0
        row = []

        for tile in self.tiles:
            tilewidth = tile.bootstrap_width()

            if tilewidth > BOOTSTRAP_ROW_WIDTH:
                raise Exception("Cant fit the widest item in a column.")

            if row_length + tilewidth <= BOOTSTRAP_ROW_WIDTH:
                row.append(tile)
                row_length += tilewidth
            else:
                rows.append(row)
                row = [tile]
                row_length = tilewidth

        rows.append(row)
        return rows

    def _mark_smallest_tile(self):
        if not self.tiles:
            return

        smallest_width = self.tiles[0].width
        for tile in self.tiles:
            tile.identifier = tile.identifier.replace("smallest_tile", "")
            if tile.width < smallest_width:
                smallest_width = tile.width

        for tile in self.tiles:
            if tile.width == smallest_width:
                tile.identifier += "smallest_tile"
                break

    def __iter__(self):
        self._mark_smallest_tile()
        self._rows = self._split_tile_list()

        return self._rows.__iter__()

    def __next(self):
        return self._rows.__next__()

