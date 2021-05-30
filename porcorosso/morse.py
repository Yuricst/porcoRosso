

import time



morse_on = """

HM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@MM@MMM@@@@@@@@@@@@@@@@@@@@@@HHHBYY=<<;;;;>+
M@@H@@H@@@@H@@@@@@@@@H@@H@@H@@@@@@@@@@@@@@@@@@@@@@@@@@@@@MMMMM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@MMHHMM@@@@@@@@@@@@HHHHBYY71<;;;;++++&gAQWWkkq
@@@@@H@@H@@@H@H@H@H@@@@@@@@@@H@H@HH@@H@@@@@H@@H@MMM@MM#MHMBrAQQMM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@MH@HM@@HHHWY9YT1<;;;;++++&gQQWWkkkkkkkkkkkkkkk
@@@H@@@@H@@@@@@@@HMMHMMMMMMMHHHHWB9UUUUUUUUWMMMHWHMHHHHHM8OdHyyyWMM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@g@@@@@@g@@@@@HMY9Y71<<;;;++++&gdXWkkkkkkkkkkkkkkkkkkkkqkkkkkkk
@@H@@@H@MMHMMMH9UXvvvzzzvvrvvrvrrrvrvrrrvrwdHpfWHH@H@H@H#tdWyyyVyyWMH@@@@@H@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@g@@@@@g@@@HBYC++++&ggQHM#MHkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkqkkkk
@@HMMMHUXvvvzwwww0wQKHXXzvrrrvvrvvrrvvrrvdMpppWMHHHHHHHMRwMQkWyyyyyyWMM@@@@@@@@@@@@@@@@@@@@@@@@@@@@g@@@@g@@@g@g@@@HB3;juHHHHHHHHHHHHM#NHkkkkkkkkkkkqkkkkkkkkkkkkqkHHHHHWY9
HMMSrvrvvwwXWHHXQHHHWuXUuvvrrrrrrrrrrrrvdMpppWHH@@H@HH@MkwMHHMHkVVyyyVWMM@@@@@@@@@@@@@@@@@@@@@@@@@@@@g@g@@g@@@@gB6;+uWHHM#MHHH@HM@HH@HM#NkkkkkkHHHHHHHHHHHBYYYY7<<<<<>>???
BXvrvvwwWkMWHpHHHHKXkWWuzwzvvrrvvrvvvrvvHpfppWHHHH@HHHHMKrMH@HHHNkVyyyVVWM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@gH9<;jdkHHWHHkMMMHHHHHHHH@HM#MNHNM#HHHHHHHHMHg+;:;:~~_~~_<<<:<
vvvvwXUzwXXXkHHWMWHHHHHUuwwuzvrrvrrrvvvwNpfppWMHHHHH@HHHNwZMH@HHHHNkVyVyyWMM@@@@@@@@@@@@@@@@g@@@g@@g@@g@@@@#3;+jWkHMWHMkkkkHMMM@H@HHH@H@HMNMH#NNNNNNN#HHHHHNaJ-~~~~~~~~:::
vvvXXXXuXXHHWHHHHHHHHkWWyXXXvvvvrvrrrrrwNppffWMH@HH@HH@HHNOdMH@@H@HHNkVyyyyWMMMMMMMMMMMMMMMMMMMMMMMMMMMHM#3;+ukHHHHWMHHHWWyZZWMMH@@HMHHHMHH##########NN#HHHHHHHHgg&J-(((++
rrvwXXvzXXWHWHXHWXkHWWWUXwXXXXXrrrrvrrrwHpppppHHH@H@H@H@HMNOZMH@H@@HH@NkyyyyWHpppppppppppppppppbWWWQkkHW3;<+XyXWHWHWZyZZZZZZZZZHMMH@@@HHHH###############HHHHHHHHHHHHHHHHH
rvvrrrvzXXWSXHWWXWHUXWWWXWUXvrrrvvrrvrrvdHfpfWWMHHHH@H@HHHHNyrTHHH@H@H@HHyyyyWMWWkWkWHWYYYYHHHWWyyyyyXC;<jXyZWHHHHyyZZyyZZZZZZZZXMMM@H@HHH######H#########HHHHHHHHMHHMHHHH
rrrvrvwXUUXWUXXWHkWXWUUXvvvvrvvrrrvrvvvvdMWkHHyWMHH@HHH@@H@HHHyZHHH@H@H@HHyyyW0K_~.~~~~~(+dyyyyyZyyyV<;jdZyXHHWMyyyZZyZZyZZZZZZZZZUMMHHHH##HH#H##H#######NMH@HH@HHHHHH#HHH
vrvrvvvvz0XXyWUUZUUXrrvvrrrrrvrvrvvvrvvwQHHyyZZyZUMMH@HHH@HH@HHmOrTMHHH@@MWyWHwM:~~~.~~(zXZyZyyyyZ0z;+dyZyXMWHHZyZZZZZZZZZZZZZZZZZuZWM#HHH#HHHH#H#HH#H###NHHH@H@H@HHHHHHHH
rrvrrvvvzXXXvrvvrvvrrvvrvvvrrvrrvvrvrwdMyZZZyZyZZZZWMH@H@H@@H@HHHNsOtVHMMHNH9wdMc~~~~_(dZZyZZyyyX6<<uyyyQHHHMZZyZZZyZyZZZZZZZZZZuZuuuXMH@HHHHHHHHHH#HHH####H@H@HH@HHHHHHHH
rrrrrrvvrrvrrrrrrrrvrrvrvrvvvvvvvwQQHNWyZyZZZZZyyyyyZHHHH@HH@H@H@HHHNmgAwwAQgMNNHx~~~<JZyyyyyZyV>;+dZyWHNWMWZZyZZyZZZZZZZZZZZuuuuuuZuuM@@@@@@@@H@@HHHHH###HH@HH@HH@HHHHHHH
rrvrvrrrvrrvrrvvrrvvvvrwQQWWHmQHM#####NWyZyyZyZZZyZyyZWMH@HHH@H@HHMM#NNNNNN#NNNMXXn.:juZZZZyZX$;;jXZXWMWMHZyZyZZZZZZZZZZZZZuuuuuuuuuuuH@H@@@H@@@@@@@@@HMH#M@H@@H@HHHHHHHHH
rvrvvrvvrvrvvvrrvvvAkW9XvvvvvW#HHHH#H##NyyZZyZyZZZZZyXWHMH@@HH@HHM##NNNNNNN#N#M8rrwWwZZZZyyZ0>;<jZZQHHWMWZZZyZZZZZZZZZZuuZuuuuuuuuuzuuU@@@@@@@@@H@@@@@@@MMH@@HHHHHHHHH##H#
rrvrrvvrrvvvvvvvvwQNvvrvvvrvvvMH#H#H#H##NyZyZZyZyyZyXWqqHHHH@HHMNNNNNNNNNNNNMMBrwQWZZZZyZZZV>;+dZXWHWMWZZZZZZZZZZZuuuuuuuuuuuuZC<<?OC77W@@@@@@@@@@@@@@@@H@@HHHHHHHH#H##H##
vvvvvvvvwAQgQNMHH#HMkvvvrrrvvvZMH##H#H#H#NyyZyZyZXWHqqqHMMMMM#NNN#NNNNNNNN#MHBAV3?NXZyZZyy6;;+dZqHWHHZZZZZZZZZZZZuuuuuuuXZVwZ>~~~..~_~~(Hgg@ggggggg@@@@@@@H@H@@HHHHHH#HHHH
wwQgQNM####H##H###HHKvvrrvvrrrvd#HH#H#H#HHNWyyyWWqHHNMMHggggMMMMNNNNNN#MMMmMM9<::<jNkXZZX$;;+dQHHWMyZZZZZZZZZuuuuuuuZC7>~~~~~~~..~~....~?Hmmmmgmmmgmgg@@@@@@@HH@HHHHHHHHHH
#H####H#H#HH###HHH##NvrvvrvrrvvvM##H##HH###MHWMHH9UXMHggggggggggggggggggmHM5<:::_dNMMNkX$;;jXWMWHWZZZZZZZZuuuuuuuuZC~~_~~~~....~...~.~..~(UHqqqqqqmmggmg@@@H@@@@MMHRz?>>>;
H#H#HH#H#H##HHHHHHH#Nkvvvrvvvrvvd####MMMBSvvvvrrrvrvrwWMHggggggggggggggHH8<:::::jNNSWMN$;:<dHWHY70ZZZZZZuuuZuuuuuzI~~~..~..~.~..~..~.~~..~~?THkkkqkkHHggHHmggmmgmgMMNe<>;;
#H#HH#H##H#H#H###HHH#NWkwvvvrvvvvMMHSvvvvrrrvrvrrvrrrrrvvVHHHggggggHMHMM3:::~:::dNNNOdNc;jdHWY~~~~~?XuuuuuuuuuuzzZ~~~.~..~..~....~..-((++<(-_~~_~~~_~_?WmqkqqmgmmgggMHHx;;
H#####H#HHH#H##H#####NbpppkkXwwAQHHSvvrvrrvrvvvvvvrvvrvrvrvrrwXUUUUXvwX>:::::::<MMMMNrMbjWWB!~~~~~~~(XuXuVV+CXzZO>~..~.~~.~.._-(JzOOlz<<:+llOOVO--_..~._7HqkkkqgmmmmggMMm+
##########NN#NNMMMMMHHNQQHHHMMHHWHHWWUWyXQAyrvrrrvrrvrrrrrrrrrrrrvrrwWSXVWWfpWWWMMNNMkdNXH=~~.~.~~.~~<~~~~~~~?<~~~~~.~...~~(XXAAAmwvOzzzwwAAAAtttwAXC.~.._4Hkbkkmmmqmmg@HM
#NNNN#MMMMMHHbppppppppbpbppWHHHUrrrrrrvrvvrwUHmyvvvvrrvvrrrvrrrrrrrrd>:::(<:::::dNNMNKd#D~~.~~.~.~~.~~~~~.~.~~..~.~.~...~..~zlXWWS===??=?dyZZ0?==dfk_.~.~.~?WkbkkqmmmmgggM
MHHbppppppppppppppppppppWHMpbWvrvrvrrrrrrrrrvvvXWmvrvrrrvrrrvrvrrrrv0::(+>++<:::dNMNN#wMr~.~~.~.~.~~.~.~.~~...~..~..~~_((&zzZZYTTTOOOOOCOOOOOCzzOOTTI==lz+.._vHkbkkqgmmmgg
WpbbpbbbppppppppppppbbWMHppppkvrrrrrvvrrrvrrrrrrrwWkrvvrvvrrrrvvrrrvI:+I1zdV<:::?MNNMNwM%~~.~~~~~~.~~~~..~.~.~~.~~.~_JVw0l==XI~~(+>>1++zzlOOlzz++>>???zwZ=Oo-.?Wkkkkkmmggm
?THkWWWWWWWkbppppppppWNpbbbppWXvrvvvrrrrrrrrvwwAwvrdHwrvrrvrrrrrvrrdr<<+wWSz1;:::dNNNNH#$~~~..~~~~~.~.~~..~..~..~..(dZOw=zz<~~~(?+zlz<<++++++<;;<+1z>>???jwOo__(kbbbkqqqmg
..~_TG+::::<<<<??7TTTYY99WHbpWkQKHmwrrrrrvvrrdKWHrvvZHwvrrrrvrrrrrvd$;+74UCu0zv<:?MNNNN#?C+>++~~.~~~.~..~.~..~....~(Ollr=v<~~(+z=<!~~!!!<<<<<<<<<<<>?1+>?1z1v(jWpppbkkqqHH
......_11_~:~::~:~::~::~:~~_..._~?77TUXXwwwzvvw0vrrrvZHvvvrrrrrrvrrdP<<+Z1O0z>::((?MNNM3:(+<:?l~~.~.~~.~.~.~.~.~.~.(ll=t<~~_(z=<! `` ` ``` `` `` `` ~~(1>>??dyyyVfpWWWVVfp
_~..~...._1-:~~:~~:~~~:~__..~............~_<?7TTXwwwvvdkrrvrrvrrrrrwR::+<1Ovv<:jM<::?=<:<+z1z<j:~~.~~.~.~...~...~..jl=?I:~(+=z<+..............       (-~1???duZXXXZZyyVVff
~<<?<+(--~._?+_~~:~:::~.......~.....~.........~..~~_?7TUXAyvrrrrrrrrW<<<:+Cz<:+@Mc:::::::(<v>::O_~~.~..~.~.~.....~.jl=?v:(+zv<<<<<<<<<<<<<<<<<<;;<;>?+1+(1??zvzuuuZZyyyVff
_:~:~:~::?1(-~?&_~:~~::__~......~.....~....~.............~_<?TTXAwwvZb::<<jC::dHHMm<:::::::::::(<~~~.~.~~.~.~.~.~..(==?l<+vz< ``` `  `` ` `` `` `` ``  (++z?OrvzuuZZZyyVff
MHaJ_::~~:~~::_~?G-:~~<11z+(----_~~..~..~....~..............~..~._??TWo-(<<:::?M@H@@HHmmmaJ+:::(l~..~.~..~...~....~(=??z?1=>_ ` `` `` `` `` `  ` ` ` `` 1;1?zrrvzuuZZyyVfp
mgmgHHaJ_::~:~::~:?A_:~~~~...~.~~<?77C1(---_..~.~~.~~~~.~~...~........~_?7Cz+<:dHH@HH@@H@@@@Ne(+2~~..~..~..~..~..~.j==?z>z1>+(--(--------------------..(l>+zztrvzuZZyWWWkq
ggggggggHHaJ_:~::~::?+::~...~......_<?771&jgsAa+J-+++17<<+11+((---_~.......~._?77MMH@HH@H@H@@@Hj>~~~~.~~.~~.~..~..~j==?z?zz;<<<<<<<<~~~~~~~~<<<<<<<<<<<1l<+zOrvzuZXWpbkkqq
gmggmggmggmgHHa+_~:~:?4+_-((JJ+zzz7T7=<<<<<~~~~~~~~~~~~~~~~~~~~~~~~<?7Ci---_~...(i+J7TWM@@@@@@@#~~.~.~..~..~..~..~.(==?z>ztz_``````````` `` ````` `` ``(v>j?OvuuyyVppbkqqm
ggmggggmmggggggHMHkVT777<<~~~~~~~~~_((JJ+awXUW9UUUUUUUUUUUUU9UUka&JJ--~~~~_?771J-_.._?7C+J?TWM@N<~~.~~.~.~..~..~..~jz==z??zz<.  `     ` `  ` `  `  ` `.+z>v?wuZZyyfpbkqqmg
MHggmggggggggmggggg@HmJ_~_((JJ&wUUUUvvvvvzzzzzvvvvvvvzvvvvvvvvvvvvvvvzUUUG&J_~~~~?7C(.~.~~<<i._?1_~~.~.~~.~..~..~.~jz=?z??1lz<-..--...................1z>z1?wZZyyfpbbkqqHp
HHMHgggggggmgmgggmggmggHMMNHHM@gHHHkQQQQQmQmmmmmmmmAwwwwwvvvzzvvvvvvvzzzvvwwXWX&.~~~~~?T&._.._?1(>~~~.~..~.~..~~..~jI==zz?>ztz>1z<<<<<<!!!!!!<<<<<<1llz>z<??dZyVfpppkHHWUU
HHHHHMHggmggggggmggmggmgmggMMNNHqqqqqqqqqqqqqqqqqqqqqmmmHHMMMHNNQKBYYYYTTC1<<<+17TTYTUw+J-?7i-_~(S_.~~.~~.~~.~.~.~.jIl=dz???1zz+<. ```` ` ` ` `  ..zz>+z<??=dyyVfpbHWU0zzz
HHHHHHHMMgggggmgggggggggmggmgggMMMHMMM@MM@@@@@@@@@@@MM@@HMMMBUZvz<;;;;;;;;;;;;;;;;;;;;;;;<OTGJ?71d-~~~~~~~~.~~~._(JdtllOz?????zOz+<_..```` ` ..(+z<>+z1???==dVVfWHUXvvwXXk
HHHHHHHHHHMMHggggggmgmggggmgggmgmggMMNkXwAAwwwrtrtrwQkW9ZtttOz<;;;;;;;;;;;;;;;;;;;:;;:;;;;;;;;?4+_~<?1J-_~~~-(+XWyyfZlldOzzz??>1?zOz<~~~~~<<<<>;+++z1???===lXVpWUuXXZUUUUU
MHHHHHHHHHHHHMMHggggmgggmgggmggggggmmggMMNmAttttAgWSttttttO<!___<;;;:;;<__<;::;:;;:;:;;:;;;;;;;;;7n(~~~~?77TWWfVVyyWwllwZwwI???Oz??+1z1+((((+zzz11tO??===wulXb9wwwQmAwvzuu
kHHMMHHHHHHHHHHHHMHggggggggggmgmgmggggggggggMNmHStttttttltO_..`..(:;;;;;-(;:;;;:;:;;:;;;:;:;;;;;;;<?WUS&-~~(JWppV=<<~<?C0zllz===?z???????+1++++?1zz1zzzzzzOdkSwXHYTTHHkzuz
bkkkkHMMHHHHHHHHHHHHHMHggggggggggggggggggmgggggHMMmgytttlttO- `.-;;;;:;;;;;;:;;;;;::;;;;;:;:::;;;;;;?UWWHHHWWpK!~..~..~.~?UyyWZZV>::::~::duXzzu<:~:::::~~__?4XH3:::(+WHuuu
kbbkkbkkbHMMHHHHHHHHHHHHMMHgggmggmggmmggmgggmgmgmgmgMMmgyttttttlzz+;;;;;;;;;;;::;;;;:;;:;;;;;;:;;;;++lOlz+;;<7G-~~..~....~_7Vyy3<~:~~::~:zXuuuX>:~~:~~.....~_W>:++d=?dMkWW
kkkkbkbbbbbbkHMHHHHHHHHHHHHHMMHgggggggmgmggmgggmgmgmmgmgHMNmAOttttttlz++<;;;;;;;;:;;;;;;;;;;;;<+1zllllluZC:;;::?S-~..~.~..~_?W$::::~::~::dZUOld>~:_..~_~..~..(uZI=W==dMSZZ
kkkbbbbqbbbkkkkkHMMHHHHHHHHHHHHHMMHggggggggggmggmggggmgggggmgMMHmAwtttttttzzz++++++++++++++zuwOlltltOQV3;;:;::;:+h__~.~~__(::+>::::::::::dVtttd>_....__.~.~.~(Kz?zH=jHMZZX
kkkHkbkbWkkkbbWHkbbbHMMHHHHHHHHHHHHHMMHgggggggmgggmgmmmmgmmgggmmmgHMHmgyOtttwXXXyyXWUU9UUUwOtlltOQd93;;;:;;:;;:;;?n+&+<::::::jc::::::::::dWttw0~.~~.._<....~-dz?=ZOzd@SZXM
kHkkbkbbbkbbbkbHHkbbbbppHMMHHHHHHHHHHHHHMMggggggmgmgmgmgmggmgggmmgmgmmmHMMmgAtttttttltltllttwQX9UOz;;;:;;;:;;:;<+++<;<?G&;;;:<n::::::::::dWrtwS~~..~~__~.~~(dD=?=zzdHNkqMH
pkbkkkkkkbkkbpbbbbbkbkkkkkbbHMMHHHHHHHHHHHHHMHgggggggmggmgmgmmgggmgmggmmmmmmHMMmmAOtttttlZUUOlltv<;;;:;:;;;<++zllll<::;;<7TOu&+Oe&+++++++WKrrw$~~.~..~.-(?WH@R===1dHMZXMHM
kkbkbbbbbbbkbbkkbkbkkbbkkbkbbbbbHMMHHHHHHHHHHHHHMHggggggmggmgmmgmggmggmmmmmmmmmmmmHMmmQAwOttlttlz+<;<++++zzlllllllz<;::;::;;;;?74&+;;;:(HH0wwWC<?1<+<?<~~.(MHN=?udMHZZXM5<
bHkbkpbbbkbkbbkbbbkkbWkHbWbbkbbbbkbbHMMHHHHHHHHHHHHMMHgggmggmggmgmggmmmmgmmmmmmgmmgmmmmmmHHMMmAOOOwwOtttlllltlllllz+;;;:;;::::;:;;?7O&+<<<<<<;;;:;;;<~-.~~(WHHHkMMZZZZWN;:
kbbbkHkbkkbkbkkkbbbbbbkkkbbbkHUUWbkbpbbpHMMHHHHHHHHHHHHMMHgggmggmggmggmmmmmgggmggmmggmgmmmmmmmmmgHmmmHMmmgAOtttltlltz+<;;;;;:;;::;::;;;?77TTTOOu+;;<~~+~~~(HWHHWZZZZZZUMNg
bbkkbkkkWbbkbbbkkbbkbbbkkkbkbWc;;<?TWWWbbppbHMMHHHHHHHHHHHHHMHHgmmmmggggmmmmmmgmmmmmmmmmgmmHHHMMmmmmqqqqqmmHHHHHmHmmmAAwz++;;;;;;;;;;;;;;;;;;;;;<7U+__>~~_dWZZZyyWHWHpWXyW
bbbbkkkHWkkkbbkkkbkkkkkpbbbb9>;;;;;;;;?TWpbbbbbbkHMMHHHHHHHHHHHHHMHHgggggggggmmmmmmgH@H@MMHgmmmmmmmmmmmmqmqqqqqqqqqqqqqqqqHHqkWkQmgag&J+++++++++<;><7GJ__(HWWWWkkkkkkXXXQk
kkkkkkkbkkbkkkbbkkkkbkbkkbH6>>>>;;;;>;;>>>?TUWbkkkkbkHMMMHHHHHHHHHHHHMMHggggggggggggggggggmggggmgmmgmmmmmmmmmmmmmmmqqqqqqqqqqqqqqqqqqqqqqqqqqqqqHHHggHMMHMgHHHgHMMMHgmmmmH
kkkbkkkkkkkbkHHWU9UTTTC1???>>>>>>>>>>>>>>>>>?>?zTUHkkbkkkbHMMHHHHHHHHHHHHHMMHgHY7UgggggggggggggggggggggggggggmmmmmmmmmmmqqqqqmmmqmqqqqqqmmqmmqqqmqmmmmmmmmmmmggmggggmgHMMM

"""

