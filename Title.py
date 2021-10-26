class Title:
    title_line = "[TITLE]" + "\n"
    attr_line = ";;Project Title/Notes" + "\n"

    def __init__(self, title=""):
        self.title = title

    def get_title(self):
        return self.title

    @staticmethod
    def get_header():
        return [Title.title_line, Title.attr_line]

    def swmm_line(self):
        return str(self.title) + "\n"
