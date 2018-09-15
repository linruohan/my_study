# coding=utf-8
import json,requests
import demjson,time,re,os
from urllib.request import urlretrieve
class Xiangce:
    xiangceID = [{'id': 192898950, 'name': '恃颜', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 36, 't': 1260524201132,
                  'ut': 1261146767405, 'cvid': 5610951936, 'curl': '2/7RX2VDZzzjT_-oaoZbfm5g==/1654509913106907464.jpg',
                  'surl': '0/8ETovtxr8xSnrYgZmqXmNg==/1654509913106907465.jpg',
                  'lurl': '2/CdTJt8852N_e3bYfr_b69Q==/3284531503238400338.jpg', 'dmt': -19156623, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/cALejyKxFWOQQaSVVGzwrQ==/49478023641598.js'},
                 {'id': 193335904, 'name': '格萨', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 12, 't': 1261146811842,
                  'ut': 1261146901998, 'cvid': 5610952280, 'curl': '2/D45VcfLZbqwj1IpnKWLjpQ==/1264385595385357310.jpg',
                  'surl': '0/ODm3sb7Z4Psc8ZnAemwVjQ==/2167075845696608124.jpg',
                  'lurl': '2/siT2GVbbmX-2iLoKuzdyIQ==/3284531503238400335.jpg', 'dmt': 435325917, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/Hz1B3iwaT-WmdV65gkzDNQ==/183618442324562.js'},
                 {'id': 193732543, 'name': '素心', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 18, 't': 1261790575212,
                  'ut': 1303996067092, 'cvid': 6922866828, 'curl': '2/8NUxs36SGv56ZtmwYqV5Sw==/1475210352942232622.jpg',
                  'surl': '0/LIdRWNuznZ8I-XJmFy1sKQ==/1475210352942232623.jpg',
                  'lurl': '1/4WAT_HfCYgB4SKkAH6Iw5Q==/1801721325926643460.jpg', 'dmt': -969380242, 'alc': 'true',
                  'kw': '', 'purl': 's1.ph.126.net/8NHlGwEk09DeUjyCcVr8LA==/73667279272218.js'},
                 {'id': 196773654, 'name': '心若', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 19, 't': 1266398582416,
                  'ut': 1307461860963, 'cvid': 5763252304, 'curl': '0/EOcAKQwmbosJ5YyYTXcLiw==/2047730455571682120.jpg',
                  'surl': '1/XIOUPf7-SIIn5fxFTOUMkg==/2047730455571682121.jpg',
                  'lurl': '2/TLgbgNESMC4xVlWZdaIlmg==/2047730455571682122.jpg', 'dmt': -436541667, 'alc': 'true',
                  'kw': '', 'purl': 's1.ph.126.net/P7EHYMh9yQCItYgJHBIbBw==/17592186350806.js'},
                 {'id': 196827861, 'name': '别域景色', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 6, 't': 1266484955059,
                  'ut': 1308054405272, 'cvid': 5765845286, 'curl': '2/YZ_52DS1KOqLotHMjzKAcA==/1612007191623157208.jpg',
                  'surl': '1/vwWGkzHQ-9hbPfRuz-Xg6g==/1612007191623157210.jpg',
                  'lurl': '0/7OcKSXmt7Z1naYnWdmHY_g==/2080100077893598470.jpg', 'dmt': -1577902471, 'alc': 'true',
                  'kw': '', 'purl': 's1.ph.126.net/DQvoniCUAU51vQy_E1I1_g==/128642860536235.js'},
                 {'id': 197284887, 'name': '雨欣', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 15, 't': 1267099913132,
                  'ut': 1303996250163, 'cvid': 6922886944, 'curl': '1/4hxYBbHQgyx8097iC_tZiQ==/2172986820207908923.jpg',
                  'surl': '2/HN_DwqCp2EhDuO-m4QFJjw==/2172986820207908924.jpg',
                  'lurl': '1/eav-e2rE477Iz2mJzMU2ZQ==/1116329757651245224.jpg', 'dmt': 435738283, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/LICcblh_XMah9PU4K9Ubxg==/87960930706345.js'},
                 {'id': 212522052, 'name': '海星', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 12, 't': 1287273246933,
                  'ut': 1287273324318, 'cvid': 6484086751, 'curl': '0/ioVqR4dLfQ0I8VG2oS1SgQ==/2130202623747536250.jpg',
                  'surl': '2/E3lbl3mQPQfDWmT3GOsALQ==/2130202623747536252.jpg',
                  'lurl': '2/yvyOKNHcvpC3xc-u67rYkQ==/2612650733845282439.jpg', 'dmt': 435513801, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/V0o6lzeR7cc7NNiYUhnPvQ==/59373628384759.js'},
                 {'id': 212522058, 'name': '玉茗', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 212, 't': 1287273518112,
                  'ut': 1308054451644, 'cvid': 6484087170, 'curl': '1/jSbMuGrnD1HGJ84LHpmuQg==/954481646026359742.jpg',
                  'surl': '2/LePXIOMlShPQwd0BFlIWZQ==/954481646026359743.jpg',
                  'lurl': '2/KXlLTH5PXcNi8tk_UBCpFA==/3868873554888472967.jpg', 'dmt': 436276925, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/b3e2YcgwW141VVLwy0pF1g==/233096465577617.js'},
                 {'id': 212605508, 'name': '夜色', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 21, 't': 1287406890295,
                  'ut': 1304055645054, 'cvid': 6519910615, 'curl': '1/_6zVZQ3A5bd-G1WmD1UP6g==/1082552760430257292.jpg',
                  'surl': '1/M4l--zUvOGh2xKUKnYoJRw==/1082552760430257295.jpg',
                  'lurl': '2/8xyI9lPAkYHTRjiVU1gTuw==/3284531503238400332.jpg', 'dmt': -353667387, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/aCfp07D3555inVXw0LT9tw==/48378511950837.js'},
                 {'id': 214351939, 'name': '梦璃', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 62, 't': 1289971694558,
                  'ut': 1306628485270, 'cvid': 6990838118, 'curl': '2/s-Z6BjBpI2iENKCgPH1VIw==/2289798935542775585.jpg',
                  'surl': '0/v19AD8bJflH_yqsleI1UHQ==/2289798935542775586.jpg',
                  'lurl': '0/QHIRLZqGeNYz5aQudLvdKA==/1116329757651245226.jpg', 'dmt': 435425723, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/RR0J8rAjUZENw9kNpPy7Mw==/160528698138813.js'},
                 {'id': 225195138, 'name': '时尚', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 120, 't': 1308824495003,
                  'ut': 1308825488505, 'cvid': 7049316577, 'curl': '0/83rv7HuYIZHJ2a12kRsOVQ==/2880614911673632608.jpg',
                  'surl': '2/oD2oVcHgtsJD_oul8Hqazw==/3349270747881511541.jpg',
                  'lurl': '0/7mK65d0hQVpUOBaMWqUS3w==/945755921748599931.jpg', 'dmt': -1577898748, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/JsX8QhaLL_l3T78k9Uwi2g==/135239930303084.js'},
                 {'id': 225195170, 'name': '梦语', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 27, 't': 1308825805898,
                  'ut': 1308826029805, 'cvid': 7049347800, 'curl': '2/hwImk1XGx63wXh3WKd-ntg==/2860911663303886778.jpg',
                  'surl': '0/AG-bSXYPaGLs3Bm27XRvqg==/3873095679539419371.jpg',
                  'lurl': '1/8MciB_i9my7QAt3OxjKSCg==/3746150465042266834.jpg', 'dmt': 1491577224, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/xV_5L6pwYyfgpGAO5VN2xA==/144036023903688.js'},
                 {'id': 225195176, 'name': '冰泪', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 36, 't': 1308826182160,
                  'ut': 1308826350499, 'cvid': 7049249184, 'curl': '2/x-RYP9Dp-grZdgxM12EuBg==/3745024565135950985.jpg',
                  'surl': '0/vTDbteFMgLKAIqDU2nUkBA==/3108609642809264040.jpg',
                  'lurl': '2/Qe8zn5hKkemAKByCfpeGaA==/1116329757651245222.jpg', 'dmt': -1735833045, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/3FoOE8M-249GVkP_-PXJIQ==/29686813999569.js'},
                 {'id': 225571599, 'name': '蓝衫', 's': 3, 'desc': '', 'st': 8, 'au': 0, 'count': 28, 't': 1309494516542,
                  'ut': 1309494895493, 'cvid': 7065914751, 'curl': '1/e_he9jjwBE0-nbb49c8EnQ==/1164743453645477998.jpg',
                  'surl': '1/u_M0cIvaxo-zYsWXY7Xckg==/1164743453645478001.jpg',
                  'lurl': '1/8jfKKR66r9XEbXZuKVTZ8A==/3284531503238400328.jpg', 'dmt': -1641789168, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/XOIGM4S1C4XO2OKXS23esw==/24189255883400.js'},
                 {'id': 229630004, 'name': '亦若', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 17, 't': 1317199854908,
                  'ut': 1317200442152, 'cvid': 7250051809, 'curl': '2/yjAacau3_i3LOw_s6tM2nQ==/2534682165296428163.jpg',
                  'surl': '0/QU713DezLD9hu51RaY81YQ==/2534682165296428164.jpg',
                  'lurl': '0/L3p-C16XQxvKGgB5CqLmiQ==/3108046692856036860.jpg', 'dmt': -1641881779, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/UFP6ukxMCqLZhiDkjZjnww==/73667279133927.js'},
                 {'id': 229630031, 'name': '意识', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 59, 't': 1317200495860,
                  'ut': 1317519044416, 'cvid': 7256646219, 'curl': '2/ayRH8kLkwPmjD2aggoVseA==/2664723604536762824.jpg',
                  'surl': '0/e8i4AIzYI0ZgIeqmiRD4zg==/2664723604536762825.jpg',
                  'lurl': '2/6HIUkWEYzMwgkGMT0rPnUQ==/2612650733845282502.jpg', 'dmt': -1641948703, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/esP9n-HeY6yF7iLICObCVg==/227598907022276.js'},
                 {'id': 229770097, 'name': '小懒', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 34, 't': 1317519186145,
                  'ut': 1317519352467, 'cvid': 7256837698, 'curl': '1/1wxY0rOIxc0mHCLxcKSowQ==/568297977995792830.jpg',
                  'surl': '2/dpwBOWBgG3DYL-kfCthDnw==/568297977995792831.jpg',
                  'lurl': '1/Cx8ZY-wbmXwlBNd2rzX3Yw==/2612650733845282513.jpg', 'dmt': -1641908294, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/o6MIpmuhIaAKX0oeEez1BA==/73667279133923.js'},
                 {'id': 229770101, 'name': '月衣朦胧', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 47, 't': 1317519510005,
                  'ut': 1317519770982, 'cvid': 7256826589, 'curl': '1/YLXoh0EwR6q-kZnxKucZlA==/1354176112971943441.jpg',
                  'surl': '2/rio5Ai7yIgKY2xFnRsG1Dg==/1354176112971943442.jpg',
                  'lurl': '2/FUgZQgLP56Y3XxTRO8isKA==/2612650733845282520.jpg', 'dmt': -1856610903, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/8vjxAuyOTVvXFIL-ZMepug==/78065325586896.js'},
                 {'id': 238543315, 'name': '剑', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 60, 't': 1336881106059,
                  'ut': 1339206045660, 'cvid': 7688005536, 'curl': '2/RhddJzT9tfFMqV-Y6KZBeA==/1003458291990534530.jpg',
                  'surl': '0/wKEcfVh6a_tZMQrmfWtsiA==/1003458291990534531.jpg',
                  'lurl': '2/G6rGVDqUpae4IyakwtzWvA==/1704612458960799179.jpg', 'dmt': -1642219220, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/yv3Ut-z9GJxSuBRwtpF-Bw==/93458488433704.js'},
                 {'id': 238543320, 'name': '月晴', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 43, 't': 1336881302763,
                  'ut': 1336881391474, 'cvid': 7637244838, 'curl': '1/EYDwg3elE7LE8pS0LDSorQ==/1087619310027296425.jpg',
                  'surl': '0/1K0MLEHiEbMTl_jyQj-Rpw==/1087619310027296427.jpg',
                  'lurl': '1/QfwcW1WSJ9_9nB1_6_quNg==/2733684973831399645.jpg', 'dmt': -1856566984, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/t1J6Dz3T0h_mz8XbEUOtqQ==/114349209303512.js'},
                 {'id': 238543323, 'name': '背景', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 15, 't': 1336881467393,
                  'ut': 1336881496353, 'cvid': 7637245066, 'curl': '1/TcTgwBT6XhgmSC6NsiKHhw==/2741003323225725904.jpg',
                  'surl': '2/ywUuZCKb_xSV47OR6n_lKw==/1346857763577844787.jpg',
                  'lurl': '0/VGFW3n8ODoGGQrTAz1PF3A==/2707507800997312527.jpg', 'dmt': 1836257497, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/iIGl0kV2R2SllDn1V4wO-g==/173722837913702.js'},
                 {'id': 238543325, 'name': '小花', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 37, 't': 1336881582581,
                  'ut': 1339206196682, 'cvid': 7688005775, 'curl': '2/sTrqx2ouV8fSjy3dmk-FuQ==/2649523955794633373.jpg',
                  'surl': '0/xoiDW7lYPqOnTlcNkmkZOQ==/2649523955794633374.jpg',
                  'lurl': '1/GTQ2xlTkXuaC4vQ-QsR1Kg==/3387832819689537406.jpg', 'dmt': -1736079605, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/0LOVHIX9rgmC3IUO-bo0bQ==/43980465160810.js'},
                 {'id': 239656068, 'name': '净尘', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 87, 't': 1339205484732,
                  'ut': 1339205945329, 'cvid': 7688045339, 'curl': '2/IdPw6aH9maPoGvNLFnvUAw==/3070610520953956424.jpg',
                  'surl': '0/aLK7ZCVqChFbKXYU0KnEwA==/2516104816834164705.jpg',
                  'lurl': '1/q_Nw05J_irseIsU0N8_Z2g==/104427216377263498.jpg', 'dmt': 448664208, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/JOavELde_ZwzPgZWeKPZ5w==/6597070961041.js'},
                 {'id': 239656069, 'name': '红楼', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 94, 't': 1339205496366,
                  'ut': 1339205557618, 'cvid': 7688014668, 'curl': '0/RcgXPiE1FN8WM3vJiqwYZw==/1046242488450606414.jpg',
                  'surl': '1/kUUJBMXVQrsDNyrGf1BvgA==/1046242488450606415.jpg',
                  'lurl': '1/yr9VlgT9cVoach4ydVnfvA==/2509630892369820952.jpg', 'dmt': -1642319290, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/CS7vkLftl49yT5EfKuHPWA==/74766790761517.js'},
                 {'id': 239656070, 'name': '风', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 21, 't': 1339205589503,
                  'ut': 1339205621994, 'cvid': 7687994825, 'curl': '0/72xfGG1l2ujJQXnAMBzKzA==/1297599642653661582.jpg',
                  'surl': '0/xehNGM4o50WQssWhMMwZ8g==/2500060743161581665.jpg',
                  'lurl': '0/sBXdG58HQTY0mI9TNC6kAg==/1353613163019153681.jpg', 'dmt': -464318831, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/nzAKH7-wDvu95vruR67kMQ==/197912093306111.js'},
                 {'id': 239656071, 'name': '剑三', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 202, 't': 1339205665773,
                  'ut': 1339205933069, 'cvid': 7688005296, 'curl': '2/eS-QNLtZ15jSsT1MT8zP1Q==/2580562586500707989.jpg',
                  'surl': '1/tx6k-F515dLHT2qCw9alWQ==/2685271277837075422.jpg',
                  'lurl': '2/6Qc6lhYPRo29wmffPzVKyA==/2532711840460096103.jpg', 'dmt': -1642142513, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/C1-Ntff2zbtrExC46x4NTA==/197912093072773.js'},
                 {'id': 239656079, 'name': '猫 喵喵', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 14, 't': 1339206281679,
                  'ut': 1339206307031, 'cvid': 7688045953, 'curl': '1/tW0CMDieHriXgCmc8IRB6g==/2709196650857608333.jpg',
                  'surl': '2/QIEhXxaZlZykRDctzZg1PQ==/2590132735708998296.jpg',
                  'lurl': '1/DDD9hHz0OCtUNGhVUF7Y_g==/2619969083240334904.jpg', 'dmt': -1965964500, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/VJ3ONK_MBtli7gXJSerfgA==/160528699219172.js'},
                 {'id': 239656083, 'name': '梦语', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 68, 't': 1339206355282,
                  'ut': 1339206394190, 'cvid': 7688006131, 'curl': '1/0EHdYHNzrpbPD3_-41aTBA==/1156017729367613518.jpg',
                  'surl': '2/H0ErDRTbYejMgy7Mr5aXcw==/1156017729367613519.jpg',
                  'lurl': '1/oJ_PmxaJePfZgfGhAlcuCg==/2563392612921554584.jpg', 'dmt': -1736053553, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/3VGGd91lJYrR-6cGPh5RBA==/122045790732746.js'},
                 {'id': 239656085, 'name': '清明', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 16, 't': 1339206396448,
                  'ut': 1339206418327, 'cvid': 7688006185, 'curl': '2/YyqX6e_Fnuku3_niIsjy4A==/2731151699040803426.jpg',
                  'surl': '1/g9LUZgYp_CfyDvC7Gz4QGg==/630503947849181422.jpg',
                  'lurl': '0/m2SCNKmzWZbhJMbopYKnSA==/1190920626463949064.jpg', 'dmt': 1625866084, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/5Ad7m6tt9ny-YqGlH6vLdw==/190215512292275.js'},
                 {'id': 239656086, 'name': '上古', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 42, 't': 1339206436700,
                  'ut': 1339206529260, 'cvid': 7688046250, 'curl': '2/kj-9KkZIzE3Hlhrv1td-dw==/2607584184265132259.jpg',
                  'surl': '2/GrPCeMVAoYxdDEKmWppaGg==/604045300038674252.jpg',
                  'lurl': '0/SEgdIUDC-NqyliQayY1NrQ==/606015624875647233.jpg', 'dmt': 151703417, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/c3kbUp0H6O4ZasFqcYr06Q==/68169721348497.js'},
                 {'id': 239656087, 'name': '怪', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 50, 't': 1339206547801,
                  'ut': 1339206578883, 'cvid': 7688036403, 'curl': '2/82m5_bODnmVsKNBWhbnhWw==/566046178182736883.jpg',
                  'surl': '0/5V-4FMBV735h5OXGQnGSqw==/598415800504461774.jpg',
                  'lurl': '1/hglPrpoCPWWei0itaUBgSQ==/2732559073924654594.jpg', 'dmt': -1577993557, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/JEsGAr_KF_AzNby23qLewA==/224300372152558.js'},
                 {'id': 239656089, 'name': '凌源', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 35, 't': 1339206620162,
                  'ut': 1339206647583, 'cvid': 7688036536, 'curl': '2/XbMoIBJ2PIshL-jiF8rmjg==/2387189277500002907.jpg',
                  'surl': '0/0ICE0vLlUY6-YzYsIsjOsA==/2387189277500002908.jpg',
                  'lurl': '1/x94Tfe8hXH3-LQT66wglPg==/3704210693512243270.jpg', 'dmt': -1642980323, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/K-ofv90OMMM8UZiHKXFo3g==/205608674466501.js'},
                 {'id': 239656091, 'name': '枪', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 25, 't': 1339206698026,
                  'ut': 1339206732423, 'cvid': 7688026770, 'curl': '1/md1B-lxkcOvF3N_5XVwJag==/21955048200881767.jpg',
                  'surl': '1/3pVw5XrE9vqADDPxFxLOyQ==/2763521321362668409.jpg',
                  'lurl': '0/4tUpzZ66pywfSstxvyWFWw==/2732559073924654596.jpg', 'dmt': -1641855465, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/pN_JIC4HMRYoELHqw22kvg==/34084860534285.js'},
                 {'id': 239656093, 'name': '风景', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 65, 't': 1339206797127,
                  'ut': 1339206875993, 'cvid': 7688027082, 'curl': '0/RYpLBCROGyINf59r1OSoyQ==/2506253192649285885.jpg',
                  'surl': '2/bSrZTjQUjF2_wYewD8h0qw==/2682175053093448736.jpg',
                  'lurl': '1/OUkJFSMd-iesnHuFdlHUSg==/2732559073924654597.jpg', 'dmt': -1578031700, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/V7snLqCsnAJ81nK5x9gLzA==/15393162874461.js'},
                 {'id': 239656095, 'name': '发夹', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 37, 't': 1339206915757,
                  'ut': 1339206945617, 'cvid': 7687997274, 'curl': '1/cSnUiKmUz9JzMyvN7QC9fg==/635007547476846916.jpg',
                  'surl': '2/89od9FQZld48dlGqDuHVfQ==/618963473804339375.jpg',
                  'lurl': '1/k6JC9Vz7m92pN3KIhId4qQ==/2513571542043770035.jpg', 'dmt': -19287251, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/KaQv3F-3zg4WY0ByGUVOgg==/236395000367644.js'},
                 {'id': 239656096, 'name': '飞天', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 24, 't': 1339206950818,
                  'ut': 1339206975143, 'cvid': 7688067139, 'curl': '0/ql-T3E0xOTC4Qq1VGOwG8g==/1550082696763183566.jpg',
                  'surl': '0/Gsfw5n5l1sjfFqUGfw-AtA==/6597151130516571399.jpg',
                  'lurl': '1/_POzHwwwKPAFtmO-abL0cg==/102175416563576185.jpg', 'dmt': -1578041482, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/qAquN8HT76H89HqTWP32jw==/155031139602990.js'},
                 {'id': 243985049, 'name': '心怜', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 284, 't': 1346202649362,
                  'ut': 1346202859488, 'cvid': 7840624406, 'curl': '0/0g6aTgBzl9ydqUx1Zznqkw==/6597216001703846637.jpg',
                  'surl': '0/8Q_Tjul7lWJchw0umQbfuw==/6597340246517768577.jpg',
                  'lurl': '1/xDbBXrL8HPijbs7kt5z0ag==/6597333649448000008.jpg', 'dmt': -1856655194, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/tbXUBm8aO3Ek6JwzPHzxEA==/114349209303507.js'},
                 {'id': 243985054, 'name': '浅茜°', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 68, 't': 1346202982864,
                  'ut': 1346203047804, 'cvid': 7840644693, 'curl': '2/OSrKiRn2VwT73XNqoIVFlg==/6597158827099201289.jpg',
                  'surl': '1/Vf82WSrRI8_7EVOPuPyAvA==/6597374331378235936.jpg',
                  'lurl': '2/c-zywrCKSo7yIRFEKAjSjg==/6597368833820095091.jpg', 'dmt': -1856630107, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/1AL7sIbweAHUCOkSV8SOAg==/78065325586883.js'},
                 {'id': 243985056, 'name': '明泽', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 41, 't': 1346203146939,
                  'ut': 1346203181270, 'cvid': 7840654885, 'curl': '1/9Jt3Vq9eiQWieuZYKEEAOg==/6597167623192223506.jpg',
                  'surl': '2/euvdO5k1YvDd24ULcw-eXw==/6597167623192223507.jpg',
                  'lurl': '1/R0-Nf_eJEtOH6rujTd20cw==/6597167623192223509.jpg', 'dmt': -1578368262, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/X4rWIzRC_nikEedTZONXrA==/53876069847653.js'},
                 {'id': 244843201, 'name': '缘来——命来', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 89, 't': 1347860377465,
                  'ut': 1347860462416, 'cvid': 7874041693, 'curl': '1/6j-33-H5LhxL-GoItIftuQ==/1321525015674353125.jpg',
                  'surl': '2/hXpRwYOY19mdT1JcwaIEuQ==/1274800169540390180.jpg',
                  'lurl': '1/TykQDhR7Gcf8o4a-3JIn4Q==/93449692285759114.jpg', 'dmt': -1578391594, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/hGFNPNyViI85VrJcWhfdKQ==/35184372175478.js'},
                 {'id': 244843204, 'name': '轻然', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 23, 't': 1347860622199,
                  'ut': 1347860662714, 'cvid': 7874052067, 'curl': '0/kLavP8wkxMqITPrK96nNfQ==/2584503236175065637.jpg',
                  'surl': '1/xupVOPpsplp39q0Y6tai2g==/2584503236175065638.jpg',
                  'lurl': '0/wRqjeHHe-nkJU2kPNheVCA==/6597217101215633958.jpg', 'dmt': -1643036645, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/ZMc1dE6mpLJM_89Du9zbLg==/235295488417460.js'},
                 {'id': 244843207, 'name': '茗茗', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 25, 't': 1347860921548,
                  'ut': 1347860951762, 'cvid': 7874092699, 'curl': '0/DWAISpQMVt4gveK0WHMNyg==/2389722552290486703.gif',
                  'surl': '1/O0s_hCdg59q02PiTcX6vSg==/2745506922853460827.gif',
                  'lurl': '2/dtpH9Gpa4p6nn5KtSJwP9A==/6597652507818840044.jpg', 'dmt': -1643053927, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/IBPp9Pa1Gw_IX6tUwj-PrQ==/49478023322794.js'},
                 {'id': 259281596, 'name': 'LOFTER', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 118, 't': 1377757421542,
                  'ut': 1379809909000, 'cvid': 8471207236, 'curl': '1/FwQBT6uJwLrBuIwK40gxBw==/3170534137769053978.jpg',
                  'surl': '2/8uoY8RZWIoDMK84nBvCt3g==/3170534137769053979.jpg',
                  'lurl': '0/EoeMcw3g5b2xXJlpN-W7JQ==/6598234149471895722.jpg', 'dmt': 1125406984, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/Pm8Fi7xjEHsn2fsCPUiP6g==/6597074170974.js'},
                 {'id': 259286286, 'name': '月玲玲分', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 118, 't': 1377745073576,
                  'ut': 1377745625299, 'cvid': 8470843379, 'curl': '0/pXGlAWMx6IrLoSsTwj34XA==/2692871102208749907.jpg',
                  'surl': '1/AgfnKspvdRoxQgddNqgp7Q==/1891511843595830626.jpg',
                  'lurl': '1/xJwAIr6EBqNvcigNRl7ZcA==/22236523178292790.jpg', 'dmt': -938876717, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/K0z0DY3MiCxGKDKJMM4DoQ==/200111120406335.js'},
                 {'id': 259339034, 'name': '【雪樱の心情】', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 12, 't': 1377847046559,
                  'ut': 1377847156323, 'cvid': 8473007077, 'curl': '0/HF-sfL9taNQB-YoPSQ2KUA==/3321404725286021685.jpg',
                  'surl': '0/xBEFGzbfr6loyMBQ5IYofA==/1890385943689001010.jpg',
                  'lurl': '1/R1-C_09rxP1AqIHpd8cbxg==/2168201745702326299.jpg', 'dmt': -837345693, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/yk-mCc9NbkzZJWVQJXqKOQ==/46179492537962.js'},
                 {'id': 259339079, 'name': '感时花溅泪', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 60, 't': 1377848519391,
                  'ut': 1377848592314, 'cvid': 8473023525, 'curl': '2/grYq0z7JA002flqbCLSXJg==/1895171018293017938.jpg',
                  'surl': '0/m9F0GTBpQFDHrUJVwydAKw==/1895171018293017939.jpg',
                  'lurl': '0/HyhNuRAFXgrQY_6ETMKNsg==/6597647010262851675.jpg', 'dmt': -835909702, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/1LVIRMrTe0WsJPWzaGjkmA==/148434073923781.js'},
                 {'id': 259533116, 'name': 'taste the feel', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 67,
                  't': 1378284174059, 'ut': 1378284490103, 'cvid': 8482416605,
                  'curl': '1/9-Mgau0xFf0xLMMZI5AoXA==/2058145029808502353.jpg',
                  'surl': '1/nPOh3TQlc2K4U8LMy0O_AA==/1882786119317851066.jpg',
                  'lurl': '0/7IvEaMTUS5785orfNMiXDA==/1137440380987945296.jpg', 'dmt': -400011913, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/JbE8qPxN7qZ9rTWs1ffm3Q==/116548236797786.js'},
                 {'id': 259737647, 'name': '安心月亮', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 67, 't': 1378793367430,
                  'ut': 1378793742469, 'cvid': 8491736351, 'curl': '1/5LCEF1NA-y6T0_BEudakPg==/1714745558221499794.jpg',
                  'surl': '0/3P10PPJEpN1WJvAuI4YAYw==/1714745558221499796.jpg',
                  'lurl': '0/7_bxcgj5jRrCUBmXuo0BlA==/3049781372760125205.jpg', 'dmt': 109240453, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/ylWHJd_AD8IoVPrXBfXXYQ==/37383399681101.js'},
                 {'id': 259737758, 'name': '冰杀', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 17, 't': 1378795933410,
                  'ut': 1378795991838, 'cvid': 8491784752, 'curl': '2/DXD-AUxSJV8FZKIHqQnIog==/2496401568464459276.jpg',
                  'surl': '0/0x-IcXgOf5yhtuvTIzkqlA==/6597165424168083276.jpg',
                  'lurl': '0/nrqnuJ_7iCJIepJF0l8bDA==/4852628598591714780.jpg', 'dmt': 111489822, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/6xL_VUuYYZCr_YE7UyVdAg==/135239934555335.js'},
                 {'id': 259772828, 'name': '小声', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 23, 't': 1378885407888,
                  'ut': 1378885497365, 'cvid': 8493387856, 'curl': '0/7xw3__guBEI7VuG55Vjo-g==/2995738177231667283.jpg',
                  'surl': '0/GHvZ_azJIffruajVMFBi4w==/3162652838421071304.jpg',
                  'lurl': '1/gG0pezK-n4lRTvQdRW9FgQ==/303430024994149153.jpg', 'dmt': 201025215, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/9G0_03geUKAwxqzmX1GnjA==/34084864812677.js'},
                 {'id': 259959141, 'name': '秦时明月', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 120, 't': 1379296644407,
                  'ut': 1379297218131, 'cvid': 8501073133, 'curl': '2/ypMKpJeS9-APuw_4PBUFGw==/1624110615720707525.jpg',
                  'surl': '0/i9HPmacPTpSlYHq014j9Zg==/6597792145797742944.jpg',
                  'lurl': '1/gmCXCbdyrIaHVfiNVvcH0Q==/2229563290625121589.jpg', 'dmt': 612716115, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/aPFAP6_izK4Vyysfke92fw==/169324795094595.js'},
                 {'id': 260195823, 'name': '山海经', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 97, 't': 1379924215539,
                  'ut': 1379924460205, 'cvid': 8512622962, 'curl': '0/yoM3Hub3BxQPIpg-hOnFgw==/3128594366239071063.jpg',
                  'surl': '0/XlM5GMvvdZY5eHcBFvQnOQ==/1893482168433156444.jpg',
                  'lurl': '0/ABdW9o2tMMEpgHtzIGV1jw==/1678435286225769117.jpg', 'dmt': 1239958189, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/uY0-ErzWr0qa9wm6BIQpYQ==/146235051011711.js'},
                 {'id': 262206015, 'name': 'wodexiangce', 's': 3, 'desc': '', 'st': 1, 'au': 2, 'count': 457,
                  't': 1385079288137, 'ut': 1385079904308, 'cvid': 8607889583,
                  'curl': '2/uB9xZN6oXhnBm53Od899RQ==/1320680590744440032.jpg',
                  'surl': '2/HSuenqF8vb2DdHCAcanSLg==/2111062325430026981.jpg',
                  'lurl': '2/M8quy2aGcfIsH6GQIWvJdg==/2667256879328220842.jpg', 'dmt': 2100434996, 'alc': 'true', 'kw': '',
                  'purl': ''},
                 {'id': 265118611, 'name': '我为真', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 24, 't': 1393662681658,
                  'ut': 1393662756785, 'cvid': 8737633781, 'curl': '1/_GLnrSnrp24mzeXwgtPopQ==/1409626683467534548.jpg',
                  'surl': '2/8GlGZczliSPxxCzGgNHqVQ==/57702370326251366.jpg',
                  'lurl': '2/CxWQHlXbbCMdzJB70QVwiA==/4853754498498809192.jpg', 'dmt': 2093352881, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/Q-DIpRC0nuB8CANXVKXScw==/30786331950102.js'},
                 {'id': 266530434, 'name': '心情', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 99, 't': 1397275822758,
                  'ut': 1397276571909, 'cvid': 8795430638, 'curl': '1/pyAiIwWwfzxBd1CClMfjgg==/857091304184207398.jpg',
                  'surl': '1/hdX7Q-tZa1sbisxkPJDuYA==/2556074263527518665.jpg',
                  'lurl': '2/-o3bkrVwEVxQR8JIsEsGJw==/2257147838342997194.jpg', 'dmt': 1412200709, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/dWlgEzatxovZ6dPkzIzMIA==/134140425591320.js'},
                 {'id': 268127152, 'name': '月徕之心', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 10, 't': 1401676922121,
                  'ut': 1401676963075, 'cvid': 8867140559, 'curl': '2/Gqwv4-cyF-qj36nFLqBLxg==/6597887803309548293.jpg',
                  'surl': '0/HtXc91kzQhwboIWMnvBYdw==/6597887803309548294.jpg',
                  'lurl': '2/u-bFF_9EI_KDZpNJZHJKEQ==/147774362873839151.jpg', 'dmt': 1401676963075, 'alc': 'true',
                  'kw': '', 'purl': 's2.ph.126.net/OzdrWhcOjkVOmi_BrxGZ2w==/46179496094294.js'},
                 {'id': 287493497, 'name': '上邪', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 9, 't': 1427705508730,
                  'ut': 1428220195289, 'cvid': 9240548020, 'curl': '0/1ml8w5qgiqsafG3GvpTVrA==/6630467432350141161.jpg',
                  'surl': '1/KcoYAPwN04Ytu41vVvZgPA==/6630547696698968311.jpg',
                  'lurl': '0/AZArd9tZPGdyA3s9_UZ2QA==/6630928127722332717.jpg', 'dmt': 1428220195289, 'alc': 'true',
                  'kw': '', 'purl': 's2.ph.126.net/aaHwPkoPeTNVSHg0FzyhSQ==/137438965263107.js'},
                 {'id': 262442643, 'name': '我', 's': 3, 'desc': '', 'st': 8, 'au': 0, 'count': 97, 't': 1385801601803,
                  'ut': 1405235153998, 'cvid': 8619264916, 'curl': '0/yEyXVmgqSiXd0iuBF76A3A==/2059833879668872248.jpg',
                  'surl': '1/j1Hq8JmsQhAH8X9oanEHHg==/2059833879668872249.jpg',
                  'lurl': '1/RJrg-0I8f9hDtpPm9X7cCA==/3016567325508397450.jpg', 'dmt': 780848206, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/w8w0BUkXHAL74-hkX3LHeQ==/1099519720011.js'},
                 {'id': 305676095, 'name': 'sketcher', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 120,
                  't': 1477022823412, 'ut': 1477023310808, 'cvid': 9696663601,
                  'curl': '2/j5jKi5pIfSBkoGJK8ew1Rg==/6631591133236678007.png',
                  'surl': '0/wPmPXwPKyiTu-WM2Fdj95Q==/6631672497097126932.png',
                  'lurl': '2/qO9mYxTRvumAYcWZ26okdw==/6631503172306455380.jpg', 'dmt': -445439016, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/2fDw-oOP0dcH6wn571svkA==/267181333569431.js'},
                 {'id': 262703134, 'name': '曰明', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 163, 't': 1386471305568,
                  'ut': 1386471731339, 'cvid': 8630275375, 'curl': '2/UNbND4biSkiWWcsPAFTSBg==/1387953110260482389.jpeg',
                  'surl': '0/w3T7ASzJovy6TX-UGDrdJw==/1373316411471467130.jpeg',
                  'lurl': '1/pSeVEXhKraZF0K5QHsqdkw==/3174474787443068782.jpg', 'dmt': -802705269, 'alc': 'true', 'kw': '',
                  'purl': 's2.ph.126.net/VlPYk4Fa06-wphjC-OkcbQ==/91259470661723.js'},
                 {'id': 266017836, 'name': '若', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 358, 't': 1395916707154,
                  'ut': 1396406282041, 'cvid': 8780317029, 'curl': '1/3OtcO3Ca6efhhWcCdiA5-Q==/1460010704298339322.jpg',
                  'surl': '1/KIIxjKctXK3ODbIXiZcb6Q==/2266717987551404503.jpg',
                  'lurl': '2/MNSxQlDlSrrUIqRIG-GzwA==/1366279537053797456.jpg', 'dmt': 543595475, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/zPsT3Ic5HimHQr0gM59Tww==/225399890566606.js'},
                 {'id': 266221379, 'name': '离', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 162, 't': 1396406301277,
                  'ut': 1396407750788, 'cvid': 8780331184, 'curl': '2/CX5bkL0ND1RCYitTMvNjLA==/6598170377797800101.jpeg',
                  'surl': '1/YQ0_TpbPdFpRxuFlvpwTBQ==/1463106929042280115.jpeg',
                  'lurl': '2/toZRDEKiuIDu4dgFynefCw==/4848406473941382770.jpg', 'dmt': 1403751329, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/jEIgzyxmX4nAk0watF5aMg==/58274123273115.js'},
                 {'id': 229770079, 'name': 'mjt1220@126.com', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 24,
                  't': 1317517986307, 'ut': 1317518127723, 'cvid': 7256803085,
                  'curl': '1/DxQz8ERzidaXWEO5ELSQdA==/2491897968836418739.jpg',
                  'surl': '2/J7OF7qLhb77VVQ4ANtOZIg==/2491897968836418740.jpg',
                  'lurl': '0/w1acWz_mB2Jfwz-BMXhQHg==/2491897968836418741.jpg', 'dmt': -1636737676, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/-3N1NTeWKfLKtQaOQBGopw==/64871189292528.js'},
                 {'id': 224744802, 'name': '无失的亲情', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 5, 't': 1308055147336,
                  'ut': 1320925853243, 'cvid': 7030020097, 'curl': '0/kB2zJSIBNd7rTOH2wHaJlg==/3318871450396951083.jpg',
                  'surl': '1/7-y4wtY7xYepG1xwOFt7aQ==/3318871450396951084.jpg',
                  'lurl': '2/EtiNHUftAjzpBiMoL9OZHA==/3318871450396951091.jpg', 'dmt': 1403751329, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/IZ05f-gBlzyU9cWlktAaew==/116548239546862.js'},
                 {'id': 196318378, 'name': '紫心', 's': 3, 'desc': '', 'st': 1, 'au': 0, 'count': 10, 't': 1265606319388,
                  'ut': 1265692418459, 'cvid': 5742910408, 'curl': '2/HDADirEWCmmBornHnjflvA==/1200772250648659649.bmp',
                  'surl': '1/r58uwd5XZPrZ9fGpQbCmWg==/1200772250648659651.bmp',
                  'lurl': '2/AbpsjIN8Eh3997O_zrV5sw==/905786475056390672.jpg', 'dmt': 2077410176, 'alc': 'true', 'kw': '',
                  'purl': 's1.ph.126.net/OfN9qAsUo92tyjf3Xlr_8A==/267181359282429.js'}]
    def __init__(self):
        self.names=[i['name'] for i in self.xiangceID]
        self.aids=[i['id'] for i in self.xiangceID]
        self.counts=[i['count'] for i in self.xiangceID]
        self.purls_js=[i['purl'] for i in self.xiangceID]
        self.all_pic_nums=0
        self.aid=None
        self.count=None
        self.url=None
        self.xiangceurls = []
        self.url_js = []
    def get_info_by_name(self,name):
        index=self.names.index(name)
        self.aid=self.xiangceID[index]["id"]
        self.count=self.xiangceID[index]["count"]
        self.url="http://blog.163.com/mjt1220@126/album/#m=1&aid=%s&p=1"%self.aid
    def get_messages(self):
        for count in self.counts:
            self.all_pic_nums+=count
        for aid in self.aids:
            url="http://blog.163.com/mjt1220@126/album/#m=1&aid=%s&p=1"%aid
            self.xiangceurls.append(url)
        # with open('xiangceURLs.txt', 'w') as f:
        #     for url in self.xiangceurls:
        #         f.write(url + "\n")
        for js in self.purls_js:
            # if js=="":return
            self.url_js.append(js)
            # with open("url_js.txt",'w')as f:f.write(js+'\n')
    def parse_js(self,name):
        real_urls,pic_names=[],[]
        self.get_messages()
        self.get_info_by_name(name)
        index=self.names.index(name)
        js=self.url_js[index]
        comments = requests.get("http://"+js)
        comments.encoding = 'utf-8'
        data=comments.text.split("var g_p$%sd="%self.aid)[1].replace(";","")
        jd = demjson.decode(data)
        base="http://img0.ph.126.net/"
        for i in jd:
            real_url=base+i['murl'].split("/",1)[1]
            pic_name=str(i['id'])
            real_urls.append(real_url)
            pic_names.append(pic_name)
        return real_urls,pic_names
    def cbk(self, a, b, c):
        '''''回调函数
        @a:已经下载的数据块
        @b:数据块的大小
        @c:远程文件的大小
        '''
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        print('%.2f%%' % per)
    def down(self,name):
        urls,names=self.parse_js(name)
        i=0
        for url in urls:
            time.sleep(1)
            new_imagename = re.sub('[\/:*?"<>|]', '-', names[i])
            path = os.path.dirname(__file__) + '/wangyi_pic/'+name+'/'
            self.my_mkdir(path)
            pathnew = path + names[i]+'.jpg'
            if not os.path.exists(pathnew):
                urlretrieve(url, pathnew, self.cbk)
                print("It has downloaded %d pics"%(i+1))
            i += 1
            print("【%s】相册已下载完毕！Successfully！")
    def my_mkdir(self, path):
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        isExists = os.path.exists(path)
        if not isExists:
            # 如果不存在则创建目录
            os.makedirs(path)
            print('【%s】 created Ok'%path)
if __name__ == '__main__':
    # get_aid("紫心")
    # get_count("紫心")
    x=Xiangce()
    x.down('紫心')
    print(x.count)