class Options:
    title_line = "[OPTIONS]" + "\n"
    attr_line = ";;Option             Value" + "\n"

    def __init__(self, flow_units="CMS", infiltration="MODIFIED_GREEN_AMPT", flow_routing="KINWAVE",
                 link_offsets="DEPTH", min_slope=0.001, allow_ponding="NO", skip_steady_state="NO",
                 start_date="01/01/2021", start_time="00:00:00", report_start_date="01/01/2021",
                 report_start_time="00:00:00", end_date="01/01/2021", end_time="01:00:00", sweep_start="01/01",
                 sweep_end="12/31", dry_days="0", report_step="00:05:00", wet_step="00:05:00", dry_step="00:05:00",
                 routing_step="0:00:30", rule_step="00:00:00", inertial_damping="PARTIAL", normal_flow_limited="BOTH",
                 force_main_equation="H-W", variable_step=0.75, lengthening_step=0, min_surfarea=12.566, max_trials=8,
                 head_tolerance=0.005, sys_flow_tol=5, lat_flow_tol=5, minimum_step=0.5, threads=1):
        self.flow_units = flow_units
        self.infiltration = infiltration
        self.flow_routing = flow_routing
        self.link_offsets = link_offsets
        self.min_slope = min_slope
        self.allow_ponding = allow_ponding
        self.skip_steady_state = skip_steady_state
        self.start_date = start_date
        self.start_time = start_time
        self.report_start_date = report_start_date
        self.report_start_time = report_start_time
        self.end_date = end_date
        self.end_time = end_time
        self.sweep_start = sweep_start
        self.sweep_end = sweep_end
        self.dry_days = dry_days
        self.report_step = report_step
        self.wet_step = wet_step
        self.dry_step = dry_step
        self.routing_step = routing_step
        self.rule_step = rule_step
        self.inertial_damping = inertial_damping
        self.normal_flow_limited = normal_flow_limited
        self.force_main_equation = force_main_equation
        self.variable_step = variable_step
        self.lengthening_step = lengthening_step
        self.min_surfarea = min_surfarea
        self.max_trials = max_trials
        self.head_tolerance = head_tolerance
        self.sys_flow_tol = sys_flow_tol
        self.lat_flow_tol = lat_flow_tol
        self.minimum_step = minimum_step
        self.threads = threads

        self.option_parameter = {
            "FLOW_UNITS": self.flow_units,
            "INFILTRATION": self.infiltration,
            "FLOW_ROUTING": self.flow_routing,
            "LINK_OFFSETS": self.link_offsets,
            "MIN_SLOPE": self.min_slope,
            "ALLOW_PONDING": self.allow_ponding,
            "SKIP_STEADY_STATE": self.skip_steady_state,
            "START_DATE": self.start_date,
            "START_TIME": self.start_time,
            "REPORT_START_DATE": self.report_start_date,
            "REPORT_START_TIME": self.report_start_time,
            "END_DATE": self.end_date,
            "END_TIME": self.end_time,
            "SWEEP_START": self.sweep_start,
            "SWEEP_END": self.sweep_end,
            "DRY_DAYS": self.dry_days,
            "REPORT_STEP": self.report_step,
            "WET_STEP": self.wet_step,
            "DRY_STEP": self.dry_step,
            "ROUTING_STEP": self.routing_step,
            "RULE_STEP": self.rule_step,
            "INERTIAL_DAMPING": self.inertial_damping,
            "NORMAL_FLOW_LIMITED": self.normal_flow_limited,
            "FORCE_MAIN_EQUATION": self.force_main_equation,
            "VARIABLE_STEP": self.variable_step,
            "LENGTHENING_STEP": self.lengthening_step,
            "MIN_SURFAREA": self.min_surfarea,
            "MAX_TRIALS": self.max_trials,
            "HEAD_TOLERANCE": self.head_tolerance,
            "SYS_FLOW_TOL": self.sys_flow_tol,
            "LAT_FLOW_TOL": self.lat_flow_tol,
            "MINIMUM_STEP": self.minimum_step,
            "THREADS": self.threads}

    @staticmethod
    def get_header():
        return [Options.title_line, Options.attr_line]

    def swmm_line(self):
        option_lines = ""
        for key in self.option_parameter:
            col_space = " " * (21 - len(key))

            if key == "START_DATE" or key == "INERTIAL_DAMPING":
                option_lines = option_lines + "\n" + (key + col_space + str(self.option_parameter[key]) + "\n")
            else:
                option_lines = option_lines + (key + col_space + str(self.option_parameter[key]) + "\n")

        return option_lines