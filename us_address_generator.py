#!/usr/bin/env python3
"""US Address Generator - 随机生成逼真的美国地址信息"""

import argparse
import json
import random
import string
import sys

# ============================================================
# 数据库
# ============================================================

FIRST_NAMES_MALE = [
    "James", "Robert", "John", "Michael", "David", "William", "Richard",
    "Joseph", "Thomas", "Christopher", "Charles", "Daniel", "Matthew",
    "Anthony", "Mark", "Donald", "Steven", "Andrew", "Paul", "Joshua",
    "Kenneth", "Kevin", "Brian", "George", "Timothy", "Ronald", "Edward",
    "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas", "Eric",
    "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon",
    "Benjamin", "Samuel", "Raymond", "Gregory", "Frank", "Alexander",
    "Patrick", "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Nathan",
    "Henry", "Peter", "Adam", "Douglas", "Zachary", "Walter", "Kyle",
]

FIRST_NAMES_FEMALE = [
    "Mary", "Patricia", "Jennifer", "Linda", "Barbara", "Elizabeth",
    "Susan", "Jessica", "Sarah", "Karen", "Lisa", "Nancy", "Betty",
    "Margaret", "Sandra", "Ashley", "Dorothy", "Kimberly", "Emily",
    "Donna", "Michelle", "Carol", "Amanda", "Melissa", "Deborah",
    "Stephanie", "Rebecca", "Sharon", "Laura", "Cynthia", "Kathleen",
    "Amy", "Angela", "Shirley", "Anna", "Brenda", "Pamela", "Emma",
    "Nicole", "Helen", "Samantha", "Katherine", "Christine", "Debra",
    "Rachel", "Carolyn", "Janet", "Catherine", "Maria", "Heather",
    "Diane", "Ruth", "Julie", "Olivia", "Joyce", "Virginia", "Victoria",
    "Kelly", "Lauren", "Christina", "Joan", "Evelyn", "Judith", "Andrea",
]

FIRST_NAMES = FIRST_NAMES_MALE + FIRST_NAMES_FEMALE

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
    "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
    "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
    "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King",
    "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green",
    "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Phillips", "Evans", "Turner", "Parker", "Collins",
    "Edwards", "Stewart", "Morris", "Murphy", "Cook", "Rogers", "Morgan",
    "Peterson", "Cooper", "Reed", "Bailey", "Bell", "Gomez", "Kelly",
    "Howard", "Ward", "Cox", "Diaz", "Richardson", "Wood", "Watson",
    "Brooks", "Bennett", "Gray", "James", "Reyes", "Cruz", "Hughes",
    "Price", "Myers", "Long", "Foster", "Sanders", "Ross", "Morales",
    "Powell", "Sullivan", "Russell", "Ortiz", "Jenkins", "Gutierrez",
    "Perry", "Butler", "Barnes", "Fisher", "Henderson", "Coleman",
]

STREET_NAMES = [
    "Main", "Oak", "Maple", "Cedar", "Elm", "Pine", "Washington",
    "Lake", "Hill", "Walnut", "Spring", "Park", "Ridge", "Sunset",
    "Meadow", "Forest", "River", "Highland", "Valley", "Willow",
    "Lincoln", "Franklin", "Jefferson", "Madison", "Adams", "Jackson",
    "Church", "School", "Mill", "Prospect", "Center", "Union",
    "Liberty", "Cherry", "Birch", "Chestnut", "Dogwood", "Magnolia",
    "Laurel", "Poplar", "Spruce", "Sycamore", "Hickory", "Aspen",
    "Fairview", "Greenwood", "Lakeview", "Riverside", "Woodland",
    "Brookside", "Creekside", "Stonegate", "Windsor", "Cambridge",
    "Oxford", "Hampton", "Coventry", "Bristol", "Sheffield", "Devon",
    "Victoria", "Colonial", "Heritage", "Pioneer", "Independence",
    "Commerce", "Industrial", "Technology", "Innovation", "Discovery",
]

STREET_TYPES = [
    "St", "Ave", "Blvd", "Dr", "Ln", "Rd", "Way", "Ct", "Pl", "Cir",
    "Ter", "Pkwy", "Trl",
]

STREET_DIRECTIONS = ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]

APT_TYPES = ["Apt", "Suite", "Unit", "#"]

