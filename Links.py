class Link:
    def __init__(self, name, from_node, to_node):
        self.name = name
        self.from_node = from_node
        self.to_node = to_node

    def get_name(self):
        return self.name

    def get_from_node(self):
        return self.from_node

    def get_to_node(self):
        return self.to_node


class Conduit(Link):
    title_line = "[CONDUITS]" + "\n"
    attr_line = ";;Name           From Node        To Node          Length     Roughness  " \
                "InOffset   OutOffset  InitFlow   MaxFlow" + "\n"
    sep_line = ";;-------------- ---------------- ---------------- ---------- " \
               "---------- ---------- ---------- ---------- ----------" + "\n"

    def __init__(self, name, from_node, to_node, length=400, roughness=0.01, inoffset=0, outoffset=0, initflow=0,
                 maxflow=0):
        super().__init__(name, from_node, to_node)
        self.length = length
        self.roughness = roughness
        self.inoffset = inoffset
        self.outoffset = outoffset
        self.initflow = initflow
        self.maxflow = maxflow

    @staticmethod
    def get_header():
        return [Conduit.title_line, Conduit.attr_line, Conduit.sep_line]

    def get_length(self):
        return self.length

    def swmm_line(self):
        name_col_space = " " * (17 - len(str(self.name)))
        from_node_col_space = " " * (17 - len(str(self.from_node)))
        to_node_col_space = " " * (17 - len(str(self.to_node)))

        length_col_space = " " * (11 - len(str(self.length)))
        roughness_col_space = " " * (11 - len(str(self.roughness)))
        inoffset_col_space = " " * (11 - len(str(self.inoffset)))
        outoffset_col_space = " " * (11 - len(str(self.outoffset)))
        initflow_col_space = " " * (11 - len(str(self.initflow)))

        maxflow_col_space = " " * (10 - len(str(self.maxflow)))

        return (str(self.name) + name_col_space +
                str(self.from_node) + from_node_col_space +
                str(self.to_node) + to_node_col_space +
                str(self.length) + length_col_space +
                str(self.roughness) + roughness_col_space +
                str(self.inoffset) + inoffset_col_space +
                str(self.outoffset) + outoffset_col_space +
                str(self.initflow) + initflow_col_space +
                str(self.maxflow) + maxflow_col_space + "\n")


class Xsection:
    title_line = "[XSECTIONS]" + "\n"
    attr_line = ";;Link           Shape        Geom1            Geom2      Geom3      Geom4      Barrels    Culvert" \
                + "\n"
    sep_line = ";;-------------- ------------ ---------------- ---------- ---------- ---------- ---------- ----------" \
               + "\n"

    def __init__(self, link, geom1, shape="CIRCULAR", geom2=0, geom3=0, geom4=0, barrels=1, culvert=""):
        self.link = link.get_name()
        self.shape = shape
        self.geom1 = geom1
        self.geom2 = geom2
        self.geom3 = geom3
        self.geom4 = geom4
        self.barrels = barrels
        self.culvert = culvert

    @staticmethod
    def get_header():
        return [Xsection.title_line, Xsection.attr_line, Xsection.sep_line]

    def get_link(self):
        return self.link

    def get_shape(self):
        return self.shape

    def get_geom1(self):
        return self.geom1

    def swmm_line(self):
        link_col_space = " " * (17 - len(str(self.link)))
        shape_col_space = " " * (13 - len(str(self.shape)))
        geom1_col_space = " " * (17 - len(str(self.geom1)))
        geom2_col_space = " " * (11 - len(str(self.geom2)))
        geom3_col_space = " " * (11 - len(str(self.geom3)))
        geom4_col_space = " " * (11 - len(str(self.geom4)))
        barrels_col_space = " " * (11 - len(str(self.barrels)))
        culvert_col_space = " " * (10 - len(str(self.culvert)))

        return (str(self.link) + link_col_space +
                str(self.shape) + shape_col_space +
                str(self.geom1) + geom1_col_space +
                str(self.geom2) + geom2_col_space +
                str(self.geom3) + geom3_col_space +
                str(self.geom4) + geom4_col_space +
                str(self.barrels) + barrels_col_space +
                str(self.culvert) + culvert_col_space + "\n")