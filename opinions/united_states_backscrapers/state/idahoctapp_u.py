import idahoctapp_civil


class Site(idahoctapp_civil.Site):
    def __init__(self):
        super(Site, self).__init__()
        self.url = 'http://www.isc.idaho.gov/opinions/caunpub.htm'
        self.court_id = self.__module__

    def _get_precedential_statuses(self):
        return ["Unpublished"] * len(self.case_names)
