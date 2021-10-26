from Errors import InputListTooLong
from Evaporation import Evaporation
from Links import Conduit, Xsection
from Nodes import Node, Junction, Outfall
from Options import Options
from Rainfall import Raingage, Timeseries
from Report import Report
from Subcatchments import Subarea, Subcatchment, Infiltration
from Title import Title


def create_model(save_location, **kwargs):
    if "subcatchment_list" in kwargs.keys():
        subcatchment_list = kwargs["subcatchment_list"]
    else:
        subcatchment_list = []

    if "junction_list" in kwargs.keys():
        junction_list = kwargs["junction_list"]
    else:
        junction_list = []

    if "conduit_list" in kwargs.keys():
        conduit_list = kwargs["conduit_list"]
    else:
        conduit_list = []

    if "outfalls_list" in kwargs.keys():
        outfalls_list = kwargs["outfalls_list"]
    else:
        outfalls_list = []

    if "xsection_list" in kwargs.keys():
        xsection_list = kwargs["xsection_list"]
    else:
        xsection_list = []

    if "subarea_list" in kwargs.keys():
        subarea_list = kwargs["subarea_list"]
    else:
        subarea_list = []

    if "infiltration_list" in kwargs.keys():
        infiltration_list = kwargs["infiltration_list"]
    else:
        infiltration_list = []

    if "timeseries_list" in kwargs.keys():
        timeseries_list = kwargs["timeseries_list"]
    else:
        timeseries_list = []

    if "raingage_list" in kwargs.keys():
        raingage_list = kwargs["raingage_list"]
    else:
        raingage_list = []

    if "title_list" in kwargs.keys():
        title_list = kwargs["title_list"]
    else:
        title_list = []

    if "option_list" in kwargs.keys():
        option_list = kwargs["option_list"]
        if len(option_list) > 1:
            raise InputListTooLong(option_list)
    else:
        option_list = []

    if "report_list" in kwargs.keys():
        report_list = kwargs["report_list"]
        if len(option_list) > 1:
            raise InputListTooLong(report_list)
    else:
        report_list = []

    if "evaporation_list" in kwargs.keys():
        evaporation_list = kwargs["evaporation_list"]
        if len(evaporation_list) > 1:
            raise InputListTooLong(evaporation_list)
    else:
        evaporation_list = []

    with open(save_location, 'w') as outfile:
        """Title"""
        for line in Title.get_header():
            outfile.write(line)
        for title in title_list:
            outfile.write(title.swmm_line())
        outfile.write("\n")

        """Options"""
        for line in Options.get_header():
            outfile.write(line)
        for option in option_list:
            outfile.write(option.swmm_line())
        outfile.write("\n")

        """Evaporation"""
        for line in Evaporation.get_header():
            outfile.write(line)
        for evaporation in evaporation_list:
            outfile.write(evaporation.swmm_line())
        outfile.write("\n")

        """Raingages"""
        for line in Raingage.get_header():
            outfile.write(line)
        for raingage in raingage_list:
            outfile.write(raingage.swmm_line())
        outfile.write("\n")

        """Subcatchments"""
        for line in Subcatchment.get_header():
            outfile.write(line)
        for subcatchment in subcatchment_list:
            outfile.write(subcatchment.swmm_line())
        outfile.write("\n")

        """Subarea"""
        for line in Subarea.get_header():
            outfile.write(line)
        for subarea in subarea_list:
            outfile.write(subarea.swmm_line())
        outfile.write("\n")

        """Infiltration"""
        for line in Infiltration.get_header():
            outfile.write(line)
        for infiltration in infiltration_list:
            outfile.write(infiltration.swmm_line())
        outfile.write("\n")

        """LID_Controls"""

        """LID_Usage"""

        """Junctions"""
        for line in Junction.get_header():
            outfile.write(line)
        for junction in junction_list:
            outfile.write(junction.swmm_line())
        outfile.write("\n")

        """Outfalls"""
        for line in Outfall.get_header():
            outfile.write(line)
        for outfalls in outfalls_list:
            outfile.write(outfalls.swmm_line())
        outfile.write("\n")

        """Conduits"""
        for line in Conduit.get_header():
            outfile.write(line)
        for conduit in conduit_list:
            outfile.write(conduit.swmm_line())
        outfile.write("\n")

        """Xsections"""
        for line in Xsection.get_header():
            outfile.write(line)
        for xsection in xsection_list:
            outfile.write(xsection.swmm_line())
        outfile.write("\n")

        """Timeseries"""
        for line in Timeseries.get_header():
            outfile.write(line)
        for timeseries in timeseries_list:
            for nr in range(len(timeseries.value_list)):
                outfile.write(timeseries.swmm_line(nr))
        outfile.write("\n")

        """Report"""
        for line in Report.get_header():
            outfile.write(line)
        for report in report_list:
            outfile.write(report.swmm_line())
        outfile.write("\n")

        """Tags"""

        """Map"""

        """Coordinates"""
        for line in Node.get_coord_header():
            outfile.write(line)
        for junction in junction_list:
            outfile.write(junction.swmm_coord_line())
        for outfall in outfalls_list:
            outfile.write(outfall.swmm_coord_line())
        outfile.write("\n")

        """Vertices"""

        """Polygons"""
        for line in Subcatchment.get_polygons_header():
            outfile.write(line)
        for subcatchment in subcatchment_list:
            outfile.write(subcatchment.swmm_polygons_line())
        outfile.write("\n")

        """Symbols"""


