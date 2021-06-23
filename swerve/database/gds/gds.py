import os
from Hulkster.swerve.core import swerveos, logger
from Hulkster.swerve.database import swervedb


"""
GDS class
"""


class GDS:
    # Human readable list
    data = []
    # Actual File List
    files = []
    # Provided for potential filtering
    mods = []
    saves = []

    def __init__(self):
        self.setup()

    def setup(self):
        """ List available files in arrays """
        list_ = ["C:\\Program Files (x86)\\GDS\\TEW2013", "C:\\Program Files (x86)\\GDS\\TEW2016",
                 "C:\\Program Files (x86)\\GDS\\TEW2020"]
        # Unsupported:
        # list_.append("C:\\Program Files (x86)\\GDS\\TEW2013")
        # list_.append("C:\\Program Files (x86)\\GDS\\TEW2016")
        # list_.append("C:\\Program Files (x86)\\GDS\\TEW2020")
        # list_.append("C:\\Program Files (x86)\\GDS\\WMMA4")
        # list_.append("C:\\Program Files (x86)\\GDS\\WMMA5")
        # list_.append("C:\\Program Files (x86)\\GDS\\WreSpi3")
        for path in list_:
            game = swerveos.filename(path, False)
            directory = path + "\\Databases"
            if os.path.exists(directory):
                for databases in os.listdir(path=directory):
                    moddir = directory + "\\" + databases + "\\SaveGames"
                    moddb = directory + "\\" + databases + "\\" + game + ".mdb"
                    # Only bother to look for save game mdbs
                    # if there is a mod mdb
                    if os.path.exists(moddb):
                        self.files.append(moddb)
                        self.mods.append(moddb)
                        description = databases + " (Mod)"
                        self.data.append(description)
                        for savegames in os.listdir(path=moddir):
                            save = moddir + "\\" + savegames + "\\" + game + ".mdb"
                            if os.path.exists(save):
                                self.files.append(save)
                                self.saves.append(save)
                                description = savegames + " (Save, " + databases + " Mod)"
                                self.data.append(description)


def get_extraction_tables(version):
    tew = swervedb.get()
    if tew is None:
        Logger.info("GDS", "Tried to get Database but it is null")
    tables = []
    versions = [13, 16, 20]
    if version not in versions:
        Logger.info("GDS", "Tried to get Extraction tables with invalid version")
        return tables
    tables.append("tblBelt")
    tables.append("tblCard")
    tables.append("tblContract")
    tables.append("tblFed")
    tables.append("tblGimmick")
    tables.append("tblInfo")
    tables.append("tblStable")
    tables.append("tblStableMember")
    tables.append("tblTeam")
    tables.append("tblTV")
    tables.append("tblWorker")
    tables.append("tblWorkerBusiness")
    tables.append("tblWorkerOver")
    tables.append("tblWorkerPerformance")
    if version == 20:
        tables.append("tblWorkerPersonality")
    tables.append("tblWorkerSkill")
    return tables


