# Function to draw the playing cards with Pokémon data on the A4 page
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Convert inches to points (1 inch = 72 points)
inch_to_points = 72
card_width = 2.5 * inch_to_points  # 2.5 inches
card_height = 3.5 * inch_to_points  # 3.5 inches

# Full Pokémon list
pokemon_list = [
    ("Bulbasaur", "001"),
    ("Ivysaur", "002"),
    ("Venusaur", "003"),
    ("Charmander", "004"),
    ("Charmeleon", "005"),
    ("Charizard", "006"),
    ("Squirtle", "007"),
    ("Wartortle", "008"),
    ("Blastoise", "009"),
    ("Caterpie", "010"),
    ("Metapod", "011"),
    ("Butterfree", "012"),
    ("Weedle", "013"),
    ("Kakuna", "014"),
    ("Beedrill", "015"),
    ("Pidgey", "016"),
    ("Pidgeotto", "017"),
    ("Pidgeot", "018"),
    ("Rattata", "019"),
    ("Raticate", "020"),
    ("Spearow", "021"),
    ("Fearow", "022"),
    ("Ekans", "023"),
    ("Arbok", "024"),
    ("Pikachu", "025"),
    ("Raichu", "026"),
    ("Sandshrew", "027"),
    ("Sandslash", "028"),
    ("Nidoran♀", "029"),
    ("Nidorina", "030"),
    ("Nidoqueen", "031"),
    ("Nidoran♂", "032"),
    ("Nidorino", "033"),
    ("Nidoking", "034"),
    ("Clefairy", "035"),
    ("Clefable", "036"),
    ("Vulpix", "037"),
    ("Ninetales", "038"),
    ("Jigglypuff", "039"),
    ("Wigglytuff", "040"),
    ("Zubat", "041"),
    ("Golbat", "042"),
    ("Oddish", "043"),
    ("Gloom", "044"),
    ("Vileplume", "045"),
    ("Paras", "046"),
    ("Parasect", "047"),
    ("Venonat", "048"),
    ("Venomoth", "049"),
    ("Diglett", "050"),
    ("Dugtrio", "051"),
    ("Meowth", "052"),
    ("Persian", "053"),
    ("Psyduck", "054"),
    ("Golduck", "055"),
    ("Mankey", "056"),
    ("Primeape", "057"),
    ("Growlithe", "058"),
    ("Arcanine", "059"),
    ("Poliwag", "060"),
    ("Poliwhirl", "061"),
    ("Poliwrath", "062"),
    ("Abra", "063"),
    ("Kadabra", "064"),
    ("Alakazam", "065"),
    ("Machop", "066"),
    ("Machoke", "067"),
    ("Machamp", "068"),
    ("Bellsprout", "069"),
    ("Weepinbell", "070"),
    ("Victreebel", "071"),
    ("Tentacool", "072"),
    ("Tentacruel", "073"),
    ("Geodude", "074"),
    ("Graveler", "075"),
    ("Golem", "076"),
    ("Ponyta", "077"),
    ("Rapidash", "078"),
    ("Slowpoke", "079"),
    ("Slowbro", "080"),
    ("Magnemite", "081"),
    ("Magneton", "082"),
    ("Farfetch'd", "083"),
    ("Doduo", "084"),
    ("Dodrio", "085"),
    ("Seel", "086"),
    ("Dewgong", "087"),
    ("Grimer", "088"),
    ("Muk", "089"),
    ("Shellder", "090"),
    ("Cloyster", "091"),
    ("Gastly", "092"),
    ("Haunter", "093"),
    ("Gengar", "094"),
    ("Onix", "095"),
    ("Drowzee", "096"),
    ("Hypno", "097"),
    ("Krabby", "098"),
    ("Kingler", "099"),
    ("Voltorb", "100"),
    ("Electrode", "101"),
    ("Exeggcute", "102"),
    ("Exeggutor", "103"),
    ("Cubone", "104"),
    ("Marowak", "105"),
    ("Hitmonlee", "106"),
    ("Hitmonchan", "107"),
    ("Lickitung", "108"),
    ("Koffing", "109"),
    ("Weezing", "110"),
    ("Rhyhorn", "111"),
    ("Rhydon", "112"),
    ("Chansey", "113"),
    ("Tangela", "114"),
    ("Kangaskhan", "115"),
    ("Horsea", "116"),
    ("Seadra", "117"),
    ("Goldeen", "118"),
    ("Seaking", "119"),
    ("Staryu", "120"),
    ("Starmie", "121"),
    ("Mr. Mime", "122"),
    ("Scyther", "123"),
    ("Jynx", "124"),
    ("Electabuzz", "125"),
    ("Magmar", "126"),
    ("Pinsir", "127"),
    ("Tauros", "128"),
    ("Magikarp", "129"),
    ("Gyarados", "130"),
    ("Lapras", "131"),
    ("Ditto", "132"),
    ("Eevee", "133"),
    ("Vaporeon", "134"),
    ("Jolteon", "135"),
    ("Flareon", "136"),
    ("Porygon", "137"),
    ("Omanyte", "138"),
    ("Omastar", "139"),
    ("Kabuto", "140"),
    ("Kabutops", "141"),
    ("Aerodactyl", "142"),
    ("Snorlax", "143"),
    ("Articuno", "144"),
    ("Zapdos", "145"),
    ("Moltres", "146"),
    ("Dratini", "147"),
    ("Dragonair", "148"),
    ("Dragonite", "149"),
    ("Mewtwo", "150"),
    ("Mew", "151"),

    # Gen 2 Pokémon
    ("Chikorita", "152"),
    ("Bayleef", "153"),
    ("Meganium", "154"),
    ("Cyndaquil", "155"),
    ("Quilava", "156"),
    ("Typhlosion", "157"),
    ("Totodile", "158"),
    ("Croconaw", "159"),
    ("Feraligatr", "160"),
    ("Sentret", "161"),
    ("Furret", "162"),
    ("Hoothoot", "163"),
    ("Noctowl", "164"),
    ("Ledyba", "165"),
    ("Ledian", "166"),
    ("Spinarak", "167"),
    ("Ariados", "168"),
    ("Crobat", "169"),
    ("Chinchou", "170"),
    ("Lanturn", "171"),
    ("Pichu", "172"),
    ("Cleffa", "173"),
    ("Igglybuff", "174"),
    ("Togepi", "175"),
    ("Togetic", "176"),
    ("Natu", "177"),
    ("Xatu", "178"),
    ("Mareep", "179"),
    ("Flaaffy", "180"),
    ("Ampharos", "181"),
    ("Bellossom", "182"),
    ("Marill", "183"),
    ("Azumarill", "184"),
    ("Sudowoodo", "185"),
    ("Politoed", "186"),
    ("Hoppip", "187"),
    ("Skiploom", "188"),
    ("Jumpluff", "189"),
    ("Aipom", "190"),
    ("Sunkern", "191"),
    ("Sunflora", "192"),
    ("Yanma", "193"),
    ("Wooper", "194"),
    ("Quagsire", "195"),
    ("Espeon", "196"),
    ("Umbreon", "197"),
    ("Murkrow", "198"),
    ("Slowking", "199"),
    ("Misdreavus", "200"),
    ("Unown", "201"),
    ("Wobbuffet", "202"),
    ("Girafarig", "203"),
    ("Pineco", "204"),
    ("Forretress", "205"),
    ("Dunsparce", "206"),
    ("Gligar", "207"),
    ("Steelix", "208"),
    ("Snubbull", "209"),
    ("Granbull", "210"),
    ("Qwilfish", "211"),
    ("Scizor", "212"),
    ("Shuckle", "213"),
    ("Heracross", "214"),
    ("Sneasel", "215"),
    ("Teddiursa", "216"),
    ("Ursaring", "217"),
    ("Slugma", "218"),
    ("Magcargo", "219"),
    ("Swinub", "220"),
    ("Piloswine", "221"),
    ("Corsola", "222"),
    ("Remoraid", "223"),
    ("Octillery", "224"),
    ("Delibird", "225"),
    ("Mantine", "226"),
    ("Skarmory", "227"),
    ("Houndour", "228"),
    ("Houndoom", "229"),
    ("Kingdra", "230"),
    ("Phanpy", "231"),
    ("Donphan", "232"),
    ("Porygon2", "233"),
    ("Stantler", "234"),
    ("Smeargle", "235"),
    ("Tyrogue", "236"),
    ("Hitmontop", "237"),
    ("Smoochum", "238"),
    ("Elekid", "239"),
    ("Magby", "240"),
    ("Miltank", "241"),
    ("Blissey", "242"),
    ("Raikou", "243"),
    ("Entei", "244"),
    ("Suicune", "245"),
    ("Larvitar", "246"),
    ("Pupitar", "247"),
    ("Tyranitar", "248"),
    ("Lugia", "249"),
    ("Ho-oh", "250"),
    ("Celebi", "251"),
    
    # Gen 3 Pokémon
    
    ("Treecko", "252"),
    ("Grovyle", "253"),
    ("Sceptile", "254"),
    ("Torchic", "255"),
    ("Combusken", "256"),
    ("Blaziken", "257"),
    ("Mudkip", "258"),
    ("Marshtomp", "259"),
    ("Swampert", "260"),
    ("Poochyena", "261"),
    ("Mightyena", "262"),
    ("Zigzagoon", "263"),
    ("Linoone", "264"),
    ("Wurmple", "265"),
    ("Silcoon", "266"),
    ("Beautifly", "267"),
    ("Cascoon", "268"),
    ("Dustox", "269"),
    ("Lotad", "270"),
    ("Lombre", "271"),
    ("Ludicolo", "272"),
    ("Seedot", "273"),
    ("Nuzleaf", "274"),
    ("Shiftry", "275"),
    ("Taillow", "276"),
    ("Swellow", "277"),
    ("Wingull", "278"),
    ("Pelipper", "279"),
    ("Ralts", "280"),
    ("Kirlia", "281"),
    ("Gardevoir", "282"),
    ("Surskit", "283"),
    ("Masquerain", "284"),
    ("Shroomish", "285"),
    ("Breloom", "286"),
    ("Slakoth", "287"),
    ("Vigoroth", "288"),
    ("Slaking", "289"),
    ("Nincada", "290"),
    ("Ninjask", "291"),
    ("Shedinja", "292"),
    ("Whismur", "293"),
    ("Loudred", "294"),
    ("Exploud", "295"),
    ("Makuhita", "296"),
    ("Hariyama", "297"),
    ("Azurill", "298"),
    ("Nosepass", "299"),
    ("Skitty", "300"),
    ("Delcatty", "301"),
    ("Sableye", "302"),
    ("Mawile", "303"),
    ("Aron", "304"),
    ("Lairon", "305"),
    ("Aggron", "306"),
    ("Meditite", "307"),
    ("Medicham", "308"),
    ("Electrike", "309"),
    ("Manectric", "310"),
    ("Plusle", "311"),
    ("Minun", "312"),
    ("Volbeat", "313"),
    ("Illumise", "314"),
    ("Roselia", "315"),
    ("Gulpin", "316"),
    ("Swalot", "317"),
    ("Carvanha", "318"),
    ("Sharpedo", "319"),
    ("Wailmer", "320"),
    ("Wailord", "321"),
    ("Numel", "322"),
    ("Camerupt", "323"),
    ("Torkoal", "324"),
    ("Spoink", "325"),
    ("Grumpig", "326"),
    ("Spinda", "327"),
    ("Trapinch", "328"),
    ("Vibrava", "329"),
    ("Flygon", "330"),
    ("Cacnea", "331"),
    ("Cacturne", "332"),
    ("Swablu", "333"),
    ("Altaria", "334"),
    ("Zangoose", "335"),
    ("Seviper", "336"),
    ("Lunatone", "337"),
    ("Solrock", "338"),
    ("Barboach", "339"),
    ("Whiscash", "340"),
    ("Corphish", "341"),
    ("Crawdaunt", "342"),
    ("Baltoy", "343"),
    ("Claydol", "344"),
    ("Lileep", "345"),
    ("Cradily", "346"),
    ("Anorith", "347"),
    ("Armaldo", "348"),
    ("Feebas", "349"),
    ("Milotic", "350"),
    ("Castform", "351"),
    ("Kecleon", "352"),
    ("Shuppet", "353"),
    ("Banette", "354"),
    ("Duskull", "355"),
    ("Dusclops", "356"),
    ("Tropius", "357"),
    ("Chimecho", "358"),
    ("Absol", "359"),
    ("Wynaut", "360"),
    ("Snorunt", "361"),
    ("Glalie", "362"),
    ("Spheal", "363"),
    ("Sealeo", "364"),
    ("Walrein", "365"),
    ("Clamperl", "366"),
    ("Huntail", "367"),
    ("Gorebyss", "368"),
    ("Relicanth", "369"),
    ("Luvdisc", "370"),
    ("Bagon", "371"),
    ("Shelgon", "372"),
    ("Salamence", "373"),
    ("Beldum", "374"),
    ("Metang", "375"),
    ("Metagross", "376"),
    ("Regirock", "377"),
    ("Regice", "378"),
    ("Registeel", "379"),
    ("Latias", "380"),
    ("Latios", "381"),
    ("Kyogre", "382"),
    ("Groudon", "383"),
    ("Rayquaza", "384"),
    ("Jirachi", "385"),
    ("Deoxys", "386"),

    
    #Gen 4 Pokémon
    
    ("Turtwig", "387"),
    ("Grotle", "388"),
    ("Torterra", "389"),
    ("Chimchar", "390"),
    ("Monferno", "391"),
    ("Infernape", "392"),
    ("Piplup", "393"),
    ("Prinplup", "394"),
    ("Empoleon", "395"),
    ("Starly", "396"),
    ("Staravia", "397"),
    ("Staraptor", "398"),
    ("Bidoof", "399"),
    ("Bibarel", "400"),
    ("Kricketot", "401"),
    ("Kricketune", "402"),
    ("Shinx", "403"),
    ("Luxio", "404"),
    ("Luxray", "405"),
    ("Budew", "406"),
    ("Roserade", "407"),
    ("Cranidos", "408"),
    ("Rampardos", "409"),
    ("Shieldon", "410"),
    ("Bastiodon", "411"),
    ("Burmy", "412"),
    ("Wormadam", "413"),
    ("Mothim", "414"),
    ("Combee", "415"),
    ("Vespiquen", "416"),
    ("Pachirisu", "417"),
    ("Buizel", "418"),
    ("Floatzel", "419"),
    ("Cherubi", "420"),
    ("Cherrim", "421"),
    ("Shellos", "422"),
    ("Gastrodon", "423"),
    ("Ambipom", "424"),
    ("Drifloon", "425"),
    ("Drifblim", "426"),
    ("Buneary", "427"),
    ("Lopunny", "428"),
    ("Mismagius", "429"),
    ("Honchkrow", "430"),
    ("Glameow", "431"),
    ("Purugly", "432"),
    ("Chingling", "433"),
    ("Stunky", "434"),
    ("Skuntank", "435"),
    ("Bronzor", "436"),
    ("Bronzong", "437"),
    ("Bonsly", "438"),
    ("Mime Jr.", "439"),
    ("Happiny", "440"),
    ("Chatot", "441"),
    ("Spiritomb", "442"),
    ("Gible", "443"),
    ("Gabite", "444"),
    ("Garchomp", "445"),
    ("Munchlax", "446"),
    ("Riolu", "447"),
    ("Lucario", "448"),
    ("Hippopotas", "449"),
    ("Hippowdon", "450"),
    ("Skorupi", "451"),
    ("Drapion", "452"),
    ("Croagunk", "453"),
    ("Toxicroak", "454"),
    ("Carnivine", "455"),
    ("Finneon", "456"),
    ("Lumineon", "457"),
    ("Mantyke", "458"),
    ("Snover", "459"),
    ("Abomasnow", "460"),
    ("Weavile", "461"),
    ("Magnezone", "462"),
    ("Lickilicky", "463"),
    ("Rhyperior", "464"),
    ("Tangrowth", "465"),
    ("Electivire", "466"),
    ("Magmortar", "467"),
    ("Togekiss", "468"),
    ("Yanmega", "469"),
    ("Leafeon", "470"),
    ("Glaceon", "471"),
    ("Gliscor", "472"),
    ("Mamoswine", "473"),
    ("Porygon-Z", "474"),
    ("Gallade", "475"),
    ("Probopass", "476"),
    ("Dusknoir", "477"),
    ("Froslass", "478"),
    ("Rotom", "479"),
    ("Uxie", "480"),
    ("Mesprit", "481"),
    ("Azelf", "482"),
    ("Dialga", "483"),
    ("Palkia", "484"),
    ("Heatran", "485"),
    ("Regigigas", "486"),
    ("Giratina", "487"),
    ("Cresselia", "488"),
    ("Phione", "489"),
    ("Manaphy", "490"),
    ("Darkrai", "491"),
    ("Shaymin", "492"),
    ("Arceus", "493"),

    #Gen 5 Pokémon

    ("Victini", "494"),
    ("Snivy", "495"),
    ("Servine", "496"),
    ("Serperior", "497"),
    ("Tepig", "498"),
    ("Pignite", "499"),
    ("Emboar", "500"),
    ("Oshawott", "501"),
    ("Dewott", "502"),
    ("Samurott", "503"),
    ("Patrat", "504"),
    ("Watchog", "505"),
    ("Lillipup", "506"),
    ("Herdier", "507"),
    ("Stoutland", "508"),
    ("Purrloin", "509"),
    ("Liepard", "510"),
    ("Pansage", "511"),
    ("Simisage", "512"),
    ("Pansear", "513"),
    ("Simisear", "514"),
    ("Panpour", "515"),
    ("Simipour", "516"),
    ("Munna", "517"),
    ("Musharna", "518"),
    ("Pidove", "519"),
    ("Tranquill", "520"),
    ("Unfezant", "521"),
    ("Blitzle", "522"),
    ("Zebstrika", "523"),
    ("Roggenrola", "524"),
    ("Boldore", "525"),
    ("Gigalith", "526"),
    ("Woobat", "527"),
    ("Swoobat", "528"),
    ("Drilbur", "529"),
    ("Excadrill", "530"),
    ("Audino", "531"),
    ("Timburr", "532"),
    ("Gurdurr", "533"),
    ("Conkeldurr", "534"),
    ("Tympole", "535"),
    ("Palpitoad", "536"),
    ("Seismitoad", "537"),
    ("Throh", "538"),
    ("Sawk", "539"),
    ("Sewaddle", "540"),
    ("Swadloon", "541"),
    ("Leavanny", "542"),
    ("Venipede", "543"),
    ("Whirlipede", "544"),
    ("Scolipede", "545"),
    ("Cottonee", "546"),
    ("Whimsicott", "547"),
    ("Petilil", "548"),
    ("Lilligant", "549"),
    ("Basculin", "550"),
    ("Sandile", "551"),
    ("Krokorok", "552"),
    ("Krookodile", "553"),
    ("Darumaka", "554"),
    ("Darmanitan", "555"),
    ("Maractus", "556"),
    ("Dwebble", "557"),
    ("Crustle", "558"),
    ("Scraggy", "559"),
    ("Scrafty", "560"),
    ("Sigilyph", "561"),
    ("Yamask", "562"),
    ("Cofagrigus", "563"),
    ("Tirtouga", "564"),
    ("Carracosta", "565"),
    ("Archen", "566"),
    ("Archeops", "567"),
    ("Trubbish", "568"),
    ("Garbodor", "569"),
    ("Zorua", "570"),
    ("Zoroark", "571"),
    ("Minccino", "572"),
    ("Cinccino", "573"),
    ("Gothita", "574"),
    ("Gothorita", "575"),
    ("Gothitelle", "576"),
    ("Solosis", "577"),
    ("Duosion", "578"),
    ("Reuniclus", "579"),
    ("Ducklett", "580"),
    ("Swanna", "581"),
    ("Vanillite", "582"),
    ("Vanillish", "583"),
    ("Vanilluxe", "584"),
    ("Deerling", "585"),
    ("Sawsbuck", "586"),
    ("Emolga", "587"),
    ("Karrablast", "588"),
    ("Escavalier", "589"),
    ("Foongus", "590"),
    ("Amoonguss", "591"),
    ("Frillish", "592"),
    ("Jellicent", "593"),
    ("Alomomola", "594"),
    ("Joltik", "595"),
    ("Galvantula", "596"),
    ("Ferroseed", "597"),
    ("Ferrothorn", "598"),
    ("Klink", "599"),
    ("Klang", "600"),
    ("Klinklang", "601"),
    ("Tynamo", "602"),
    ("Eelektrik", "603"),
    ("Eelektross", "604"),
    ("Elgyem", "605"),
    ("Beheeyem", "606"),
    ("Litwick", "607"),
    ("Lampent", "608"),
    ("Chandelure", "609"),
    ("Axew", "610"),
    ("Fraxure", "611"),
    ("Haxorus", "612"),
    ("Cubchoo", "613"),
    ("Beartic", "614"),
    ("Cryogonal", "615"),
    ("Shelmet", "616"),
    ("Accelgor", "617"),
    ("Stunfisk", "618"),
    ("Mienfoo", "619"),
    ("Mienshao", "620"),
    ("Druddigon", "621"),
    ("Golett", "622"),
    ("Golurk", "623"),
    ("Pawniard", "624"),
    ("Bisharp", "625"),
    ("Bouffalant", "626"),
    ("Rufflet", "627"),
    ("Braviary", "628"),
    ("Vullaby", "629"),
    ("Mandibuzz", "630"),
    ("Heatmor", "631"),
    ("Durant", "632"),
    ("Deino", "633"),
    ("Zweilous", "634"),
    ("Hydreigon", "635"),
    ("Larvesta", "636"),
    ("Volcarona", "637"),
    ("Cobalion", "638"),
    ("Terrakion", "639"),
    ("Virizion", "640"),
    ("Tornadus", "641"),
    ("Thundurus", "642"),
    ("Reshiram", "643"),
    ("Zekrom", "644"),
    ("Landorus", "645"),
    ("Kyurem", "646"),
    ("Keldeo", "647"),
    ("Meloetta", "648"),
    ("Genesect", "649"),

    #Gen 6 Pokémon

    ("Chespin", "650"),
    ("Quilladin", "651"),
    ("Chesnaught", "652"),
    ("Fennekin", "653"),
    ("Braixen", "654"),
    ("Delphox", "655"),
    ("Froakie", "656"),
    ("Frogadier", "657"),
    ("Greninja", "658"),
    ("Bunnelby", "659"),
    ("Diggersby", "660"),
    ("Fletchling", "661"),
    ("Fletchinder", "662"),
    ("Talonflame", "663"),
    ("Scatterbug", "664"),
    ("Spewpa", "665"),
    ("Vivillon", "666"),
    ("Litleo", "667"),
    ("Pyroar", "668"),
    ("Flabébé", "669"),
    ("Floette", "670"),
    ("Florges", "671"),
    ("Skiddo", "672"),
    ("Gogoat", "673"),
    ("Pancham", "674"),
    ("Pangoro", "675"),
    ("Furfrou", "676"),
    ("Espurr", "677"),
    ("Meowstic", "678"),
    ("Honedge", "679"),
    ("Doublade", "680"),
    ("Aegislash", "681"),
    ("Spritzee", "682"),
    ("Aromatisse", "683"),
    ("Swirlix", "684"),
    ("Slurpuff", "685"),
    ("Inkay", "686"),
    ("Malamar", "687"),
    ("Binacle", "688"),
    ("Barbaracle", "689"),
    ("Skrelp", "690"),
    ("Dragalge", "691"),
    ("Clauncher", "692"),
    ("Clawitzer", "693"),
    ("Helioptile", "694"),
    ("Heliolisk", "695"),
    ("Tyrunt", "696"),
    ("Tyrantrum", "697"),
    ("Amaura", "698"),
    ("Aurorus", "699"),
    ("Sylveon", "700"),
    ("Hawlucha", "701"),
    ("Dedenne", "702"),
    ("Carbink", "703"),
    ("Goomy", "704"),
    ("Sliggoo", "705"),
    ("Goodra", "706"),
    ("Klefki", "707"),
    ("Phantump", "708"),
    ("Trevenant", "709"),
    ("Pumpkaboo", "710"),
    ("Gourgeist", "711"),
    ("Bergmite", "712"),
    ("Avalugg", "713"),
    ("Noibat", "714"),
    ("Noivern", "715"),
    ("Xerneas", "716"),
    ("Yveltal", "717"),
    ("Zygarde", "718"),
    ("Diancie", "719"),
    ("Hoopa", "720"),
    ("Volcanion", "721"),

    # Gen 7 Pokémon (Alola Region),

    ("Rowlet", "722"),
    ("Dartrix", "723"),
    ("Decidueye", "724"),
    ("Litten", "725"),
    ("Torracat", "726"),
    ("Incineroar", "727"),
    ("Popplio", "728"),
    ("Brionne", "729"),
    ("Primarina", "730"),
    ("Pikipek", "731"),
    ("Trumbeak", "732"),
    ("Toucannon", "733"),
    ("Yungoos", "734"),
    ("Gumshoos", "735"),
    ("Grubbin", "736"),
    ("Charjabug", "737"),
    ("Vikavolt", "738"),
    ("Crabrawler", "739"),
    ("Crabominable", "740"),
    ("Oricorio", "741"),
    ("Cutiefly", "742"),
    ("Ribombee", "743"),
    ("Rockruff", "744"),
    ("Lycanroc", "745"),
    ("Wishiwashi", "746"),
    ("Mareanie", "747"),
    ("Toxapex", "748"),
    ("Mudbray", "749"),
    ("Mudsdale", "750"),
    ("Dewpider", "751"),
    ("Araquanid", "752"),
    ("Fomantis", "753"),
    ("Lurantis", "754"),
    ("Morelull", "755"),
    ("Shiinotic", "756"),
    ("Salandit", "757"),
    ("Salazzle", "758"),
    ("Stufful", "759"),
    ("Bewear", "760"),
    ("Bounsweet", "761"),
    ("Steenee", "762"),
    ("Tsareena", "763"),
    ("Comfey", "764"),
    ("Oranguru", "765"),
    ("Passimian", "766"),
    ("Wimpod", "767"),
    ("Golisopod", "768"),
    ("Sandygast", "769"),
    ("Palossand", "770"),
    ("Pyukumuku", "771"),
    ("Type: Null", "772"),
    ("Silvally", "773"),
    ("Minior", "774"),
    ("Komala", "775"),
    ("Turtonator", "776"),
    ("Togedemaru", "777"),
    ("Mimikyu", "778"),
    ("Bruxish", "779"),
    ("Drampa", "780"),
    ("Dhelmise", "781"),
    ("Jangmo-o", "782"),
    ("Hakamo-o", "783"),
    ("Kommo-o", "784"),
    ("Tapu Koko", "785"),
    ("Tapu Lele", "786"),
    ("Tapu Bulu", "787"),
    ("Tapu Fini", "788"),
    ("Cosmog", "789"),
    ("Cosmoem", "790"),
    ("Solgaleo", "791"),
    ("Lunala", "792"),
    ("Nihilego", "793"),
    ("Buzzwole", "794"),
    ("Pheromosa", "795"),
    ("Xurkitree", "796"),
    ("Celesteela", "797"),
    ("Kartana", "798"),
    ("Guzzlord", "799"),
    ("Necrozma", "800"),
    ("Magearna", "801"),
    ("Marshadow", "802"),
    ("Poipole", "803"),
    ("Naganadel", "804"),
    ("Stakataka", "805"),
    ("Blacephalon", "806"),
    ("Zeraora", "807"),
    ("Meltan", "808"),
    ("Melmetal", "809"),

    # Generation 7 (Alola)
    ("Meowth (Alola)", "52"),
    ("Vileplume (Alola)", "45"),
    ("Geodude (Alola)", "74"),
    ("Graveler (Alola)", "75"),
    ("Golem (Alola)", "76"),
    ("Diglett (Alola)", "50"),
    ("Dugtrio (Alola)", "51"),
    ("Exeggutor (Alola)", "103"),
    ("Raichu (Alola)", "26"),
    ("Zubat (Alola)", "41"),
    ("Golbat (Alola)", "42"),
    ("Sandshrew (Alola)", "27"),
    ("Sandslash (Alola)", "28"),
    ("Marowak (Alola)", "105"),
    ("Rattata (Alola)", "19"),
    ("Raticate (Alola)", "20"),

    # Gen 8 Pokémon (Galar Region)

    ("Grookey", "810"),
    ("Thwackey", "811"),
    ("Rillaboom", "812"),
    ("Scorbunny", "813"),
    ("Raboot", "814"),
    ("Cinderace", "815"),
    ("Sobble", "816"),
    ("Drizzile", "817"),
    ("Inteleon", "818"),
    ("Skwovet", "819"),
    ("Greedent", "820"),
    ("Rookidee", "821"),
    ("Corvisquire", "822"),
    ("Corviknight", "823"),
    ("Blipbug", "824"),
    ("Dottler", "825"),
    ("Orbeetle", "826"),
    ("Nickit", "827"),
    ("Thievul", "828"),
    ("Gossifleur", "829"),
    ("Eldegoss", "830"),
    ("Wooloo", "831"),
    ("Dubwool", "832"),
    ("Chewtle", "833"),
    ("Drednaw", "834"),
    ("Yamper", "835"),
    ("Boltund", "836"),
    ("Rolycoly", "837"),
    ("Carkol", "838"),
    ("Coalossal", "839"),
    ("Applin", "840"),
    ("Flapple", "841"),
    ("Appletun", "842"),
    ("Silicobra", "843"),
    ("Sandaconda", "844"),
    ("Cramorant", "845"),
    ("Arrokuda", "846"),
    ("Barraskewda", "847"),
    ("Toxel", "848"),
    ("Toxtricity", "849"),
    ("Sizzlipede", "850"),
    ("Centiskorch", "851"),
    ("Clobbopus", "852"),
    ("Grapploct", "853"),
    ("Sinistea", "854"),
    ("Polteageist", "855"),
    ("Hatenna", "856"),
    ("Hattrem", "857"),
    ("Hatterene", "858"),
    ("Impidimp", "859"),
    ("Morgrem", "860"),
    ("Grimmsnarl", "861"),
    ("Obstagoon", "862"),
    ("Perrserker", "863"),
    ("Cursola", "864"),
    ("Sirfetch'd", "865"),
    ("Mr. Rime", "866"),
    ("Runerigus", "867"),
    ("Milcery", "868"),
    ("Alcremie", "869"),
    ("Falinks", "870"),
    ("Pincurchin", "871"),
    ("Snom", "872"),
    ("Frosmoth", "873"),
    ("Stonjourner", "874"),
    ("Eiscue", "875"),
    ("Indeedee", "876"),
    ("Morpeko", "877"),
    ("Cufant", "878"),
    ("Copperajah", "879"),
    ("Dracozolt", "880"),
    ("Arctozolt", "881"),
    ("Dracovish", "882"),
    ("Arctovish", "883"),
    ("Duraludon", "884"),
    ("Dreepy", "885"),
    ("Drakloak", "886"),
    ("Dragapult", "887"),
    ("Zacian", "888"),
    ("Zamazenta", "889"),
    ("Eternatus", "890"),
    ("Kubfu", "891"),
    ("Urshifu", "892"),
    ("Zarude", "893"),
    ("Regieleki", "894"),
    ("Regidrago", "895"),
    ("Glastrier", "896"),
    ("Spectrier", "897"),
    ("Calyrex", "898"),

    # Generation 8 (Galar)
    ("Meowth (Galar)", "52"),
    ("Ponyta (Galar)", "77"),
    ("Rapidash (Galar)", "78"),
    ("Zigzagoon (Galar)", "263"),
    ("Linoone (Galar)", "264"),
    ("Darumaka (Galar)", "554"),
    ("Darmanitan (Galar)", "555"),
    ("Yamask (Galar)", "562"),
    ("Runerigus", "867"),
    ("Mimikyu (Galar)", "778"),

    # Generation 8 (Hisuian)
    ("Zorua (Hisuian)", "570"),
    ("Zoroark (Hisuian)", "571"),
    ("Growlithe (Hisuian)", "58"),
    ("Arcanine (Hisuian)", "59"),
    ("Voltorb (Hisuian)", "100"),
    ("Electrode (Hisuian)", "101"),
    ("Sneasel (Hisuian)", "215"),
    ("Weavile (Hisuian)", "461"),
    ("Basculin (Hisuian)", "335"),
    ("Basculegion", "902"),
    ("Samurott (Hisuian)", "395"),
    ("Decidueye (Hisuian)", "722"),
    ("Lilligant (Hisuian)", "549"),
    ("Enamorus (Hisuian)", "905"),

    # Gen 9 Pokémon (Paldea Region)
    ("Sprigatito", "906"),
    ("Floragato", "907"),
    ("Meowscarada", "908"),
    ("Fuecoco", "909"),
    ("Crocalor", "910"),
    ("Skeledirge", "911"),
    ("Quaxly", "912"),
    ("Quaxwell", "913"),
    ("Quaquaval", "914"),
    ("Lechonk", "915"),
    ("Oinkologne", "916"),
    ("Tarountula", "917"),
    ("Spidops", "918"),
    ("Nymble", "919"),
    ("Lokix", "920"),
    ("Pawmi", "921"),
    ("Pawmo", "922"),
    ("Pawmot", "923"),
    ("Tandemaus", "924"),
    ("Maushold", "925"),
    ("Fidough", "926"),
    ("Dachsbun", "927"),
    ("Smoliv", "928"),
    ("Dolliv", "929"),
    ("Arboliva", "930"),
    ("Squawkabilly", "931"),
    ("Nacli", "932"),
    ("Naclstack", "933"),
    ("Garganacl", "934"),
    ("Charcadet", "935"),
    ("Armarouge", "936"),
    ("Ceruledge", "937"),
    ("Tadbulb", "938"),
    ("Bellibolt", "939"),
    ("Wattrel", "940"),
    ("Kilowattrel", "941"),
    ("Maschiff", "942"),
    ("Mabosstiff", "943"),
    ("Shroodle", "944"),
    ("Grafaiai", "945"),
    ("Bramblin", "946"),
    ("Brambleghast", "947"),
    ("Toedscool", "948"),
    ("Toedscruel", "949"),
    ("Klawf", "950"),
    ("Capsakid", "951"),
    ("Scovillain", "952"),
    ("Rellor", "953"),
    ("Rabsca", "954"),
    ("Flittle", "955"),
    ("Espathra", "956"),
    ("Tinkatink", "957"),
    ("Tinkatuff", "958"),
    ("Tinkaton", "959"),
    ("Wiglett", "960"),
    ("Wugtrio", "961"),
    ("Bombirdier", "962"),
    ("Finizen", "963"),
    ("Palafin", "964"),
    ("Varoom", "965"),
    ("Revavroom", "966"),
    ("Cyclizar", "967"),
    ("Orthworm", "968"),
    ("Glimmet", "969"),
    ("Glimmora", "970"),
    ("Greavard", "971"),
    ("Houndstone", "972"),
    ("Flamigo", "973"),
    ("Cetoddle", "974"),
    ("Cetitan", "975"),
    ("Veluza", "976"),
    ("Dondozo", "977"),
    ("Tatsugiri", "978"),
    ("Annihilape", "979"),
    ("Clodsire", "980"),
    ("Farigiraf", "981"),
    ("Dudunsparce", "982"),
    ("Kingambit", "983"),
    ("Great Tusk", "984"),
    ("Scream Tail", "985"),
    ("Brute Bonnet", "986"),
    ("Flutter Mane", "987"),
    ("Slither Wing", "988"),
    ("Sandy Shocks", "989"),
    ("Iron Treads", "990"),
    ("Iron Bundle", "991"),
    ("Iron Hands", "992"),
    ("Iron Jugulis", "993"),
    ("Iron Moth", "994"),
    ("Iron Thorns", "995"),
    ("Frigibax", "996"),
    ("Arctibax", "997"),
    ("Baxcalibur", "998"),
    ("Gimmighoul", "999"),
    ("Gholdengo", "1000"),
    ("Wo-Chien", "1001"),
    ("Chien-Pao", "1002"),
    ("Ting-Lu", "1003"),
    ("Chi-Yu", "1004"),
    ("Roaring Moon", "1005"),
    ("Iron Valiant", "1006"),
    ("Koraidon", "1007"),
    ("Miraidon", "1008"),
    ("Walking Wake", "1009"),
    ("Iron Leaves", "1010"),
    ("Dipplin", "1011"),
    ("Poltchageist", "1012"),
    ("Sinistcha", "1013"),
    ("Okidogi", "1014"),
    ("Munkidori", "1015"),
    ("Fezandipiti", "1016"),
    ("Ogerpon", "1017"),
    ("Archaludon", "1018"),
    ("Hydrapple", "1019"),
    ("Gouging Fire", "1020"),
    ("Raging Bolt", "1021"),
    ("Iron Boulder", "1022"),
    ("Iron Crown", "1023"),
    ("Terapagos", "1024"),
    ("Pecharunt", "1025"),

    # Generation 9 (Paldea)
    ("Wooper (Paldea)", "194"),
    ("Quagsire (Paldea)", "195"),
    ("Tauros (Paldea)", "128"),
    ("Tauros (Paldea)", "128"),
    ("Tauros (Paldea)", "128"),
    ("Donphan (Paldea)", "232"),
    ("Sneasel (Paldea)", "215"),
    ("Zorua (Paldea)", "570"),
    ("Zoroark (Paldea)", "571")

]

