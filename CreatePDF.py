from xhtml2pdf import pisa
from DerializationSerializationXML import SerializationXML
class CreatePDF():

    def __init__(self,fileName):
        self.fileName = fileName
        xml = SerializationXML(fileName)
        self.NIP, self.nr_dokumentu, self.status =xml.getBasic_information()
        self.nr_zalacznika = xml.getAttachment_number()
        self.cel_zlozenia, self.nazwa_urzedu =  xml.getPlace()
        self.rodzaj_podatnika, self.nazwisko, self.imie, self.data_urodzenia = xml.getTaxpayer_data()
        self.marka, self.model, self.numer_rejestracyjny, self.rok_produkkcji, self.data_nabycia, self.data_poniesienai = xml.getVehicle_data()
        self.fillingEmptyTeble()
        self.imie, self.nazwisko, self.telefon, self.data_wypelnienia, self.podpis = xml.getSignature()
        self.uwagi, self.id_przyjmujacego, self.popis_przyjmujacego = xml.getAnnotations()
        self.createHTML()
        self.saveNewPDF()

    def fillingEmptyTeble(self):
        if(len(self.marka) < 9):
            counter = 9 - len(self.marka)
            for i in range(counter):
                self.marka.append("")
                self.model.append("")
                self.numer_rejestracyjny.append("")
                self.rok_produkkcji.append("")
                self.data_nabycia.append("")
                self.data_poniesienai.append("")

    def saveNewPDF(self):
        outfile = self.fileName.split('.')[0] + '.pdf'
        result_file = open(outfile, "w+b")
        pisa.CreatePDF(self.contentHTML, dest=result_file)
        result_file.close()
        print("save:",outfile)

    def createHTML(self):
        self.contentHTML ="""
        <html>
            <body>
                <h1>VAT-26</h1>
                 <p align="center" >
                   <table border="1" cellpadding="3">
                    <tr>
                        <td><b>1. Identyfikator podatkowy NIP </b></td> <td> <b>2. Numer dokumentu </b></td> <td> <b>3. Status</b></td>
                    </tr>
                    <tr>
                        <td>"""+self.NIP+""" </td> <td> """+self.nr_dokumentu+""" </td> <td> """+self.status+"""</td>
                    </tr>
                    </table>
                    <h1>Informacja o pojazdach samochodowych wykorzystywanych wylacznie do dzialalnosci gospodarczej</h1>
                </p>
                <p align="center">
                    <table border="1" cellpadding="3">
                    <tr>
                        <td width="100"><b>4. Nr zalacznika</b></td> 
                    </tr>
                    <tr>
                        <td>"""+self.nr_zalacznika+"""</td> 
                    </tr>
                    </table>
                </p>
                <p align="center">
                    <h1>A. MIEJSCE I CEL SKLADANIA INFORMACJI</h1>
                    <table border="1" cellpadding="3">
                    <tr>
                        <td><b>5. Urzad skarbowy, do ktorego adresowana jest informacja</b></td> <td>"""+self.nazwa_urzedu+"""</td> 
                    </tr>
                    <tr>
                        <td><b>Cel zlozenia folrmularza</b></td> <td>"""+self.cel_zlozenia+"""</td> 
                    </tr>
                    </table>
                </p>
                <p align="center">
                    <h1>B. DANE INDENTYFIKACYJNE PODATNIKA</h1>
                    <table border="1" cellpadding="3">
                    <tr>
                        <td width="100"><b>8. Rodzaj podatnika </b></td> <td width="100">"""+self.rodzaj_podatnika+""" </td> 
                    </tr>
                    <tr>
                        <td width="100"><b>Nazwisko</b></td> <td width="100">"""+self.nazwisko+"""</td> 
                    </tr>
                    <tr>
                        <td width="100"><b>Imie</b></td> <td width="100">"""+self.imie+"""</td> 
                    </tr>
                    <tr>
                        <td width="100"><b>Data urodzenia</b></td> <td width="100">"""+self.data_urodzenia+"""</td> 
                    </tr>
                    </table>
                </p>
                <p align="center">
                    <h1>C. DANE POJAZDU SAMOCHODOWEGO WYKORZYSTAWANEGO WYLACZNIE DO DZIALANOSCI GOSPODARCZEJ</h1>
                    <table border="1" cellpadding="3">
                    <tr>
                        <td width="15">Lp.</td> <td><b>Marka</b></td> <td><b>Model</b></td> <td><b>Numer rejestracyjny</b></td> <td><b>Rok produkcji</b></td> <td><b>Data nabycia pojazdu</b></td> <td><b>Data poniesienia pierwszego wydatku</b></td> 
                    </tr>
                    <tr>
                        <td>1</td> <td>"""+self.marka[0]+"""</td> <td>"""+self.model[0]+"""</td> <td>"""+self.numer_rejestracyjny[0]+"""</td> <td>"""+self.rok_produkkcji[0]+"""</td> <td>"""+self.data_nabycia[0]+"""</td> <td>"""+self.data_poniesienai[0]+"""</td> 
                    </tr>
                    <tr>
                        <td>2</td> <td>"""+self.marka[1]+"""</td> <td>"""+self.model[1]+"""</td> <td>"""+self.numer_rejestracyjny[1]+"""</td> <td>"""+self.rok_produkkcji[1]+"""</td> <td>"""+self.data_nabycia[1]+"""</td> <td>"""+self.data_poniesienai[1]+"""</td>  
                    </tr>
                    <tr>
                        <td>3</td> <td>"""+self.marka[2]+"""</td> <td>"""+self.model[2]+"""</td> <td>"""+self.numer_rejestracyjny[2]+"""</td> <td>"""+self.rok_produkkcji[2]+"""</td> <td>"""+self.data_nabycia[2]+"""</td> <td>"""+self.data_poniesienai[2]+"""</td> 
                    </tr>
                    <tr>
                        <td>4</td> <td>"""+self.marka[3]+"""</td> <td>"""+self.model[3]+"""</td> <td>"""+self.numer_rejestracyjny[3]+"""</td> <td>"""+self.rok_produkkcji[3]+"""</td> <td>"""+self.data_nabycia[3]+"""</td> <td>"""+self.data_poniesienai[3]+"""</td> 
                    </tr>
                    <tr>
                        <td>5</td> <td>"""+self.marka[4]+"""</td> <td>"""+self.model[4]+"""</td> <td>"""+self.numer_rejestracyjny[4]+"""</td> <td>"""+self.rok_produkkcji[4]+"""</td> <td>"""+self.data_nabycia[4]+"""</td> <td>"""+self.data_poniesienai[4]+"""</td> 
                    </tr>
                    <tr>
                        <td>6</td> <td>"""+self.marka[5]+"""</td> <td>"""+self.model[5]+"""</td> <td>"""+self.numer_rejestracyjny[5]+"""</td> <td>"""+self.rok_produkkcji[5]+"""</td> <td>"""+self.data_nabycia[5]+"""</td> <td>"""+self.data_poniesienai[5]+"""</td>  
                    </tr>
                    <tr>
                        <td>7</td> <td>"""+self.marka[6]+"""</td> <td>"""+self.model[6]+"""</td> <td>"""+self.numer_rejestracyjny[6]+"""</td> <td>"""+self.rok_produkkcji[6]+"""</td> <td>"""+self.data_nabycia[6]+"""</td> <td>"""+self.data_poniesienai[6]+"""</td> 
                    </tr>
                    <tr>
                        <td>8</td> <td>"""+self.marka[7]+"""</td> <td>"""+self.model[7]+"""</td> <td>"""+self.numer_rejestracyjny[7]+"""</td> <td>"""+self.rok_produkkcji[7]+"""</td> <td>"""+self.data_nabycia[7]+"""</td> <td>"""+self.data_poniesienai[7]+"""</td> 
                    </tr>
                    <tr>
                        <td>9</td> <td>"""+self.marka[8]+"""</td> <td>"""+self.model[8]+"""</td> <td>"""+self.numer_rejestracyjny[8]+"""</td> <td>"""+self.rok_produkkcji[8]+"""</td> <td>"""+self.data_nabycia[8]+"""</td> <td>"""+self.data_poniesienai[8]+"""</td> 
                    </tr>
                    </table>
                </p>
                <p align="center">
                    <h1>D. PODPIS PODATNIKA LUB OSOBY REPREZENTUJACEJ PODATNIKA</h1>
                    <table border="1" cellpadding="3">
                    <tr>
                        <td width="100"><b>10. Imie </b></td> <td width="100">"""+self.imie+"""</td> 
                    </tr>
                    <tr>
                        <td width="100"><b>11. Nazwisko</b></td> <td width="100">"""+self.nazwisko+"""</td> 
                    </tr>
                    <tr>
                        <td width="100"><b>13. Telefon kontaktowy</b></td> <td width="100">"""+self.telefon+"""</td> 
                    </tr>
                    <tr>
                        <td width="100"><b>14. Data wypelenienia</b></td> <td width="100">"""+self.data_wypelnienia+"""</td> 
                    </tr>
                    <tr>
                        <td width="200"><b>12. Popis podatnika lub osoby reprezentujacej podatnika</b></td> <td width="200">"""+self.podpis+"""</td>
                    </tr>
                    </table>
                </p>
                <p align="center">
                    <h1>E. ADNOTACJE URZEDU SKARBOWEGO</h1>
                    <table border="1" cellpadding="3">
                    <tr>
                        <td><b>15. Uwagi urzedu skarbowego </b></td> 
                    </tr>
                    <tr>
                        <td> """+self.uwagi+"""</td> 
                    </tr>
                </p>
                <p align="center" >
                    <table border="1" cellpadding="3">
                    <tr>
                        <td ><b>16. Identyfikator przyjmujacego formularz</b></td> <td ><b>17. Podpis przyjmujacego formularz</b></td> 
                    </tr>
                    <tr>
                        <td >"""+self.id_przyjmujacego+"""</td> <td> """+self.popis_przyjmujacego+"""</td> 
                    </tr>
                    </table>
                </p>
            </body> 
         </html>"""

