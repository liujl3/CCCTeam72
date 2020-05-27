# coding:utf-8
import numpy
import pandas as pd
import couchdb
import json
from pprint import pprint
import sys
from geopy.geocoders import Nominatim
import requests
import datetime
import time

state_code = {'QLD': 'Queensland', 'NT': 'Northern Territory', 'WA': 'Western Australia', 'SA': 'South Australia',
              'NSW': 'New South Wales', 'VIC': 'Victoria', 'TAS': 'Tasmania', 'ACT': 'Australian Capital Territory'}
state_name = {'Queensland','Northern Territory','Western Australia','South Australia','New South Wales','Victoria',
              'Tasmania','Australian Capital Territory'}

def connect_database(database_name):
    couch = couchdb.Server('http://admin:123456@45.113.235.44:5984//')
    db = couch[database_name]

    return db

def create_view(db):
    if "_design/newDesign" not in db:
        viewData = {
             "new-view": {
                "map": "function (doc) {\n  var hashList = [\"covid\", \"COVID\", \"corona\", \"Corona\", \"nCoV\", "
                       "\"marchapelocorona\", \"caronavirususa\", \"caronavirusindia\", \"caronavirusoutbreak\", "
                       "\"caronavirus\", \"carona virus\", \"2019nCoV\", \"codvid_19\", \"codvid19\", "
                       "\"conronaviruspandemic\", \"coronga virus\", \"corongavirus\", \"Corvid19virus\", \"covd19\", "
                       "\"ForcaCoronaVirus\", \"infocoronavirus\", \"kamitidaktakutviruscorona\", "
                       "\"NeuerCoronavirus\", \"NeuerCoronavirus\", \"Nouveau coronavirus\", \"NouveauCoronavirus\", "
                       "\"novel coronavirus\", \"NovelCorona\", \"novelcoronavirus\", \"novelcoronavirus\", "
                       "\"NovelCoronavirus\", \"NuovoCoronavirus\", \"ohiocoronavirus\", \"SARSCoV2\", \"SARSCoV2\", "
                       "\"the coronas\", \"thecoronas\", \"trumpdemic\", \"Virus Corona\", \"viruscorona\", "
                       "\"bayarealockdown\", \"stayathomechallenge\", \"stayhomechallenge\", \"quarantinelife\", "
                       "\"dontbeaspreader\", \"stayhomechallenge\", \"howtokeeppeoplehome\", \"togetherathome\", "
                       "\"alcool em gel\", \"alcool gel\", \"alcoolemgel\", \"alcoolgel\", \"avoidcrowds\", "
                       "\"bares cerrados\", \"bares fechados\", \"bars closed\", \"canceleverything\", "
                       "\"CerradMadridYa\", \"clases anuladas\", \"CLOSENYCPUBLICSCHOOLS\", \"confinementtotal\", "
                       "\"CONVID19\", \"cuarentena\", \"cuarentena\", \"CuarentenaCoronavirus\", \"cuarentenaYA\", "
                       "\"dont touch ur face\", \"dont touch your face\", \"DontBeASpreader\", \"donttouchyourface\", "
                       "\"escolas fechadas\", \"escolas fechando\", \"escolas sem aula\", \"escolas sem aulas\", "
                       "\"euficoemcasa\", \"evitar el contagio\", \"ficaemcasa\", \"flatten the curve\", \"flattening "
                       "the curve\", \"flatteningthecurve\", \"flattenthecurve\", \"FrenaLaCurva\", "
                       "\"Hand sanitizer\", \"Handsanitizer\", \"HoldTheVirus\", \"lava tu manos\", \"lavatumanos\", "
                       "\"lave as maos\", \"laveasmaos\", \"lockdown\", \"lockdown\", \"pandemic\", \"pandemic\", "
                       "\"panicbuying\", \"panickbuing\", \"quarantaine\", \"quarantine\", \"quarantine\", "
                       "\"QuarantineAndChill\", \"quarantined\", \"quarentena\", \"quarentena\", \"quarentine\", "
                       "\"quarentined\", \"quarentined\", \"quarentinelife\", \"quedateencasa\", \"remotework\", "
                       "\"remoteworking\", \"restaurantes cerrados\", \"restaurantes fechados\", \"restaurants "
                       "closed\", \"selfisolating\", \"SiMeContagioYo\", \"social distancing\", \"socialdistance\", "
                       "\"socialdistancing\", \"socialdistancingnow\", \"socialdistnacing\", \"stayathome\", "
                       "\"stayathome\", \"stayhome\", \"stayhome\", \"stayhomechallenge\", \"stayhomesavelives\", "
                       "\"StayTheFHome\", \"StayTheFuckHome\", \"suspendanlasclases\", \"teletrabajo\", "
                       "\"teletrabajo\", \"ToiletPaperApocalypse\", \"toiletpaperpanic\", \"trabajadores a la "
                       "calle\", \"trabajar desde casa\", \"trabajardesdecasa\", \"trabalhando de casa\", \"trabalhar "
                       "de casa\", \"wash ur hands\", \"wash your hands\", \"washurhands\", \"washyourhands\", "
                       "\"WashYourHandsAgain\", \"wfh\", \"work from home\", \"workfromhome\", \"working from home\", "
                       "\"workingfromhome\", \"yomequedoencasa\", \"2019_ncov\", \"21dayslockdown\", "
                       "\"5baje5minute\", \"9minute9baje\", \"9minutesforindia\", \"AislamientoObligatorio\", "
                       "\"ampliarlacuarentenaes\", \"auxilioemergencial\", \"BersamaMelawanCorona\", "
                       "\"bloqueioderuas\", \"Bogotaencasa\", \"bolsonarogenocida\", \"BreakCorona\", "
                       "\"cadeostestes\", \"californialockdown\", \"californiaquarantine\", \"californiashutdown\", "
                       "\"calockdown\", \"capitaocorona\", \"CegahTangkalCorona\", \"chegadequarentena\", "
                       "\"clapforourcarers\", \"ClubQuarantine\", \"coronovirus\", \"coronvirus\", \"corronavirus\", "
                       "\"CuarentenaHastaJunioEs\", \"CuarentenaInformando\", \"cuarentenametadata\", "
                       "\"cubaporlasalud\", \"cubasalvavidas\", \"CubriendoElCoronavirus\", \"CurfewInIndia\", "
                       "\"CurfewInIndia\", \"CuronaVairus\", \"curonavirus\", \"depoisdaquarentenaeu\", "
                       "\"dirumahaja\", \"disciplinaparavolver\", \"disiplincegahcorona\", \"ecuadorencrisis\", "
                       "\"ecuadorenemergencia\", \"eunaquarentena\", \"FightCoronaWithJokowi\", \"fiqueemcasa\", "
                       "\"FlexibilizarElAislamientoEs\", \"frontline_warriors_intern\", \"frontlineheroes\", "
                       "\"frontlineworkers\", \"frontlineworkersappreciation\", \"GerakanSocialDistancing\", "
                       "\"homeschool\", \"homeschooling\", \"HomeTasking\", \"hydroxychloroquine\", "
                       "\"indiafightcorona\", \"indiaprotectdoctors\", \"indonesialawancorona\", "
                       "\"JagaDiriJagaJarak\", \"JanataCurfewMarch22\", \"JantaCurfewChallenge\", "
                       "\"KanikaCoronaRow\", \"KanikaKaCoronaCrime\", \"koronaindonesia\", \"koronavirusIndonesia\", "
                       "\"LawanCorona\", \"LawanCoronaBersama\", \"Lockdowhustle\", \"lockdown21\", \"LockdownEnd\", "
                       "\"LockdownNow\", \"lockdowntillmay3\", \"losangeleslockdown\", \"mascaras\", "
                       "\"mascarasalva\", \"mascarilla\", \"mascarillas\", \"mascarillassolidarias\", \"masks4all\", "
                       "\"maskuplagos\", \"micasaesmiplaza\", \"michiganshutdown\", \"ModiKiBaatMano   \", \"mp927\", "
                       "\"mpdafome\", \"mpdamorte\", \"mpdobolsonaro\", \"mumbailockdown\", \"n95\", "
                       "\"NeuerCoronavirusSchweiz\", \"NoAlAislamientoInteligente\", \"NotDying4WallStreet\", "
                       "\"notessential\", \"obrasilnaopodeparar\", \"OBrasilnaoVaiParar\", \"obrasilvaiparar\", "
                       "\"OneTeamFromHome\", \"onlineclasses\", \"ParemosElVirus\", \"PMCares\", \"PPE\", "
                       "\"ppeshortage\", \"pralernaquarentena\", \"PrioridadDineroOSalud\", "
                       "\"QuarantineMoneyMakingIdeas\", \"quaratinelife\", \"quarentenabrasil\", \"quarentenaLGBTQ\", "
                       "\"quarentenou\", \"quaretenabrasil\", \"QuaronaVirus\", \"ReceitasDaQuarentena\", "
                       "\"remdesivir\", \"SCNaoQuerMorrer\", \"selfemployedmattertoo\", \"SendUsBackHome\", "
                       "\"ShamblesStayAtHome\", \"sideeffectsofquarantinelife\", \"Social_Distancing\", "
                       "\"sosecuador\", \"spcontraocoronavirus\", \"stayathomeorder\", \"StayAtHomeReadABook\", "
                       "\"StayAtHomeSaveLives\", \"stayhomestaysafe\", \"suspendonlineclasses\", "
                       "\"taxarfortunassalvarvidas\", \"TaxarFortunasSalvarVidas\", \"TaxarFortunasSalvarVidas\", "
                       "\"testesmasivosja\", \"testesmassivosja\", \"ThaliBajao\", \"thankyouwarriors\", "
                       "\"UKCoronavirusBill\", \"uklockdown\", \"UNExigimosGarantiasLaborales\", "
                       "\"unidosvenceremos\", \"UNSuspendanClasesOParamos\", \"unsuspendanclasesya\", "
                       "\"UNSuspendanlasClasesOParamos\", \"usemascara\", \"vaipassar\", \"vegasshutdown\", "
                       "\"viviremosyvenceremos\", \"VivirEnCuarentenaEs\", \"WarAgainstVirus\", \"waragainstvirus\", "
                       "\"wearamask\", \"WhenCoronaVirusIsOver\", \"WorkingFromHomeLife\", \"workingfromhometips\", "
                       "\"aula online\", \"auxilio emergencial\", \"Bloody Diwali\", \"bloqueio de ruas\", "
                       "\"bloqueio de vias\", \"bloqueio em vias\", \"bloqueou as ruas\", \"coron virus\", "
                       "\"coronga vairus\", \"corono virus\", \"coronovirus\", \"corrona virus\", \"Curona Vairus\", "
                       "\"curona virus\", \"Diwali In April\", \"Ecoronavirusescuador\", \"en primera linea\", "
                       "\"essencial service\", \"essencial services\", \"essential service\", \"essential services\", "
                       "\"face shield\", \"face shields\", \"Frontline\", \"hand sanitisers\", \"health worker\", "
                       "\"health workers\", \"homeschooling\", \"hydroxychloroquine\", \"India for 21\", \"India Hum "
                       "Honge Kamyab\", \"linha de frente\", \"mascara\", \"mascarilla\", \"mascarillas\", "
                       "\"mascarillas desechables\", \"n95 mask\", \"no mask\", \"personal protective equipment\", "
                       "\"quarentenou\", \"Quarona Virus\", \"remdesivir\", \"servicio esencial\", \"servicios "
                       "esenciales\", \"servi?os essenciais\", \"Shankh\", \"trabajador sanitario\", \"Trabajadora "
                       "sanitaria\", \"trabajadores de la salud\", \"trabalhador essencial\", \"trabalhadores "
                       "essenciais\", \"LockdownLife\", \"LockdownExtended\", \"lockdowneffect\", \"mortonaocompra\", "
                       "\"isolamentoparcial\", \"isolamento parcial\", \"lockdownparcial\", \"mortonaovota\", "
                       "\"passaportes de imunidade\", \"imunidade de rebanho\", \"UnitedAgainstCoronavirus\", "
                       "\"testes em humanos\", \"human trials\", \"gripezinha\", \"the virus\"];\n  for(var j=0, "
                       "l=doc.raw.entities.hashtags.length; j<l; j++){\n    var found = false;\n    for(var i=0, "
                       "k=hashList.length; i<k; i++){\n      if(doc.raw.entities.hashtags[j].text.indexOf(hashList["
                       "i]) != -1){\n        emit({'id':doc.raw.id,'place':doc.raw.place}, {'id':doc.raw.id,"
                       "'place':doc.raw.place,'lang':doc.raw.lang});\n        found = true;\n        break;\n      "
                       "}\n    }\n    if(found){\n      break;\n    }\n  }\n  if(!found){\n    for(var i=0, "
                       "k=hashList.length; i<k; i++){\n      if(doc.raw.text.indexOf(hashList[i]) != -1){\n        "
                       "emit({'id':doc.raw.id,'place':doc.raw.place}, {'id':doc.raw.id,'place':doc.raw.place,"
                       "'lang':doc.raw.lang});\n        break;\n      }\n    }\n  }\n} "
                },
              "coording": {
                "map": "function (doc) {\n  var hashList = [\"covid\", \"COVID\", \"corona\", \"Corona\", \"nCoV\", "
                       "\"marchapelocorona\", \"caronavirususa\", \"caronavirusindia\", \"caronavirusoutbreak\", "
                       "\"caronavirus\", \"carona virus\", \"2019nCoV\", \"codvid_19\", \"codvid19\", "
                       "\"conronaviruspandemic\", \"coronga virus\", \"corongavirus\", \"Corvid19virus\", \"covd19\", "
                       "\"ForcaCoronaVirus\", \"infocoronavirus\", \"kamitidaktakutviruscorona\", "
                       "\"NeuerCoronavirus\", \"NeuerCoronavirus\", \"Nouveau coronavirus\", \"NouveauCoronavirus\", "
                       "\"novel coronavirus\", \"NovelCorona\", \"novelcoronavirus\", \"novelcoronavirus\", "
                       "\"NovelCoronavirus\", \"NuovoCoronavirus\", \"ohiocoronavirus\", \"SARSCoV2\", \"SARSCoV2\", "
                       "\"the coronas\", \"thecoronas\", \"trumpdemic\", \"Virus Corona\", \"viruscorona\", "
                       "\"bayarealockdown\", \"stayathomechallenge\", \"stayhomechallenge\", \"quarantinelife\", "
                       "\"dontbeaspreader\", \"stayhomechallenge\", \"howtokeeppeoplehome\", \"togetherathome\", "
                       "\"alcool em gel\", \"alcool gel\", \"alcoolemgel\", \"alcoolgel\", \"avoidcrowds\", "
                       "\"bares cerrados\", \"bares fechados\", \"bars closed\", \"canceleverything\", "
                       "\"CerradMadridYa\", \"clases anuladas\", \"CLOSENYCPUBLICSCHOOLS\", \"confinementtotal\", "
                       "\"CONVID19\", \"cuarentena\", \"cuarentena\", \"CuarentenaCoronavirus\", \"cuarentenaYA\", "
                       "\"dont touch ur face\", \"dont touch your face\", \"DontBeASpreader\", \"donttouchyourface\", "
                       "\"escolas fechadas\", \"escolas fechando\", \"escolas sem aula\", \"escolas sem aulas\", "
                       "\"euficoemcasa\", \"evitar el contagio\", \"ficaemcasa\", \"flatten the curve\", \"flattening "
                       "the curve\", \"flatteningthecurve\", \"flattenthecurve\", \"FrenaLaCurva\", "
                       "\"Hand sanitizer\", \"Handsanitizer\", \"HoldTheVirus\", \"lava tu manos\", \"lavatumanos\", "
                       "\"lave as maos\", \"laveasmaos\", \"lockdown\", \"lockdown\", \"pandemic\", \"pandemic\", "
                       "\"panicbuying\", \"panickbuing\", \"quarantaine\", \"quarantine\", \"quarantine\", "
                       "\"QuarantineAndChill\", \"quarantined\", \"quarentena\", \"quarentena\", \"quarentine\", "
                       "\"quarentined\", \"quarentined\", \"quarentinelife\", \"quedateencasa\", \"remotework\", "
                       "\"remoteworking\", \"restaurantes cerrados\", \"restaurantes fechados\", \"restaurants "
                       "closed\", \"selfisolating\", \"SiMeContagioYo\", \"social distancing\", \"socialdistance\", "
                       "\"socialdistancing\", \"socialdistancingnow\", \"socialdistnacing\", \"stayathome\", "
                       "\"stayathome\", \"stayhome\", \"stayhome\", \"stayhomechallenge\", \"stayhomesavelives\", "
                       "\"StayTheFHome\", \"StayTheFuckHome\", \"suspendanlasclases\", \"teletrabajo\", "
                       "\"teletrabajo\", \"ToiletPaperApocalypse\", \"toiletpaperpanic\", \"trabajadores a la "
                       "calle\", \"trabajar desde casa\", \"trabajardesdecasa\", \"trabalhando de casa\", \"trabalhar "
                       "de casa\", \"wash ur hands\", \"wash your hands\", \"washurhands\", \"washyourhands\", "
                       "\"WashYourHandsAgain\", \"wfh\", \"work from home\", \"workfromhome\", \"working from home\", "
                       "\"workingfromhome\", \"yomequedoencasa\", \"2019_ncov\", \"21dayslockdown\", "
                       "\"5baje5minute\", \"9minute9baje\", \"9minutesforindia\", \"AislamientoObligatorio\", "
                       "\"ampliarlacuarentenaes\", \"auxilioemergencial\", \"BersamaMelawanCorona\", "
                       "\"bloqueioderuas\", \"Bogotaencasa\", \"bolsonarogenocida\", \"BreakCorona\", "
                       "\"cadeostestes\", \"californialockdown\", \"californiaquarantine\", \"californiashutdown\", "
                       "\"calockdown\", \"capitaocorona\", \"CegahTangkalCorona\", \"chegadequarentena\", "
                       "\"clapforourcarers\", \"ClubQuarantine\", \"coronovirus\", \"coronvirus\", \"corronavirus\", "
                       "\"CuarentenaHastaJunioEs\", \"CuarentenaInformando\", \"cuarentenametadata\", "
                       "\"cubaporlasalud\", \"cubasalvavidas\", \"CubriendoElCoronavirus\", \"CurfewInIndia\", "
                       "\"CurfewInIndia\", \"CuronaVairus\", \"curonavirus\", \"depoisdaquarentenaeu\", "
                       "\"dirumahaja\", \"disciplinaparavolver\", \"disiplincegahcorona\", \"ecuadorencrisis\", "
                       "\"ecuadorenemergencia\", \"eunaquarentena\", \"FightCoronaWithJokowi\", \"fiqueemcasa\", "
                       "\"FlexibilizarElAislamientoEs\", \"frontline_warriors_intern\", \"frontlineheroes\", "
                       "\"frontlineworkers\", \"frontlineworkersappreciation\", \"GerakanSocialDistancing\", "
                       "\"homeschool\", \"homeschooling\", \"HomeTasking\", \"hydroxychloroquine\", "
                       "\"indiafightcorona\", \"indiaprotectdoctors\", \"indonesialawancorona\", "
                       "\"JagaDiriJagaJarak\", \"JanataCurfewMarch22\", \"JantaCurfewChallenge\", "
                       "\"KanikaCoronaRow\", \"KanikaKaCoronaCrime\", \"koronaindonesia\", \"koronavirusIndonesia\", "
                       "\"LawanCorona\", \"LawanCoronaBersama\", \"Lockdowhustle\", \"lockdown21\", \"LockdownEnd\", "
                       "\"LockdownNow\", \"lockdowntillmay3\", \"losangeleslockdown\", \"mascaras\", "
                       "\"mascarasalva\", \"mascarilla\", \"mascarillas\", \"mascarillassolidarias\", \"masks4all\", "
                       "\"maskuplagos\", \"micasaesmiplaza\", \"michiganshutdown\", \"ModiKiBaatMano   \", \"mp927\", "
                       "\"mpdafome\", \"mpdamorte\", \"mpdobolsonaro\", \"mumbailockdown\", \"n95\", "
                       "\"NeuerCoronavirusSchweiz\", \"NoAlAislamientoInteligente\", \"NotDying4WallStreet\", "
                       "\"notessential\", \"obrasilnaopodeparar\", \"OBrasilnaoVaiParar\", \"obrasilvaiparar\", "
                       "\"OneTeamFromHome\", \"onlineclasses\", \"ParemosElVirus\", \"PMCares\", \"PPE\", "
                       "\"ppeshortage\", \"pralernaquarentena\", \"PrioridadDineroOSalud\", "
                       "\"QuarantineMoneyMakingIdeas\", \"quaratinelife\", \"quarentenabrasil\", \"quarentenaLGBTQ\", "
                       "\"quarentenou\", \"quaretenabrasil\", \"QuaronaVirus\", \"ReceitasDaQuarentena\", "
                       "\"remdesivir\", \"SCNaoQuerMorrer\", \"selfemployedmattertoo\", \"SendUsBackHome\", "
                       "\"ShamblesStayAtHome\", \"sideeffectsofquarantinelife\", \"Social_Distancing\", "
                       "\"sosecuador\", \"spcontraocoronavirus\", \"stayathomeorder\", \"StayAtHomeReadABook\", "
                       "\"StayAtHomeSaveLives\", \"stayhomestaysafe\", \"suspendonlineclasses\", "
                       "\"taxarfortunassalvarvidas\", \"TaxarFortunasSalvarVidas\", \"TaxarFortunasSalvarVidas\", "
                       "\"testesmasivosja\", \"testesmassivosja\", \"ThaliBajao\", \"thankyouwarriors\", "
                       "\"UKCoronavirusBill\", \"uklockdown\", \"UNExigimosGarantiasLaborales\", "
                       "\"unidosvenceremos\", \"UNSuspendanClasesOParamos\", \"unsuspendanclasesya\", "
                       "\"UNSuspendanlasClasesOParamos\", \"usemascara\", \"vaipassar\", \"vegasshutdown\", "
                       "\"viviremosyvenceremos\", \"VivirEnCuarentenaEs\", \"WarAgainstVirus\", \"waragainstvirus\", "
                       "\"wearamask\", \"WhenCoronaVirusIsOver\", \"WorkingFromHomeLife\", \"workingfromhometips\", "
                       "\"aula online\", \"auxilio emergencial\", \"Bloody Diwali\", \"bloqueio de ruas\", "
                       "\"bloqueio de vias\", \"bloqueio em vias\", \"bloqueou as ruas\", \"coron virus\", "
                       "\"coronga vairus\", \"corono virus\", \"coronovirus\", \"corrona virus\", \"Curona Vairus\", "
                       "\"curona virus\", \"Diwali In April\", \"Ecoronavirusescuador\", \"en primera linea\", "
                       "\"essencial service\", \"essencial services\", \"essential service\", \"essential services\", "
                       "\"face shield\", \"face shields\", \"Frontline\", \"hand sanitisers\", \"health worker\", "
                       "\"health workers\", \"homeschooling\", \"hydroxychloroquine\", \"India for 21\", \"India Hum "
                       "Honge Kamyab\", \"linha de frente\", \"mascara\", \"mascarilla\", \"mascarillas\", "
                       "\"mascarillas desechables\", \"n95 mask\", \"no mask\", \"personal protective equipment\", "
                       "\"quarentenou\", \"Quarona Virus\", \"remdesivir\", \"servicio esencial\", \"servicios "
                       "esenciales\", \"servi?os essenciais\", \"Shankh\", \"trabajador sanitario\", \"Trabajadora "
                       "sanitaria\", \"trabajadores de la salud\", \"trabalhador essencial\", \"trabalhadores "
                       "essenciais\", \"LockdownLife\", \"LockdownExtended\", \"lockdowneffect\", \"mortonaocompra\", "
                       "\"isolamentoparcial\", \"isolamento parcial\", \"lockdownparcial\", \"mortonaovota\", "
                       "\"passaportes de imunidade\", \"imunidade de rebanho\", \"UnitedAgainstCoronavirus\", "
                       "\"testes em humanos\", \"human trials\", \"gripezinha\", \"the virus\"];\n  for(var j=0, "
                       "l=doc.raw.entities.hashtags.length; j<l; j++){\n    var found = false;\n    for(var i=0, "
                       "k=hashList.length; i<k; i++){\n      if(doc.raw.entities.hashtags[j].text.indexOf(hashList["
                       "i]) != -1){\n        var latitude = 0;\n        var longitude = 0;\n        for(var u=0; u<4; "
                       "u++){\n          longitude += doc.raw.place.bounding_box.coordinates[0][u][0];\n          "
                       "latitude += doc.raw.place.bounding_box.coordinates[0][u][1];\n        }\n        longitude = "
                       "longitude/4;\n        latitude = latitude/4;\n        var state;\n        var city;\n        "
                       "if(doc.raw.place.full_name.split(\",\").length<=1){\n          state = \" \" + "
                       "doc.raw.place.full_name.split(\",\")[0];\n          city = \"Unknown\";\n        }\n        "
                       "else if(doc.raw.place.full_name.split(\",\")[1] != ' Australia'){\n           state = "
                       "doc.raw.place.full_name.split(\",\")[1];\n           city = doc.raw.place.full_name.split(\","
                       "\")[0];\n        }\n        else{\n          state = \" \" + doc.raw.place.full_name.split("
                       "\",\")[0];\n          city = \"Unknown\";\n        }\n        emit({'id':doc.raw.id,"
                       "'place':doc.raw.place}, {'id':doc.raw.id,'coordinates':[longitude,latitude],'city':city,"
                       "'state':state,'time':doc.raw.created_at});\n        found = true;\n        break;\n      }\n  "
                       "  }\n    if(found){\n      break;\n    }\n  }\n  if(!found){\n    for(var i=0, "
                       "k=hashList.length; i<k; i++){\n      if(doc.raw.text.indexOf(hashList[i]) != -1){\n        "
                       "var latitude = 0;\n        var longitude = 0;\n        for(var u=0; u<4; u++){\n          "
                       "longitude += doc.raw.place.bounding_box.coordinates[0][u][0];\n          latitude += "
                       "doc.raw.place.bounding_box.coordinates[0][u][1];\n        }\n        longitude = "
                       "longitude/4;\n        latitude = latitude/4;\n        if(doc.raw.place.full_name.split(\","
                       "\").length<=1){\n          state = doc.raw.place.full_name.split(\",\")[0];\n          city = "
                       "\"Unknown\";\n        }\n        else if(doc.raw.place.full_name.split(\",\")[1] != ' "
                       "Australia'){\n           state = doc.raw.place.full_name.split(\",\")[1];\n           city = "
                       "doc.raw.place.full_name.split(\",\")[0];\n        }\n        else{\n          state = \" \" + "
                       "doc.raw.place.full_name.split(\",\")[0];\n          city = \"Unknown\";\n        }\n        "
                       "emit({'id':doc.raw.id,'place':doc.raw.place}, {'id':doc.raw.id,'coordinates':[longitude,"
                       "latitude],'city':city,'state':state,'time':doc.raw.created_at});\n        break;\n      }\n   "
                       " }\n  }\n}\n "
                }
        }
        db['_design/newDesign'] = dict(language='javascript', views=viewData)

