class Genus:
    def __init__(self, scientific_name):
        self.scientific_name = scientific_name

felis_genus_instance = Genus("felis")
canis_genus_instance = Genus("canis")
mustela_instance = Genus("Mustela")



class Specimen:
    def __init__(self, scientific_name, common_name, region, genus):
        self.scientific_name = scientific_name
        self.common_name = common_name
        self.region = region
        self.genus = genus



canis = Genus("canis")

mog_the_cat = Specimen("Felis catus", "Domestic Cat", felis_genus_instance)


print(mog_the_cat.common_name)