morse_off = """

MMHM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@MMHMMM@@@@@@@@@@@@@@@@@@@@@@HHHYYY=<<<::::(
HM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@MMMMM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@g@@@@@@@@@@@@@@@@@@@@@@MMMMMM@@@@@@@@@@@@HHHHYYT7<<::::(((J+&gQXWbkk
M@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@MMH@MMHMHM8OAQXMM@@@@@@@@@@@@@g@g@g@@@@@g@g@g@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@MMHHM@@HHHWYYT7<<:::(((+J+&gQXWbkkkkkkkkkkkkkk
@@@@@@@@@@@@@@@@@@MMMMMMMMMHHBBW9U9UUUUUUUUUWMMMHWHHHHHHHM6wKWZyyWMM@@@@g@g@g@@@g@@@@@g@@@@@g@@@@@g@@g@@g@@g@g@@g@@g@@@@gHHY9T=<<::::(++++gdWWbkkkkkkkkkkkkkkkkkkkkkkkkkkk
@@@@@@@@@MMMMMHB90rrrrtrtttttttttttttttttttAHHVVWHH@H@H@MDlWyZyZyZZWMM@@@@@g@@@@@@@@@g@@g@@@@@@@g@@@@@@@@@@@g@@g@@@g@HBYC+(JJ+ggQHMMMNkkkkkkkkkkkkkkkkkkkkkkkkkkbkkkkkbbbb
@@@@MMMBUwtrtrwwAyVwQXH0XwOtttttttrtttttttdMfffWM@@H@H@HHIdNQkXyZyyyyWMM@@@@@@g@@@g@@@@g@@@@@@@@@@@@g@@g@@@@@@g@@@HB3:+jHHHHHH#HHHHHMNNHkkkkkkkkkkkkkkkkkkkbbbkkWHHHHWBYYT
@@MM8tttttOwXWHHkQWHHXzXXvrttttttttttttttdNffVWHHH@HHH@HMZdHHH@HkyyZZyyWMH@@@@@@@@@@g@@@g@gg@g@@@@@@@@@@g@@@@@@@#3<<+XHHMMMMHHHMMHHHHHMNNHkkkkHHHHNHHHHHHHHHHWUWZZXx<::::;
MM0ttrrOwXXMWHWHWHHHXXXkwwwrrtttrtttttttrHfVffWM@HH@@HH@MRtM@@HH@NkyyZyZyWM@@@@g@@@@@@@@@@@@@@@@g@@g@@g@@g@g@H9<:(dkHMWHHbHMMHHHHMMHHHHHMNNMMNNNMMMM#H##NHkXZZuZZuuuzI<:::
ZttttwdUwwwuXkHWWMWWWWWUUwwwzwttttttrttrwNfVVVWM@H@H@H@HHNOvMH@HH@HNkyZyZZUMH@@@@@g@@@gg@@g@@@@@@g@@g@@g@@@HY:<+WkWHbHMkkHHHMMMHHHH#MHHHH#M#NNMNMMNNMNMHHHH#NHkZuuzvrZ<!_.
trrrrrwXXwXWHXHpHHHHHHWWWXkXrrttrttttrttwNfVVVWMH@H@H@H@@HNOvMH@@H@H@NkyyZyZHM@H@@H@@@@@H@@@@@@@MMMM@@@@MM3:(jHHHMHWMHWWyZZyyWMMMHHHH#HHMN#NNMNNNNNMNMMMMHHHH###MMNm+J((((
ttttrwrrtwwWWWWkHXWWWWWUXwwuXXUOttttttttrHfVfVVHMH@HH@@H@HHNywMHH@H@H@HNkyZyZWNpppffpppffpfppWWkWWUUYYT7=:(JXZXWMWMWyyZZZZyZZZyWMMMHHHHMM#NMNMNMNMMNMNNNMNH##HHHH##HMNHH#H
ttttttttrwXWSwWWUXWUXXUyXuU0ttttttttrttttdHVfWQWMHH@HH@HH@HHNstdMH@H@H@@HHyZyyHNkWWUYYT""7<!~........__~~JXZZqMHHHyZZyyyZZZZZZZZZWMMMHHN#NMNNNMNNNMNNMNNMN##HHHHHHMM#M#HHH
tttrtttwXUwwUUwXppWWXUUwtttttttttttttttrtwMWHWZZZWMM@@H@H@@HHMNytTMH@HH@H@HyZyHdr.....`..`.``.``.`.-_~~(dZZXHNWMWyyyyZZZyZyZyZZZyZZWMM#NNNMNMNNMNNNMNNMMMMMHHH#H#H#NH#M#H#
tttttrrttrrwwXUUXXVOtttttttrtttttrtttrttAdHZZZuuZuuWMH@H@H@H@H@MNstZWMHH@HNZXH6d@..``.`..`..`...`.__:(zuZZWMWMHyyyyyZyZyZZyZyyZyZyZyXMM#NNNMNMNMMNMNNMNNMMM#HHH#HHHM#HN#HH
ttttttttrrtrrttttttttttttrtrtrtttrrtrtQHWZZuZuZZuZuZXMHHH@H@H@H@HHMmslOVWHMB6OdNN,`..`.``.`.``..._::(XXZqHHHMyZyyZyZyyyyyZZyZZZZyZyZZyM##H#H######MMNMNMMMM#HHHHHH####N#HH
ttrtttttttttttttttttttttrttrrttrrwQgH#MKZZuZuZuZZZZZZuUMH@H@HH@H@@HHMNNmggggMNNN#X+..`..`..`..._~::(dZQHNWMWyZyZyyyyyZyZyyZZ0C<<<?TyZyMHHHHHHHHHHH#H##NMMMMH#H#H#HHH##N#H#
tttttttttttttttrttttttwAQUU9VXNHH#HHHHHMkZZZZuZuuZuZZZZWMH@H@@HH@HMMNNNNNNNNNNNM8tZh,..`....`._~::_jXXMWMHyyZyyyZyZZyyZyZZyZ>.....-dyyW#HH#HHHHHHHHHHHHMMM##HHH###MMNNMMNN
ttrtrtrtrttrtrttrtrrd90rtrtttrZMHH#H#H#HMkZZZuZZuuuuZZXqkMH@HH@HMMNNNNNNNNNNNNM#ttOd!..`.`.._~::~(jqMHHMZZZZZyZyyZyyZyZyZyZyk._--(JZZZUHHH#H#HH#HHH#HHHHMMH###NNNMMMMNMNMN
ttttrtttttttrrwwAggHMwrtttttttrdHHH#HH##HMkZuZuZZZZZXWqkkHMHHHMMNNNNNNNNMNNMMM#rAZ8~..`...._::(d&dHHWMWyZZZyZZZZyZyZyZyZZyZZZZZZZZZZZZZM#HHHH#HHHH#HH###N#MNMMNMNNNNMMNNNM
trtrtrwAQgQHM#H#HHHHHKrttttrtttrW#HHH#H#HHMkZZZuZXXWqqHHMMgMM#NNNNNNNMNNMNMMHMyY<~?n_....-_~:(dXWMWMWZZZyZyyZyZZZZZyZZZZZZZZZyZZZZZZZ0UVMHHHHH#HH#HH#H#N#MMNNNMNMMMNMNMMNM
QgmHM##HH#HHHHHHHH##HNOrtrttttttZMHHHHHH#H#HHXXXWHHHMMHmggggmggMMMMMMMMMMgmMH3~~~_jMNe---~:~(dqMWHHZZZZZZyZZyZZZZZZZZyZZZZZZZZZZZ0V77~_._7M#HHH#HH##MN##NMNMNMNMNMNMMHHHHH
HHHHHHHHH#H#HH#HHHHHH#kttttrttttrdMH###H#MMH9VVVrttttZHHHggmggmgggggggmggHM5~~~~~(NMMNNX$::(qMHWMZZZZZyyZZyZZZZZZZZZZZZZZZZZZZZZV~........(WH#HH###MMH#NNMNMMMHHHMNNx;;;>!
H#H#HHH#HH#HH#HH#HHHH#NXwrttrtttrrM#MMBUwttrttttttttttttXHHHgggmmgmgmgHNM9~~~~~~(MMNOdMP<:(dNWHWXZ=7TTT=???7<<7TXZZZZZZZZZZZZZy0:........-.._7YWHHY9"TMNMHHH#MHHHHHMMm+;<.
HH#H#H#HH#HH#HH#H#H#HHMWpkkwwrrttrdH0wttrtttttttttttttttttrrVTHMHHHHMBSd3~~~~~~~(MMMNOdN<jHHH8VC!..............._?XZZZZZZZZZZZX>_((JdUUCziZUG+.-......-7M#MHHH#MHHHH#MMm<<
HHHHH#H#HHHHH####NNNMMMNffppWWQkWMHpkwwwOrtttrtttrtttttttttttttttrtttrdi(JJJJJJJ(MMMM#vTIXWY_.__........`.`..`... (XVVVTC?CXQkHHWXXXXz+++wXXwwXXXWAJ,...-TMMHHHH#HHHHHMMNx
NNNNNNNNNNNMMMMMMHppppfWHHHHppWHHUUOtttrrZVVWWAOttttrttttttttttttttttdY?77777777TMMMMNo(N9!.....`.`..`.`.`.`..`............_dUWMMMSuuuuuuMMMMNuuzWM#_.`.`.(HNMHHH##HHHHHMN
MMMMMMMHHppppffffpffffpffpWkHHW0rtttttttttttttrVHmOtttttttttttttttttO$~~~(<___~~(MMMMNOd#_...`.`.`.`..`.`.`.`..`.`......-.-(jQWMMMmQQQmmQMMNNNQQQdMH-(.---..?MMHHHHMMHHHHH
kppfpffpfpffpffpffpffffpWHHffpSrttttttttttttttttttVkOtrtttttttttttttw>~(v>+dc~~~~dNMMNRd#_.....`..`.`..`..`.`.`..`..`-(UM8zzqW<::+zzzzXXQQmmmmXzzzzzzzwQXWN,.(WNMHHHH#HHHH
_7WkWffpffpffffffpfpfpWHHpffffkOtttttttttttttttrtttOWyttrtttttttttttd<(<+jWI<_~~~(MMMMNM#_.``...`.`.``.`.`.`..`.`.`.(kXWUzzZ7C:(JwQXHHH9UUZuXUUHHHmwzzZU0wQX{..dNMHHHHHHHH
``` ?T9YT\"\"\"\"TTTYYU9WWHpWWWWpffkOAAsrttttttrttdHXRtttdktttttttttttttd<_(wWSzjz+<~~dNMMMN@i---- ..`...`..`..`.`.`.`.(SvzXXXS>::+QWHHWQQMHH#H#HHMNmyzUWkzvzVH8$_(MMHHHHHHHHM
``````.?1-~~~~~~..~~.~~.~~~_~~<?7"TTXwwwOrtrttZUV0trttdyttttttttttttd<(<(z1z0z>~~~_WNMMM:~(<~(l-..``..`.`.`.`.`..` (=7CXV>::(dWKHQdHHHHHHHMMHHHHHHMmy?4XzzzzWMMHHHHHMMMmmm
`.```````._1-...~..~...~.._```````````.` _?7"TVwwwOttrtHOttrttttttttdr~_<<iOz<~_+P~~?W8:~(zz(<(l`..``.``.`...`` `  `````` _+XW8XHHHHHHHHM%``(MHHHHHH#m<?kzzzMHHHMMHqmmmmmm
<<?<<(...``.-1.~.~..~~~._`````````````````````..` _?77TXkyOtttttttttwb~_<(j1<~~jHb~~~~~~~~<+v~~j-......`.``.  `    `` `````,WSdH#M###M###m..(MMMMM####N+dRuuHMmmmmmmmmmmmm
-~~~~~~~~<<+.. ?+_~.~.~~_ .``.````.``````````````````.``. _?7TXAAOttrX/~~(<x>~_WHHm-~~~~~~~~~~~(l.``.`.`..`.`    ` `` ``````(XHHHHHHHHHHHHHHHHHHHHHHHH#NkXRugmmmmmmmmmmmmm
mHmJ..~~.~~~._~_-?&_.~._(((-... .``.`````.````````````````````.` _?7TwN-~~(>~~~dHHHMHg&++J._~~~~z_..`.`..`.``  `   ``` ```` (MHHHHHHHHHHHHHHHHHHHHHHHHH#NuHugmmmmmmmmmmggg
mqqmqHmJ._~.~~~~~.~?&_~.~._```._<??<<+((....`.``.`.`.`.```````````.```._?71+-_~?MH@HHHHHHHHHNe-~I_...`..``...``  `  ``````.dX###########H#HHH#H#H#H#HHH#MudXHmmmmmmmgHHMMM
mmmmmmmmgHHg._~~.~~.~?+~~_````````` _?7<<(J+OIuJ..-((((-((((......`.`````````_?71MHHHHHHHHHHHHNxr...`.`..`.``.`      ...JdMKXHHHHHHHHHHHH#HH#HHH#HHH#HH#M0dSHmgggHHMHHHHHH
mmmmmmmmmqmmmHHa._.~~~_4,_.....(---+v777777<!~_.................._<??=1+-...`.`` (((7YHMH@HHHHHM{..`..``....`......(RvzdRXHHXMHHHHHHHHHHHHHHHHHHHHHHHH##NzXXHHHMHHHHHHHHM#
gmmmmmmmmmmmmmmmHMHgy7?7"7<~.........--(((J+ewwU0UUUUUUUUUUUUXwA+J----...._?7=i-..`` ?71((7TWMHMr...`...`.`..`.`.`.(KzzdKzMNXHHHH#HHHHHHHHHHHHHHHHHHH##H8XHzMHHHHHHHMH##HM
HMHmgmmmmmmmmmmmmmmmHHm._.._-((J+OUUUVrttrrtrrrrtttrtrrtrrrtrttrttrrrwVUUG+--...._?1(..`.._<+.-_7x-..`...`.`..`.`..(KzzXKzXMNXMHHHH#H#HHHHHH#H#HH#H####BXWSuMHH@HM#MHHMM@`
HHHMMHgmgmmgmgmmmmmmmmggHM#NHqgHHHkQQQQQmmmmmgmmQAAAwwwwrrttrrrrrrtttrrrtrrrwUWa._...._7i..`. ?1Jr_...`.....``..`..(KzzXKzzVMNXM##HH#H##HH#HHHHHHHH##MBXWSzzMHM#HHHHMMMHH+
HHHHHHMHggmmmmgmmgmgmmmmggmgHMNNHkkkkkqkkkqkkkkqkqkqqkqqHHHMMHmHmQKUYYTTTT7<<<<??7TTT4u+-._?i-...z<....`.``....`...(HzzXKzzzZMNmVMHHHHHHHHHHHHHHH#NMBXqH0vzzMHHHH#MMMHWZZZ
HHHHHHHHHMHggmgmmmmgmmgmmmmmqqmmMMMMMMMMMMMMM@@@@@@@@MMMMHMMH9UOz<<:~::::~::~:::::~::~:::(?TI+-?<JI-..`....`.....-(uKzzXKzzzzzWMNmXHMMHHHHHHHMMMMMSzQWSvzzvuMHH#MMMWyXXXQQ
HHHHHHHHHHHHMHgmmggmmgmmmmmmmmmmmmmmMMMkwwAAwwOlltltwQWB9Olllz<<:::~:~~:~:~:~~:~:~:~~:~~:~::::?T&-._?1i---..--JgHqmMKzzXKuXwzuuXXMMmy<:<?7TTTUUuXQkBXvvzzzzuMHMMHHWWHHHWWW
MMMHH@HHHHHHHHHMHgmgmmmgmgmmmmmmmmgmmmmmMMNmszlllug96lll=llv<:::~:~::~:~:~:~:~~~~:~::~:~~:~:~::::?4,-_.._?7TWgmmmmmMNuudKVH8zzzWWSzXUMMWgg+&gWHHUXHHzzzzwHHuMMMZXQmmkXZZZZ
pHpHHMMHHHHHHHHHHHMHHgmmgmmgmgmmgmmmmmmmmmmmgMMmM0lllll=l==z<:~::~:~::~:~::~::::~:~~::~::~:~:~:::::?UKUX+__-(dHHH9=!~_?TWkXXXXuXXXXXwXwXXXXXXXXXXXwwwwXXwQQdMHQMM9TTMNkZZZ
ppWppppHMMHHHHHHHHHHHMMHHggmgmmgmmmgmmmmgmmmmmmmmHMHgsll=l==lz+(::::~::~:~::~~:::~::~~::::~::~:~~::::?HBMMgHHgH=....`..`.-?MHM@@@@MMMB=<:dMM@@@c:::::<<~__?WkWM=~~_(jMNZZZ
pppfppfWpppHMMHHHHHHHHHHHHMHHgmgmmmmgmmmmgmmmmmmgmmmmHMHmszlll===z++(::~::~:~:~_~` `  ~~~::~:::::::++zllOu<::<Tn,.`.``.`..._?MM@@H#3:::::dMM@HMI:~~__.. 6-..d@<~(+K?=MMHHM
pppppppbppppppWMMHHHHHHHHHHHHHMHgggmmggmmmgmgggmmgmmmmqmmmMMmgyll=ll==z++(::::(_``   ` _::~::((+++==lllud3:::~:<7e....`.`..(:<TMM9::::~::dMHUzW{..```.`..r..(bJT11@?jMNZZy
WWbbppppbpppppppbbHMMHHHHHHHHHHHHHMHHgmggmmmmmmmmmmmmmmmmmmmmmgMMmgszll=ll==z1+i.``` .(++++uaQy=l=lluQY=<:~:~::::dx_----_(:::::<K<::~::::dM0zzW~.`..``...0.`(MS??d@?dH#ZZd
ppbppbpbppbpppppppbppbHMMMHHHHHHHHHHHHMHHggmgmmmggmmgmmmmmgmmmmmqmmmHMHmeOlllZU9U99U99UUVOll=l=lugX5>::::~:::~~::<TZwGJ::::::::(P:~::~::~dMXzwK_.``..``..~..(#z?1nZ1HMyyWM
WWppbbppHpbpppppppppppppppHMMHHHHHHHHHHHHHMHHggmgmmmmmmgmmmmgmmmmmgmmmmmmHMHmayll===ll=ll=lzudV9Olv:::~::::~:::(++z<::<7G+:::::($::~:::~.gMXzXD..`.`.`.`(_.(M$??>?1dMHWHMN
pppbbpbbpppbpppppppppppbbWbpppHMMHHHHHHHHHHHHHMHgggmmgmmgmmmmgmmmmggmmgmmmmmmmHMMmQslll=lzOOllllz<:::::~:::(++==lllv:::::<177X&+w+::::<._d#zzXr_....... .(gMNI???uHMHZdNM#
ppbbppppppppppfppppbpppppWpbppppppHMMHHHHHHHHHHHHHMHgggmggmmmmmgmmmgmmmmmmmmmmmmmmggMHHmggaszlllz+++++++z==l=ll==lz<:~~:~:::~::<74kZC+?7XMWXXX<??TT777?<~_WNNN=1gMMZZyM@~~
bpppppHWpppppppppppbbpppWppkpppWHpppppHMMHHHHHHHHHHHHHMHggmmgmmmgmmgmmmgmmmmmmmmmmmmmmmmmmmmHMmQgggggAyzll=llllll==z<:::::~::~:::::<?TG+++<:::::::::::-_..(MMM#MMWZZZZMb:~
bWWpWpppHppppbppppbpppfpHbppppH=7TWWpfWpfpWMMHHHHHHHHHHHHMMHHggmmmmgmmgmmmmmmgmmgmmmgmmmmmmmgmmHH@mmmmgHMHHgQasyzzlllz++<:::::~:::::::::::<?<<?TG+<:::j-..(NyWWkkkkXZyUMMM
ppppppppppppbppbbppppppbbHppppVC::::<?TWpHppHfWHMMHMHHHHHHHHHHMMHggmmgmmmgmmmmgmmmmmmgmgggHHHMMmmmmmmmmmmmmmmmmmgggHHHkmgggJ++++:::::::::::::::::<?S+:(>.(dWZZZyZZZXWWWWZy
ppppbppWpppppppppppppfHbpbWpp$::~~~::~::<?TWpppppfpWMMMMHHHHHHHHHHHMHHgggmgmgmmmmgmmgHMMHmmgmgggmmgmgmmgmmmmmmgmmmmmgmmmmmmmmmmmmmmmmHkmmmggggggJJ+J&XQJ(dHWpWHHHWHHmQkHHg
pbbppppbppbpbpppppbbpHpWW9UY>::::::::::::::::?TUWppppbppHMMHHHHHHHHHHHHHMHHggggggggggmmmmgmggmgggggggmggmggmgggggggggggmggmggmggmmmmmmmmmmmmmmmmgmmmmgggggmgmggmggggggggNM
ppbbppbpppWUUTYTC1<<;;;;;;;:::::;::::::::::;:;;;;;?7UWppbkbbHMMMHHHHHHHHHHHHMMHgggggggggggggggggggggmggggggggggmggggggggggggggggggggggggggmgggggggggggmgggggmgggmgmgHMMMgg
TC711<<>>>;>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;>17UWHbbbbbHMMMHHHHHHHHHHHHMMHHgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggMMMMgggggg

"""

print(morse_on)
time.sleep(0.5)
print(morse_off)