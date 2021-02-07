import xml.etree.ElementTree as ET
from Validator import Validator
from tkinter import messagebox


class SerializationXML():

    def __init__(self, fileName ='config\empty.xml' ):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

        self.basic_information = self.root[0][0].attrib
        self.NIP = self.basic_information["NIP"]
        self.document_number = self.basic_information["nr_dokumentu"]
        self.status = self.basic_information["status"]

        self.attachment_number = self.root[0][1].text

        self.place = self.root[0][2].attrib
        self.purpose_submission = self.place["cel_zlozenia"]
        self.name_office = self.root[0][2][0].text

        self.taxpayer_data = self.root[0][3].attrib
        self.taxpayer_type = self.taxpayer_data["rodzaj_podatnika"]
        self.surname = self.root[0][3][0].text
        self.name = self.root[0][3][1].text
        self.date_birth = self.root[0][3][2].text

        self.brand = []
        self.model = []
        self.registration_number = []
        self.year_production = []
        self.date_acquisition = []
        self.date_incurred = []
        for vehicle_data in self.root.iter('dane_pojazdu'):
            self.brand.append(vehicle_data[0].text)
            self.model.append(vehicle_data[1].text)
            self.registration_number.append(vehicle_data[2].text)
            self.year_production.append(vehicle_data[3].text)
            self.date_acquisition.append(vehicle_data[4].text)
            self.date_incurred.append(vehicle_data[5].text)

        self.taxpayer_signature = self.root[0].find('podpis_podatnika')
        self.name = self.taxpayer_signature[0].text
        self.surname = self.taxpayer_signature[1].text
        self.phone_number = self.taxpayer_signature[2].text
        self.date_completion = self.taxpayer_signature[3].text
        self.signature = self.taxpayer_signature[4].text

        self.annotations = self.root[0].find('adnotacje')
        self.comments = self.annotations[0].text
        self.id_host = self.annotations[1].text
        self.signature_host = self.annotations[2].text

    def getBasic_information(self):
        return self.NIP, self.document_number, self.status

    def getAttachment_number(self):
        return self.attachment_number

    def getPlace(self):
        return self.purpose_submission, self.name_office

    def getTaxpayer_data(self):
        return self.taxpayer_type, self.surname, self.name, self.date_birth

    def getVehicle_data(self):
        return self.brand, self.model, self.registration_number, self.year_production, self.date_acquisition, self.date_incurred

    def getSignature(self):
        return self.name, self.surname, self.phone_number, self.date_completion, self.signature

    def getAnnotations(self):
        return self.comments, self.id_host, self.signature_host

    def saveSerializationXML(self,fileName):
        self.removeEmptyMarker()
        self.tree.write(fileName)
        val = Validator()
        if (val.validation(fileName)):
            messagebox.showinfo(title="Walidacja", message="Zapisano plik\nPrawidlowa walidacja")
        else:
            messagebox.showerror(title="Walidacja", message="Zapisano plik\nBlad podczas walidacji")
        print("save: " + fileName)


    def removeEmptyMarker(self):
        for vehicle_data in self.root[0].findall('dane_pojazdu'):
            checkModel = vehicle_data[0].text
            checkMarka = vehicle_data[1].text
            checkNumer = vehicle_data[2].text
            if checkModel == "" or checkMarka == "" or checkNumer == "":
                self.root[0].remove(vehicle_data)

    def setBasic_information(self, NIP, document_number, status):
        self.basic_information["NIP"] = NIP
        self.basic_information["nr_dokumentu"] = document_number
        self.basic_information["status"] = status

    def setAttachment_number(self, attachment_number):
        self.root[0][1].text = attachment_number

    def setPlace(self, purpose_submission, name_office):
        self.place["cel_zlozenia"] = purpose_submission
        self.root[0][2][0].text = name_office

    def setTaxpayer_data(self, taxpayer_type, surname, name, date_birth):
        self.taxpayer_data["rodzaj_podatnika"] = taxpayer_type
        self.root[0][3][0].text = surname
        self.root[0][3][1].text = name
        self.root[0][3][2].text = date_birth

    def setVehicle_data(self, marka, model, registration_number, year_production, date_acquisition, date_incurred):
        counter = 0
        for dane_pojazdu in self.root.iter('dane_pojazdu'):
            dane_pojazdu[0].text = marka[counter].get()
            dane_pojazdu[1].text = model[counter].get()
            dane_pojazdu[2].text = registration_number[counter].get()
            dane_pojazdu[3].text = year_production[counter]
            dane_pojazdu[4].text = date_acquisition[counter]
            dane_pojazdu[5].text = date_incurred[counter]
            counter += 1

    def setSignature(self, name, surname, phone_number, date_completion, signature):
        self.taxpayer_signature[0].text = name
        self.taxpayer_signature[1].text = surname
        self.taxpayer_signature[2].text = phone_number
        self.taxpayer_signature[3].text = date_completion
        self.taxpayer_signature[4].text = signature

    def setAnnotations(self, comments, id_host, signature_host):
        self.annotations[0].text = comments
        self.annotations[1].text = id_host
        self.annotations[2].text = signature_host