EMAIL_DOMAINS = [
    "gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "icloud.com",
    "aol.com", "mail.com", "protonmail.com", "zoho.com", "yandex.com",
]

# 州数据：(全称, 缩写, [城市列表], [邮编前缀], [区号列表])
STATES = {
    "AL": ("Alabama", [
        "Birmingham", "Montgomery", "Huntsville", "Mobile", "Tuscaloosa",
        "Hoover", "Dothan", "Auburn", "Decatur", "Madison",
    ], range(350, 370), ["205", "251", "256", "334", "938"]),
    "AK": ("Alaska", [
        "Anchorage", "Fairbanks", "Juneau", "Sitka", "Ketchikan",
        "Wasilla", "Kenai", "Kodiak", "Bethel", "Palmer",
    ], range(995, 1000), ["907"]),
    "AZ": ("Arizona", [
        "Phoenix", "Tucson", "Mesa", "Chandler", "Scottsdale",
        "Glendale", "Gilbert", "Tempe", "Peoria", "Surprise",
    ], range(850, 866), ["480", "520", "602", "623", "928"]),
    "AR": ("Arkansas", [
        "Little Rock", "Fort Smith", "Fayetteville", "Springdale", "Jonesboro",
        "North Little Rock", "Conway", "Rogers", "Pine Bluff", "Bentonville",
    ], range(716, 730), ["479", "501", "870"]),
    "CA": ("California", [
        "Los Angeles", "San Diego", "San Jose", "San Francisco", "Fresno",
        "Sacramento", "Long Beach", "Oakland", "Bakersfield", "Anaheim",
        "Santa Ana", "Riverside", "Stockton", "Irvine", "Chula Vista",
        "Fremont", "San Bernardino", "Modesto", "Fontana", "Moreno Valley",
        "Santa Clarita", "Glendale", "Huntington Beach", "Garden Grove",
        "Oceanside", "Rancho Cucamonga", "Ontario", "Santa Rosa", "Elk Grove",
        "Pasadena", "Hayward", "Pomona", "Escondido", "Sunnyvale", "Torrance",
    ], range(900, 962), ["209", "213", "310", "323", "408", "415", "424",
                          "510", "530", "559", "562", "619", "626", "650",
                          "657", "661", "707", "714", "747", "760", "805",
                          "818", "831", "858", "909", "916", "925", "949", "951"]),
    "CO": ("Colorado", [
        "Denver", "Colorado Springs", "Aurora", "Fort Collins", "Lakewood",
        "Thornton", "Arvada", "Westminster", "Pueblo", "Boulder",
    ], range(800, 817), ["303", "719", "720", "970"]),
    "CT": ("Connecticut", [
        "Bridgeport", "New Haven", "Stamford", "Hartford", "Waterbury",
        "Norwalk", "Danbury", "New Britain", "West Hartford", "Greenwich",
    ], range(60, 70), ["203", "475", "860", "959"]),
    "DE": ("Delaware", [
        "Wilmington", "Dover", "Newark", "Middletown", "Bear",
        "Glasgow", "Hockessin", "Brookside", "Smyrna", "Milford",
    ], range(197, 200), ["302"]),
    "FL": ("Florida", [
        "Jacksonville", "Miami", "Tampa", "Orlando", "St. Petersburg",
        "Hialeah", "Tallahassee", "Fort Lauderdale", "Port St. Lucie",
        "Cape Coral", "Pembroke Pines", "Hollywood", "Gainesville",
        "Miramar", "Coral Springs", "Clearwater", "Palm Bay", "Lakeland",
        "West Palm Beach", "Pompano Beach",
    ], range(320, 350), ["239", "305", "321", "352", "386", "407", "561",
                          "727", "754", "772", "786", "813", "850", "863",
                          "904", "941", "954"]),
    "GA": ("Georgia", [
        "Atlanta", "Augusta", "Columbus", "Macon", "Savannah",
        "Athens", "Sandy Springs", "Roswell", "Johns Creek", "Albany",
    ], range(300, 320), ["229", "404", "470", "478", "678", "706", "762", "770", "912"]),
    "HI": ("Hawaii", [
        "Honolulu", "Pearl City", "Hilo", "Kailua", "Waipahu",
        "Kaneohe", "Mililani Town", "Kahului", "Ewa Gentry", "Kihei",
    ], range(967, 969), ["808"]),
    "ID": ("Idaho", [
        "Boise", "Meridian", "Nampa", "Idaho Falls", "Caldwell",
        "Pocatello", "Coeur d'Alene", "Twin Falls", "Lewiston", "Post Falls",
    ], range(832, 839), ["208", "986"]),
    "IL": ("Illinois", [
        "Chicago", "Aurora", "Naperville", "Joliet", "Rockford",
        "Springfield", "Elgin", "Peoria", "Champaign", "Waukegan",
    ], range(600, 630), ["217", "224", "309", "312", "331", "618", "630",
                          "708", "773", "779", "815", "847", "872"]),
    "IN": ("Indiana", [
        "Indianapolis", "Fort Wayne", "Evansville", "South Bend", "Carmel",
        "Fishers", "Bloomington", "Hammond", "Gary", "Lafayette",
    ], range(460, 480), ["219", "260", "317", "463", "574", "765", "812", "930"]),
    "IA": ("Iowa", [
        "Des Moines", "Cedar Rapids", "Davenport", "Sioux City", "Iowa City",
        "Waterloo", "Council Bluffs", "Ames", "Dubuque", "West Des Moines",
    ], range(500, 529), ["319", "515", "563", "641", "712"]),
    "KS": ("Kansas", [
        "Wichita", "Overland Park", "Kansas City", "Olathe", "Topeka",
        "Lawrence", "Shawnee", "Manhattan", "Lenexa", "Salina",
    ], range(660, 680), ["316", "620", "785", "913"]),
    "KY": ("Kentucky", [
        "Louisville", "Lexington", "Bowling Green", "Owensboro", "Covington",
        "Richmond", "Georgetown", "Florence", "Hopkinsville", "Nicholasville",
    ], range(400, 428), ["270", "364", "502", "606", "859"]),
    "LA": ("Louisiana", [
        "New Orleans", "Baton Rouge", "Shreveport", "Lafayette", "Lake Charles",
        "Kenner", "Bossier City", "Monroe", "Alexandria", "Houma",
    ], range(700, 715), ["225", "318", "337", "504", "985"]),
    "ME": ("Maine", [
        "Portland", "Lewiston", "Bangor", "South Portland", "Auburn",
        "Biddeford", "Sanford", "Brunswick", "Augusta", "Scarborough",
    ], range(39, 50), ["207"]),
    "MD": ("Maryland", [
        "Baltimore", "Columbia", "Germantown", "Silver Spring", "Waldorf",
        "Glen Burnie", "Frederick", "Ellicott City", "Dundalk", "Rockville",
    ], range(206, 219), ["240", "301", "410", "443", "667"]),
    "MA": ("Massachusetts", [
        "Boston", "Worcester", "Springfield", "Lowell", "Cambridge",
        "New Bedford", "Brockton", "Quincy", "Lynn", "Fall River",
    ], range(10, 28), ["339", "351", "413", "508", "617", "774", "781", "857", "978"]),
    "MI": ("Michigan", [
        "Detroit", "Grand Rapids", "Warren", "Sterling Heights", "Ann Arbor",
        "Lansing", "Flint", "Dearborn", "Livonia", "Troy",
    ], range(480, 500), ["231", "248", "269", "313", "517", "586", "616", "734", "810", "906", "947", "989"]),
    "MN": ("Minnesota", [
        "Minneapolis", "St. Paul", "Rochester", "Duluth", "Bloomington",
        "Brooklyn Park", "Plymouth", "St. Cloud", "Eagan", "Woodbury",
    ], range(550, 568), ["218", "320", "507", "612", "651", "763", "952"]),
    "MS": ("Mississippi", [
        "Jackson", "Gulfport", "Southaven", "Hattiesburg", "Biloxi",
        "Meridian", "Tupelo", "Olive Branch", "Greenville", "Horn Lake",
    ], range(386, 398), ["228", "601", "662", "769"]),
    "MO": ("Missouri", [
        "Kansas City", "St. Louis", "Springfield", "Columbia", "Independence",
        "Lee's Summit", "O'Fallon", "St. Joseph", "St. Charles", "Blue Springs",
    ], range(630, 659), ["314", "417", "573", "636", "660", "816"]),
    "MT": ("Montana", [
        "Billings", "Missoula", "Great Falls", "Bozeman", "Butte",
        "Helena", "Kalispell", "Havre", "Anaconda", "Miles City",
    ], range(590, 600), ["406"]),
    "NE": ("Nebraska", [
        "Omaha", "Lincoln", "Bellevue", "Grand Island", "Kearney",
        "Fremont", "Hastings", "Norfolk", "North Platte", "Columbus",
    ], range(680, 694), ["308", "402", "531"]),
    "NV": ("Nevada", [
        "Las Vegas", "Henderson", "Reno", "North Las Vegas", "Sparks",
        "Carson City", "Fernley", "Elko", "Mesquite", "Boulder City",
    ], range(889, 899), ["702", "725", "775"]),
    "NH": ("New Hampshire", [
        "Manchester", "Nashua", "Concord", "Derry", "Dover",
        "Rochester", "Salem", "Merrimack", "Hudson", "Londonderry",
    ], range(30, 39), ["603"]),
    "NJ": ("New Jersey", [
        "Newark", "Jersey City", "Paterson", "Elizabeth", "Edison",
        "Woodbridge", "Lakewood", "Toms River", "Hamilton", "Trenton",
    ], range(70, 90), ["201", "551", "609", "732", "848", "856", "862", "908", "973"]),
    "NM": ("New Mexico", [
        "Albuquerque", "Las Cruces", "Rio Rancho", "Santa Fe", "Roswell",
        "Farmington", "Clovis", "Hobbs", "Alamogordo", "Carlsbad",
    ], range(870, 885), ["505", "575"]),
    "NY": ("New York", [
        "New York", "Buffalo", "Rochester", "Yonkers", "Syracuse",
        "Albany", "New Rochelle", "Mount Vernon", "Schenectady", "Utica",
        "White Plains", "Hempstead", "Troy", "Niagara Falls", "Binghamton",
    ], range(100, 150), ["212", "315", "347", "516", "518", "585", "607",
                          "631", "646", "716", "718", "845", "914", "917", "929"]),
    "NC": ("North Carolina", [
        "Charlotte", "Raleigh", "Greensboro", "Durham", "Winston-Salem",
        "Fayetteville", "Cary", "Wilmington", "High Point", "Concord",
    ], range(270, 290), ["252", "336", "704", "743", "828", "910", "919", "980", "984"]),
    "ND": ("North Dakota", [
        "Fargo", "Bismarck", "Grand Forks", "Minot", "West Fargo",
        "Williston", "Dickinson", "Mandan", "Jamestown", "Wahpeton",
    ], range(580, 589), ["701"]),
    "OH": ("Ohio", [
        "Columbus", "Cleveland", "Cincinnati", "Toledo", "Akron",
        "Dayton", "Parma", "Canton", "Youngstown", "Lorain",
    ], range(430, 459), ["216", "220", "234", "330", "380", "419", "440",
                          "513", "567", "614", "740", "937"]),
    "OK": ("Oklahoma", [
        "Oklahoma City", "Tulsa", "Norman", "Broken Arrow", "Edmond",
        "Lawton", "Moore", "Midwest City", "Enid", "Stillwater",
    ], range(730, 750), ["405", "539", "580", "918"]),
    "OR": ("Oregon", [
        "Portland", "Salem", "Eugene", "Gresham", "Hillsboro",
        "Beaverton", "Bend", "Medford", "Springfield", "Corvallis",
    ], range(970, 980), ["458", "503", "541", "971"]),
    "PA": ("Pennsylvania", [
        "Philadelphia", "Pittsburgh", "Allentown", "Reading", "Erie",
        "Bethlehem", "Scranton", "Lancaster", "Harrisburg", "York",
    ], range(150, 197), ["215", "223", "267", "272", "412", "484", "570",
                          "610", "717", "724", "814", "878"]),
    "RI": ("Rhode Island", [
        "Providence", "Warwick", "Cranston", "Pawtucket", "East Providence",
        "Woonsocket", "Newport", "Central Falls", "Westerly", "North Providence",
    ], range(28, 30), ["401"]),
    "SC": ("South Carolina", [
        "Charleston", "Columbia", "North Charleston", "Mount Pleasant", "Rock Hill",
        "Greenville", "Summerville", "Goose Creek", "Hilton Head Island", "Florence",
    ], range(290, 300), ["803", "843", "854", "864"]),
    "SD": ("South Dakota", [
        "Sioux Falls", "Rapid City", "Aberdeen", "Brookings", "Watertown",
        "Mitchell", "Yankton", "Pierre", "Huron", "Vermillion",
    ], range(570, 578), ["605"]),
    "TN": ("Tennessee", [
        "Nashville", "Memphis", "Knoxville", "Chattanooga", "Clarksville",
        "Murfreesboro", "Franklin", "Jackson", "Johnson City", "Bartlett",
    ], range(370, 386), ["423", "615", "629", "731", "865", "901", "931"]),
    "TX": ("Texas", [
        "Houston", "San Antonio", "Dallas", "Austin", "Fort Worth",
        "El Paso", "Arlington", "Corpus Christi", "Plano", "Laredo",
        "Lubbock", "Garland", "Irving", "Amarillo", "Grand Prairie",
        "Brownsville", "McKinney", "Frisco", "Pasadena", "Killeen",
    ], range(750, 800), ["210", "214", "254", "281", "325", "346", "361",
                          "409", "430", "432", "469", "512", "682", "713",
                          "726", "737", "806", "817", "830", "832", "903",
                          "915", "936", "940", "956", "972", "979"]),
    "UT": ("Utah", [
        "Salt Lake City", "West Valley City", "Provo", "West Jordan", "Orem",
        "Sandy", "Ogden", "St. George", "Layton", "Taylorsville",
    ], range(840, 848), ["385", "435", "801"]),
    "VT": ("Vermont", [
        "Burlington", "South Burlington", "Rutland", "Barre", "Montpelier",
        "Winooski", "St. Albans", "Newport", "Vergennes", "Bennington",
    ], range(50, 60), ["802"]),
    "VA": ("Virginia", [
        "Virginia Beach", "Norfolk", "Chesapeake", "Richmond", "Newport News",
        "Alexandria", "Hampton", "Roanoke", "Portsmouth", "Suffolk",
    ], range(220, 247), ["276", "434", "540", "571", "703", "757", "804"]),
    "WA": ("Washington", [
        "Seattle", "Spokane", "Tacoma", "Vancouver", "Bellevue",
        "Kent", "Everett", "Renton", "Spokane Valley", "Federal Way",
    ], range(980, 995), ["206", "253", "360", "425", "509", "564"]),
    "WV": ("West Virginia", [
        "Charleston", "Huntington", "Morgantown", "Parkersburg", "Wheeling",
        "Weirton", "Fairmont", "Martinsburg", "Beckley", "Clarksburg",
    ], range(247, 269), ["304", "681"]),
    "WI": ("Wisconsin", [
        "Milwaukee", "Madison", "Green Bay", "Kenosha", "Racine",
        "Appleton", "Waukesha", "Oshkosh", "Eau Claire", "Janesville",
    ], range(530, 550), ["262", "414", "534", "608", "715", "920"]),
    "WY": ("Wyoming", [
        "Cheyenne", "Casper", "Laramie", "Gillette", "Rock Springs",
        "Sheridan", "Green River", "Evanston", "Riverton", "Jackson",
    ], range(820, 832), ["307"]),
    "DC": ("District of Columbia", [
        "Washington",
    ], range(200, 206), ["202"]),
}

