from tkinter import *
from tkinter import messagebox
from DerializationSerializationXML import SerializationXML
from tkinter.filedialog import askopenfilename, asksaveasfilename,askdirectory
from Validator import Validator
from CreatePDF import CreatePDF
from InfoVat import InfoVat26
from SaveDownloadDrive import SaveDownloadDrive


class GUI():

    def __init__(self):
        self.drive = SaveDownloadDrive()
        self.window = Tk()
        self.window.title("Vat 26")
        self.titleNIP = Label(self.window, text="Identyfikator podatkowy NIP(*)", width=30)
        self.NIP = Entry(self.window, text="", width=20, validate="focusout", validatecommand=(self.window.register(self.checkNIP)))
        self.titleDocumentNumber = Label(self.window, text="Numer dokumentu(*)", width=20)
        self.documentNumber = Entry(self.window, text="", width=20, validate="focusout", validatecommand=(self.window.register(lambda: self.checkNumber(self.documentNumber))))
        self.titleStatus = Label(self.window, text="Status", width=20)
        self.status = StringVar()
        self.active = Radiobutton(self.window, variable=self.status, value="1", text="Aktywny")
        self.finished = Radiobutton(self.window, variable=self.status, value="2", text="Zakonczona")
        self.paused = Radiobutton(self.window, variable=self.status, value="3", text="Wstrzymano")
        self.status.set("1")
        self.titleattachmentNumber = Label(self.window, text="Nr zalacznika(*)", width=30)
        self.achmentNumbe = Entry(self.window, text="", width=20, validate="focusout", validatecommand=(self.window.register(lambda: self.checkNumber(self.achmentNumbe))))
        self.titletaxOffice = Label(self.window, text="Urzad skarbowy(*)", width=30)
        self.taxOffice = Entry(self.window, text="", width=20, validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.taxOffice))))
        self.purposeForm = StringVar()
        self.titlePurposeForm = Label(self.window, text="Cel zlozenia formularza")
        self.submitting = Radiobutton(self.window, variable=self.purposeForm, value="1", text="Zlozenie informacji")
        self.update = Radiobutton(self.window, variable=self.purposeForm, value="2", text="Aktualizacja informacji")
        self.purposeForm.set("1")
        self.typeTaxpayer = StringVar()
        self.titleTypeTaxpayer = Label(self.window, text="Rodzaj podatnika")
        self.person = Radiobutton(self.window, variable=self.typeTaxpayer, value="1", text="Osoba fizyczna")
        self.notPerson = Radiobutton(self.window, variable=self.typeTaxpayer, value="2", text="Osoba nie fizyczna")
        self.typeTaxpayer.set("1")
        self.titlesurname = Label(self.window, text="Nazwisko(*)", width=30)
        self.surname = Entry(self.window, text="", width=20,  validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.surname))))
        self.titlename = Label(self.window, text="Imie(*)", width=20)
        self.name = Entry(self.window, text="", width=20,  validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.name))))
        self.titleDateBirth = Label(self.window, text="Data urodzenia", width=20)
        self.dayDateBirth = Listbox(self.window, width=3, height=1)
        for i in range(1, 32):
            self.dayDateBirth.insert('end', str(i))
        self.monthDateBirth = Listbox(self.window, width=3, height=1)
        for i in range(1, 13):
            self.monthDateBirth.insert('end', str(i))
        self.yearDateBirth = Listbox(self.window, width=5, height=1)
        for i in range(1900, 2021):
            self.yearDateBirth.insert('end', str(i))
        self.titleTableCar = Label(self.window, text="***************************************************************************************************************************Dane Pojazdow***************************************************************************************************************************",width=180)
        self.tableCar()
        self.titlesurname1 = Label(self.window, text="Nazwisko(*)", width=30)
        self.surname1 = Entry(self.window, text="", width=20, validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.surname1))))
        self.titlename1 = Label(self.window, text="Imie(*)", width=20)
        self.name1 = Entry(self.window, text="", width=20, validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.name1))))
        self.titlephoneNumber = Label(self.window, text="Numer telefonu(*)")
        self.phoneNumber = Entry(self.window, text="", width=20, validate="focusout", validatecommand=(self.window.register(self.checkPhoneNumber)))
        self.titledateCompletion = Label(self.window, text="Data wypelnienia(*)", width=20)
        self.dayDateCompletion = Listbox(self.window, width=3, height=1)
        for i in range(1, 32):
            self.dayDateCompletion.insert('end', str(i))
        self.monthDateCompletion = Listbox(self.window, width=3, height=1)
        for i in range(1, 13):
            self.monthDateCompletion.insert('end', str(i))
        self.yearDateCompletion = Listbox(self.window, width=5, height=1)
        for i in range(1900, 2021):
            self.yearDateCompletion.insert('end', str(i))
        self.titlecomments = Label(self.window, text="Uwagi urzedu skarbowego(*)", width=30)
        self.comments = Entry(self.window, text="", width=40, validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.comments))))
        self.titlIdForms = Label(self.window, text="ID przyjmujacego(*)", width=20)
        self.idForms = Entry(self.window, text="", width=20, validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.idForms))))
        self.titleSignatureTaxpayer = Label(self.window, text="Podpis podatnika(*)", width=20)
        self.signatureTaxpayer = Entry(self.window, text="", width=20, validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.signatureTaxpayer))))
        self.titleSignatureHost = Label(self.window, text="Podpis przyjmujacego(*)", width=20)
        self.signatureHost = Entry(self.window, text="", width=20, validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.signatureHost))))
        self.load = Button(self.window, text="Wczytaj", width=20, command=self.loadXML)
        self.buttonSaveXML = Button(self.window, text="Zapisz XML", width=20, command=self.saveXML)
        self.buttonSavePDF = Button(self.window, text="Zapisz XML i PDF", width=20, command=self.savePDF)
        self.buttonInfoVat26 = Button(self.window, text="Informacje vat26", width=20, command=self.infoVat)
        self.buttonSaveDrive = Button(self.window, text="Zapisz i wyslij na dysk Google", width=22, command=self.saveGoogleDrive)
        self.buttonLoadDrive = Button(self.window, text="Pobierz pliki z dysku Google", width=22, command=self.downloadGoogleDrive)
        self.createGrid()
        mainloop()



    def createGrid(self):
        PADX = 5
        PADY = 2
        self.titleNIP.grid(row=0, column=0, padx=PADX, pady=PADY)
        self.NIP.grid(row=1, column=0, padx=PADX, pady=PADY)
        self.titleDocumentNumber.grid(row=0, column=1, padx=PADX, pady=PADY)
        self.documentNumber.grid(row=1, column=1, padx=PADX, pady=PADY)
        self.titleStatus.grid(row=0, column=2, columnspan=2, padx=PADX, pady=PADY)
        self.active.grid(row=1, column=1, columnspan=3, padx=PADX, pady=PADY)
        self.finished.grid(row=1, column=2, columnspan=2, padx=PADX, pady=PADY)
        self.paused.grid(row=1, column=3, columnspan=1, padx=PADX, pady=PADY)
        self.titlesurname.grid(row=2, column=1, padx=PADX, pady=PADY)
        self.surname.grid(row=3, column=1, padx=PADX, pady=PADY)
        self.titlename.grid(row=2, column=2, padx=PADX, pady=PADY)
        self.name.grid(row=3, column=2, padx=PADX, pady=PADY)
        self.titleDateBirth.grid(row=2, column=3, columnspan=6, padx=PADX, pady=PADY)
        self.dayDateBirth.grid(row=3, column=3, columnspan=5,  padx=PADX, pady=PADY)
        self.monthDateBirth.grid(row=3, column=4, columnspan=2, padx=PADX, pady=PADY)
        self.yearDateBirth.grid(row=3, column=5, columnspan=1, padx=PADX, pady=PADY)
        self.titleattachmentNumber.grid(row=0, column=3,  padx=PADX, columnspan=6, pady=PADY)
        self.achmentNumbe.grid(row=1, column=3, padx=PADX,  columnspan=6, pady=PADY)
        self.titletaxOffice.grid(row=2, column=0, padx=PADX, pady=PADY)
        self.taxOffice.grid(row=3, column=0, padx=PADX, pady=PADY)
        self.titlePurposeForm.grid(row=4, column=0, columnspan=3, padx=PADX, pady=PADY)
        self.submitting.grid(row=5, column=0, columnspan=2, padx=PADX, pady=PADY)
        self.update.grid(row=5, column=1, columnspan=2, padx=PADX, pady=PADY)
        self.titleTypeTaxpayer.grid(row=4, column=3, columnspan=6, padx=PADX, pady=PADY)
        self.person.grid(row=5, column=3, columnspan=3, padx=PADX, pady=PADY)
        self.notPerson.grid(row=5, column=5,columnspan=3, padx=PADX, pady=PADY)
        self.titlesurname1.grid(row=6, column=0, padx=PADX, pady=PADY)
        self.surname1.grid(row=7, column=0, padx=PADX, pady=PADY)
        self.titlename1.grid(row=6, column=1, padx=PADX, pady=PADY)
        self.name1.grid(row=7, column=1, padx=PADX, pady=PADY)
        self.titlephoneNumber.grid(row=6, column=2, padx=PADX, pady=PADY)
        self.phoneNumber.grid(row=7, column=2, padx=PADX, pady=PADY)
        self.titledateCompletion.grid(row=6, column=3, columnspan=6, padx=PADX, pady=PADY)
        self.dayDateCompletion.grid(row=7, column=3, columnspan=5, padx=1, pady=PADY)
        self.monthDateCompletion.grid(row=7, column=4, columnspan=2, padx=1, pady=PADY)
        self.yearDateCompletion.grid(row=7, column=5, columnspan=1, padx=1, pady=PADY)
        self.titleTableCar.grid(row=8, column=0,  columnspan=10,padx=PADX, pady=PADY)
        self.titlecomments.grid(row=27, column=0, columnspan=2, padx=PADX, pady=PADY)
        self.comments.grid(row=28, column=0, columnspan=2, padx=PADX, pady=PADY)
        self.titlIdForms.grid(row=27, column=1, columnspan=2, padx=PADX, pady=PADY)
        self.idForms.grid(row=28, column=1, columnspan=2, padx=PADX, pady=PADY)
        self.titleSignatureTaxpayer.grid(row=27, columnspan=2, column=3, padx=PADX, pady=PADY)
        self.signatureTaxpayer.grid(row=28, column=3, columnspan=2, padx=PADX, pady=PADY)
        self.titleSignatureHost.grid(row=27, column=5, columnspan=2, padx=PADX, pady=PADY )
        self.signatureHost.grid(row=28, column=5, columnspan=2, padx=PADX, pady=PADY)
        self.load.grid(row=29, column=0, columnspan=2, padx=PADX, pady=20)
        self.buttonInfoVat26.grid(row=29, column=1, columnspan=2, padx=PADX, pady=20)
        self.buttonSaveXML.grid(row=29, column=2, columnspan=2, padx=PADX, pady=20)
        self.buttonSavePDF.grid(row=29, column=3, columnspan=2, padx=PADX, pady=20)
        self.buttonSaveDrive.grid(row=29, column=5, columnspan=2, padx=PADX, pady=20)
        self.buttonLoadDrive.grid(row=29, column=7, columnspan=2, padx=PADX, pady=20)


    def tableCar(self):
        PADX = 5
        PADY = 2
        BASE_ROW_TITLE = 9
        BASE_ROW_ENTRY = 10

        self.titleCarBrand= []
        self.carBrand = []
        self.titleModel = []
        self.model = []
        self.titleRegistration = []
        self.registration = []
        self.titleYearProduction = []
        self.yearProduction = []
        self.titleAcquisitionDate  = []
        self.dayAcquisitionDate = []
        self.monthAcquisitionDate = []
        self.yearAcquisitionDate = []
        self.titleFirstCost = []
        self.dayFirstCost  = []
        self.monthFirstCost  = []
        self.yearFirstCost  = []
        for j in range(9):
            if j == 0:
                self.titleCarBrand.append(Label(self.window, text="Marka(*)", width=30))
                self.titleModel.append(Label(self.window, text="Model(*)", width=30))
                self.titleRegistration.append(Label(self.window, text="Rejestracja(*)", width=30))
            else:
                self.titleCarBrand.append(Label(self.window, text="Marka", width=30))
                self.titleModel.append(Label(self.window, text="Model", width=30))
                self.titleRegistration.append(Label(self.window, text="Rejestracja", width=30))
            self.carBrand.append(Entry(self.window, text="", width=20))
            self.model.append(Entry(self.window, text="", width=20, validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.model[j])))))
            self.registration.append(Entry(self.window, text="", width=20, validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.registration[j])))))
            self.titleYearProduction.append(Label(self.window, text="Rok produkcji", width=30))
            self.yearProduction.append(Listbox(self.window, width=5, height=1))
            for i in range(1900, 2021):
                self.yearProduction[j].insert('end', str(i))
            self.titleAcquisitionDate.append(Label(self.window, text="Data nabycia", width=30))
            self.dayAcquisitionDate.append(Listbox(self.window, width=3, height=1))
            for i in range(1, 32):
                self.dayAcquisitionDate[j].insert('end', str(i))
            self.monthAcquisitionDate.append(Listbox(self.window, width=3, height=1))
            for i in range(1, 13):
                self.monthAcquisitionDate[j].insert('end', str(i))
            self.yearAcquisitionDate.append(Listbox(self.window, width=5, height=1))
            for i in range(1900, 2021):
                self.yearAcquisitionDate[j].insert('end', str(i))
            self.titleFirstCost.append(Label(self.window, text="Pierwszy wydatek", width=30))
            self.dayFirstCost.append(Listbox(self.window, width=3, height=1))
            for i in range(1, 32):
                self.dayFirstCost[j].insert('end', str(i))
            self.monthFirstCost.append(Listbox(self.window, width=3, height=1))
            for i in range(1, 13):
                self.monthFirstCost[j].insert('end', str(i))
            self.yearFirstCost.append(Listbox(self.window, width=5, height=1))
            for i in range(1900, 2021):
                self.yearFirstCost[j].insert('end', str(i))

            self.titleCarBrand[j].grid(row=BASE_ROW_TITLE + j*2, column=0, padx=PADX, pady=PADY)
            self.carBrand[j].grid(row=BASE_ROW_ENTRY+ j*2, column=0, padx=PADX, pady=PADY)
            self.titleModel[j].grid(row=BASE_ROW_TITLE+ j*2, column=1, padx=PADX, pady=PADY)
            self.model[j].grid(row=BASE_ROW_ENTRY+ j*2, column=1, padx=PADX, pady=PADY)
            self.titleRegistration[j].grid(row=BASE_ROW_TITLE+ j*2, column=2, padx=PADX, pady=PADY)
            self.registration[j].grid(row=BASE_ROW_ENTRY+ j*2, column=2, padx=PADX, pady=PADY)
            self.titleYearProduction[j].grid(row=BASE_ROW_TITLE + j*2, column=3, padx=PADX, pady=PADY)
            self.yearProduction[j].grid(row=BASE_ROW_ENTRY+ j*2, column=3, padx=1, pady=PADY)
            self.titleAcquisitionDate[j].grid(row=BASE_ROW_TITLE+ j*2, column=4, columnspan=3, padx=PADX, pady=PADY)
            self.dayAcquisitionDate[j].grid(row=BASE_ROW_ENTRY+ j*2, sticky= E, column=4, padx=1, pady=PADY)
            self.monthAcquisitionDate[j].grid(row=BASE_ROW_ENTRY+ j*2, column=5, padx=1, pady=PADY)
            self.yearAcquisitionDate[j].grid(row=BASE_ROW_ENTRY+ j*2, sticky= W, column=6, padx=1, pady=PADY)
            self.titleFirstCost[j].grid(row=BASE_ROW_TITLE+ j*2, column=7, columnspan=3, padx=PADX, pady=PADY)
            self.dayFirstCost[j].grid(row=BASE_ROW_ENTRY+ j*2, sticky= E, column=7, padx=1, pady=PADY)
            self.monthFirstCost[j].grid(row=BASE_ROW_ENTRY+ j*2, column=8, padx=1, pady=PADY)
            self.yearFirstCost[j].grid(row=BASE_ROW_ENTRY+ j*2, sticky= W, column=9, padx=1, pady=PADY)

        self.carBrand[0].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.carBrand[0]))))
        self.carBrand[1].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.carBrand[1]))))
        self.carBrand[2].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.carBrand[2]))))
        self.carBrand[3].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.carBrand[3]))))
        self.carBrand[4].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.carBrand[4]))))
        self.carBrand[5].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.carBrand[5]))))
        self.carBrand[6].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.carBrand[6]))))
        self.carBrand[7].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.carBrand[7]))))
        self.carBrand[8].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.carBrand[8]))))
        self.model[0].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.model[0]))))
        self.model[1].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.model[1]))))
        self.model[2].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.model[2]))))
        self.model[3].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.model[3]))))
        self.model[4].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.model[4]))))
        self.model[5].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.model[5]))))
        self.model[6].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.model[6]))))
        self.model[7].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.model[7]))))
        self.model[8].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.model[8]))))
        self.registration[0].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.registration[0]))))
        self.registration[1].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.registration[1]))))
        self.registration[2].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.registration[2]))))
        self.registration[3].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.registration[3]))))
        self.registration[4].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.registration[4]))))
        self.registration[5].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.registration[5]))))
        self.registration[6].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.registration[6]))))
        self.registration[7].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.registration[7]))))
        self.registration[8].config(validate="focusout", validatecommand=(self.window.register(lambda: self.checkSmallString(self.registration[8]))))


    def infoVat(self):
        newInfo = InfoVat26()
        text = newInfo.getInfoVat26()
        messagebox.showinfo("Jak wyliczyć termin na złozenie druku VAT-26?", text)

    def saveGoogleDrive(self):
        filname = self.saveXML()
        if(filname != ""):
            self.drive.saveFile(filname)
            messagebox.showinfo("Info", "Wylano plik")

    def downloadGoogleDrive(self):
        directory = askdirectory()
        counter = self.drive.downloadFiles(directory)
        messagebox.showinfo("Info", "Pobrano "+counter+"plikow")

    def convertDate(self, date):
        year = int(date[0:4])
        year = year - 1900
        month = int(date[5:7])-1
        day = int(date[8:10])-1
        return day,month,year

    def convertDateToString(self, day,month,year):
        newDay = day.nearest(0) + 1
        if newDay < 10:
            newDay = "0"+str(newDay)
        newMonth = month.nearest(0) + 1
        if newMonth < 10:
            newMonth = "0"+str(newMonth)
        newYear = year.nearest(0) + 1900
        newDate = str(newYear)+"-"+str(newMonth)+"-"+str(newDay)
        return newDate

    def checkIfEmptyData(self):
        check = True
        if len(self.NIP.get()) == 0:
           check = False
        elif len(self.documentNumber.get()) == 0:
           check = False
        elif len(self.status.get()) == 0:
           check = False
        elif len(self.achmentNumbe.get()) == 0:
           check = False
        elif len(self.surname.get()) == 0:
           check = False
        elif len(self.name.get()) == 0:
           check = False
        elif len(self.taxOffice.get()) == 0:
           check = False
        elif len(self.surname1.get()) == 0:
           check = False
        elif len(self.name1.get()) == 0:
           check = False
        elif len(self.comments.get()) == 0:
           check = False
        elif len(self.idForms.get()) == 0:
           check = False
        elif len(self.signatureTaxpayer.get()) == 0:
           check = False
        elif len(self.signatureHost.get()) == 0:
           check = False
        elif len(self.carBrand[0].get()) == 0:
           check = False
        elif len(self.model[0].get()) == 0:
           check = False
        elif len(self.registration[0].get()) == 0:
           check = False
        return check

    def saveXML(self):
        if(self.checkIfEmptyData()):
            xml = SerializationXML()
            fileName = self.selectedSaveFile()
            if (self.status.get() == "1"):
                newStatus = "aktywny"
            elif(self.status.get() == "2"):
                newStatus = "zakonczona"
            else:
                newStatus = "wstrzymano"
            xml.setBasic_information(self.NIP.get(),self.documentNumber.get(), newStatus)
            xml.setAttachment_number(self.achmentNumbe.get())
            if(self.purposeForm.get() == "1"):
                newPurposeForm ="zlozenie informacji"
            else:
                newPurposeForm = "aktualizacja informacji"
            xml.setPlace(newPurposeForm,self.taxOffice.get())
            if (self.typeTaxpayer.get() == "1"):
                newTypeTaxpayer = "jest osoba fizyczna"
            else:
                newTypeTaxpayer = "nie jest osoba fizyczna"
            date = self.convertDateToString(self.dayDateBirth, self.monthDateBirth, self.yearDateBirth)
            xml.setTaxpayer_data(newTypeTaxpayer, self.surname.get(), self.name.get(), date)
            date = self.convertDateToString(self.dayDateCompletion, self.monthDateCompletion, self.yearDateCompletion)
            xml.setSignature(self.name1.get(), self.surname1.get(), self.phoneNumber.get(), date, self.signatureTaxpayer.get())
            xml.setAnnotations(self.comments.get(), self.idForms.get(), self.signatureHost.get())

            newYearProduction = []
            newAcquisitionDate = []
            newFirstCost = []
            for i in range(len(self.carBrand)):
                newYearProduction.append(str(self.yearProduction[i].nearest(0) + 1900))
                date = self.convertDateToString(self.dayAcquisitionDate[i], self.monthAcquisitionDate[i], self.yearAcquisitionDate[i])
                newAcquisitionDate.append(date)
                date = self.convertDateToString(self.dayFirstCost[i], self.monthFirstCost[i],self.yearFirstCost[i])
                newFirstCost.append(date)
            xml.setVehicle_data(self.carBrand, self.model, self.registration, newYearProduction, newAcquisitionDate, newFirstCost)
            xml.saveSerializationXML(fileName)
            return fileName
        else:
            messagebox.showerror(title="Blad danych", message="Prosze uzupenic wszystkie kolumny z obowiazkowe (*)")
            return ""

    def savePDF(self):
        name = self.saveXML()
        if(name != ""):
            CreatePDF(name)


    def selectedLoadFile(self):
        fileName = askopenfilename(filetypes=[("XML","*.xml")])
        return fileName

    def selectedSaveFile(self):
        fileName = asksaveasfilename(filetypes=[("XML","*.xml")], defaultextension = "*.xml")
        return fileName

    def loadXML(self):
        fileName = self.selectedLoadFile()
        val  = Validator()
        if(val.validation(fileName)):
            xml = SerializationXML(fileName)
            newNIP, newDocumentNumber, newStatus = xml.getBasic_information()
            self.NIP.delete(0, END)
            self.NIP.insert(0,newNIP)
            self.documentNumber.delete(0, END)
            self.documentNumber.insert(0,newDocumentNumber)
            if newStatus == "aktywny":
                self.status.set("1")
            elif newStatus == "zakonczona":
                self.status.set("2")
            else:
                self.status.set("3")

            newAchmentNumbe = xml.getAttachment_number()
            self.achmentNumbe.delete(0, END)
            self.achmentNumbe.insert(0, newAchmentNumbe)

            newPurposeForm, newTaxOffice = xml.getPlace()
            if newPurposeForm == "zlozenie informacji":
                self.purposeForm.set("1")
            else:
                self.purposeForm.set("2")
            self.taxOffice.delete(0, END)
            self.taxOffice.insert(0, newTaxOffice)

            newTypeTaxpayer, newSurname, newName, newDateBirth = xml.getTaxpayer_data()
            self.surname.delete(0, END)
            self.surname.insert(0, newSurname)
            self.name.delete(0, END)
            self.name.insert(0, newName)

            if newTypeTaxpayer == "jest osoba fizyczna":
                self.typeTaxpayer.set("1")
            else:
                self.typeTaxpayer.set("2")

            day, month,year =self.convertDate(newDateBirth)
            self.yearDateBirth.yview(year)
            self.monthDateBirth.yview(month)
            self.dayDateBirth.yview(day)

            newName, newSurname, newPhoneNumber, newDateCompletion, newSignatureTaxpayer = xml.getSignature()
            self.name1.delete(0, END)
            self.name1.insert(0, newName)
            self.surname1.delete(0, END)
            self.surname1.insert(0, newSurname)
            self.phoneNumber.delete(0, END)
            self.phoneNumber.insert(0, newPhoneNumber)
            self.signatureTaxpayer.delete(0, END)
            self.signatureTaxpayer.insert(0, newSignatureTaxpayer)
            day, month, year = self.convertDate(newDateCompletion)
            self.yearDateCompletion.yview(year)
            self.monthDateCompletion.yview(month)
            self.dayDateCompletion.yview(day)

            newComments, newIdForms, newSignatureHost = xml.getAnnotations()
            self.comments.delete(0, END)
            self.comments.insert(0, newComments)
            self.idForms.delete(0, END)
            self.idForms.insert(0, newIdForms)
            self.signatureHost.delete(0, END)
            self.signatureHost.insert(0, newSignatureHost)

            newCarBrand, newModel, newRegistration, newYearProduction, newAcquisitionDate, newYearFirstCost = xml.getVehicle_data()
            for i in range(len(newCarBrand)):
                self.carBrand[i].delete(0, END)
                self.carBrand[i].insert(0, newCarBrand[i])
                self.model[i].delete(0, END)
                self.model[i].insert(0, newModel[i])
                self.registration[i].delete(0, END)
                self.registration[i].insert(0, newRegistration[i])
                yearProduction = int(newYearProduction[i]) - 1900
                self.yearProduction[i].yview(yearProduction)
                day, month, year = self.convertDate(newAcquisitionDate[i])
                self.dayAcquisitionDate[i].yview(day)
                self.monthAcquisitionDate[i].yview(month)
                self.yearAcquisitionDate[i].yview(year)
                day, month, year = self.convertDate(newYearFirstCost[i])
                self.dayFirstCost[i].yview(day)
                self.monthFirstCost[i].yview(month)
                self.yearFirstCost[i].yview(year)
            print("open: " +fileName)
        else:
            messagebox.showerror(title="Blad danych", message="Wybrano bledny plik")

    def checkInt(self,number):
        try:
            int(number)
            return True
        except ValueError:
            return False

    def checkNIP(self):
        if(self.checkInt(self.NIP.get())):
            NIP = int(self.NIP.get())
            if(NIP < 1000000000 or NIP >9999999999):
                messagebox.showerror(title="Blad danych", message="Bledny NIP\nPrawidlowy NIP zawiara 10 cyfr")
                self.NIP.delete(0, END)
                return False
        else:
            messagebox.showerror(title="Blad danych", message="Nie mozna uzywac znakow w numereach liczbowych")
            self.NIP.delete(0, END)
            return False
        return True

    def checkNumber(self,widget):
        if (self.checkInt(widget.get())):
            number = int(widget.get())
            if (number < 0):
                messagebox.showerror(title="Blad danych", message="Numery musza byc liczbami dodatnimi")
                widget.delete(0, END)
                return False
        else:
            messagebox.showerror(title="Blad danych", message="Nie mozna uzywac znakow w numerach liczbowych")
            widget.delete(0, END)
            return False
        return True

    def checkPhoneNumber(self):
        if(self.checkInt(self.phoneNumber.get())):
            phoneNumber = int(self.phoneNumber.get())
            if(phoneNumber < 100000000 or phoneNumber >999999999):
                messagebox.showerror(title="Blad danych", message="Bledny numer telefonu\nPrawidlowy numer telefonu zawiara 9 cyfr")
                self.phoneNumber.delete(0, END)
                return False
        else:
            messagebox.showerror(title="Blad danych", message="Nie mozna uzywac znakow w numereach liczbowych")
            self.phoneNumber.delete(0, END)
            return False
        return True

    def checkSmallString(self,widget):
        text = widget.get()
        if (len(text) > 20):
            messagebox.showerror(title="Blad danych", message="Tekst nie moze przekraczac 20 znakow")
            widget.delete(0, END)
            return False
        elif len(text) == 0:
            messagebox.showerror(title="Blad danych", message="Pole nie moze byc puste")
            return False
        else:
            return True