def create_pokemon_card_pdf(pokemon_list):
    # Get the current working directory
    current_directory = os.getcwd()

    # Define the output file path (in the current directory)
    filename = os.path.join(current_directory, "pokemon_cards.pdf")

    # Create a canvas object for the PDF
    c = canvas.Canvas(filename, pagesize=A4)

    # Set the size of the page to A4 dimensions
    width, height = A4

    # Define margins and card spacing
    margin_x = (width - (3 * card_width)) / 4
    margin_y = (height - (3 * card_height)) / 4

    # Function to draw cards on the page
    def draw_cards(start_index):
        for index, (pokemon_name, pokemon_number) in enumerate(pokemon_list[start_index:start_index + 9]):
            # Calculate row and column based on the index
            row = index // 3
            col = index % 3

            # Calculate position for each card
            x = margin_x + col * card_width
            y = height - (margin_y + (row + 1) * card_height)

            # Draw the card rectangle
            c.setStrokeColor(colors.black)
            c.setFillColor(colors.white)
            c.rect(x, y, card_width, card_height, fill=1)

            # Draw the Pokémon name and number, centered on the card
            c.setFont("Helvetica", 10)
            c.setFillColor(colors.black)

            # Center the Pokémon name
            c.drawCentredString(x + card_width / 2, y + card_height / 2 + 10, pokemon_name)

            # Center the Pokémon number (slightly lower than the name)
            c.setFont("Helvetica", 8)  # Smaller font for the number
            c.drawCentredString(x + card_width / 2, y + card_height / 2 - 10, pokemon_number)

    # Draw cards in chunks of 9 until all Pokémon are processed
    num_cards = len(pokemon_list)
    cards_per_page = 9

    for start_index in range(0, num_cards, cards_per_page):
        # Draw cards for the current page
        draw_cards(start_index)

        # Add a new page if there are more cards to draw
        if start_index + cards_per_page < num_cards:
            c.showPage()

    # Save the PDF file to the current directory
    c.save()

# Call the function to create the PDF
create_pokemon_card_pdf(pokemon_list)