# 默认免税州
TAX_FREE_STATES = ["OR", "MT", "NH", "DE", "AK"]


# ============================================================
# 生成函数
# ============================================================

def generate_address(state_code=None):
    """生成一个完整的美国地址"""
    # 选择州
    if state_code:
        code = state_code.upper()
        if code not in STATES:
            print(f"Error: Unknown state code '{state_code}'. Use two-letter abbreviation (e.g., CA, NY).", file=sys.stderr)
            sys.exit(1)
    else:
        code = random.choice(TAX_FREE_STATES)

    state_name, cities, zip_prefixes, area_codes = STATES[code]

    # 姓名
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)

    # 街道地址
    house_number = random.randint(1, 19999)
    street_name = random.choice(STREET_NAMES)
    street_type = random.choice(STREET_TYPES)
    # 30% 概率加方向前缀
    if random.random() < 0.3:
        direction = random.choice(STREET_DIRECTIONS)
        street = f"{house_number} {direction} {street_name} {street_type}"
    else:
        street = f"{house_number} {street_name} {street_type}"

    # 公寓号（25% 概率）
    apt = ""
    if random.random() < 0.25:
        apt_type = random.choice(APT_TYPES)
        # 不同格式的门牌号
        fmt = random.choice(["num", "letter_num", "num_letter"])
        if fmt == "num":
            apt_num = str(random.randint(1, 999))
        elif fmt == "letter_num":
            apt_num = random.choice(string.ascii_uppercase) + str(random.randint(1, 99))
        else:
            apt_num = str(random.randint(1, 30)) + random.choice(string.ascii_uppercase)
        apt = f"{apt_type} {apt_num}"

    # 城市
    city = random.choice(cities)

    # 邮编（5 位）
    zip_prefix = random.choice(list(zip_prefixes))
    zip_code = f"{zip_prefix:03d}{random.randint(0, 99):02d}"
    # 确保恰好 5 位
    zip_code = zip_code[:5].zfill(5)

    # 电话
    area_code = random.choice(area_codes)
    phone = f"({area_code}) {random.randint(200, 999):03d}-{random.randint(0, 9999):04d}"

    # 邮箱
    email = _generate_email(first_name, last_name)

    return {
        "first_name": first_name,
        "last_name": last_name,
        "street": street,
        "apt": apt,
        "city": city,
        "state": code,
        "zip": zip_code,
        "phone": phone,
        "email": email,
    }


