c = 33193272573438901687137069041958072461118493827599952695078475142307269872695033337104152253224436940843778391482338662101986768918106831321681532133384605677475109821059864659552739769348021565974280304560037425321436433616552027256787070001013693201152986974059569931606272482207315453110847059498832635025
e = 49446678600051379228760906286031155509742239832659705731559249988210578539211813543612425990507831160407165259046991194935262200565953842567148786053040450198919753834397378188932524599840027093290217612285214105791999673535556558448523448336314401414644879827127064929878383237432895170442176211946286617205
n = 109676931776753394141394564514720734236796584022842820507613945978304098920529412415619708851314423671483225500317195833435789174491417871864260375066278885574232653256425434296113773973874542733322600365156233965235292281146938652303374751525426102732530711430473466903656428846184387282528950095967567885381
d = 21780352155588618020563641971337344243907391969899764877790673891831527301137
from Crypto.Util.number import *
print(long_to_bytes(pow(c,d,n)))
