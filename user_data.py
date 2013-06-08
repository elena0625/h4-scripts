#!/usr/bin/env python
# coding:utf-8

data = [
	{ 
		"alias"     : [ "mat", "matlinuxer2", "matlee" ], # 寫筆記時的代號
		"url_name"  : "matlinuxer2",                      # 網址名稱 ex: http://www.hackingthursday.org/user:matlinuxer2
		"rel_name"  : "Mat",				  # 顯示全名
		"email"     : "matlinuxer2@gmail.com",		  # email
	},
	{ 
		"alias"     : [ "ca" ],
		"url_name"  : "ca",
		"rel_name"  : "CA",
		"email"     : "",
	},
	{ 
		"alias"     : [ "4$","$4","Fourdollars" ],
		"url_name"  : "fourdollars",
		"rel_name"  : "Fourdollars",
		"email"     : "",
	},
	{ 
		"alias"     : [ "聖博","shengpo" ],
		"url_name"  : "shengpo",
		"rel_name"  : "聖博",
		"email"     : "",
	},
	{ 
		"alias"     : [ "aki.k" ],
		"url_name"  : "aki-k",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : [ "aki" ],
		"url_name"  : "aki",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : [ "tsung" ],
		"url_name"  : "tsung",
		"rel_name"  : "Tsung",
		"email"     : "",
	},
	{ 
		"alias"     : [ "clyde", "clydewu" ],
		"url_name"  : "clyde",
		"rel_name"  : "克勞德",
		"email"     : "",
	},
	{ 
		"alias"     : ["ypwang","blue119"],
		"url_name"  : "ypwang",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["ducati"],
		"url_name"  : "ducati",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["honkia","honki"],
		"url_name"  : "honki",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["yuren", "yurenju"],
		"url_name"  : "yurenju",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["huebuer","gittrac"],
		"url_name"  : "gittrac",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["Rex", "chihchun"],
		"url_name"  : "rex",
		"rel_name"  : "Rex Tsai",
		"email"     : "",
	},
	{ 
		"alias"     : ["小迪克"],
		"url_name"  : "nctusdk",
		"rel_name"  : "Mark",
		"email"     : "",
	},
	{ 
		"alias"     : ["魏藥"],
		"url_name"  : "yaowei",
		"rel_name"  : "魏藥",
		"email"     : "",
	},
	{ 
		"alias"     : ["Alex Lin"],
		"url_name"  : "alex-lin",
		"rel_name"  : "Alex Lin",
		"email"     : "",
	},
	{ 
		"alias"     : ["lcamel"],
		"url_name"  : "lcamel",
		"rel_name"  : "LCamel",
		"email"     : "",
	},
	{ 
		"alias"     : ["thinker"],
		"url_name"  : "thinker",
		"rel_name"  : "Thinker Li",
		"email"     : "",
	},
	{ 
		"alias"     : ["CIH"],
		"url_name"  : "cih",
		"rel_name"  : "C.I.H",
		"email"     : "",
	},
	{ 
		"alias"     : ["layla"],
		"url_name"  : "layla",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["mark"],
		"url_name"  : "mark",
		"rel_name"  : "Mark",
		"email"     : "",
	},
	{ 
		"alias"     : ["Max","sakana"],
		"url_name"  : "sakana",
		"rel_name"  : "Max Huang",
		"email"     : "",
	},
	{ 
		"alias"     : ["AL"],
		"url_name"  : "al",
		"rel_name"  : "AL",
		"email"     : "",
	},
	{ 
		"alias"     : ["AceLan"],
		"url_name"  : "acelan",
		"rel_name"  : "AceLan",
		"email"     : "",
	},
	{ 
		"alias"     : ["amos"],
		"url_name"  : "amos",
		"rel_name"  : "Amos Tsai",
		"email"     : "",
	},
	{ 
		"alias"     : ["Anson"],
		"url_name"  : "anson",
		"rel_name"  : "Anson",
		"email"     : "",
	},
	{ 
		"alias"     : ["Atsushi Enomoto"],
		"url_name"  : "atsushi-enomoto",
		"rel_name"  : "Atsushi Enomoto",
		"email"     : "",
	},
	{ 
		"alias"     : ["ben","benlin"],
		"url_name"  : "ben",
		"rel_name"  : "Ben Lin",
		"email"     : "",
	},
	{ 
		"alias"     : ["Ben Wei"],
		"url_name"  : "ben-wei",
		"rel_name"  : "Ben Wei",
		"email"     : "",
	},
	{ 
		"alias"     : ["ben6"],
		"url_name"  : "ben6",
		"rel_name"  : "Ben6",
		"email"     : "",
	},
	{ 
		"alias"     : ["CYJ"],
		"url_name"  : "cyj",
		"rel_name"  : "C.Y.J",
		"email"     : "",
	},
	{ 
		"alias"     : ["czchen"],
		"url_name"  : "czchen",
		"rel_name"  : "czchen",
		"email"     : "",
	},
	{ 
		"alias"     : ["Daniel Lee","dclee", "dclee9"],
		"url_name"  : "dclee9",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["kanru"],
		"url_name"  : "kanru",
		"rel_name"  : "Kanru Chen",
		"email"     : "",
	},
	{ 
		"alias"     : ["kcliu","KuangChe"],
		"url_name"  : "kcliu",
		"rel_name"  : "kcliu",
		"email"     : "",
	},
	{ 
		"alias"     : ["peter"],
		"url_name"  : "peter",
		"rel_name"  : "Peter",
		"email"     : "",
	},
	{ 
		"alias"     : ["rocfatcat"],
		"url_name"  : "rocfatcat",
		"rel_name"  : "rocfatcat",
		"email"     : "",
	},
	{ 
		"alias"     : ["Samuel"],
		"url_name"  : "samuel",
		"rel_name"  : "Samuel Chen",
		"email"     : "",
	},
	{ 
		"alias"     : ["Shih-En"],
		"url_name"  : "shih-en",
		"rel_name"  : "Shih-En Chou",
		"email"     : "",
	},
	{ 
		"alias"     : ["venation", "Venation Vault"],
		"url_name"  : "venation",
		"rel_name"  : "Venation Vault",
		"email"     : "",
	},
	{ 
		"alias"     : ["Vincent"],
		"url_name"  : "vincent",
		"rel_name"  : "Vincent",
		"email"     : "",
	},
	{ 
		"alias"     : ["wayling"],
		"url_name"  : "wayling",
		"rel_name"  : "Wayling",
		"email"     : "",
	},
	{ 
		"alias"     : ["DanielLin", "dlin"],
		"url_name"  : "dlin",
		"rel_name"  : "Daniel Lin",
		"email"     : "",
	},
	{ 
		"alias"     : ["eric629"],
		"url_name"  : "eric629",
		"rel_name"  : "Eric Sun",
		"email"     : "",
	},
	{ 
		"alias"     : ["hsinchn"],
		"url_name"  : "hsinchn",
		"rel_name"  : "hsinchn",
		"email"     : "",
	},
	{ 
		"alias"     : ["hychen"],
		"url_name"  : "hychen",
		"rel_name"  : "hychen",
		"email"     : "",
	},
	{ 
		"alias"     : ["idryman"],
		"url_name"  : "idryman",
		"rel_name"  : "idryman",
		"email"     : "",
	},
	{ 
		"alias"     : ["mosky"],
		"url_name"  : "mosky",
		"rel_name"  : "mosky",
		"email"     : "",
	},
	{ 
		"alias"     : ["pct"],
		"url_name"  : "pct",
		"rel_name"  : "pct",
		"email"     : "",
	},
	{ 
		"alias"     : ["myron"],
		"url_name"  : "myron",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["shawn"],
		"url_name"  : "shawn",
		"rel_name"  : "shawn",
		"email"     : "",
	},
	{ 
		"alias"     : ["qerter"],
		"url_name"  : "qerter",
		"rel_name"  : "qerter",
		"email"     : "",
	},
	{ 
		"alias"     : ["sinsun"],
		"url_name"  : "sinsun",
		"rel_name"  : "sinsun",
		"email"     : "",
	},
	{ 
		"alias"     : ["tardy"],
		"url_name"  : "tardy",
		"rel_name"  : "tardy",
		"email"     : "",
	},
	{ 
		"alias"     : ["wuman"],
		"url_name"  : "wuman",
		"rel_name"  : "wuman",
		"email"     : "",
	},
	{ 
		"alias"     : ["wycc"],
		"url_name"  : "wycc",
		"rel_name"  : "wycc",
		"email"     : "",
	},
	{ 
		"alias"     : ["yan"],
		"url_name"  : "yan",
		"rel_name"  : "yan",
		"email"     : "",
	},
	{ 
		"alias"     : ["ypchen"],
		"url_name"  : "ypchen",
		"rel_name"  : "ypchen",
		"email"     : "",
	},
	{ 
		"alias"     : ["lichain"],
		"url_name"  : "lichain",
		"rel_name"  : "lichain",
		"email"     : "",
	},
	{ 
		"alias"     : ["cclien"],
		"url_name"  : "cclien",
		"rel_name"  : "cclien",
		"email"     : "",
	},
	{ 
		"alias"     : ["aguai"],
		"url_name"  : "aguai",
		"rel_name"  : "aguai",
		"email"     : "",
	},
	{ 
		"alias"     : ["clkao"],
		"url_name"  : "clkao",
		"rel_name"  : "clkao",
		"email"     : "",
	},
	{ 
		"alias"     : ["jidanni"],
		"url_name"  : "jidanni",
		"rel_name"  : "jidanni",
		"email"     : "",
	},
	{ 
		"alias"     : ["jserv"],
		"url_name"  : "jserv",
		"rel_name"  : "jserv",
		"email"     : "",
	},
	{ 
		"alias"     : ["lcp"],
		"url_name"  : "lcp",
		"rel_name"  : "lcp",
		"email"     : "",
	},
	{ 
		"alias"     : ["宏任"],
		"url_name"  : "",
		"rel_name"  : "宏任",
		"email"     : "",
	},
	{ 
		"alias"     : ["ianian"],
		"url_name"  : "ianian",
		"rel_name"  : "ianian",
		"email"     : "",
	},
	{ 
		"alias"     : ["hana", "hanamizuki"],
		"url_name"  : "hanamizuki",
		"rel_name"  : "hanamizuki",
		"email"     : "",
	},
	{ 
		"alias"     : ["lis186"],
		"url_name"  : "lis186",
		"rel_name"  : "lis186",
		"email"     : "",
	},
	{ 
		"alias"     : ["Orange Tsai"],
		"url_name"  : "orange-tsai",
		"rel_name"  : "Orange Tsai",
		"email"     : "",
	},
	{ 
		"alias"     : ["sleepnova"],
		"url_name"  : "sleepnova",
		"rel_name"  : "sleepnova",
		"email"     : "",
	},
	{ 
		"alias"     : ["jiing"],
		"url_name"  : "jiing",
		"rel_name"  : "jiing",
		"email"     : "",
	},
	{ 
		"alias"     : ["yap"],
		"url_name"  : "yap",
		"rel_name"  : "yap",
		"email"     : "",
	},
	{ 
		"alias"     : ["YChao"],
		"url_name"  : "ychao",
		"rel_name"  : "Yuan Chao",
		"email"     : "",
	},
	{ 
		"alias"     : ["joseph"],
		"url_name"  : "joseph",
		"rel_name"  : "joseph",
		"email"     : "",
	},
	{ 
		"alias"     : ["asil"],
		"url_name"  : "asil",
		"rel_name"  : "asil",
		"email"     : "",
	},
	{ 
		"alias"     : ["yuju"],
		"url_name"  : "trista",
		"rel_name"  : "Trista",
		"email"     : "",
	},
	{ 
		"alias"     : ["Chaos Eternal","chaos"],
		"url_name"  : "chaosethernal",
		"rel_name"  : "Chaos Eternal",
		"email"     : "chaos@shlug.org",
	},
	{ 
		"alias"     : ["someone","?", "??","新朋友","新朋友2"],
		"url_name"  : "",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["PhilipZ"],
		"url_name"  : "",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["Maxi"],
		"url_name"  : "maxi",
		"rel_name"  : "Maxi",
		"email"     : "",
	},
	{ 
		"alias"     : ["Ray"],
		"url_name"  : "ray",
		"rel_name"  : "Ray",
		"email"     : "",
	},
	{ 
		"alias"     : ["cades"],
		"url_name"  : "cades",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["shock"],
		"url_name"  : "shock",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["EugeneHu"],
		"url_name"  : "",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["Hab"],
		"url_name"  : "hab",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["cj"],
		"url_name"  : "cj",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["WM"],
		"url_name"  : "wm",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["joe"],
		"url_name"  : "joe",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["CZ"],
		"url_name"  : "cz",
		"rel_name"  : "",
		"email"     : "",
	},
	{ 
		"alias"     : ["PhilipZ"],
		"url_name"  : "philipz",
		"rel_name"  : "PhilipZ",
		"email"     : "",
	},
	{ 
		"alias"     : ["choupi"],
		"url_name"  : "choupi",
		"rel_name"  : "choupi",
		"email"     : "",
	},
	{ 
		"alias"     : ["EugeneHu"],
		"url_name"  : "eugenehu",
		"rel_name"  : "EugeneHu",
		"email"     : "",
	},
	{ 
		"alias"     : ["預約討論","前情提要","前言","特別活動","活動訊息", "近期討論"],
		"url_name"  : "",
		"rel_name"  : "",
		"email"     : "",
	},
]