class Node:
    coord_title_line = "[COORDINATES]" + "\n"
    coord_attr_line = ";;Node           X-Coord            Y-Coord" + "\n"
    coord_sep_line = ";;-------------- ------------------ ------------------" + "\n"

    def __init__(self, name, x, y):
        """
        :param name: string, name of node
        :param x: float or int, x-position
        :param y: float or int, y-position
        """
        self.name = name
        self.x = x
        self.y = y

    @staticmethod
    def get_coord_header():
        return [Node.coord_title_line, Node.coord_attr_line, Node.coord_sep_line]

    def get_name(self):
        return self.name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def swmm_coord_line(self):
        node_col_space = " " * (17 - len(str(self.name)))
        x_col_space = " " * (19 - len(str(self.x)))
        y_col_space = " " * (19 - len(str(self.y)))

        return (str(self.name) + node_col_space +
                str(self.x) + x_col_space +
                str(self.y) + y_col_space + "\n")


class Junction(Node):
    title_line = "[JUNCTIONS]" + "\n"
    attr_line = ";;Name           Elevation  MaxDepth   InitDepth  SurDepth   Aponded" + "\n"
    sep_line = ";;-------------- ---------- ---------- ---------- ---------- ----------" + "\n"

    def __init__(self, name, elevation, x=0.0, y=0.0, maxdepth=4, initdepth=0, surdepth=0, aponded=0):
        """
        :param name: string, name of node
        :param elevation: float or int, elevation of node
        :param x: float or int, x-position
        :param y: float or int, y-position
        :param maxdepth: float or int, max depth of node
        :param initdepth: float or int, init depth of node
        :param surdepth:
        :param aponded:
        """
        super().__init__(name, x, y)

        self.elevation = elevation
        self.maxdepth = maxdepth
        self.initdepth = initdepth
        self.surdepth = surdepth
        self.aponded = aponded

    @staticmethod
    def get_header():
        return [Junction.title_line, Junction.attr_line, Junction.sep_line]

    def get_elevation(self):
        return self.elevation

    def get_maxdepth(self):
        return self.maxdepth

    def swmm_line(self):
        name_col_space = " " * (17 - len(str(self.name)))
        elevation_col_space = " " * (11 - len(str(self.elevation)))
        maxdepth_col_space = " " * (11 - len(str(self.maxdepth)))
        initdepth_col_space = " " * (11 - len(str(self.initdepth)))
        surdepth_col_space = " " * (11 - len(str(self.surdepth)))
        aponded_col_space = " " * (10 - len(str(self.aponded)))

        return (str(self.name) + name_col_space + str(self.elevation) + elevation_col_space + str(
            self.maxdepth) + maxdepth_col_space + str(self.initdepth) +
                initdepth_col_space + str(self.surdepth) + surdepth_col_space + str(
                    self.aponded) + aponded_col_space + "\n")


class Outfall(Node):
    title_line = "[OUTFALLS]" + "\n"
    attr_line = ";;Name           Elevation  Type       Stage Data       Gated    Route To" + "\n"
    sep_line = ";;-------------- ---------- ---------- ---------------- -------- ----------------" + "\n"

    def __init__(self, name, elevation, x=0.0, y=0.0, otype="FREE", stage_data="", gated="NO", routeto=""):
        super().__init__(name, x, y)
        self.elevation = elevation
        self.otype = otype
        self.stage_data = stage_data
        self.gated = gated
        self.routeto = routeto

    @staticmethod
    def get_header():
        return [Outfall.title_line, Outfall.attr_line, Outfall.sep_line]

    def get_elevation(self):
        return self.elevation

    def get_otype(self):
        return self.otype

    def swmm_line(self):
        name_col_space = " " * (17 - len(str(self.name)))
        elevation_col_space = " " * (11 - len(str(self.elevation)))
        otype_col_space = " " * (11 - len(str(self.otype)))
        stage_data_col_space = " " * (17 - len(str(self.stage_data)))
        gated_col_space = " " * (9 - len(str(self.gated)))
        routeto_col_space = " " * (16 - len(str(self.routeto)))

        return (str(self.name) + name_col_space +
                str(self.elevation) + elevation_col_space +
                str(self.otype) + otype_col_space +
                str(self.stage_data) + stage_data_col_space +
                str(self.gated) + gated_col_space +
                str(self.routeto) + routeto_col_space + "\n")