def gather(db):
    create_view(db)
    full_name = []
    coordinates = []
    ids = []
    lang = []
    geo = Nominatim()
    count = 0
    for item in db.view("_design/newDesign/_view/new-view"):
        tweet_id = item.value['id']
        if tweet_id not in ids:
            count += 1
            ids.append(tweet_id)
            longitude = 0
            latitude = 0
            for i in range(0,3):
                longitude += item.value['place']['bounding_box']['coordinates'][0][i][0]
                latitude += item.value['place']['bounding_box']['coordinates'][0][i][1]
            coordinates.append([longitude/4,latitude/4])
            if item.value['place']['full_name'].split(",")[0] not in state_name and item.value['place']['full_name']!= 'Australia':
                full_name.append(item.value['place']['full_name'])
            else:
                full_name.append('Unknown, '+item.value['place']['full_name'].split(",")[0])
            lang.append(item.value['lang'])

    data = {'full_name': full_name, 'coordinates': coordinates}
    df = pd.DataFrame(data=data)
    city = pd.DataFrame({'content':full_name})['content'].str.split(',', expand=True)
    data_lang = {'city': city[0].values.tolist(), 'state': city[1].values.tolist(), 'coordinates': coordinates, 'lang': lang,'count':ids}
    dlf = pd.DataFrame(data=data_lang)
    city_lang = dlf.groupby(['city','state','lang']).count()
    clf = pd.DataFrame(city_lang)["count"].reset_index(name="Count")
    print(df)
    print(count)
    save_result(clf, "city_lang_results")
