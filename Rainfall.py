
class Timeseries:
    title_line = "[TIMESERIES]" + "\n"
    attr_line = ";;Name           Date       Time       Value" + "\n"
    sep_line = ";;-------------- ---------- ---------- ----------" + "\n"

    def __init__(self, name, csv_file_location, date=""):
        import pandas as pd
        self.name = name
        self.date = date

        time_value_df = pd.read_csv(csv_file_location)
        self.time_list = time_value_df['time'].tolist()
        self.value_list = time_value_df['value'].tolist()

    @staticmethod
    def get_header():
        return [Timeseries.title_line, Timeseries.attr_line, Timeseries.sep_line]

    def get_name(self):
        return self.name

    def get_time_and_value(self, nr):
        return self.time_list[nr], self.value_list[nr]

    def get_date(self):
        return self.date

    def swmm_line(self, nr):
        name_col_space = " " * (17 - len(str(self.name)))
        date_col_space = " " * (11 - len(str(self.date)))
        time_col_space = " " * (11 - len(str(self.time_list[nr])))
        value_col_space = " " * (11 - len(str(self.value_list[nr])))

        return (str(self.name) + name_col_space +
                str(self.date) + date_col_space +
                str(self.time_list[nr]) + time_col_space +
                str(self.value_list[nr]) + value_col_space + "\n")


class Raingage:
    title_line = "[RAINGAGES]" + "\n"
    attr_line = ";;Name           Format    Interval SCF      Source" + "\n"
    sep_line = ";;-------------- --------- ------ ------ ----------" + "\n"

    def __init__(self, name, source, rformat="INTENSITY", interval="0:05", scf=1.0):
        self.name = name
        self.rformat = rformat
        self.interval = interval
        self.scf = scf
        self.source = source
        self.source_name = "TIMESERIES " + str(source.get_name())

    @staticmethod
    def get_header():
        return [Raingage.title_line, Raingage.attr_line, Raingage.sep_line]

    def get_name(self):
        return self.name

    def get_source(self):
        return self.source

    def get_rformat(self):
        return self.rformat

    def swmm_line(self):
        name_col_space = " " * (17 - len(str(self.name)))
        format_col_space = " " * (10 - len(str(self.rformat)))
        interval_col_space = " " * (7 - len(str(self.interval)))
        scf_col_space = " " * (7 - len(str(self.scf)))
        source_col_space = " " * (10 - len(str(self.source_name)))

        return (str(self.name) + name_col_space +
                str(self.rformat) + format_col_space +
                str(self.interval) + interval_col_space +
                str(self.scf) + scf_col_space +
                str(self.source_name) + source_col_space + "\n")