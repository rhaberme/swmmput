class Report:
    title_line = "[REPORT]" + "\n"
    attr_line = ";;Reporting Options" + "\n"

    def __init__(self, subcatchments_report=True, nodes_report=True, links_report=True):

        if subcatchments_report == True:
            self.subcatchments_report = "ALL"
        else:
            self.subcatchments_report = "NONE"

        if nodes_report == True:
            self.nodes_report = "ALL"
        else:
            self.nodes_report = "NONE"

        if links_report == True:
            self.links_report = "ALL"
        else:
            self.links_report = "NONE"

        self.report_option_parameter = {
            "SUBCATCHMENTS": self.subcatchments_report,
            "NODES": self.nodes_report,
            "LINKS": self.links_report
        }

    @staticmethod
    def get_header():
        return [Report.title_line, Report.attr_line]

    def swmm_line(self):
        report_lines = ""
        for key in self.report_option_parameter:
            col_space = " "

            report_lines = report_lines + (key + col_space + str(self.report_option_parameter[key]) + "\n")

        return report_lines
