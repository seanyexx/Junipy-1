
############################# print control #############################
DEBUG_MODE = False   # True: print as much information False: default
SILENT_MODE = False  # True: print as less information False: default



########################## local configuration ##########################
# files inside tmp folder will be ignored by Git
ZIP_PATH = './tmp/' # zip file will be download here
CSV_PATH = './tmp/' # csv file will be unzip here
GIF_PATH = './tmp/' # gif file will be download here

# cache folder
FLAG_CACHE = './static/'   # used to store retrieved flag image
# LOCATOR_CACHE = './static/'   # used to store retrieved locator image

# default value
NON_FLAG = './static/default_flag.gif'     
# NON_LOCATOR = './static/default_flag.gif'  
NON_INTRO = ''      # default country introduction



########################### mlab configuration ##########################
# database for debug
# DB_URL = "mongodb://junipy:comp9321@ds217350.mlab.com:17350/junipy_debug"
# database for deploy
DB_URL = "mongodb://junipy:comp9321@ds143907.mlab.com:43907/junipy_deploy"

# database collections, used in query(col=database collection)
OVERVIEW = 1    # latest GDP
INDICATOR = 2
FLAG = 3
# LOCATOR = 4
INTRODUCTION = 5    # country introduction



############################ data source domain #########################
# the years to be processed
global_years = [str(year) for year in range(1990, 2016 + 1)]

# the indicators to be processed
global_indicators = {"GDP_total": "NY.GDP.MKTP.CD",
                    "GDP_agriculture": "NV.AGR.TOTL.ZS",
                    "GDP_industry": "NV.IND.TOTL.ZS",
                    "GDP_service": "NV.SRV.TETC.ZS",
                    "CO2_emission": "EN.ATM.CO2E.KT",
                    "PM25_index": "EN.ATM.PM25.MC.M3",
                    "freshwater_withdrawals": "ER.H2O.FWTL.K3",
                    "Population": "SP.POP.TOTL"
                    }