def _generate_email(first_name, last_name):
    """基于姓名生成邮箱地址"""
    first = first_name.lower()
    last = last_name.lower()
    domain = random.choice(EMAIL_DOMAINS)

    patterns = [
        f"{first}.{last}",
        f"{first}{last}",
        f"{first}_{last}",
        f"{first[0]}{last}",
        f"{first}.{last[0]}",
        f"{first}{random.randint(1, 99)}",
        f"{first}.{last}{random.randint(1, 999)}",
        f"{first[0]}.{last}{random.randint(1, 99)}",
    ]
    return f"{random.choice(patterns)}@{domain}"


# ============================================================
# 输出格式化
# ============================================================

def format_text(addr):
    """文本格式输出"""
    lines = [
        f"{addr['first_name']} {addr['last_name']}",
    ]
    street_line = addr["street"]
    if addr["apt"]:
        street_line += f", {addr['apt']}"
    lines.append(street_line)
    lines.append(f"{addr['city']}, {addr['state']} {addr['zip']}")
    lines.append(f"Phone: {addr['phone']}")
    lines.append(f"Email: {addr['email']}")
    return "\n".join(lines)


def format_json(addresses):
    """JSON 格式输出"""
    if len(addresses) == 1:
        return json.dumps(addresses[0], indent=2, ensure_ascii=False)
    return json.dumps(addresses, indent=2, ensure_ascii=False)


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="US Address Generator - 随机生成逼真的美国地址信息",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
examples:
  %(prog)s                  生成 1 个免税州地址
  %(prog)s -n 5             生成 5 个免税州地址
  %(prog)s -s CA            生成 1 个加州地址
  %(prog)s -n 3 -f json     生成 3 个地址，JSON 格式输出
  %(prog)s -n 2 -s NY -f json
""",
    )
    parser.add_argument(
        "-n", "--count", type=int, default=1,
        help="生成数量（默认 1）",
    )
    parser.add_argument(
        "-s", "--state", type=str, default=None,
        help="指定州缩写（如 CA、NY），不指定则从免税州随机选取",
    )
    parser.add_argument(
        "-f", "--format", type=str, choices=["text", "json"], default="text",
        help="输出格式：text（默认）或 json",
    )
    args = parser.parse_args()

    if args.count < 1:
        print("Error: --count must be at least 1.", file=sys.stderr)
        sys.exit(1)

    addresses = [generate_address(args.state) for _ in range(args.count)]

    if args.format == "json":
        print(format_json(addresses))
    else:
        for i, addr in enumerate(addresses):
            if i > 0:
                print()  # 地址之间空行分隔
            print(format_text(addr))


if __name__ == "__main__":
    main()
