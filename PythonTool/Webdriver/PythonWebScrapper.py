# Author:
#   Juan Luis Flores Garza
# Date: 7/21/2017
#
# CENACE WebScrapper

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Global Variables
    # Helper download counter (must reach 12 downloads at the end)
downloadcount = 0
    # Define firefox as the wedriver
browser = webdriver.Firefox()

################################### loadsite ###################################
# Function that loads the site
def loadsite() :
    global browser
    # Check if the table is correctly loaded
    try:
        # Check if contents are propertly loaded if not, website if refreshed
        element_present = EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_treePrincipal'))
        WebDriverWait(browser, 15).until(element_present)
        print ("Page is ready!")
        checkboxes()
        return
    # Timeout for loading website
    except TimeoutException:
        print ("Error Code 1: Error Cargando página")
    # Table not loaded
    except ElementNotVisibleException as nv:
        print("Error Code 2: Error cargado la tabla")
    # Table partialy loaded
    except ElementNotInteractableException as ni:
        print("Error Code 3: Error cargado la tabla")
    browser.refresh()
    loadsite()
    return

################################## checkboxes ##################################
# Index of each checkbox (select the daily checkboxes)
def checkboxes():
    time.sleep(5);
    #PML/MDA/D
    searchcheckbox('4')
    #PML/MTR/D
    searchcheckbox('3')
    #PND/MDA/D
    searchcheckbox('5')
    #PND/MTR/D
    searchcheckbox('5')
    return

################################ searchcheckbox ################################
# Click on checkboxes
def searchcheckbox(mychar):
    global browser
    # Click checkbox
    try:
        browser.find_element_by_xpath("(//SPAN[@class='rtUnchecked'])[" + mychar + "]").click()
        return
    # Element not found
    except NoSuchElementException as e:
        print("Error finding the element")
        #Reload website and redownload files
        browser.refresh()
        loadsite()
        return

################################ downloadfiles #################################
# Download files according to Xpath in table
def downloadfiles(Xpath):
    global browser
    time.sleep(10);
    # Click csv img
    try:
        browser.find_element_by_xpath(Xpath).click()
        global downloadcount
        downloadcount = downloadcount + 1
        return
    # Element not found
    except NoSuchElementException as e:
        print("Error enxontró csv")
    return

#################################### start #####################################
# Start execution
def start():
    global browser
    ### Precios Marginales Locales
    # MDA SISTEMA INTERCONECTADO NACIONAL
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Downloader-CENACE\PythonTool\CSVdir\PML\MDA")
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values'))
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
    loadsite()
    downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl0_ListViewArchivosSIN_ctrl0_linkCSV\"]")
    time.sleep(60)
    print("PML MDA SISTEMA INTERCONECTADO NACIONAL DONE")
    browser.quit()

    # MDA SISTEMA INTERCONECTADO BAJA CALIFORNIA
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Downloader-CENACE\PythonTool\CSVdir\PML\MDA")
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values'))
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
    loadsite()
    downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl0_ListViewArchivosBCN_ctrl0_A1\"]")
    time.sleep(60)
    print("PML MDA SISTEMA INTERCONECTADO BAJA CALIFORNIA DONE")
    browser.quit()

    # MDA SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Downloader-CENACE\PythonTool\CSVdir\PML\MDA")
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values'))
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
    loadsite()
    downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl0_ListViewArchivosBCS_ctrl0_A4\"]")
    time.sleep(60)
    print("PML MDA SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR DONE")
    browser.quit()

    # MTR SISTEMA INTERCONECTADO NACIONAL
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Downloader-CENACE\PythonTool\CSVdir\PML\MTR")
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values'))
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
    loadsite()
    downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl1_ListViewArchivosSIN_ctrl0_linkCSV\"]")
    time.sleep(60)
    print("PML MTR SISTEMA INTERCONECTADO NACIONAL DONE")
    browser.quit()

    # MTR SISTEMA INTERCONECTADO BAJA CALIFORNIA
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Downloader-CENACE\PythonTool\CSVdir\PML\MTR")
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values'))
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
    loadsite()
    downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl1_ListViewArchivosBCN_ctrl0_A1\"]")
    time.sleep(60)
    print("PML MTR SISTEMA INTERCONECTADO BAJA CALIFORNIA DONE")
    browser.quit()

    # MTR SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Downloader-CENACE\PythonTool\CSVdir\PML\MTR")
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values'))
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
    loadsite()
    downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl1_ListViewArchivosBCS_ctrl0_A4\"]")
    time.sleep(60)
    print("PML MTR SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR DONE")
    browser.quit()

    ### Precios de Nodos Distribuidos
    # MDA SISTEMA INTERCONECTADO NACIONAL
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Downloader-CENACE\PythonTool\CSVdir\PND\MDA")
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values'))
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
    loadsite()
    downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl2_ListViewArchivosSIN_ctrl0_linkCSV\"]")
    time.sleep(60)
    print("PND MDA SISTEMA INTERCONECTADO NACIONAL DONE")
    browser.quit()

    # MDA SISTEMA INTERCONECTADO BAJA CALIFORNIA
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Downloader-CENACE\PythonTool\CSVdir\PND\MDA")
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values'))
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
    loadsite()
    downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl2_ListViewArchivosBCN_ctrl0_A1\"]")
    time.sleep(60)
    print("PND MDA SISTEMA INTERCONECTADO BAJA CALIFORNIA DONE")
    browser.quit()

    # MDA SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Downloader-CENACE\PythonTool\CSVdir\PND\MDA")
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values'))
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
    loadsite()
    downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl2_ListViewArchivosBCS_ctrl0_A4\"]")
    time.sleep(60)
    print("PND MDA SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR DONE")
    browser.quit()

    # MTR SISTEMA INTERCONECTADO NACIONAL
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Downloader-CENACE\PythonTool\CSVdir\PND\MTR")
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values'))
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
    loadsite()
    downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl3_ListViewArchivosSIN_ctrl0_linkCSV\"]")
    time.sleep(60)
    print("PND MTR SISTEMA INTERCONECTADO NACIONAL DONE")
    browser.quit()

    # MTR SISTEMA INTERCONECTADO BAJA CALIFORNIA
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Downloader-CENACE\PythonTool\CSVdir\PND\MTR")
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values'))
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
    loadsite()
    downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl3_ListViewArchivosBCN_ctrl0_A1\"]")
    time.sleep(60)
    print("PND MTR SISTEMA INTERCONECTADO BAJA CALIFORNIA DONE")
    browser.quit()

    # MTR SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Downloader-CENACE\PythonTool\CSVdir\PND\MTR")
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values'))
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
    loadsite()
    downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl3_ListViewArchivosBCS_ctrl0_A4\"]")
    time.sleep(60)
    print("PND MTR SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR DONE")
    browser.quit()

    return

################################# Main Program #################################
# Main program
start()
print(downloadcount)
# check 12 valid downloads
if (downloadcount < 12):
    print("Ejecutión Incorrecta... reiniciando programa")
    downloadcount = 0
    # if execution error, restart the program
    start()
else:
    print("Ejecutión Correcta")