# the country code to be processed
global_codes = {
    "AFG": {
        "name": "Afghanistan",
        "short": "AF"
    },
    "ALB": {
        "name": "Albania",
        "short": "AL"
    },
    "DZA": {
        "name": "Algeria",
        "short": "AG"
    },
    "ASM": {
        "name": "American Samoa",
        "short": "AQ"
    },
    "AND": {
        "name": "Andorra",
        "short": "AN"
    },
    "AGO": {
        "name": "Angola",
        "short": "AO"
    },
    "AIA": {
        "name": "Anguilla",
        "short": "AV"
    },
    "ATA": {
        "name": "Antarctica",
        "short": "AY"
    },
    "ATG": {
        "name": "Antigua and Barbuda",
        "short": "AC"
    },
    "ARG": {
        "name": "Argentina",
        "short": "AR"
    },
    "ARM": {
        "name": "Armenia",
        "short": "AM"
    },
    "ABW": {
        "name": "Aruba",
        "short": "AA"
    },
    "AUS": {
        "name": "Australia",
        "short": "AS"
    },
    "AUT": {
        "name": "Austria",
        "short": "AU"
    },
    "AZE": {
        "name": "Azerbaijan",
        "short": "AJ"
    },
    "BHS": {
        "name": "Bahamas",
        "short": "BF"
    },
    "BHR": {
        "name": "Bahrain",
        "short": "BA"
    },
    "BGD": {
        "name": "Bangladesh",
        "short": "BG"
    },
    "BRB": {
        "name": "Barbados",
        "short": "BB"
    },
    "BLR": {
        "name": "Belarus",
        "short": "BO"
    },
    "BEL": {
        "name": "Belgium",
        "short": "BE"
    },
    "BLZ": {
        "name": "Belize",
        "short": "BH"
    },
    "BEN": {
        "name": "Benin",
        "short": "BN"
    },
    "BMU": {
        "name": "Bermuda",
        "short": "BD"
    },
    "BTN": {
        "name": "Bhutan",
        "short": "BT"
    },
    "BOL": {
        "name": "Bolivia (Plurinational State of)",
        "short": "BL"
    },
    "BES": {
        "name": "Bonaire, Sint Eustatius and Saba",
        "short": "NL"
    },
    "BIH": {
        "name": "Bosnia and Herzegovina",
        "short": "BK"
    },
    "BWA": {
        "name": "Botswana",
        "short": "BC"
    },
    "BVT": {
        "name": "Bouvet Island",
        "short": "BV"
    },
    "BRA": {
        "name": "Brazil",
        "short": "BR"
    },
    "IOT": {
        "name": "British Indian Ocean Territory",
        "short": "IO"
    },
    "VGB": {
        "name": "British Virgin Islands",
        "short": "VI"
    },
    "BRN": {
        "name": "Brunei Darussalam",
        "short": "BX"
    },
    "BGR": {
        "name": "Bulgaria",
        "short": "BU"
    },
    "BFA": {
        "name": "Burkina Faso",
        "short": "UV"
    },
    "BDI": {
        "name": "Burundi",
        "short": "BY"
    },
    "CPV": {
        "name": "Cabo Verde",
        "short": "CV"
    },
    "KHM": {
        "name": "Cambodia",
        "short": "CB"
    },
    "CMR": {
        "name": "Cameroon",
        "short": "CM"
    },
    "CAN": {
        "name": "Canada",
        "short": "CA"
    },
    "CYM": {
        "name": "Cayman Islands",
        "short": "CJ"
    },
    "CAF": {
        "name": "Central African Republic",
        "short": "CT"
    },
    "TCD": {
        "name": "Chad",
        "short": "CD"
    },
    "CHL": {
        "name": "Chile",
        "short": "CI"
    },
    "CHN": {
        "name": "China",
        "short": "CH"
    },
    "HKG": {
        "name": "China, Hong Kong Special Administrative Region",
        "short": "HK"
    },
    "MAC": {
        "name": "China, Macao Special Administrative Region",
        "short": "MC"
    },
    "CXR": {
        "name": "Christmas Island",
        "short": "KT"
    },
    "CCK": {
        "name": "Cocos (Keeling) Islands",
        "short": "CK"
    },
    "COL": {
        "name": "Colombia",
        "short": "CO"
    },
    "COM": {
        "name": "Comoros",
        "short": "CN"
    },
    "COG": {
        "name": "Congo",
        "short": "CF"
    },
    "COK": {
        "name": "Cook Islands",
        "short": "CW"
    },
    "CRI": {
        "name": "Costa Rica",
        "short": "CS"
    },
    "HRV": {
        "name": "Croatia",
        "short": "HR"
    },
    "CUB": {
        "name": "Cuba",
        "short": "CU"
    },
    "CUW": {
        "name": "Curaao",
        "short": "UC"
    },
    "CYP": {
        "name": "Cyprus",
        "short": "CY"
    },
    "CZE": {
        "name": "Czechia",
        "short": "EZ"
    },
    "CIV": {
        "name": "Cte d'Ivoire",
        "short": "IV"
    },
    "PRK": {
        "name": "Democratic People's Republic of Korea",
        "short": "KN"
    },
    "COD": {
        "name": "Democratic Republic of the Congo",
        "short": "CG"
    },
    "DNK": {
        "name": "Denmark",
        "short": "DA"
    },
    "DJI": {
        "name": "Djibouti",
        "short": "DJ"
    },
    "DMA": {
        "name": "Dominica",
        "short": "DO"
    },
    "DOM": {
        "name": "Dominican Republic",
        "short": "DR"
    },
    "ECU": {
        "name": "Ecuador",
        "short": "EC"
    },
    "EGY": {
        "name": "Egypt",
        "short": "EG"
    },
    "SLV": {
        "name": "El Salvador",
        "short": "ES"
    },
    "GNQ": {
        "name": "Equatorial Guinea",
        "short": "EK"
    },
    "ERI": {
        "name": "Eritrea",
        "short": "ER"
    },
    "EST": {
        "name": "Estonia",
        "short": "EN"
    },
    "ETH": {
        "name": "Ethiopia",
        "short": "ET"
    },
    "FLK": {
        "name": "Falkland Islands (Malvinas)",
        "short": "FK"
    },
    "FRO": {
        "name": "Faroe Islands",
        "short": "FO"
    },
    "FJI": {
        "name": "Fiji",
        "short": "FJ"
    },
    "FIN": {
        "name": "Finland",
        "short": "FI"
    },
    "FRA": {
        "name": "France",
        "short": "FR"
    },
    "GUF": {
        "name": "French Guiana",
        "short": "FG"
    },
    "PYF": {
        "name": "French Polynesia",
        "short": "FP"
    },
    "ATF": {
        "name": "French Southern Territories",
        "short": "FS"
    },
    "GAB": {
        "name": "Gabon",
        "short": "GB"
    },
    "GMB": {
        "name": "Gambia",
        "short": "GA"
    },
    "GEO": {
        "name": "Georgia",
        "short": "GG"
    },
    "DEU": {
        "name": "Germany",
        "short": "GM"
    },
    "GHA": {
        "name": "Ghana",
        "short": "GH"
    },
    "GIB": {
        "name": "Gibraltar",
        "short": "GI"
    },
    "GRC": {
        "name": "Greece",
        "short": "GR"
    },
    "GRL": {
        "name": "Greenland",
        "short": "GL"
    },
    "GRD": {
        "name": "Grenada",
        "short": "GJ"
    },
    "GLP": {
        "name": "Guadeloupe",
        "short": "GP"
    },
    "GUM": {
        "name": "Guam",
        "short": "GQ"
    },
    "GTM": {
        "name": "Guatemala",
        "short": "GT"
    },
    "GGY": {
        "name": "Guernsey",
        "short": "GK"
    },
    "GIN": {
        "name": "Guinea",
        "short": "GV"
    },
    "GNB": {
        "name": "Guinea-Bissau",
        "short": "PU"
    },
    "GUY": {
        "name": "Guyana",
        "short": "GY"
    },
    "HTI": {
        "name": "Haiti",
        "short": "HA"
    },
    "HMD": {
        "name": "Heard Island and McDonald Islands",
        "short": "HM"
    },
    "VAT": {
        "name": "Holy See",
        "short": "VT"
    },
    "HND": {
        "name": "Honduras",
        "short": "HO"
    },
    "HUN": {
        "name": "Hungary",
        "short": "HU"
    },
    "ISL": {
        "name": "Iceland",
        "short": "IC"
    },
    "IND": {
        "name": "India",
        "short": "IN"
    },
    "IDN": {
        "name": "Indonesia",
        "short": "ID"
    },
    "IRN": {
        "name": "Iran (Islamic Republic of)",
        "short": "IR"
    },
    "IRQ": {
        "name": "Iraq",
        "short": "IZ"
    },
    "IRL": {
        "name": "Ireland",
        "short": "EI"
    },
    "IMN": {
        "name": "Isle of Man",
        "short": "IM"
    },
    "ISR": {
        "name": "Israel",
        "short": "IS"
    },
    "ITA": {
        "name": "Italy",
        "short": "IT"
    },
    "JAM": {
        "name": "Jamaica",
        "short": "JM"
    },
    "JPN": {
        "name": "Japan",
        "short": "JA"
    },
    "JEY": {
        "name": "Jersey",
        "short": "JE"
    },
    "JOR": {
        "name": "Jordan",
        "short": "JO"
    },
    "KAZ": {
        "name": "Kazakhstan",
        "short": "KZ"
    },
    "KEN": {
        "name": "Kenya",
        "short": "KE"
    },
    "KIR": {
        "name": "Kiribati",
        "short": "KR"
    },
    "KWT": {
        "name": "Kuwait",
        "short": "KU"
    },
    "KGZ": {
        "name": "Kyrgyzstan",
        "short": "KG"
    },
    "LAO": {
        "name": "Lao People's Democratic Republic",
        "short": "LA"
    },
    "LVA": {
        "name": "Latvia",
        "short": "LG"
    },
    "LBN": {
        "name": "Lebanon",
        "short": "LE"
    },
    "LSO": {
        "name": "Lesotho",
        "short": "LT"
    },
    "LBR": {
        "name": "Liberia",
        "short": "LI"
    },
    "LBY": {
        "name": "Libya",
        "short": "LY"
    },
    "LIE": {
        "name": "Liechtenstein",
        "short": "LS"
    },
    "LTU": {
        "name": "Lithuania",
        "short": "LH"
    },
    "LUX": {
        "name": "Luxembourg",
        "short": "LU"
    },
    "MDG": {
        "name": "Madagascar",
        "short": "MA"
    },
    "MWI": {
        "name": "Malawi",
        "short": "MI"
    },
    "MYS": {
        "name": "Malaysia",
        "short": "MY"
    },
    "MDV": {
        "name": "Maldives",
        "short": "MV"
    },
    "MLI": {
        "name": "Mali",
        "short": "ML"
    },
    "MLT": {
        "name": "Malta",
        "short": "MT"
    },
    "MHL": {
        "name": "Marshall Islands",
        "short": "RM"
    },
    "MTQ": {
        "name": "Martinique",
        "short": "MB"
    },
    "MRT": {
        "name": "Mauritania",
        "short": "MR"
    },
    "MUS": {
        "name": "Mauritius",
        "short": "MP"
    },
    "MYT": {
        "name": "Mayotte",
        "short": "MF"
    },
    "MEX": {
        "name": "Mexico",
        "short": "MX"
    },
    "FSM": {
        "name": "Micronesia (Federated States of)",
        "short": "FM"
    },
    "MCO": {
        "name": "Monaco",
        "short": "MN"
    },
    "MNG": {
        "name": "Mongolia",
        "short": "MG"
    },
    "MNE": {
        "name": "Montenegro",
        "short": "MJ"
    },
    "MSR": {
        "name": "Montserrat",
        "short": "MH"
    },
    "MAR": {
        "name": "Morocco",
        "short": "MO"
    },
    "MOZ": {
        "name": "Mozambique",
        "short": "MZ"
    },
    "MMR": {
        "name": "Myanmar",
        "short": "BM"
    },
    "NAM": {
        "name": "Namibia",
        "short": "WA"
    },
    "NRU": {
        "name": "Nauru",
        "short": "NR"
    },
    "NPL": {
        "name": "Nepal",
        "short": "NP"
    },
    "NLD": {
        "name": "Netherlands",
        "short": "NL"
    },
    "NCL": {
        "name": "New Caledonia",
        "short": "NC"
    },
    "NZL": {
        "name": "New Zealand",
        "short": "NZ"
    },
    "NIC": {
        "name": "Nicaragua",
        "short": "NU"
    },
    "NER": {
        "name": "Niger",
        "short": "NG"
    },
    "NGA": {
        "name": "Nigeria",
        "short": "NI"
    },
    "NIU": {
        "name": "Niue",
        "short": "NE"
    },
    "NFK": {
        "name": "Norfolk Island",
        "short": "NF"
    },
    "MNP": {
        "name": "Northern Mariana Islands",
        "short": "CQ"
    },
    "NOR": {
        "name": "Norway",
        "short": "NO"
    },
    "OMN": {
        "name": "Oman",
        "short": "MU"
    },
    "PAK": {
        "name": "Pakistan",
        "short": "PK"
    },
    "PLW": {
        "name": "Palau",
        "short": "PS"
    },
    "PAN": {
        "name": "Panama",
        "short": "PM"
    },
    "PNG": {
        "name": "Papua New Guinea",
        "short": "PP"
    },
    "PRY": {
        "name": "Paraguay",
        "short": "PA"
    },
    "PER": {
        "name": "Peru",
        "short": "PE"
    },
    "PHL": {
        "name": "Philippines",
        "short": "RP"
    },
    "PCN": {
        "name": "Pitcairn",
        "short": "PC"
    },
    "POL": {
        "name": "Poland",
        "short": "PL"
    },
    "PRT": {
        "name": "Portugal",
        "short": "PO"
    },
    "PRI": {
        "name": "Puerto Rico",
        "short": "RQ"
    },
    "QAT": {
        "name": "Qatar",
        "short": "QA"
    },
    "KOR": {
        "name": "Republic of Korea",
        "short": "KS"
    },
    "MDA": {
        "name": "Republic of Moldova",
        "short": "MD"
    },
    "ROU": {
        "name": "Romania",
        "short": "RO"
    },
    "RUS": {
        "name": "Russian Federation",
        "short": "RS"
    },
    "RWA": {
        "name": "Rwanda",
        "short": "RW"
    },
    "REU": {
        "name": "Runion",
        "short": "RE"
    },
    "BLM": {
        "name": "Saint Barthlemy",
        "short": "TB"
    },
    "SHN": {
        "name": "Saint Helena",
        "short": "SH"
    },
    "KNA": {
        "name": "Saint Kitts and Nevis",
        "short": "SC"
    },
    "LCA": {
        "name": "Saint Lucia",
        "short": "ST"
    },
    "MAF": {
        "name": "Saint Martin (French Part)",
        "short": "RN"
    },
    "SPM": {
        "name": "Saint Pierre and Miquelon",
        "short": "SB"
    },
    "VCT": {
        "name": "Saint Vincent and the Grenadines",
        "short": "VC"
    },
    "WSM": {
        "name": "Samoa",
        "short": "WS"
    },
    "SMR": {
        "name": "San Marino",
        "short": "SM"
    },
    "STP": {
        "name": "Sao Tome and Principe",
        "short": "TP"
    },
    "SAU": {
        "name": "Saudi Arabia",
        "short": "SA"
    },
    "SEN": {
        "name": "Senegal",
        "short": "SG"
    },
    "SYC": {
        "name": "Seychelles",
        "short": "SE"
    },
    "SLE": {
        "name": "Sierra Leone",
        "short": "SL"
    },
    "SGP": {
        "name": "Singapore",
        "short": "SN"
    },
    "SXM": {
        "name": "Sint Maarten (Dutch part)",
        "short": "NN"
    },
    "SVK": {
        "name": "Slovakia",
        "short": "LO"
    },
    "SVN": {
        "name": "Slovenia",
        "short": "SI"
    },
    "SLB": {
        "name": "Solomon Islands",
        "short": "BP"
    },
    "SOM": {
        "name": "Somalia",
        "short": "SO"
    },
    "ZAF": {
        "name": "South Africa",
        "short": "SF"
    },
    "SGS": {
        "name": "South Georgia and the South Sandwich Islands",
        "short": "SX"
    },
    "SSD": {
        "name": "South Sudan",
        "short": "OD"
    },
    "ESP": {
        "name": "Spain",
        "short": "SP"
    },
    "LKA": {
        "name": "Sri Lanka",
        "short": "CE"
    },
    "SDN": {
        "name": "Sudan",
        "short": "SU"
    },
    "SUR": {
        "name": "Suriname",
        "short": "NS"
    },
    "SWZ": {
        "name": "Swaziland",
        "short": "WZ"
    },
    "SWE": {
        "name": "Sweden",
        "short": "SW"
    },
    "CHE": {
        "name": "Switzerland",
        "short": "SZ"
    },
    "SYR": {
        "name": "Syrian Arab Republic",
        "short": "SY"
    },
    "TJK": {
        "name": "Tajikistan",
        "short": "TI"
    },
    "THA": {
        "name": "Thailand",
        "short": "TH"
    },
    "MKD": {
        "name": "The former Yugoslav Republic of Macedonia",
        "short": "MK"
    },
    "TLS": {
        "name": "Timor-Leste",
        "short": "TT"
    },
    "TGO": {
        "name": "Togo",
        "short": "TO"
    },
    "TKL": {
        "name": "Tokelau",
        "short": "TL"
    },
    "TON": {
        "name": "Tonga",
        "short": "TN"
    },
    "TTO": {
        "name": "Trinidad and Tobago",
        "short": "TD"
    },
    "TUN": {
        "name": "Tunisia",
        "short": "TS"
    },
    "TUR": {
        "name": "Turkey",
        "short": "TU"
    },
    "TKM": {
        "name": "Turkmenistan",
        "short": "TX"
    },
    "TCA": {
        "name": "Turks and Caicos Islands",
        "short": "TK"
    },
    "TUV": {
        "name": "Tuvalu",
        "short": "TV"
    },
    "UGA": {
        "name": "Uganda",
        "short": "UG"
    },
    "UKR": {
        "name": "Ukraine",
        "short": "UP"
    },
    "ARE": {
        "name": "United Arab Emirates",
        "short": "AE"
    },
    "GBR": {
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "short": "UK"
    },
    "TZA": {
        "name": "United Republic of Tanzania",
        "short": "TZ"
    },
    "VIR": {
        "name": "United States Virgin Islands",
        "short": "VQ"
    },
    "USA": {
        "name": "United States of America",
        "short": "US"
    },
    "URY": {
        "name": "Uruguay",
        "short": "UY"
    },
    "UZB": {
        "name": "Uzbekistan",
        "short": "UZ"
    },
    "VUT": {
        "name": "Vanuatu",
        "short": "NH"
    },
    "VEN": {
        "name": "Venezuela (Bolivarian Republic of)",
        "short": "VE"
    },
    "VNM": {
        "name": "Viet Nam",
        "short": "VM"
    },
    "WLF": {
        "name": "Wallis and Futuna Islands",
        "short": "WF"
    },
    "ESH": {
        "name": "Western Sahara",
        "short": "WI"
    },
    "YEM": {
        "name": "Yemen",
        "short": "YM"
    },
    "ZMB": {
        "name": "Zambia",
        "short": "ZA"
    },
    "ZWE": {
        "name": "Zimbabwe",
        "short": "ZI"
    }
}