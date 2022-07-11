sql = f'''
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "brand" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "disc" (
	"id"	INTEGER NOT NULL UNIQUE,
	"brand_id"	INTEGER,
	"mold"	TEXT,
	"type"	TEXT,
	"speed"	REAL,
	"glide"	REAL,
	"turn"	REAL,
	"fade"	REAL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "plastic" (
	"id"	INTEGER NOT NULL UNIQUE,
	"brand_id"	INTEGER,
	"name"	TEXT,
	"category"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "inventory" (
	"id"	INTEGER NOT NULL UNIQUE,
	"mold"	TEXT,
	"brand"	TEXT,
	"speed"	REAL,
	"glide"	REAL,
	"turn"	REAL,
	"fade"	REAL,
	"plastic"	TEXT,
	"weight"	INTEGER,
	"color"	TEXT,
	"notes"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT OR IGNORE INTO "brand" VALUES (1,'Axiom Discs');
INSERT OR IGNORE INTO "brand" VALUES (2,'Dynamic Discs');
INSERT OR IGNORE INTO "brand" VALUES (3,'Innova');
INSERT OR IGNORE INTO "brand" VALUES (4,'Kastaplast');
INSERT OR IGNORE INTO "brand" VALUES (5,'MVP Disc Sports');
INSERT OR IGNORE INTO "brand" VALUES (6,'Streamline');
INSERT OR IGNORE INTO "brand" VALUES (7,'Westside Discs');
INSERT OR IGNORE INTO "disc" VALUES (1,1,'Alias','Midrange',4.0,4.0,-1.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (2,1,'Clash','Fairway',6.5,4.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (3,1,'Crave','Fairway',6.5,5.0,-1.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (4,1,'Defy','Distance',11.0,5.0,-1.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (5,1,'Envy','Putter',3.0,3.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (6,1,'Excite','Distance',14.5,5.5,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (7,1,'Fireball','Fairway',9.0,3.5,-0.5,4.0);
INSERT OR IGNORE INTO "disc" VALUES (8,1,'Insanity','Fairway',9.0,5.0,-2.0,1.5);
INSERT OR IGNORE INTO "disc" VALUES (9,1,'Inspire','Fairway',6.5,5.0,-1.5,1.0);
INSERT OR IGNORE INTO "disc" VALUES (10,1,'Mayhem','Distance',13.0,5.0,-1.5,2.0);
INSERT OR IGNORE INTO "disc" VALUES (11,1,'Panic','Distance',13.0,4.0,-0.5,3.0);
INSERT OR IGNORE INTO "disc" VALUES (12,1,'Proxy','Putter',3.0,3.0,-1.0,0.5);
INSERT OR IGNORE INTO "disc" VALUES (13,1,'Tantrum','Distance',14.5,5.0,-1.5,3.0);
INSERT OR IGNORE INTO "disc" VALUES (14,1,'Tenacity','Distance',13.0,5.0,-2.5,2.0);
INSERT OR IGNORE INTO "disc" VALUES (15,1,'Theory','Midrange',4.0,4.0,-1.5,1.0);
INSERT OR IGNORE INTO "disc" VALUES (16,1,'Thrill','Distance',11.0,4.0,-1.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (17,1,'Vanish','Distance',11.0,5.0,-3.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (18,1,'Virus','Fairway',9.0,5.0,-3.5,1.0);
INSERT OR IGNORE INTO "disc" VALUES (19,1,'Wrath','Fairway',9.0,4.5,-0.5,2.0);
INSERT OR IGNORE INTO "disc" VALUES (20,2,'Breakout','Fairway',8.0,5.0,-1.0,1.5);
INSERT OR IGNORE INTO "disc" VALUES (21,2,'Captain','Distance',13.0,5.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (22,2,'Convict','Fairway',9.0,4.0,-0.5,3.0);
INSERT OR IGNORE INTO "disc" VALUES (23,2,'Criminal','Fairway',10.0,3.0,1.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (24,2,'Defender','Distance',13.0,5.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (25,2,'Deputy','Putter',3.0,4.0,-1.5,0.0);
INSERT OR IGNORE INTO "disc" VALUES (26,2,'EMAC Truth','Midrange',5.0,5.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (27,2,'Enforcer','Distance',12.0,4.0,0.5,4.0);
INSERT OR IGNORE INTO "disc" VALUES (28,2,'Escape','Fairway',9.0,5.0,1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (29,2,'Evidence','Midrange',5.0,5.0,-1.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (30,2,'Felon','Fairway',9.0,3.0,0.5,4.0);
INSERT OR IGNORE INTO "disc" VALUES (31,2,'Freedom','Distance',14.0,5.0,-3.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (32,2,'Gavel','Putter',3.0,5.0,-2.0,0.5);
INSERT OR IGNORE INTO "disc" VALUES (33,2,'Getaway','Fairway',9.0,5.0,-0.5,3.0);
INSERT OR IGNORE INTO "disc" VALUES (34,2,'Guard','Putter',2.0,5.0,0.0,0.5);
INSERT OR IGNORE INTO "disc" VALUES (35,2,'Judge','Putter',2.0,4.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (36,2,'Justice','Midrange',5.0,1.0,0.5,4.0);
INSERT OR IGNORE INTO "disc" VALUES (37,2,'Marshal','Putter',3.0,4.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (38,2,'Maverick','Fairway',7.0,4.0,-1.5,2.0);
INSERT OR IGNORE INTO "disc" VALUES (39,2,'Patrol','Midrange',5.0,5.0,-3.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (40,2,'Proof','Midrange',5.0,5.0,-3.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (41,2,'Renegade','Distance',11.0,5.0,-1.5,2.5);
INSERT OR IGNORE INTO "disc" VALUES (42,2,'Sheriff','Distance',13.0,5.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (43,2,'Slammer','Putter',3.0,2.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (44,2,'Suspect','Midrange',4.0,3.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (45,2,'Thief','Fairway',8.0,5.0,-1.5,2.0);
INSERT OR IGNORE INTO "disc" VALUES (46,2,'Trespass','Distance',12.0,5.0,-0.5,3.0);
INSERT OR IGNORE INTO "disc" VALUES (47,2,'Truth','Midrange',5.0,5.0,-1.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (48,2,'Verdict','Midrange',5.0,4.0,0.0,3.5);
INSERT OR IGNORE INTO "disc" VALUES (49,2,'Warden','Putter',2.0,4.0,0.0,0.5);
INSERT OR IGNORE INTO "disc" VALUES (50,2,'Warrant','Midrange',5.0,5.0,-2.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (51,2,'Witness','Fairway',8.0,6.0,-3.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (52,3,'Ape','Distance',13.0,5.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (53,3,'Aero','Putter',3.0,6.0,0.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (54,3,'Archangel','Fairway',8.0,6.0,-4.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (55,3,'Archon','Distance',11.0,5.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (56,3,'Atlas','Midrange',5.0,4.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (57,3,'Aviar','Putter',2.0,3.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (58,3,'AviarX3','Putter',3.0,2.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (59,3,'Aviar 3','Putter',3.0,2.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (60,3,'Aviar XD','Putter',3.0,4.0,-1.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (61,3,'Banshee','Fairway',7.0,3.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (62,3,'Beast','Distance',10.0,5.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (63,3,'Birdie','Putter',1.0,2.0,0.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (64,3,'Boss','Distance',13.0,5.0,-1.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (65,3,'Bullfrog','Putter',3.0,1.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (66,3,'Caiman','Midrange',5.5,2.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (67,3,'Cheetah','Midrange',6.0,4.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (68,3,'Classic Roc','Putter',3.0,3.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (69,3,'Cobra','Midrange',4.0,5.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (70,3,'Colossus','Distance',14.0,5.0,-2.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (71,3,'Colt','Putter',3.0,4.0,-1.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (72,3,'Corvette','Distance',14.0,6.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (73,3,'Coyote','Midrange',4.0,5.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (74,3,'CRO','Midrange',5.0,3.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (75,3,'Daedalus','Distance',13.0,6.0,-3.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (76,3,'Dart','Putter',3.0,4.0,0.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (77,3,'Destroyer','Distance',12.0,5.0,-1.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (78,3,'Dominator','Distance',13.0,5.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (79,3,'Dragon','Fairway',8.0,5.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (80,3,'Eagle (old)','Fairway',7.0,4.0,-1.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (81,3,'Eagle (new)','Fairway',7.0,4.0,-1.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (82,3,'Firebird','Fairway',9.0,3.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (83,3,'Firebird L (FL)','Fairway',9.0,3.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (84,3,'Firestorm','Distance',14.0,4.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (85,3,'Foxbat','Midrange',5.0,6.0,-1.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (86,3,'Gator','Midrange',5.0,2.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (87,3,'Gator3','Midrange',5.0,2.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (88,3,'Gazelle','Midrange',6.0,4.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (89,3,'Groove','Distance',13.0,6.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (90,3,'Hydra','Putter',3.0,3.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (91,3,'Katana','Distance',13.0,5.0,-3.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (92,3,'Kite','Midrange',5.0,6.0,-3.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (93,3,'Krait','Distance',11.0,5.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (94,3,'Leopard','Midrange',6.0,5.0,-2.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (95,3,'Leopard 3','Fairway',7.0,5.0,-2.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (96,3,'Mako','Midrange',4.0,5.0,0.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (97,3,'Mako 3','Midrange',5.0,5.0,0.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (98,3,'Mamba','Distance',11.0,6.0,-5.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (99,3,'Manta','Midrange',5.0,5.0,-2.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (100,3,'Max','Distance',11.0,3.0,0.0,5.0);
INSERT OR IGNORE INTO "disc" VALUES (101,3,'Mirage','Putter',3.0,4.0,-3.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (102,3,'Monarch','Distance',10.0,5.0,-4.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (103,3,'Monster','Distance',10.0,3.0,0.0,5.0);
INSERT OR IGNORE INTO "disc" VALUES (104,3,'Mystere','Distance',11.0,6.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (105,3,'Nova','Putter',2.0,3.0,0.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (106,3,'ORC','Distance',10.0,4.0,-1.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (107,3,'Panther','Midrange',5.0,4.0,-2.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (108,3,'Pig','Putter',3.0,1.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (109,3,'Pole Cat','Putter',1.0,3.0,0.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (110,3,'Rat','Midrange',4.0,2.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (111,3,'Rhyno','Putter',2.0,1.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (112,3,'Roadrunner','Fairway',9.0,5.0,-4.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (113,3,'Roc','Midrange',4.0,4.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (114,3,'Roc 3','Midrange',5.0,4.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (115,3,'RocX3','Midrange',5.0,4.0,0.0,3.5);
INSERT OR IGNORE INTO "disc" VALUES (116,3,'Savant','Fairway',9.0,5.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (117,3,'Shark','Midrange',4.0,4.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (118,3,'Shark 3','Midrange',5.0,4.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (119,3,'Shryke','Distance',13.0,6.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (120,3,'Sidewinder','Fairway',9.0,5.0,-3.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (121,3,'Skeeter','Midrange',5.0,5.0,-1.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (122,3,'Sonic','Putter',1.0,2.0,-4.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (123,3,'Spider','Midrange',5.0,3.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (124,3,'Starfire','Distance',10.0,4.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (125,3,'Starfire L (SL)','Distance',10.0,4.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (126,3,'Stingray','Midrange',4.0,5.0,-3.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (127,3,'Stud','Putter',3.0,3.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (128,3,'TeeBird','Fairway',7.0,5.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (129,3,'Teebird 3','Fairway',8.0,4.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (130,3,'TL','Fairway',7.0,5.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (131,3,'TeeDevil','Distance',12.0,5.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (132,3,'Tee-Rex','Distance',11.0,4.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (133,3,'Tern','Distance',12.0,6.0,-3.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (134,3,'TL 3','Fairway',8.0,4.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (135,3,'Thunderbird','Fairway',9.0,5.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (136,3,'Valkyrie','Fairway',9.0,4.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (137,3,'Viking','Fairway',9.0,4.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (138,3,'Viper','Midrange',6.0,4.0,1.0,5.0);
INSERT OR IGNORE INTO "disc" VALUES (139,3,'VRoc','Midrange',4.0,4.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (140,3,'Vulcan','Distance',13.0,5.0,-4.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (141,3,'Wahoo','Distance',12.0,6.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (142,3,'Wedge','Putter',3.5,3.0,-3.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (143,3,'Whale','Putter',2.0,3.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (144,3,'Whippet','Midrange',6.0,3.0,1.0,5.0);
INSERT OR IGNORE INTO "disc" VALUES (145,3,'Wolf','Midrange',4.0,3.0,-4.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (146,3,'Wombat','Midrange',5.0,6.0,-1.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (147,3,'Wombat3','Midrange',5.0,6.0,-1.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (148,3,'Wraith','Distance',11.0,5.0,-1.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (149,3,'XCaliber','Distance',12.0,5.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (150,3,'Lion','Midrange',5.0,4.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (151,4,'Berg','Putter',1.0,1.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (152,4,'Falk','Fairway',9.0,6.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (153,4,'Grym','Distance',13.0,5.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (154,4,'Grym X','Distance',13.0,5.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (155,4,'Kaxe','Midrange',6.0,4.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (156,4,'Kaxe Z','Midrange',6.0,5.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (157,4,'Rask (old)','Distance',14.0,3.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (158,4,'Rask (new)','Distance',14.0,3.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (159,4,'Reko','Putter',3.0,3.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (160,4,'Stål','Fairway',9.0,4.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (161,5,'Amp','Fairway',8.0,5.0,-1.5,1.0);
INSERT OR IGNORE INTO "disc" VALUES (162,5,'Anode','Putter',2.5,3.0,0.0,0.5);
INSERT OR IGNORE INTO "disc" VALUES (163,5,'Atom','Putter',3.0,3.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (164,5,'Axis','Midrange',5.0,5.0,-1.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (165,5,'Catalyst','Distance',13.0,5.5,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (166,5,'Deflector','Midrange',5.0,3.5,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (167,5,'Dimension','Distance',14.5,5.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (168,5,'Energy','Distance',13.0,4.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (169,5,'Impulse','Distance',9.0,5.0,-3.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (170,5,'Inertia','Distance',9.0,5.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (171,5,'Ion','Putter',2.5,3.0,0.0,1.5);
INSERT OR IGNORE INTO "disc" VALUES (172,5,'Limit','Distance',14.5,3.5,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (173,5,'Matrix','Midrange',5.0,4.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (174,5,'Motion','Distance',9.0,3.5,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (175,5,'Nitro','Distance',13.0,4.0,-0.5,3.0);
INSERT OR IGNORE INTO "disc" VALUES (176,5,'Octane','Distance',13.0,5.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (177,5,'Orbital','Distance',11.0,5.0,-4.5,1.0);
INSERT OR IGNORE INTO "disc" VALUES (178,5,'Particle','Putter',3.0,3.0,0.0,2.5);
INSERT OR IGNORE INTO "disc" VALUES (179,5,'Phase','Distance',11.0,3.5,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (180,5,'Photon','Distance',11.0,5.0,-1.0,2.5);
INSERT OR IGNORE INTO "disc" VALUES (181,5,'Relativity','Distance',14.5,5.5,-3.0,1.5);
INSERT OR IGNORE INTO "disc" VALUES (182,5,'Relay','Fairway',6.0,5.0,-2.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (183,5,'Resistor','Fairway',6.5,4.0,0.0,3.5);
INSERT OR IGNORE INTO "disc" VALUES (184,5,'Servo','Fairway',6.5,5.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (185,5,'Shock','Fairway',8.0,5.0,0.0,2.5);
INSERT OR IGNORE INTO "disc" VALUES (186,5,'Signal','Fairway',6.0,5.0,-3.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (187,5,'Spin','Putter',2.5,4.0,-2.0,0.0);
INSERT OR IGNORE INTO "disc" VALUES (188,5,'Switch','Fairway',6.5,5.0,-1.5,1.0);
INSERT OR IGNORE INTO "disc" VALUES (189,5,'Tangent','Midrange',4.0,4.0,-0.5,0.5);
INSERT OR IGNORE INTO "disc" VALUES (190,5,'Teleport','Distance',14.5,5.0,-1.5,2.5);
INSERT OR IGNORE INTO "disc" VALUES (191,5,'Tensor','Midrange',4.0,4.0,0.0,2.5);
INSERT OR IGNORE INTO "disc" VALUES (192,5,'Tesla','Distance',9.0,5.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (193,5,'Vector','Midrange',5.0,4.0,0.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (194,5,'Vertex','Midrange',4.0,4.0,-2.0,0.5);
INSERT OR IGNORE INTO "disc" VALUES (195,5,'Volt','Fairway',8.0,5.0,-0.5,2.0);
INSERT OR IGNORE INTO "disc" VALUES (196,5,'Wave','Distance',11.0,5.0,-2.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (197,6,'Drift','Fairway',7.0,5.0,-2.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (198,6,'Pilot','Putter',2.0,5.0,-1.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (199,6,'Runway','Midrange',5.0,4.0,0.0,3.5);
INSERT OR IGNORE INTO "disc" VALUES (200,6,'Trace','Distance',11.0,5.0,-2.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (201,7,'Ahti','Fairway',9.0,3.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (202,7,'Anvil','Midrange',4.0,2.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (203,7,'Maiden','Putter',3.0,4.0,0.0,1.0);
INSERT OR IGNORE INTO "disc" VALUES (204,7,'Sampo','Fairway',10.0,4.0,-1.0,2.0);
INSERT OR IGNORE INTO "disc" VALUES (205,1,'Pyro','Midrange',5.0,4.0,0.0,2.5);
INSERT OR IGNORE INTO "disc" VALUES (206,2,'Raider','Distance',13.0,5.0,-1.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (207,6,'Flare','Fairway',9.0,4.0,0.0,3.5);
INSERT OR IGNORE INTO "disc" VALUES (208,5,'Entropy','Putter',3.0,3.0,0.0,4.0);
INSERT OR IGNORE INTO "disc" VALUES (209,6,'Lift','Fairway',9.0,5.0,-2.0,1.5);
INSERT OR IGNORE INTO "disc" VALUES (210,6,'Stabilizer','Putter',3.0,3.0,0.0,3.0);
INSERT OR IGNORE INTO "disc" VALUES (211,1,'Delirium','Distance',14.5,5.0,-0.5,3.0);
INSERT OR IGNORE INTO "plastic" VALUES (1,1,'Neutron',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (2,5,'Neutron',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (3,6,'Neutron',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (4,1,'Proton',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (5,5,'Proton',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (6,6,'Proton',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (7,1,'Electron',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (8,5,'Electron',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (9,6,'Electron',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (10,1,'Fission',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (11,5,'Fission',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (12,6,'Fission',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (13,1,'Plasma',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (14,5,'Plasma',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (15,6,'Plasma',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (16,3,'DX',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (17,3,'Pro',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (18,3,'R-Pro',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (19,3,'Star',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (20,3,'G-Star',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (21,3,'Champion',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (22,3,'Blizzard',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (23,2,'Fuzion',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (24,2,'Lucid',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (25,2,'Classic',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (26,2,'Classic Burst',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (27,2,'Prime',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (28,2,'Prime Burst',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (29,4,'K1',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (30,4,'K1 Soft',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (31,4,'K2',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (32,4,'K3',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (33,7,'VIP',NULL);
INSERT OR IGNORE INTO "plastic" VALUES (34,7,'Origio',NULL);
COMMIT;
'''