#city lang state count
    return df


def tweets_count(df):
    city_NumTweet = df.groupby(['full_name']).count()
    city_df = pd.DataFrame(city_NumTweet)["coordinates"].reset_index(name="Tweets_Num")
    full_name = city_df['full_name']
    city = full_name.str.split(',', expand=True)
    city_state = pd.DataFrame({'full_name': full_name, 'city': city[0].values.tolist(), 'state': city[1].values.tolist()})
    city_df = pd.merge(city_df, city_state, on='full_name')
    return city_df
# full_name city state Tweets_Num Hospital_Num

def tweets_deal(db):
    full_name = []
    coordinates = []
    ids = []
    city = []
    state = []
    time_date = []
    time_second = []
    count = 0
    for item in db.view("_design/newDesign/_view/coording"):
        tweet_id = item.value['id']
        if tweet_id not in ids:
            count += 1
            ids.append(tweet_id)
            coordinates.append(item.value['coordinates'])
            city.append(item.value['city'])
            state.append(item.value['state'])
            this_date = datetime.datetime.strptime(item.value['time'], "%a %b %d %H:%M:%S %z %Y")
            print(this_date.date())
            time_date.append(str(this_date.date()))
            time_second.append(str(time.mktime(this_date.timetuple())))

    id_str = []
    for i in range(len(ids)):
        id_str.append(str(int(ids[i])))

    df_coor = pd.DataFrame({'id': id_str, 'coordinate': coordinates})
    save_result(df_coor, 'tweet_coord')
    df_day_state = pd.DataFrame({'state': state, 'day': time_date, 'second': time_second, 'city': city})
    print(df_day_state)
    day_state = df_day_state.groupby(['state', 'day','second']).count()
    print(day_state)
    df_day_state = pd.DataFrame(day_state)["city"].reset_index(name="Tweets_Num")
    print(df_day_state)
    save_result(df_day_state, 'day_state_tweets')

