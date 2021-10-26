class Subcatchment:
    title_line = "[SUBCATCHMENTS]" + "\n"
    attr_line = ";;Name           Rain Gage        Outlet           Area     %Imperv  Width    " \
                "%Slope   CurbLen  SnowPack" + "\n"
    sep_line = ";;-------------- ---------------- ---------------- -------- -------- -------- " \
               "-------- -------- ----------------" + "\n"

    polygons_title_line = "[Polygons]" + "\n"
    polygons_attr_line = ";;Subcatchment   X-Coord            Y-Coord" + "\n"
    polygons_sep_line = ";;-------------- ------------------ ------------------" + "\n"

    def __init__(self, name, raingage, outlet, area, imperv_perc=50, width=400, slope_perc=0.5, curblen=0, snowpack="",
                 x=0.0, y=0.0):
        self.name = name
        self.raingage = raingage
        self.outlet = outlet
        self.area = area
        self.imperv_perc = imperv_perc
        self.width = width
        self.slope_perc = slope_perc
        self.curblen = curblen
        self.snowpack = snowpack
        self.x = x
        self.y = y

    @staticmethod
    def get_header():
        return [Subcatchment.title_line, Subcatchment.attr_line, Subcatchment.sep_line]

    @staticmethod
    def get_polygons_header():
        return [Subcatchment.polygons_title_line, Subcatchment.polygons_attr_line, Subcatchment.polygons_sep_line]

    def get_name(self):
        return self.name

    def get_raingage(self):
        return self.raingage

    def get_outlet(self):
       return self.outlet

    def get_area(self):
        return self.area

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def swmm_line(self):
        name_col_space = " " * (17 - len(str(self.name)))
        raingage_col_space = " " * (17 - len(str(self.raingage.get_name())))
        outlet_col_space = " " * (17 - len(str(self.outlet)))
        area_col_space = " " * (9 - len(str(self.area)))
        imperv_perc_col_space = " " * (9 - len(str(self.imperv_perc)))
        width_col_space = " " * (9 - len(str(self.width)))
        slope_perc_col_space = " " * (9 - len(str(self.slope_perc)))
        curblen_col_space = " " * (9 - len(str(self.curblen)))
        snowpack_col_space = " " * (16 - len(str(self.snowpack)))

        return (str(self.name) + name_col_space +
                str(self.raingage.get_name()) + raingage_col_space +
                str(self.outlet) + outlet_col_space +
                str(self.area) + area_col_space +
                str(self.imperv_perc) + imperv_perc_col_space +
                str(self.width) + width_col_space +
                str(self.slope_perc) + slope_perc_col_space +
                str(self.curblen) + curblen_col_space +
                str(self.snowpack) + snowpack_col_space + "\n")

    def swmm_polygons_line(self):
        name_col_space = " " * (17 - len(str(self.name)))
        x_col_space = " " * (19 - len(str(self.x)))
        y_col_space = " " * (19 - len(str(self.y)))

        return (str(self.name) + name_col_space +
                str(self.x) + x_col_space +
                str(self.y) + y_col_space + "\n")


class Subarea:
    title_line = "[SUBAREAS]" + "\n"
    attr_line = ";;Subcatchment   N-Imperv   N-Perv     S-Imperv   S-Perv     PctZero    RouteTo    PctRouted" + "\n"
    sep_line = ";;-------------- ---------- ---------- ---------- ---------- ---------- ---------- ----------" + "\n"

    def __init__(self, subcatchment, nimperv=0.01, nperv=0.10, s_imperv=0.05, sperv=0.05, pctzero=25, routeto="OUTLET",
                 pctrounded=""):
        self.subcatchment = subcatchment
        self.nimperv = nimperv
        self.nperv = nperv
        self.s_imperv = s_imperv
        self.sperv = sperv
        self.pctzero = pctzero
        self.routeto = routeto
        self.pctrounded = pctrounded

    @staticmethod
    def get_header():
        return [Subarea.title_line, Subarea.attr_line, Subarea.sep_line]

    def get_subcatchment(self):
        return self.subcatchment

    def swmm_line(self):
        subcatchment_col_space = " " * (17 - len(str(self.subcatchment.get_name())))
        nimperv_col_space = " " * (11 - len(str(self.nimperv)))
        nperv_col_space = " " * (11 - len(str(self.nperv)))
        s_imperv_col_space = " " * (11 - len(str(self.s_imperv)))
        sperv_col_space = " " * (11 - len(str(self.sperv)))
        pctzero_col_space = " " * (11 - len(str(self.pctzero)))
        routeto_col_space = " " * (11 - len(str(self.routeto)))
        pctrounded_col_space = " " * (10 - len(str(self.pctrounded)))

        return (str(self.subcatchment.get_name()) + subcatchment_col_space +
                str(self.nimperv) + nimperv_col_space +
                str(self.nperv) + nperv_col_space +
                str(self.s_imperv) + s_imperv_col_space +
                str(self.sperv) + sperv_col_space +
                str(self.pctzero) + pctzero_col_space +
                str(self.routeto) + routeto_col_space +
                str(self.pctrounded) + pctrounded_col_space + "\n")


class Infiltration:
    title_line = "[INFILTRATION]" + "\n"
    attr_line = ";;Subcatchment   Param1     Param2     Param3     Param4     Param5" + "\n"
    sep_line = ";;-------------- ---------- ---------- ---------- ---------- ----------" + "\n"

    def __init__(self, subcatchment, param1=3.5, param2=0.5, param3=0.26, param4="", param5=""):
        self.subcatchment = subcatchment
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.param5 = param5

    @staticmethod
    def get_header():
        return [Infiltration.title_line, Infiltration.attr_line, Infiltration.sep_line]

    def get_subcatchment(self):
        return self.subcatchment

    def get_param1(self):
        return self.param1

    def get_param2(self):
        return self.param2

    def get_param3(self):
        return self.param3

    def swmm_line(self):
        subcatchment_col_space = " " * (17 - len(str(self.subcatchment.get_name())))
        param1_col_space = " " * (11 - len(str(self.param1)))
        param2_col_space = " " * (11 - len(str(self.param2)))
        param3_col_space = " " * (11 - len(str(self.param3)))
        param4_col_space = " " * (11 - len(str(self.param4)))
        param5_col_space = " " * (10 - len(str(self.param5)))

        return (str(self.subcatchment.get_name()) + subcatchment_col_space +
                str(self.param1) + param1_col_space +
                str(self.param2) + param2_col_space +
                str(self.param3) + param3_col_space +
                str(self.param4) + param4_col_space +
                str(self.param5) + param5_col_space + "\n")