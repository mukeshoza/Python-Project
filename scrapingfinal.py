from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import pandas as pd


urls = [
    'http://americanflags.com/12x18usanfl.html',
'http://americanflags.com/18cowhalflwi.html',
'http://americanflags.com/28ftx1ingoal.html',
'http://americanflags.com/8x12puristfl.html',
'http://americanflags.com/8x12usanfl.html',
'http://amricanflags.com/alfldomo.html',
'http://americanflags.com/alflsimo.html',
'http://americanflags.com/alflwhmo.html',
'http://americanflags.com/amcobl3x5fl.html',
'http://americanflags.com/amflme8by10c.html',
'http://americanflags.com/ardivefl.html',
'http://americanflags.com/auunliisgoli.html',
'http://americanflags.com/baorvefl.html',
'http://americanflags.com/baraamfl.html',
'http://americanflags.com/baunliisgoli.html',
'http://americanflags.com/baunvefl.html',
'http://americanflags.com/beastcarflag.html',
'http://americanflags.com/bingoflag.html',
'http://americanflags.com/bocovefl.html',
'http://americanflags.com/borefl.html',
'http://americanflags.com/brgustflor.html',
'http://americanflags.com/brkeststfl.html',
'http://americanflags.com/capaamfl.html',
'http://americanflags.com/chbeamfl.html',
'http://americanflags.com/chelspcupcar.html',
'http://www.americanflags.com/cibeamfl.html',
'http://americanflags.com/cirevefl.html',
'http://americanflags.com/clearanceflag.html',
'http://americanflags.com/coflpin.html',
'http://americanflags.com/condosflag.html',
'http://americanflags.com/corovefl.html',
'http://americanflags.com/daeajrstands.html',
'http://americanflags.com/daealefl.html',
'http://americanflags.com/deliamfl.html',
'http://americanflags.com/delivefl.html',
'http://americanflags.com/deteamunfl.html',
'http://americanflags.com/dorecarfl.html',
'http://americanflags.com/dotronmerefl.html',
'http://americanflags.com/duunvebafl.html',
'http://americanflags.com/ecinmoset.html',
'http://americanflags.com/ecumo.html',
'http://americanflags.com/forretefl.html',
'http://americanflags.com/furnitureflag.html',
'http://americanflags.com/goalbaflorwi.html',
'http://americanflags.com/hacovefl.html',
'http://americanflags.com/hoandsafl.html',
'http://americanflags.com/hoteamfl.html',
'http://americanflags.com/hotevefl.html',
'http://americanflags.com/incovefl.html',
'http://americanflags.com/jajaamfl.html',
'http://americanflags.com/kakaststfl.html',
'http://americanflags.com/laoffrhoofbr.html',
'http://americanflags.com/losanravefl.html',
'http://americanflags.com/midoamfl.html',
'http://americanflags.com/midovefl.html',
'http://americanflags.com/miflofcoset.html',
'http://americanflags.com/migrnyarlofl.html',
'http://americanflags.com/neworsaamfl.html',
'http://americanflags.com/newyojeamfl.html',
'http://americanflags.com/newyojevefl.html',
'http://americanflags.com/oaraamfl.html',
'http://americanflags.com/patedrfl.html',
'http://americanflags.com/pestunstands.html',
'http://americanflags.com/pheaamfl.html',
'http://americanflags.com/prtobeambeto.html',
'http://americanflags.com/robltedrfl.html',
'http://americanflags.com/roblwetedrfl.html',
'http://americanflags.com/rwbwetefl.html',
'http://americanflags.com/sandichamfl.html',
'http://americanflags.com/seseamfl.html',
'http://americanflags.com/sesevefl.html',
'http://americanflags.com/sopoulbrbato.html',
'http://www.americanflags.com/st-louis-rams-car-flags.html',
'http://www.americanflags.com/st-louis-rams-flags.html',
'http://americanflags.com/stloraamfl.html',
'http://www.americanflags.com/ststquli.html',
'http://americanflags.com/ststtedrfl.html',
'http://americanflags.com/syunststfl.html',
'http://americanflags.com/tabaybuamfl.html',
'http://americanflags.com/tedrflfl.html',
'http://americanflags.com/tedrflpoinmo.html',
'http://americanflags.com/tedrposumo.html',
'http://americanflags.com/tetiamfl.html',
'http://americanflags.com/ucogume4by6d.html',
'http://americanflags.com/ucogume7pico.html',
'http://americanflags.com/ucogumedebox.html',
'http://americanflags.com/ulbrbatopfll.html',
'http://americanflags.com/usctrveflba.html',
'http://americanflags.com/viamflmaco.html',
'http://americanflags.com/vitevefl.html',
'http://americanflags.com/wareamfl.html',
'http://americanflags.com/20tefl.html',
'http://americanflags.com/alhoflset.html',
'http://www.americanflags.com/as9100cflag.html',
'http://americanflags.com/emhenycofl.html',
'http://americanflags.com/huse25flwha.html',
'http://americanflags.com/huse30flwha.html',
'http://americanflags.com/huse35flwha.html',
'http://americanflags.com/huse40flwha.html',
'http://americanflags.com/huse50flwha.html',
'http://americanflags.com/is16fl.html',
'http://americanflags.com/is17fl.html',
'http://americanflags.com/iso1348503flag.html',
'http://americanflags.com/iso1400104flag.html',
'http://americanflags.com/iso1400115flag.html',
'http://americanflags.com/iso2200005flag.html',
'http://americanflags.com/iso2700113flag.html',
'http://americanflags.com/iso5000111flag.html',
'http://americanflags.com/iso900115flag.html',
'http://americanflags.com/iso90fl1.html',
'http://americanflags.com/iso90qumafl.html',
'http://americanflags.com/lipocofl.html',
'http://americanflags.com/nystsethuflp.html',
'http://americanflags.com/ohsas18001flag.html',
'http://americanflags.com/prnycofl.html',
'http://americanflags.com/regalflagset.html',
'http://americanflags.com/waamflcuset.html'

]

data = []

driver = webdriver.PhantomJS()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

for url in urls:
    for page in range(1, 8):
        driver.get(url + str(page))
        # wait for the page to load
        content = driver.find_element_by_class_name("eyBreadcrumbs").text

driver.close()

df = pd.DataFrame(data)
print(df)