def data_combine(tweet_df, aurin_df):
    geolocator = Nominatim()
    latitude = aurin_df[' latitude'].values.tolist()
    longitude = aurin_df[' longitude'].values.tolist()
    state = aurin_df[' state'].values.tolist()
    for i in range(len(state)):
        state[i] = state_code[state[i]]

    coordinates = []
    city_list = tweet_df['city'].values.tolist()
    city_aurin = []
    for i in range(len(latitude)):
        hasCity = False
        city_name = geolocator.reverse(str(latitude[i]) + "," + str(longitude[i]))
        coordinates.append([longitude[i], latitude[i]])
        for j in range(len(city_list)):
            if city_list[j] != 'Australia'and city_list[j] not in state_name and city_list[j] in city_name.address:
                city_aurin.append(city_list[j])
                hasCity = True
                break

        if not hasCity:
            city_aurin.append('Unknown')

    full_name = []
    for i in range(len(city_aurin)):
        full_name.append(city_aurin[i]+', '+state[i])

    hops_data = pd.DataFrame({'coordinates': coordinates})
    save_result(hops_data, 'hosp_coord')
    citys_hospital = pd.DataFrame({'full_name': full_name,'city': city_aurin, 'state': state, 'coordinate': coordinates})
    hospital_num = citys_hospital.groupby(['full_name']).count()
    new_aurin_df = pd.DataFrame(hospital_num)['coordinate'].reset_index(name="Hospital_Num")
    final_df = pd.merge(tweet_df, new_aurin_df, on='full_name')

    return final_df


def save_result(final_df, database_name):
    couch = couchdb.Server('http://admin:123456@45.113.235.44:5984//')

    if database_name in couch:
        del couch[database_name]
        couch = couch.create(database_name)
    else:
        couch = couch.create(database_name)

    final_json = final_df.to_json(orient="columns", force_ascii=False)
    with open(database_name+".txt", "w") as f:
        f.write(final_json)
    couch.save(json.loads(final_json))


def main():
    resource_database = 'tweet'
    result_database = 'result'
    db = connect_database(resource_database)
    tweet_df = gather(db)
    tweets_deal(db)
    count_df = tweets_count(tweet_df)
    aurin_file = pd.read_csv('Hospital.csv')
    aurin_df = pd.DataFrame(aurin_file)
    final_df = data_combine(count_df, aurin_df)
    save_result(final_df, result_database)

main()