if __name__ == "__main__":

    t1 = Title(title="title of this test inp file")

    opt = Options(flow_units="CMS")
    rep = Report(nodes_report=False)

    ts1 = Timeseries(name="t1", csv_file_location="test_timeseries.csv")
    r1 = Raingage(name="r1", source=ts1)

    e1 = Evaporation(data_source="CONSTANT", parameters=0.0)

    j1 = Junction(name="J1", elevation=96, x=3846.585, y=3874.580)
    j2 = Junction(name="J2", elevation=90, x=3924.972, y=2105.263)
    j3 = Junction(name="J3", elevation=93, x=1528.555, y=3493.841)
    j4 = Junction(name="J4", elevation=88, x=1528.555, y=1948.488)

    s1 = Subcatchment(name="S1", raingage=r1, outlet="J1", area=4, x=3477.044, y=4781.635)
    s2 = Subcatchment(name="S2", raingage=r1, outlet="J2", area=4, x=3029.115, y=3325.868)
    s3 = Subcatchment(name="S3", raingage=r1, outlet="J3", area=4, x=565.510, y=4904.815)

    c1 = Conduit(name="C1", from_node="J1", to_node="J2")
    c4 = Conduit(name="C4", from_node="J4", to_node="O1")
    c2 = Conduit(name="C2", from_node="J2", to_node="J4")
    c3 = Conduit(name="C3", from_node="J3", to_node="J4")

    o1 = Outfall(name="O1", elevation=85, x=5.599, y=1948.488)

    title_list = [t1]
    option_list = [opt]
    report_list = [rep]
    evaporation_list = [e1]
    subcatchment_list = [s1, s2, s3]
    junction_list = [j1, j2, j3, j4]
    conduit_list = [c1, c4, c2, c3]
    outfalls_list = [o1]
    timeseries_list = [ts1]
    raingage_list = [r1]

    xsection_list = []
    for c in conduit_list:
        c_inst = Xsection(link=c, shape="CIRCULAR", geom1=1)
        xsection_list.append(c_inst)

    subarea_list = []
    for s in subcatchment_list:
        sa_inst = Subarea(subcatchment=s)
        subarea_list.append(sa_inst)

    infiltration_list = []
    for s in subcatchment_list:
        i_inst = Infiltration(subcatchment=s)
        infiltration_list.append(i_inst)

    create_model("test_new_swmmput.inp",
                 subcatchment_list=subcatchment_list, title_list=title_list, option_list=option_list,
                 report_list=report_list, junction_list=junction_list, conduit_list=conduit_list,
                 outfalls_list=outfalls_list, xsection_list=xsection_list, subarea_list=subarea_list,
                 infiltration_list=infiltration_list, timeseries_list=timeseries_list, raingage_list=raingage_list,
                 evaporation_list=evaporation_list)
