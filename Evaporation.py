class Evaporation:
    title_line = "[EVAPORATION]" + "\n"
    attr_line = ";;Data Source    Parameters" + "\n"
    sep_line = ";;-------------- ----------------" + "\n"

    def __init__(self, data_source="CONSTANT", parameters=0.0, dry_only="NO"):

        self.data_source = data_source
        self.dry_only = dry_only
        self.parameters = parameters

        if type(self.parameters) is not list:
            self.evaporation_name_dict = {
                self.data_source: self.parameters,
                "DRY_ONLY": self.dry_only
            }
        else:
            if len(self.parameters) != 12:
                raise MonthlyListNotRightLength(self.parameters)
            parameters_line = ""
            for par in self.parameters:
                col_space = " " * (7 - len(str(par)))
                parameters_line = parameters_line + str(par) + col_space

            self.evaporation_name_dict = {
                self.data_source: parameters_line,
                "DRY_ONLY": dry_only}

    @staticmethod
    def get_header():
        return [Evaporation.title_line, Evaporation.attr_line, Evaporation.sep_line]

    def swmm_line(self):

        evaporation_lines = ""

        for key in self.evaporation_name_dict:
            col_space = " " * (17 - len(str(key)))

            evaporation_lines = evaporation_lines + (key + col_space + str(self.evaporation_name_dict[key]) + "\n")

        return evaporation_lines
