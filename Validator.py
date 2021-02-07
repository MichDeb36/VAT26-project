import xmlschema

class Validator():

    def __init__(self):
        self.schema = xmlschema.XMLSchema('config\schema.xsd')

    def validation(self,filname):
        check = self.schema.is_valid(filname)
        return check
