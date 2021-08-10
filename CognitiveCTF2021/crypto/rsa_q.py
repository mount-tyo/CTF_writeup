"""
nc shell1.production.cognitivectf.com 15584
4636878989
93089
836623060
256931246631782714357241556582441991993437399854161372646318659020994329843524306570818293602492485385337029697819837182169818816821461486018802894936801257629375428544752970630870631166355711254848465862207765051226282541748174535990314552471546936536330397892907207943448897073772015986097770443616540466471245438117157152783246654401668267323136450122287983612851171545784168132230208726238881861407976917850248110805724300421712827401063963117423718797887144760360749619552577176382615108244813
1405046269503207469140791548403639533127416416214210694972085079171787580463776820425965898174272870486015739516125786182821637006600742140682552321645503743280670839819078749092730110549881891271317396450158021688253989767145578723458252769465545504142139663476747479225923933192421405464414574786272963741656223941750084051228611576708609346787101088759062724389874160693008783334605903142528824559223515203978707969795087506678894006628296743079886244349469131831225757926844843554897638786146036869572653204735650843186722732736888918789379054050122205253165705085538743651258400390580971043144644984654914856729
6078410600178719860725320675722672872181996798384907119212553793311315750429244099131469222021852237136223121311133780931000241125855949316105214991209407893854326389889435055000289791609492459481736963666648087906658445102007272741082838264131720224172915183567829389616783456112753389279867772266289257411362826185726781594294552150197523789022471014850178062272033305703417180823972594662208949403457656680154369695788110907374735965833877437913304597830044956886227710739612619398280905714995802591416998630383144324266247684426631989397135134854234700126123922859314298189098807851986697186266291609747134226214
"""

from typing import DefaultDict


# p = 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433
# e = 65537
# n = 23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864395158783509535039259714359526738924736952759753503357614939203434092075676169179112452620687731670534906069845965633455748606649062394293289967059348143206600765820021392608270528856238306849191113241355842396325210132358046616312901337987464473799040762271876389031455051640937681745409057246190498795697239
# c = 13925006792430713233174555208233800811232101914964195479581080148687421792884326101488565638966158319524661995496093048313734810764342971448163920627619172917279691427480566757759730679020344629104124290917316827483696323577114223836552367205588344656506459694196044875733909257660283659180736236336702451927401048291434446894983270506594854550458448494488247128346647785496320975125219060722981222650602111233676710587478870030733416648920371379300748106634096046753712862341609434319452976425019331046094290958861584333383744279675609162212635827775295005309896143105802702583638288391922995497525767129088839749147
# plain = 6357294171489311547190987615544575133581967886499484091352661406414044440475205342882841236357665973431462491355089413710392273380203038793241564304774271529108729717

# cypher = plain ** e % n
# print(cypher)
# import math
# q = int(n / p)
# print(f"q = {q}")
# lamda = math.lcm(p-1, q-1)
# print(f"lamda = {lamda}")

# def ex_euclid(x, y):
#     c0, c1 = x, y
#     a0, a1 = 1, 0
#     b0, b1 = 0, 1

#     while c1 != 0:
#         m = c0 % c1
#         q = c0 // c1

#         c0, c1 = c1, m
#         a0, a1 = a1, (a0 - q * a1)
#         b0, b1 = b1, (b0 - q * b1)

#     return c0, a0, b0

# c, a, b = ex_euclid(e, lamda)
# d = a % lamda
# print(f"d = {d}")

# q = int(n/p)
# totient = (q-1) * (p-1)
# from egcd import egcd
# d = egcd(e, totient)[1]
# if d < 0:
#     d += totient
# pt = pow(c, d, n)
# pt = str(pt)
# print(pt)
# index = 0
# import binascii
# for pti in pt:
#     if index%3 == 0:
#         print(" ", end="")
#     print(f"{int(pti, 16)}", end="")
#     # work = f'\x{pt[index]}\x{pt[index+1]}'
#     # print(str(binascii.hexlify(b'%' ,work), 'utf-8'))
#     index += 1
# 302679338E7365D2534405DAB208800197794B100532D7B8B0E3E4BA2A8B70B40EC9D177CD9DB826EA119790A182602CBF4A3F4F67A33881F67861CCA061843CB9A092808FEBE51535D167E00B90E06D5DB1461C52542DA5C13DC86D0CB110E40882EBE36A6150F600B3267970AC94496B47E7C80833A88B60FB87D8DC5D6139FDD888688AF81015C952FEAC354FAF71BAFD82A6E2EBEE668AA62D015AE6E5DA8539D39C446C8691ADF73F1C4A42F7976392C66C494866A6394D43A22AC448B730B30D05B756074116FC74AD75E8253ABE60367D4207D1E57CE038AA66392F98A76F00AD9A7A7F078D09E388ED80E11B1026E7557BAECD16FADAF3E5E76221F26


# q = n // p
# print(f"type q = {type(q)}")
# print(f"q = {q}")
# print(f"a = {p*q}")
# print(f"n = {n}")
# from Crypto.Util.number import inverse
# phai = (p - 1) * (q - 1)
# d = inverse(e, phai)
# pt = pow(c, d, n)
# print(pt)


# miniRSA
"""
eがとても小さい場合には、cのe乗根をとれば、dの算出は不要
"""
n = 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
e = 3
c = 632842384140587174830925541187412664996674169932996191508185732662783016874159287466298559845859187680481790912872257884508491688706582583466621670584934824968165027905248218081988895883829955005590459045563487575434041612025991120362101218958824365113954333662349365055333 
from Crypto.Util.number import *
import gmpy
m = int(gmpy.root(c, e)[0])
print(long_to_bytes(m))