def get_import_schema():
    schema = []
    schema.append("CREATE TABLE IF NOT EXISTS imported_Belt( UID INTEGER UNIQUE ON CONFLICT ABORT, Name TEXT, Picture TEXT, Fed INTEGER, AllianceUID INTEGER, Profile INTEGER, Style INTEGER, BeltLevel INTEGER, Prestige INTEGER, Function INTEGER, Active BOOLEAN, Gender INTEGER, Minimum_Weight INTEGER, Maximum_Weight INTEGER, Brand INTEGER, Holder1 INTEGER, Holder2 INTEGER, Holder3 INTEGER, Defences INTEGER, Reign INTEGER, CapturedD INTEGER, CapturedW INTEGER, CapturedM INTEGER, CapturedY INTEGER, LastDefenceD INTEGER, LastDefenceW INTEGER, LastDefenceM INTEGER, LastDefenceY INTEGER, Tournament BOOLEAN, TournamentMonth INTEGER, DoneThisYear BOOLEAN, Event_Frequency INTEGER, Tour_Frequency INTEGER, TV_Frequency INTEGER, LastContender1 INTEGER, LastContender2 INTEGER, LastContender3 INTEGER, OriginalFed INTEGER, AnnualTitle INTEGER, CardUID INTEGER, RetainTitle INTEGER, Achievement INTEGER, AnnualType INTEGER, ValidMatches INTEGER, PrevMatch1 INTEGER, PrevMatch2 INTEGER);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_Card( UID INTEGER UNIQUE ON CONFLICT ABORT, Name TEXT, Fed INTEGER, Logo TEXT, Length INTEGER, Schedule INTEGER, Showday INTEGER, Showweek INTEGER, Showmonth INTEGER, Brand INTEGER, Importance INTEGER, Postfix INTEGER, Numerals BOOLEAN, Dormant BOOLEAN, Instructions INTEGER, Music INTEGER, Celebs INTEGER, SpecialSet INTEGER, Finale BOOLEAN, DateSort TEXT, Location INTEGER, Venue INTEGER,ShowIntent INTEGER,Ticket INTEGER,WakeM INTEGER,WakeY INTEGER,SleepM INTEGER,SleepY INTEGER);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_Contract( UID INTEGER UNIQUE ON CONFLICT ABORT, FedUID INTEGER, ParentFedUID INTEGER, WorkerUID INTEGER, Name TEXT, Shortname TEXT, Picture TEXT, Perception INTEGER, PerceptionScore INTEGER, Face INTEGER, Division INTEGER, Turn_Change INTEGER, Manager INTEGER, Male INTEGER, Moveset INTEGER, WrittenContract INTEGER, ExclusiveContract INTEGER, PaidMonthly INTEGER, OnLoan INTEGER, Developmental INTEGER, PrimaryUsage INTEGER, SecondaryUsage INTEGER, ExpectedShows INTEGER, BonusAmount INTEGER, BonusType INTEGER, Creative INTEGER, HiringVeto INTEGER, WageMatch INTEGER, IronClad INTEGER, SittingOut INTEGER, BeganMonth INTEGER, BeganYear INTEGER, Length INTEGER, Daysleft INTEGER, Dateslength INTEGER, DatesLeft INTEGER, StartsIn INTEGER, DebutedMonth INTEGER, DebutedYear INTEGER, LastSeenDay INTEGER, LastSeenWeek INTEGER, LastSeenMonth INTEGER, LastSeenYear INTEGER, Amount INTEGER, Downside INTEGER, Monthly_Earn INTEGER, Leaving INTEGER, Brand INTEGER, TonightFed INTEGER, WorkedTonight INTEGER, Away INTEGER, Last_Gimmick INTEGER, Last_Turn INTEGER, Workedthismonth INTEGER, Mask INTEGER, ShowsUnused INTEGER, ContractMomentum INTEGER, Shorty INTEGER, Travel INTEGER, TravelPaid INTEGER, OneNightOnly INTEGER, AllianceSpecial INTEGER, HouseShows INTEGER, AIElsewhere INTEGER, DevCallUp INTEGER, DevRelease INTEGER, Position_Wrestler INTEGER, Position_Occasional INTEGER, Position_Referee INTEGER, Position_Announcer INTEGER, Position_Colour INTEGER, Position_Manager INTEGER, Position_Personality INTEGER, Position_Roadagent INTEGER, Excursion INTEGER, Merch INTEGER, BookA INTEGER, BookB INTEGER, BookC INTEGER, DetroitRockCity INTEGER, PlasterCaster_Gimmick INTEGER, PlasterCaster_Rating INTEGER, PlasterCaster_Lower INTEGER, PlasterCaster_Upper INTEGER, PlasterCaster_Lifespan INTEGER, PlasterCaster_Tweaks INTEGER, PlasterCaster_Tweaked INTEGER, PlasterCaster_Byte1 INTEGER, PlasterCaster_Byte2 INTEGER, PlasterCaster_Byte3 INTEGER, PlasterCaster_Byte4 INTEGER, PlasterCaster_Byte5 INTEGER, PlasterCaster_Byte6 INTEGER, PlasterCaster_Bool1 INTEGER, PlasterCaster_Bool2 INTEGER, PlasterCaster_Bool3 INTEGER, PlasterCaster_Bool4 INTEGER, PlasterCaster_Bool5 INTEGER, PlasterCaster_Bool6 INTEGER, PlasterCaster_Bool7 INTEGER, PlasterCaster_Bool8 INTEGER, PlasterCaster_Bool9 INTEGER, PlasterCaster_Bool10 INTEGER, PlasterCaster_Bool11 INTEGER, PlasterCaster_Bool12 INTEGER, PlasterCaster_Bool13 INTEGER, PlasterCaster_Bool14 INTEGER, PlasterCaster_Bool15 INTEGER, PlasterCaster_Bool16 INTEGER, PlasterCaster_Bool17 INTEGER, PlasterCaster_Bool18 INTEGER, PlasterCaster_Bool19 INTEGER, PlasterCaster_Bool20 INTEGER, PlasterCaster_Bool21 INTEGER, PlasterCaster_Bool22 INTEGER, PlasterCaster_Bool23 INTEGER, PlasterCaster_Bool24 INTEGER, PlasterCaster_Bool25 INTEGER, DrugTested INTEGER, Push INTEGER, StickyPush INTEGER, Gimmick INTEGER, Gimmick_Rating INTEGER, Gimmick_Lower INTEGER, Gimmick_Upper INTEGER, Gimmick_Lifespan INTEGER, Gimmick_Tweaks INTEGER, Gimmick_Tweaked INTEGER, Gimmick_Change INTEGER, Gimmick_Unsuited INTEGER, Type INTEGER, PushControl INTEGER, NonCompete INTEGER, Status INTEGER, Yearscompleted INTEGER, PreTonight INTEGER, Tonight INTEGER, ProperTonight INTEGER, Development INTEGER, Stigma INTEGER);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_Fed( UID INTEGER UNIQUE ON CONFLICT ABORT, Name TEXT, Initials TEXT, URL TEXT, ClosedMonth INTEGER, ClosedYear INTEGER, Trading BOOLEAN, Mediagroup INTEGER, Strategy INTEGER, Logo TEXT, Banner TEXT, Based_In INTEGER, Prestige INTEGER, Influence INTEGER, User_Controlled INTEGER, Lockerroom INTEGER, SecretNumber INTEGER, OpenMonth INTEGER, OpenYear INTEGER, Money INTEGER, Bank_Warning INTEGER, Parent_Warning INTEGER, Size INTEGER, LimitSize INTEGER, SizeChange INTEGER, RiseGrace INTEGER, BattleImmunity INTEGER, Ranking INTEGER, RankingRating INTEGER, BlockChange INTEGER, BattleQuality INTEGER, Momentum INTEGER, Announce1 INTEGER, Announce2 INTEGER, Announce3 INTEGER, UnbeatableSQ INTEGER, TonightLocation INTEGER, TonightLocationUsed INTEGER, KittyPryde INTEGER, LoanTurn INTEGER, SleazeD INTEGER, SleazeW INTEGER, SleazeM INTEGER, SleazeY INTEGER, FixBelts INTEGER, NotBefore INTEGER, NotAfter INTEGER, AlliancePreset INTEGER, Ace INTEGER, AceRating INTEGER, AceLength INTEGER, AceCheckedToday INTEGER, AceLastApp INTEGER, TVFirst INTEGER, TVAsc INTEGER, EventASC INTEGER, HouseSmartBooking INTEGER, House11 INTEGER, House12 INTEGER, House13 INTEGER, House14 INTEGER, House15 INTEGER, House16 INTEGER, House17 INTEGER, House21 INTEGER, House22 INTEGER, House23 INTEGER, House24 INTEGER, House25 INTEGER, House26 INTEGER, House27 INTEGER, House31 INTEGER, House32 INTEGER, House33 INTEGER, House34 INTEGER, House35 INTEGER, House36 INTEGER, House37 INTEGER, House41 INTEGER, House42 INTEGER, House43 INTEGER, House44 INTEGER, House45 INTEGER, House46 INTEGER, House47 INTEGER, TicketEvent INTEGER, TicketTV INTEGER, TicketHouse INTEGER, DoPerceptions INTEGER, NextFirings INTEGER, NextDraft INTEGER, TrueBorn INTEGER, TippyToe INTEGER, YoungLion INTEGER, HomeArena INTEGER, DeckCleanse INTEGER, PaulStanley INTEGER, Lackofaces INTEGER, NextHouseShow INTEGER, Touring INTEGER, Shows_Per_Week INTEGER, Touring_Month1 INTEGER, Touring_Month2 INTEGER, Touring_Month3 INTEGER, Touring_Month4 INTEGER, Touring_Month5 INTEGER, Touring_Month6 INTEGER, Touring_Month7 INTEGER, Touring_Month8 INTEGER, Touring_Month9 INTEGER, Touring_Month10 INTEGER, Touring_Month11 INTEGER, Touring_Month12 INTEGER, TourName TEXT, PrevTourName TEXT);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_Gimmick( UID INTEGER UNIQUE ON CONFLICT ABORT, Name TEXT, Profile TEXT, FaceGimmick BOOLEAN, HeelGimmick BOOLEAN, GimmickBasis INTEGER, Generic BOOLEAN, Risk INTEGER, Subtlety INTEGER, Difficulty INTEGER, Minimum_Weight INTEGER, Maximum_Weight INTEGER, Air INTEGER, Technique INTEGER, Power INTEGER, Athletic INTEGER, Psych INTEGER, Sell INTEGER, Selling INTEGER, Charisma INTEGER, Mic INTEGER, Microphone INTEGER, Menace INTEGER, Looks INTEGER, Act INTEGER, Max_Air INTEGER, Max_Technique INTEGER, Max_Power INTEGER, Max_Athletic INTEGER, Max_Psych INTEGER, Max_Sell INTEGER, Max_Charisma INTEGER, Max_Mic INTEGER, Max_Menace INTEGER, Max_Looks INTEGER, Max_Act INTEGER, Age INTEGER, Gender INTEGER, Race1 BOOLEAN, Race2 BOOLEAN, Race3 BOOLEAN, Race4 BOOLEAN, Race5 BOOLEAN, Race6 BOOLEAN, Race7 BOOLEAN, Race8 BOOLEAN, Race9 BOOLEAN,Shape1 INTEGER, Shape2 INTEGER, Shape3 INTEGER, Shape4 INTEGER, Shape5 INTEGER, Shape6 INTEGER, Shape7 INTEGER, Shape8 INTEGER);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_Info( Title TEXT, PicDir TEXT, InfoVersion TEXT, Author TEXT, Description TEXT, Whiteboard TEXT, StartYear INTEGER, StartMonth INTEGER, Restrictions INTEGER, StartVariance BOOLEAN, Economy1 INTEGER, Economy2 INTEGER, Economy3 INTEGER, Economy4 INTEGER, Economy5 INTEGER, Economy6 INTEGER, Economy7 INTEGER, Economy8 INTEGER, Industry1 INTEGER, Industry2 INTEGER, Industry3 INTEGER, Industry4 INTEGER, Industry5 INTEGER, Industry6 INTEGER, Industry7 INTEGER, Industry8 INTEGER, Loyalty1 INTEGER, Loyalty2 INTEGER, Loyalty3 INTEGER, Loyalty4 INTEGER, Loyalty5 INTEGER, Loyalty6 INTEGER, Loyalty7 INTEGER, YoungLion1 INTEGER, YoungLion2 INTEGER, YoungLion3 INTEGER, YoungLion4 INTEGER, YoungLion5 INTEGER, YoungLion6 INTEGER, YoungLion7 INTEGER, NewGenYear INTEGER, NewGenMonth INTEGER, TV_Rating_Unit INTEGER, PPV_Rating_Unit INTEGER, OrganicFed BOOLEAN, USAActive BOOLEAN, CanadaActive BOOLEAN, MexicoActive BOOLEAN, UKActive BOOLEAN, JapanActive BOOLEAN, EuropeActive BOOLEAN, OzActive BOOLEAN, IndiaActive BOOLEAN);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_Stable( UID INTEGER UNIQUE ON CONFLICT ABORT, Name TEXT, Profile TEXT, Fed INTEGER, Type INTEGER, Formed TEXT, Logo TEXT, Min INTEGER, Max INTEGER, FocalPoint INTEGER, Dispo INTEGER, Gender INTEGER, Active INTEGER, Closed INTEGER, Important INTEGER, Member1 INTEGER, Role1 INTEGER, Member2 INTEGER, Role2 INTEGER, Member3 INTEGER, Role3 INTEGER, Member4 INTEGER, Role4 INTEGER, Member5 INTEGER, Role5 INTEGER, Member6 INTEGER, Role6 INTEGER, Member7 INTEGER, Role7 INTEGER, Member8 INTEGER, Role8 INTEGER, Member9 INTEGER, Role9 INTEGER, Member10 INTEGER, Role10 INTEGER, Member11 INTEGER, Role11 INTEGER, Member12 INTEGER, Role12 INTEGER, Member13 INTEGER, Role13 INTEGER, Member14 INTEGER, Role14 INTEGER, Member15 INTEGER, Role15 INTEGER, Member16 INTEGER, Role16 INTEGER, Member17 INTEGER, Role17 INTEGER, Member18 INTEGER, Role18 INTEGER, Checked INTEGER);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_StableMember( UID INTEGER UNIQUE ON CONFLICT ABORT, StableUID INTEGER, Worker INTEGER, Role BOOLEAN);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_Team( UID INTEGER UNIQUE ON CONFLICT ABORT, Recordname TEXT, Name TEXT, Fed INTEGER, Worker1 INTEGER, Worker2 INTEGER, Type INTEGER, Experience INTEGER, Formed TEXT, Finisher TEXT, Active BOOLEAN);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_TV( UID INTEGER UNIQUE ON CONFLICT ABORT, Name TEXT, Logo TEXT, Fed INTEGER, Prestige INTEGER, B_Show BOOLEAN, Length INTEGER, Brand INTEGER, Showday INTEGER, OnAirAtMo BOOLEAN, Announcer1 INTEGER, Announcer2 INTEGER, Announcer3 INTEGER, ToCheck BOOLEAN, Dormant BOOLEAN, TapedFor INTEGER, TapeBlock INTEGER, Numbering INTEGER);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_Worker( UID INTEGER UNIQUE ON CONFLICT ABORT, User BOOLEAN, Regen INTEGER, Active BOOLEAN, Name TEXT, Shortname TEXT, Male BOOLEAN, Sexuality INTEGER, Outsiderel INTEGER, Outsiderel_Counter INTEGER, Birth_Month INTEGER, Birth_Year INTEGER, BodyType INTEGER, Size INTEGER, MinSize INTEGER, MaxSize INTEGER, Picture TEXT, Nationality INTEGER, Race INTEGER, Based_In INTEGER, Real_Based_In INTEGER, LeftBusiness INTEGER, Dead INTEGER, Retired INTEGER, NonWrestler INTEGER, Style INTEGER, Freelance INTEGER, Loyalty INTEGER, TrueBorn INTEGER, USA INTEGER, Canada INTEGER, Mexico INTEGER, Japan INTEGER, UK INTEGER, Europe INTEGER, Oz INTEGER, India INTEGER, Speak_English INTEGER, Speak_Japanese INTEGER, Speak_Spanish INTEGER, Speak_French INTEGER, Speak_Central INTEGER, Speak_Med INTEGER, Speak_Scand INTEGER, Speak_Eastern INTEGER, Speak_Hindi INTEGER, Lastworked INTEGER, Retiring INTEGER, Moveset INTEGER, Position_Wrestler INTEGER, Position_Occasional INTEGER, Position_Referee INTEGER, Position_Announcer INTEGER, Position_Colour INTEGER, Position_Manager INTEGER, Position_Personality INTEGER, Position_Roadagent INTEGER, Locationlastnight INTEGER, Mask INTEGER, SecretNumber INTEGER, Debut_Month INTEGER, Debut_Year INTEGER, Age_Matures INTEGER, Age_Declines INTEGER, Age_TalkDeclines INTEGER, Age_Retires INTEGER, OrganicBio INTEGER, UpdateBio INTEGER, MMASecretNumber INTEGER, Hirable INTEGER, WarnCount INTEGER, PlasterCaster_Face INTEGER, PlasterCaster_FaceBasis INTEGER, PlasterCaster_Heel INTEGER, PlasterCaster_HeelBasis INTEGER, Status INTEGER, Maximum_Over INTEGER, Pos_Wrestler INTEGER, Pos_Occasional INTEGER, Pos_Referee INTEGER, Pos_Announcer INTEGER, Pos_Colour INTEGER, Pos_Manager INTEGER, Pos_Personality INTEGER, Pos_Roadagent INTEGER, Gimmick_Face INTEGER, Gimmick_Heel INTEGER, MovieStar INTEGER, Music INTEGER, MMA INTEGER);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_WorkerBusiness( WorkerUID INTEGER UNIQUE ON CONFLICT ABORT, Business INTEGER, Business_Size INTEGER, Business_Pacts INTEGER, Business_Patience INTEGER, Business_Turnover INTEGER, Business_Finance INTEGER, Business_Preference INTEGER, Booking_Reputation INTEGER, Booking_Skill INTEGER, Booking_Hiring INTEGER, Booking_Favours INTEGER, Booking_Firing INTEGER, Booking_Reigns INTEGER, Booking_Titles INTEGER, OwnerMin INTEGER, OwnerMax INTEGER, Wealth INTEGER, Favour INTEGER, OwnerMinAge INTEGER, BookerMinAge INTEGER);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_WorkerOver( WorkerUID INTEGER UNIQUE ON CONFLICT ABORT, Over1 INTEGER, Over2 INTEGER, Over3 INTEGER, Over4 INTEGER, Over5 INTEGER, Over6 INTEGER, Over7 INTEGER, Over8 INTEGER, Over9 INTEGER, Over10 INTEGER, Over11 INTEGER, Over12 INTEGER, Over13 INTEGER, Over14 INTEGER, Over15 INTEGER, Over16 INTEGER, Over17 INTEGER, Over18 INTEGER, Over19 INTEGER, Over20 INTEGER, Over21 INTEGER, Over22 INTEGER, Over23 INTEGER, Over24 INTEGER, Over25 INTEGER, Over26 INTEGER, Over27 INTEGER, Over28 INTEGER, Over29 INTEGER, Over30 INTEGER, Over31 INTEGER, Over32 INTEGER, Over33 INTEGER, Over34 INTEGER, Over35 INTEGER, Over36 INTEGER, Over37 INTEGER, Over38 INTEGER, Over39 INTEGER, Over40 INTEGER, Over41 INTEGER, Over42 INTEGER, Over43 INTEGER, Over44 INTEGER, Over45 INTEGER, Over46 INTEGER, Over47 INTEGER, Over48 INTEGER, Over49 INTEGER, Over50 INTEGER, Over51 INTEGER, Over52 INTEGER, Over53 INTEGER, Over54 INTEGER, Over55 INTEGER, Over56 INTEGER);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_WorkerPerformance( WorkerUID INTEGER UNIQUE ON CONFLICT ABORT, Performance_Face INTEGER, Performance_Heel INTEGER, Performance_Cool INTEGER, Performance_Cocky INTEGER, Performance_Crazy INTEGER, Performance_Legit INTEGER, Performance_Comedy INTEGER, Performance_Weasel INTEGER, Performance_Wholesome INTEGER, Performance_Brute INTEGER, Performance_Weird INTEGER);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_WorkerPersonality( WorkerUID INTEGER UNIQUE ON CONFLICT ABORT, Brain_Ego INTEGER, Brain_Generosity INTEGER, Brain_Compassion INTEGER, Brain_Optimism INTEGER, Brain_Naive INTEGER, Brain_Dependable INTEGER, Brain_Social INTEGER, Brain_Loyalty INTEGER, Brain_Bold INTEGER, Brain_Driven INTEGER, Brain_Liberal INTEGER);")
    schema.append("CREATE TABLE IF NOT EXISTS imported_WorkerSkill(  WorkerUID INTEGER UNIQUE ON CONFLICT ABORT, Brawl INTEGER, Air INTEGER, Mat INTEGER, Chain INTEGER, Submissions INTEGER, Power INTEGER, Athletic INTEGER, Stamina INTEGER, Psych INTEGER, Basics INTEGER, Tough INTEGER, Sell INTEGER, Charisma INTEGER, Mic INTEGER, Menace INTEGER, Respect INTEGER, Reputation INTEGER, Safety INTEGER, Looks INTEGER, Star INTEGER, Consistency INTEGER, Act INTEGER, Injury INTEGER, Puroresu INTEGER, Flash INTEGER, Hardcore INTEGER, Announcing INTEGER, Colour INTEGER, Potential INTEGER, Refereeing INTEGER, ScoutRing INTEGER, ScoutEnt INTEGER, ScoutAnn INTEGER, ScoutColour INTEGER, ScoutRef INTEGER, ScoutGimmick INTEGER, Technical INTEGER, Experience INTEGER, PotentialPrimary INTEGER, PotentialMental INTEGER, PotentialPerformance INTEGER, PotentialFundamental INTEGER, PotentialPhysical INTEGER, PotentialAnnouncing INTEGER, PotentialColour INTEGER, PotentialRefereeing INTEGER, ScoutPhysical INTEGER, ScoutBroadcast INTEGER, ScoutType INTEGER);")
    return schema