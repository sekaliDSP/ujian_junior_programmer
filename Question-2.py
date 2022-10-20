#hello for this script i write it and run it on python 3.10 version.
#if you want to alter the json you need to alter the function as well as i make this code as simple as it is.
category = [
    {
        "name":"Buku",
        "childs":[
            {
                "name":"Arsitektur Desain",
                "childs":[
                    {
                        "name":"Buku bangunan"
                    }
                ]
            },
            {
                "name":"Kedokteran",
                "childs":[
                    {
                        "name":"Buku farmasi"
                    }
                ]
            }
        ]
    },
    {
        "name":"Dapur",
        "childs":[
            {
                "name":"Aksesoris Dapur",
                "childs":[
                    {
                        "name":"Celemek"
                    }
                ]
            },
            {
                "name":"Bekal",
                "childs":[
                    {
                        "name":"Botol Minuman"
                    }
                ]
            }
        ]
    },{
        "name":"Elektronik",
        "childs":[
            {
                "name":"Audio",
                "childs":[
                    {
                        "name":"Amplifier"
                    }
                ]
            },
            {
                "name":"Lampu",
                "childs":[
                    {
                        "name":"Bohlam"
                    }
                ]
            }
        ]
    },{
        "name":"Fashion Anak & Bayi",
        "childs":[
            {
                "name":"Aksesoris Anak",
                "childs":[
                    {
                        "name":"Dasi anak"
                    }
                ]
            },
            {
                "name":"Tas Anak",
                "childs":[
                    {
                        "name":"Tas Koper Anak"
                    }
                ]
            }
        ]
    },{
        "name":"Fashion Muslim",
        "childs":[
            {
                "name":"Jilbab",
                "childs":[
                    {
                        "name":"Cadar"
                    }
                ]
            },
            {
                "name":"Masker Hijab",
                "childs":[
                    {
                        "name":"Masker Kain"
                    }
                ]
            }
        ]
    },{
        "name":"Fashion Pria",
        "childs":[
            {
                "name":"Tas Pria",
                "childs":[
                    {
                        "name":"Clutch Pria"
                    }
                ]
            },
            {
                "name":"Batik Pria",
                "childs":[
                    {
                        "name":"Kemeja Batik Pria"
                    }
                ]
            }
        ]
    },{
        "name":"Fashion Wanita",
        "childs":[
            {
                "name":"Dress",
                "childs":[
                    {
                        "name":"Mini Dress"
                    }
                ]
            },
            {
                "name":"Batik Wanita",
                "childs":[
                    {
                        "name":"Kain Batik"
                    }
                ]
            }
        ]
    },{
        "name":"Film & Musik",
        "childs":[
            {
                "name":"Vokal",
                "childs":[
                    {
                        "name":"Efek vokal"
                    }
                ]
            },
            {
                "name":"Gitar & Bass",
                "childs":[
                    {
                        "name":"Bass Akustik"
                    }
                ]
            }
        ]
    },{
        "name":"Gaming",
        "childs":[
            {
                "name":"CD game",
                "childs":[
                    {
                        "name":"CD Xbox"
                    }
                ]
            },
            {
                "name":"Game Console",
                "childs":[
                    {
                        "name":"Game Boy"
                    }
                ]
            }
        ]
    },{
        "name":"Handphone & Tablet",
        "childs":[
            {
                "name":"JHandphone",
                "childs":[
                    {
                        "name":"Android OS"
                    }
                ]
            },
            {
                "name":"Tablet",
                "childs":[
                    {
                        "name":"iOS"
                    }
                ]
            }
        ]
    },{
        "name":"Ibu & Bayi",
        "childs":[
            {
                "name":"Pakaian Ibu hamil",
                "childs":[
                    {
                        "name":"Atasan hamil"
                    }
                ]
            },
            {
                "name":"Perawatan bayi",
                "childs":[
                    {
                        "name":"Baby oil"
                    }
                ]
            }
        ]
    },{
        "name":"Kamera",
        "childs":[
            {
                "name":"Digital Kamera",
                "childs":[
                    {
                        "name":"DSLR"
                    }
                ]
            },
            {
                "name":"Analog",
                "childs":[
                    {
                        "name":"Disposable kamera"
                    }
                ]
            }
        ]
    },{
        "name":"Kecantikan",
        "childs":[
            {
                "name":"Make up mata",
                "childs":[
                    {
                        "name":"Eye liner"
                    }
                ]
            },
            {
                "name":"Make up wajah",
                "childs":[
                    {
                        "name":"BB cream"
                    }
                ]
            }
        ]
    },{
        "name":"Kmputer & Laptop",
        "childs":[
            {
                "name":"Networking",
                "childs":[
                    {
                        "name":"Adapter"
                    }
                ]
            },
            {
                "name":"Kabel & adaptor",
                "childs":[
                    {
                        "name":"Kabel DVI"
                    }
                ]
            }
        ]
    },{
        "name":"Mainan",
        "childs":[
            {
                "name":"Boneka",
                "childs":[
                    {
                        "name":"Boneka Bantal"
                    }
                ]
            },
            {
                "name":"Kostum",
                "childs":[
                    {
                        "name":"Kostum Pria"
                    }
                ]
            }
        ]
    },{
        "name":"Makanan",
        "childs":[
            {
                "name":"Kue",
                "childs":[
                    {
                        "name":"Kue Kering"
                    }
                ]
            },
            {
                "name":"Makanan beku",
                "childs":[
                    {
                        "name":"Dessert"
                    }
                ]
            }
        ]
    },{
        "name":"Office",
        "childs":[
            {
                "name":"Kertas",
                "childs":[
                    {
                        "name":"Kertas Fax"
                    }
                ]
            },
            {
                "name":"Pemotong Kertas",
                "childs":[
                    {
                        "name":"Cutter"
                    }
                ]
            }
        ]
    },{
        "name":"Olahraga",
        "childs":[
            {
                "name":"Beladiri",
                "childs":[
                    {
                        "name":"Baton"
                    }
                ]
            },
            {
                "name":"Boxing",
                "childs":[
                    {
                        "name":"samsak tinju"
                    }
                ]
            }
        ]
    },{
        "name":"Otomotif",
        "childs":[
            {
                "name":"Spare part motor",
                "childs":[
                    {
                        "name":"Aki Motor"
                    }
                ]
            },
            {
                "name":"Interior Mobil",
                "childs":[
                    {
                        "name":"Bantal mobil"
                    }
                ]
            }
        ]
    },{
        "name":"Perawatan Hewan",
        "childs":[
            {
                "name":"Grooming hewan",
                "childs":[
                    {
                        "name":"Pet glove"
                    }
                ]
            },
            {
                "name":"Perawatan ikan",
                "childs":[
                    {
                        "name":"Aquarium"
                    }
                ]
            }
        ]
    },{
        "name":"Perawatan tubuh",
        "childs":[
            {
                "name":"Grooming",
                "childs":[
                    {
                        "name":"Alat cukur"
                    }
                ]
            },
            {
                "name":"Perawatan kuku",
                "childs":[
                    {
                        "name":"Foot Scrub"
                    }
                ]
            }
        ]
    },{
        "name":"Perlengkapan pesta",
        "childs":[
            {
                "name":"Balon",
                "childs":[
                    {
                        "name":"Balon LED"
                    }
                ]
            },
            {
                "name":"Hadiah",
                "childs":[
                    {
                        "name":"Hampers"
                    }
                ]
            }
        ]
    },{
        "name":"Pertukangan",
        "childs":[
            {
                "name":"Ledeng",
                "childs":[
                    {
                        "name":"Bath tub"
                    }
                ]
            },
            {
                "name":"Pneumatic",
                "childs":[
                    {
                        "name":"Vacuum Pneumatic"
                    }
                ]
            }
        ]
    },{
        "name":"Properti",
        "childs":[
            {
                "name":"Perumahan",
                "childs":[
                    {
                        "name":"Apartemen"
                    }
                ]
            },
            {
                "name":"Sewa Properti",
                "childs":[
                    {
                        "name":"Gudang"
                    }
                ]
            }
        ]
    },{
        "name":"Tour",
        "childs":[
            {
                "name":"VOucher travel",
                "childs":[
                    {
                        "name":"Travel voucher"
                    }
                ]
            },
            {
                "name":"Paket tur",
                "childs":[
                    {
                        "name":"Land tour"
                    }
                ]
            }
        ]
    },{
        "name":"Wedding",
        "childs":[
            {
                "name":"Venue",
                "childs":[
                    {
                        "name":"Ballroom Hotel"
                    }
                ]
            },
            {
                "name":"Decoration",
                "childs":[
                    {
                        "name":"Florist"
                    }
                ]
            }
        ]
    }
]

def listcon(a = [],counted = 0):
    try:
        if (counted>len(a)-1):
            print("habis cuyy")

        else:
            print(a[counted]['name'])
            print(" "+a[counted]['childs'][0]['name'])
            print("  "+a[counted]['childs'][0]['childs'][0]['name'])
            print(" "+a[counted]['childs'][1]['name'])
            print("  "+a[counted]['childs'][1]['childs'][0]['name']+"\n")
            counted +=1
            listcon(category,counted)
    except Exception as e:
        print(e)

listcon(category)
