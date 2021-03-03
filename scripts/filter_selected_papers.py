import os
from shutil import copyfile

selected_papers = [
    'journals/software/AldrichGKGMRSST19',
    'conf/ssrr/CichonSR16',
    'conf/icse/MalavoltaLSLG20',
    'conf/icse/JamshidiCSKG19',
    'conf/icse/HalderPMS17',
    'journals/jss/EstefoSRF19',
    'conf/icse/BardaroSM18',
    'conf/iceccs/LiWJGLS17',
    'conf/ssrr/CichonR17',
    'conf/sigsoft/00020BBP20',
    'journals/tr/HuDYSZ20',
    'journals/jss/DelgadoYC19',
    'conf/ssrr/SantosPR13',
    'conf/ssrr/NooriPRC17',
    'conf/ssrr/WatanabeEYN16',
    'conf/oopsla/MorleyWRWBS13',
    'conf/reconfig/PodlubneG19',
    'conf/sigsoft/0001CM18',
    'conf/models/GarciaDLSKB19',
    'conf/models/ChengCFLM20',
    'conf/icse/Fischer-Nielsen20',
    'conf/icse/WitteT18',
    'conf/icsm/KolakAGHT20',
    'conf/reconfig/StrohmerBSL19',
    'conf/iscas/VancinDPJCA20',
    'conf/iscas/IshidaMT18a',
    'conf/models/BaccouriGB18',
    'conf/saso/Hrabia16',
    'conf/kbse/WitteT19',
    'conf/icse/OreDE18',
    'conf/icse/ErnstKB18',
    'conf/ssrr/WiemannIPPSHVH19',
    'conf/icse/OhkawaSWOOY19',
    'conf/ssrr/IslamANIS20',
    'conf/ssrr/FerreiraCAR13',
    'conf/iscas/AldegheriBDFGP18',
    'conf/icfpt/NittaTYT19',
    'conf/icfpt/HasegawaTNIKT19',
    'conf/iscas/GongXLZMYL19',
    'conf/fmec/QueraltaLZW20',
]

DOWNLOAD_DIRECTORY = 'downloaded_papers'
FILTER_DIRECTORY = 'selected_papers'

for current_paper in selected_papers:
    file_title = current_paper.replace('/', '@')

    if not os.path.exists(f'{DOWNLOAD_DIRECTORY}/{file_title}.pdf'):
        print(f'Paper {current_paper} was not in the download folder.')
        continue

    (venue, name) = current_paper.split('/')[1:]
    authors = name[:-2]
    year = f'20{name[-2:]}'
    copyfile(f'{DOWNLOAD_DIRECTORY}/{file_title}.pdf',
             f'{FILTER_DIRECTORY}/{venue.upper()}_{authors.upper()}_{year}.pdf')
