import getpass
import time
import hashlib
import json
import random
import requests
import numpy as np
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
 
kek = np.array([['http://www.tremorgames.com/playgame/5087/death-call.html','http://www.tremorgames.com/games/files/DeathCall_withAds.swf',63,'sf5tghy7uj'],
['http://www.tremorgames.com/playgame/5289/amberial-axis.html','http://www.tremorgames.com/games/files/A2D_Amberial Axis - Tremor.swf',70,'def5tghy67'],
['http://www.tremorgames.com/playgame/3451/tiny-airships.html','http://www.tremorgames.com/games/files/Tiny-AirShips.swf',10,'fhtjyr'],
['http://www.tremorgames.com/playgame/5708/tu-unleashed.html','http://www.tremorgames.com/games/files/LaunchInTheSky AD.swf',86,'kl8ut5fr43'],
['http://www.tremorgames.com/playgame/7567/wheely-2.html','http://www.tremorgames.com/games/files/1382436929_7567_wheely-2.swf',226,'DFNHG&%$gherkjoi987'],
['http://www.tremorgames.com/playgame/7568/ragdoll-achievement-2.html','http://www.tremorgames.com/games/files/1382443391_7568_RA2.swf',227,'DFBGHRTyt645t3765ft'],
['http://www.tremorgames.com/playgame/3721/zombie-madness.html','http://www.tremorgames.com/games/files/zombie-madness.swf',23,'3r5tyk'],
['http://www.tremorgames.com/playgame/7679/crest-breakout.html','http://www.tremorgames.com/games/files/1394896704_7679_ProjectWM.swf',229,'DFG%TG((JRFfgd23'],
['http://www.tremorgames.com/playgame/7479/revive-the-monster.html','http://www.tremorgames.com/games/files/1378479699_7479_revive_the_monster _SecureOpt.swf',224,'GNFHYt*(yh342da'],
['http://www.tremorgames.com/playgame/7968/shape-fold-animals.html','http://www.tremorgames.com/games/files/ShapeFoldAnimals - 2015 04 23 (TremorGames).swf',232,'asdfr45#$tgGTHgrt12'],
['http://www.tremorgames.com/playgame/7678/catsnfish.html','http://www.tremorgames.com/games/files/1394896624_7678_ProjectGP.swf',230,'3445FGT5467tfhfdG'],
['http://www.tremorgames.com/playgame/7680/potato-rebellion.html','http://www.tremorgames.com/games/files/1394896778_7680_ProjectKF.swf',228,'DFRtgbngh567hF@'],
['http://www.tremorgames.com/playgame/7967/zombonarium.html','http://www.tremorgames.com/games/files/zombonarium.swf',231,'asd45tgfVFr657yh'],
['http://www.tremorgames.com/playgame/7534/bombrunner.html','http://www.tremorgames.com/games/files/1380453238_7534_bombrunner_tremor.swf',225,'GFTR567ujM)(#$th5'],
['http://www.tremorgames.com/playgame/7464/euridissey-i-the-fall-of-horus.html','http://www.tremorgames.com/games/files/1377619930_7464_EuridisseyTremor.swf',223,'GNHTYFgrbt5674yu'],
['http://www.tremorgames.com/playgame/3553/zomblast.html','http://www.tremorgames.com/games/files/zomblast.swf',217,'BGh67&*%$rfDErR'],
['http://www.tremorgames.com/playgame/7274/zombie-smasher.html','http://www.tremorgames.com/games/files/1362947141_7274_Zombie_Smasher.swf',220,'fvGFRt56yHy#$#$2ws'],
['http://www.tremorgames.com/playgame/7277/the-engineer.html','http://www.tremorgames.com/games/files/1363614939_7277_Engineer.swf',218,'Fvgb&*$5hy#ghtD'],
['http://www.tremorgames.com/playgame/7266/shape-shifters.html','http://www.tremorgames.com/games/files/1362945541_7266_ShapeShifters.swf',216,'FVgbhNJ&*H*93erD'],
['http://www.tremorgames.com/playgame/7235/soul-shift.html','http://www.tremorgames.com/games/files/1362598225_7235_SoulShift.swf',209,'gbFVcde#$%2$1'],
['http://www.tremorgames.com/playgame/5058/werebox-2.html','http://www.tremorgames.com/games/files/werebox-2.swf',210,'gbFGT65&*$8uaq2'],
['http://www.tremorgames.com/playgame/7104/iron-ladies.html','http://www.tremorgames.com/games/files/IronLadies.swf',215,'hnbFGTr$#@345'],
['http://www.tremorgames.com/playgame/7262/dechmog.html','http://www.tremorgames.com/games/files/1362600708_7262_dechmog.swf',214,'hnBGF%$#&876@1'],
['http://www.tremorgames.com/playgame/7261/vehicles-2-levelpack.html','http://www.tremorgames.com/games/files/1362946533_7261_Vehicles2.swf',208,'afgvbRTF$%&*54'],
['http://www.tremorgames.com/playgame/7258/bottle-on-head.html','http://www.tremorgames.com/games/files/1362923651_7258_BottleOnHead.swf',212,'fvbgTRF5$%*lk1'],
['http://www.tremorgames.com/playgame/7278/cripple-cannon.html','http://www.tremorgames.com/games/files/1363614807_7278_Cripple Cannon.swf',222,'GVbTYh76*#$gTy1'],
['http://www.tremorgames.com/playgame/2844/connect-it.html','http://www.tremorgames.com/games/files/connect-it.swf',219,'kmJHNbg786&*$@r4'],
['http://www.tremorgames.com/playgame/7246/rotation-experiment.html','http://www.tremorgames.com/games/files/1362623612_7246_FD.swf',207,'frg$#eDFrfg&sdfg12'],
['http://www.tremorgames.com/playgame/7257/beaver-blocks.html','http://www.tremorgames.com/games/files/1362923363_7257_BeaverBlocks.swf',211,'sdfc456%$#4RFDer@'],
['http://www.tremorgames.com/playgame/7263/frozen-age.html','http://www.tremorgames.com/games/files/1362603168_7263_frozenage.swf',213,'sdfVFD45&*%rtg1'],
['http://www.tremorgames.com/playgame/7245/minigames-world.html','http://www.tremorgames.com/games/files/1361788509_7245_minig_adfree.swf',206,'bgf54f%&hyGTREwe'],
['http://www.tremorgames.com/playgame/7244/pandoras-epic-battles.html','http://www.tremorgames.com/games/files/1361732006_7244_questLife.swf',205,'adfvgfr45$%rED'],
['http://www.tremorgames.com/playgame/7243/terra-god.html','http://www.tremorgames.com/games/files/1361562565_7243_TerraGod.swf',191,'avg56hnbj78'],
['http://www.tremorgames.com/playgame/7238/the-forgotten-dungeon.html','http://www.tremorgames.com/games/files/1361017735_7238_ForgottenDungeon.swf',204,'bghnb%$2DEws@'],
['http://www.tremorgames.com/playgame/4802/match-move-2.html','http://www.tremorgames.com/games/files/MFP_MM2.swf',47,'asd4f5tg'],
['http://www.tremorgames.com/playgame/7024/endless-war-4.html','http://www.tremorgames.com/games/files/1353859784_7024_ew4 Tremor.swf',168,'g56tfvb56g'],
['http://www.tremorgames.com/playgame/7198/carveola-incident-2118-ad.html','http://www.tremorgames.com/games/files/1356897432_7198_CarveolaIncident2118AD.swf',200,'gbhtwmkl915'],
['http://www.tremorgames.com/playgame/7177/monsters-mash-3.html','http://www.tremorgames.com/games/files/monster-mash-3.swf',162,'hb56gthy67uj'],
['http://www.tremorgames.com/playgame/7023/feudalism-ii.html','http://www.tremorgames.com/games/files/1355744490_7023_Feudalism2 Tremor.swf',170,'gt4dfvce324'],
['http://www.tremorgames.com/playgame/7178/super-mega-bot.html','http://www.tremorgames.com/games/files/1355948580_7178_super_mega_bot_stl_tremorgames.com_v1.1.1.swf',194,'hngtry675'],
['http://www.tremorgames.com/playgame/7167/nelly.html','http://www.tremorgames.com/games/files/1355348269_7167_Nelly sitelock2.swf',188,'ghbn6238ik'],
['http://www.tremorgames.com/playgame/7169/snake-squad.html','http://www.tremorgames.com/games/files/1355946918_7169_snake_squad_tremor_games_stl_lic_v1.1.2.swf',192,'hytnmki89ki'],
['http://www.tremorgames.com/playgame/7179/on-the-edge.html','http://www.tremorgames.com/games/files/1355594581_7179_on_the_edge_stl_tremorgames.com_v1.1.swf',195,'asbg56hn78j3'],
['http://www.tremorgames.com/playgame/7140/secret-ways.html','http://www.tremorgames.com/games/files/1355060628_7140_SecretWays.swf',185,'afgt5ry5767'],
['http://www.tremorgames.com/playgame/7165/pack-up-the-toy.html','http://www.tremorgames.com/games/files/1355347518_7165_Pack Up the Toy tremor.swf',189,'gt5rbvnhy7'],
['http://www.tremorgames.com/playgame/7168/the-suspense.html','http://www.tremorgames.com/games/files/1355425440_7168_city time2 sitelock.swf',190,'ghny654ws32'],
['http://www.tremorgames.com/playgame/7005/tome-sweet-tome.html','http://www.tremorgames.com/games/files/1351706533_7005_TomeSweetTome.swf',152,'gbn65hty4'],
['http://www.tremorgames.com/playgame/7155/intruder-combat-training-.html','http://www.tremorgames.com/games/files/1354915602_7155_deathmatch_secure.swf',187,'gthyt5rfgvb4'],
['http://www.tremorgames.com/playgame/7001/izzi.html','http://www.tremorgames.com/games/files/1349647467_7001_iZZi Tremor.swf',148,'sv45gth45gh6'],
['http://www.tremorgames.com/playgame/7010/endless-war-defense.html','http://www.tremorgames.com/games/files/1350000811_7010_ewd Tremor.swf',138,'sf56gbn78jmn'],
['http://www.tremorgames.com/playgame/7135/biometal.html','http://www.tremorgames.com/games/files/1353958052_7135_Untitled-1.swf',184,'hngyt65th89'],
['http://www.tremorgames.com/playgame/5935/gravibounce.html','http://www.tremorgames.com/games/files/1352415832_5935_Gravibounce.swf',159,'m876gt54dc'],
['http://www.tremorgames.com/playgame/7110/tower-dash.html','http://www.tremorgames.com/games/files/1353011295_7110_knightclimber_cpm.swf',182,'hngjtyuhrnfaw'],
['http://www.tremorgames.com/playgame/7111/planet-blirp-2.html','http://www.tremorgames.com/games/files/1353342079_7111_planet blirp 2 main - ads.swf',181,'gtr45ght567'],
['http://www.tremorgames.com/playgame/7008/bulletspree.html','http://www.tremorgames.com/games/files/1351984510_7008_BulletSpree Tremor.swf',155,'bn5t6yvde3'],
['http://www.tremorgames.com/playgame/5934/tower-of-greed.html','http://www.tremorgames.com/games/files/1352659079_5934_TowerofGreed.swf',158,'mk876tgbf4'],
['http://www.tremorgames.com/playgame/5928/cat-toss.html','http://www.tremorgames.com/games/files/1352826329_5928_cattoss-tremorgames.swf',145,'nh76tgvefdr43'],
['http://www.tremorgames.com/playgame/5933/pixel-purge.html','http://www.tremorgames.com/games/files/1352415633_5933_PixelPurge.swf',157,'hnjyuhgr45'],
['http://www.tremorgames.com/playgame/7092/cube-assembler.html','http://www.tremorgames.com/games/files/1352319997_7092_CubeAssembler_Normal.swf',178,'$^*oPKNbgt198)(fAs'],
['http://www.tremorgames.com/playgame/7052/cave-explorer.html','http://www.tremorgames.com/games/files/1351091477_7052_cBuild.swf',173,'fvbg54rfgvv'],
['http://www.tremorgames.com/playgame/7003/the-gun-game-2.html','http://www.tremorgames.com/games/files/1351700224_7003_Gun Game 2 Tremor.swf',150,'jd34fg67h5'],
['http://www.tremorgames.com/playgame/7070/funny-bees.html','http://www.tremorgames.com/games/files/FunnyBees.swf',172,'jn76tgbvf54'],
['http://www.tremorgames.com/playgame/7006/romeogogo.html','http://www.tremorgames.com/games/files/1349637693_7006_RomeoGOGO.swf',153,'vg5hbnuiq8'],
['http://www.tremorgames.com/playgame/7007/gnome-sweet-gnome.html','http://www.tremorgames.com/games/files/1351705262_7007_GnomeSweetGnome.swf',154,'n6tg8k3d7c'],
['http://www.tremorgames.com/playgame/7004/the-gun-game.html','http://www.tremorgames.com/games/files/1349647505_7004_Gun Game Tremor.swf',151,'b65nhj78mj'],
['http://www.tremorgames.com/playgame/5936/jetpack-jerome.html','http://www.tremorgames.com/games/files/1352365617_5936_JetpackJerome.swf',160,'814wb9y6d'],
['http://www.tremorgames.com/playgame/7057/path-of-honor-chapter-1.html','http://www.tremorgames.com/games/files/poh1M.swf',174,'hyt567jhfe4'],
['http://www.tremorgames.com/playgame/7014/feudalism.html','http://www.tremorgames.com/games/files/1350074796_7014_Feudalism Tremor.swf',139,'juy76hnbg45'],
['http://www.tremorgames.com/playgame/7037/notebook-wars.html','http://www.tremorgames.com/games/files/notewars.swf',140,'hy76tgf45r3'],
['http://www.tremorgames.com/playgame/7026/eleventh-hour.html','http://www.tremorgames.com/games/files/EleventhHour(Tremor).swf',165,'g5rf45gt6y7'],
['http://www.tremorgames.com/playgame/3864/space-is-key-2.html','http://www.tremorgames.com/games/files/space-is-key-2.swf',166,'mnh67ygtr45'],
['http://www.tremorgames.com/playgame/7027/platcore.html','http://www.tremorgames.com/games/files/U4Q_Platcore(Tremor).swf',164,'nh7yhg5trfd'],
['http://www.tremorgames.com/playgame/7031/spell-storm.html','http://www.tremorgames.com/games/files/1350360112_7031_SpellStorm_Tremor.swf',146,'gt56hybgfrt'],
['http://www.tremorgames.com/playgame/7016/space-is-key.html','http://www.tremorgames.com/games/files/1349996691_7016_Space Is Key (Tremor).swf',167,'n7uy86yg54r'],
['http://www.tremorgames.com/playgame/5946/invertion.html','http://www.tremorgames.com/games/files/1350100245_5946_InvertionGame.swf',171,'nhgyt65tfr4'],
['http://www.tremorgames.com/playgame/1568/notebook-wars-2.html','http://www.tremorgames.com/games/files/1349972207_7015_notewars2.swf',141,'fr5tgbvcde32'],
['http://www.tremorgames.com/playgame/5864/swordfall-kingdoms.html','http://www.tremorgames.com/games/files/PIE_sfk.swf',121,'dfrgthyu76h45'],
['http://www.tremorgames.com/playgame/5671/notebook-wars-3.html','http://www.tremorgames.com/games/files/nw3.swf',142,'57hyuj89ikne3'],
['http://www.tremorgames.com/playgame/5927/abstract-defense.html','http://www.tremorgames.com/games/files/1349462460_5927_abstract-defense.swf',144,'gtfbvnh76ju8'],
['http://www.tremorgames.com/playgame/5908/fat-snake.html','http://www.tremorgames.com/games/files/MrFatSnake.swf',133,'fr54tgbvfth'],
['http://www.tremorgames.com/playgame/5896/ragdoll-achievement.html','http://www.tremorgames.com/games/files/Ragdoll-Achievement.swf',135,'afrtgbnhyg'],
['http://www.tremorgames.com/playgame/5899/endless-war-6.html','http://www.tremorgames.com/games/files/1349202105_5899_ew6 Tremor.swf',136,'t5rfgtrf43'],
['http://www.tremorgames.com/playgame/5910/super-pig.html','http://www.tremorgames.com/games/files/superpig1.swf',131,'jhbny65tghh'],
['http://www.tremorgames.com/playgame/5909/xenosquad.html','http://www.tremorgames.com/games/files/1348951954_5909_xenosquad.swf',132,'bf45rfgt6yhju'],
['http://www.tremorgames.com/playgame/5891/legend-of-pandora.html','http://www.tremorgames.com/games/files/pandora.swf',129,'hbnhy654tdvf'],
['http://www.tremorgames.com/playgame/5892/legend-of-the-void.html','http://www.tremorgames.com/games/files/8QC_Game.swf',130,'avgt67yhnju8'],
['http://www.tremorgames.com/playgame/5895/pheus-and-mor.html','http://www.tremorgames.com/games/files/Pheus_and_Mor.swf',134,'hbn76trf43'],
['http://www.tremorgames.com/playgame/5869/scrap-metal-heroes.html','http://www.tremorgames.com/games/files/SMH.swf',125,'afr45tgbn67'],
['http://www.tremorgames.com/playgame/5870/shatterbot.html','http://www.tremorgames.com/games/files/ShatterBot.swf',126,'grf45thy65a'],
['http://www.tremorgames.com/playgame/5874/bird-blast.html','http://www.tremorgames.com/games/files/bird-blast.swf',115,'nhjuy76tgb'],
['http://www.tremorgames.com/playgame/5860/bug-slayer.html','http://www.tremorgames.com/games/files/BGJ_1.02_BugSlayer.swf',123,'sdf4ghbnm89'],
['http://www.tremorgames.com/playgame/5819/acorn-story.html','http://www.tremorgames.com/games/files/AcornStory.swf',128,'fnkjui89io87']])
 
kek2 = np.array([['http://www.tremorgames.com/playgame/5872/super-defence.html','http://www.tremorgames.com/games/files/ZI3_SuperShooterV4.3.swf',127,'fr5tgbhny67'],
['http://www.tremorgames.com/playgame/5862/endless-war-5.html','http://www.tremorgames.com/games/files/CX6_ew5 TG.swf',120,'afrtg56yhgt'],
['http://www.tremorgames.com/playgame/5861/cardmania-golf-solitaire.html','http://www.tremorgames.com/games/files/LEP_golfSolitaire.swf',124,'gtr54rgtyhn'],
['http://www.tremorgames.com/playgame/5855/creatively-complicated.html','http://www.tremorgames.com/games/files/creatively-complicated.swf',113,'cngi8ujhlljni'],
['http://www.tremorgames.com/playgame/5812/lights-off.html','http://www.tremorgames.com/games/files/E1H_lights_off.swf',101,'asr45tgfgh'],
['http://www.tremorgames.com/playgame/5837/spectromancer-gamers-pack.html','http://www.tremorgames.com/games/files/SPGP.swf',116,'ae43rf5tgy67'],
['http://www.tremorgames.com/playgame/5813/unblock-it-2.html','http://www.tremorgames.com/games/files/27F_UnblockIt2.swf',110,'bgnh76ymkjio9'],
['http://www.tremorgames.com/playgame/5800/magi-the-fallen-world.html','http://www.tremorgames.com/games/files/X2T_battle_final_non_exclusive.swf',106,'dfvb56tgy'],
['http://www.tremorgames.com/playgame/5755/melancholia.html','http://www.tremorgames.com/games/files/melancholia.swf',94,'gt6yhg45rf'],
['http://www.tremorgames.com/playgame/5816/unblock-it.html','http://www.tremorgames.com/games/files/UnblockIt.swf',112,'ajyh67tgfrs'],
['http://www.tremorgames.com/playgame/5774/-commit-point-five.html','http://www.tremorgames.com/games/files/CommitLoader.swf',100,'fgrt254hbn76'],
['http://www.tremorgames.com/playgame/5809/max-connect-2.html','http://www.tremorgames.com/games/files/mc2_fix.swf',109,'r45gt67yhsd'],
['http://www.tremorgames.com/playgame/5786/zombie-situation.html','http://www.tremorgames.com/games/files/zombie1975.swf',103,'km78uyhg564'],
['http://www.tremorgames.com/playgame/4714/pigs-will-fly.html','http://www.tremorgames.com/games/files/pigs-will-fly.swf',108,'adr43fg67hnj8'],
['http://www.tremorgames.com/playgame/5757/fall-of-the-dead.html','http://www.tremorgames.com/games/files/P9Q_Fall of the dead vihutuoCMPStar.swf',102,'tyygg34'],
['http://www.tremorgames.com/playgame/5254/flood-runner-4.html','http://www.tremorgames.com/games/files/FloodRunner4_reloaded.swf',57,'f6g4h5j8mk'],
['http://www.tremorgames.com/playgame/5762/gnomes-coins.html','http://www.tremorgames.com/games/files/gnome-coins.swf',96,'adfrtg567ad'],
['http://www.tremorgames.com/playgame/5761/whats-unnecessary.html','http://www.tremorgames.com/games/files/Whatsunnecessary.swf',99,'af54gtyh67uh'],
['http://www.tremorgames.com/playgame/5608/ion-swarm.html','http://www.tremorgames.com/games/files/ion-swarm.swf',76,'16tg75gki9'],
['http://www.tremorgames.com/playgame/5717/gears-and-chains-spin-it.html','http://www.tremorgames.com/games/files/Gears 0.5.4 TG CPM.swf',87,'af5rgh7uj'],
['http://www.tremorgames.com/playgame/5728/shiftarium.html','http://www.tremorgames.com/games/files/shiftarium.swf',92,'fre3gt6yh'],
['http://www.tremorgames.com/playgame/5729/blackwood-prologue.html','http://www.tremorgames.com/games/files/BlackwoodPrologue(ads).swf',88,'rt6yh78ih'],
['http://www.tremorgames.com/playgame/656/jet-pod-remanufactured.html','http://www.tremorgames.com/games/files/jet-pod-remanufactured.swf',93,'dfr45tghy'],
['http://www.tremorgames.com/playgame/5723/mini-crash-boy.html','http://www.tremorgames.com/games/files/MiniCrashBoy.swf',90,'mn78qw123'],
['http://www.tremorgames.com/playgame/5707/boss-slayer.html','http://www.tremorgames.com/games/files/XN7_secure_BossKiller.swf',75,'gtbh67yde4'],
['http://www.tremorgames.com/playgame/5698/blast-boxes.html','http://www.tremorgames.com/games/files/BlastBoxes_Normal.swf',84,'kij87yhu'],
['http://www.tremorgames.com/playgame/5258/tremor-rocket-2.html','http://www.tremorgames.com/games/files/TremorRocket2_Normal.swf',73,'kjhyuinhg'],
['http://www.tremorgames.com/playgame/5686/unusual-way.html','http://www.tremorgames.com/games/files/UnusualWay.swf',83,'fdsf45dsfgF'],
['http://www.tremorgames.com/playgame/5607/easy-way.html','http://www.tremorgames.com/games/files/IGRA.swf',82,'sdfRgdg456'],
['http://www.tremorgames.com/playgame/4663/dogfight-aces.html','http://www.tremorgames.com/games/files/dogfight-aces.swf',33,'hj76gy'],
['http://www.tremorgames.com/playgame/5690/incoming.html','http://www.tremorgames.com/games/files/incoming.swf',81,'d34f6h7j89'],
['http://www.tremorgames.com/playgame/5291/just-a-random-day.html','http://www.tremorgames.com/games/files/K35_Just a Random Day 1.2.swf',74,'drtygh56ty'],
['http://www.tremorgames.com/playgame/1312/factory-balls-4.html','http://www.tremorgames.com/games/files/factory-balls-4.swf',69,'hb65n91kilp'],
['http://www.tremorgames.com/playgame/5200/back2back.html','http://www.tremorgames.com/games/files/back2back.swf',67,'fbg65hy7uj'],
['http://www.tremorgames.com/playgame/4708/masons-medals.html','http://www.tremorgames.com/games/files/masons-medals.swf',44,'afgh76hyt'],
['http://www.tremorgames.com/playgame/4919/caldera-legends.html','http://www.tremorgames.com/games/files/Caldera Legends Sitelock.swf',52,'asdf56gfqwe'],
['http://www.tremorgames.com/playgame/4962/salad-ninja.html','http://www.tremorgames.com/games/files/SaladNinja_Normal.swf',61,'addfgtr45ty62'],
['http://www.tremorgames.com/playgame/4834/freeway-challenge.html','http://www.tremorgames.com/games/files/FreewayChallenge.swf',58,'as4fr5tg67'],
['http://www.tremorgames.com/playgame/4651/zombie-city.html','http://www.tremorgames.com/games/files/zombiesiti.28.swf',37,'f4tg56'],
['http://www.tremorgames.com/playgame/4833/cursed-dungeon.html','http://www.tremorgames.com/games/files/secure_RPGGame2.swf',54,'kjyu78nm3er'],
['http://www.tremorgames.com/playgame/4774/air-maze-3.html','http://www.tremorgames.com/games/files/A5F_AirMaze3_Tremor_secure.swf',50,'asnh56rfgf'],
['http://www.tremorgames.com/playgame/4750/zombie-defense-agency.html','http://www.tremorgames.com/games/files/zomTremor.swf',55,'r54tn7yh8'],
['http://www.tremorgames.com/playgame/4711/shifting-castle.html','http://www.tremorgames.com/games/files/shifting-castle.swf',46,'asd5tgh67'],
['http://www.tremorgames.com/playgame/5697/planet-lucha.html','http://www.tremorgames.com/games/files/PTF_planet lucha.swf',85,'sdfsFretg46d'],
['http://www.tremorgames.com/playgame/4713/glowrunner.html','http://www.tremorgames.com/games/files/E54_Main.swf',51,'ad4jm90f'],
['http://www.tremorgames.com/playgame/4712/pipeline-master.html','http://www.tremorgames.com/games/files/PipelineMaster.swf',49,'as34frt56y'],
['http://www.tremorgames.com/playgame/4662/zombie-tormentor.html','http://www.tremorgames.com/games/files/BieberTormentor_prototype_v12b.swf',43,'drtfGtukl56s'],
['http://www.tremorgames.com/playgame/4654/aargh.html','http://www.tremorgames.com/games/files/secure_Aargh.swf',42,'ruhtyGtrh4wj'],
['http://www.tremorgames.com/playgame/4648/musicball.html','http://www.tremorgames.com/games/files/MusicBall_WithAds.swf',40,'bgh67y'],
['http://www.tremorgames.com/playgame/4609/blockstachio.html','http://www.tremorgames.com/games/files/Blockstachio-Preview-v1.8.swf',35,'m9u7k8'],
['http://www.tremorgames.com/playgame/4610/cupid-rescue.html','http://www.tremorgames.com/games/files/CubidRescue_Normal.swf',31,'alpo98'],
['http://www.tremorgames.com/playgame/4607/captain-fugly-2.html','http://www.tremorgames.com/games/files/captain-fugly-2.swf',34,'m8h7yu'],
['http://www.tremorgames.com/playgame/4606/penguins-attack-2.html','http://www.tremorgames.com/games/files/WPA_2_TremorGames.swf',32,'bg67hy'],
['http://www.tremorgames.com/playgame/4561/billi-color-lines.html','http://www.tremorgames.com/games/files/billi-color-lines.swf',30,'acf47k'],
['http://www.tremorgames.com/playgame/4425/dart-wheel.html','http://www.tremorgames.com/games/files/DAI_DartWheel_Normal.swf',27,'vmkl8q'],
['http://www.tremorgames.com/playgame/4284/zombie-shooter.html','http://www.tremorgames.com/games/files/zombie-shooter.swf',26,'ase45g'],
['http://www.tremorgames.com/playgame/4170/speed-rally.html','http://www.tremorgames.com/games/files/speed-rally.swf',25,'jmg65t'],
['http://www.tremorgames.com/playgame/3913/ninja-sequence.html','http://www.tremorgames.com/games/files/NinjaSequenceCPMStar.swf',21,'ace3rt'],
['http://www.tremorgames.com/playgame/3719/crazy-soldier.html','http://www.tremorgames.com/games/files/crazy-soldier.swf',22,'jngyu7'],
['http://www.tremorgames.com/playgame/3687/tremor-gunslinger.html','http://www.tremorgames.com/games/files/I9H_TremorGunslinger_Normal.swf',19,'bhngy6'],
['http://www.tremorgames.com/playgame/3656/tremor-ace.html','http://www.tremorgames.com/games/files/Tremor-Ace.swf',17,'pr9gij'],
['http://www.tremorgames.com/playgame/3477/cave-run.html','http://www.tremorgames.com/games/files/Cave-Run.swf',15,'a3ertg'],
['http://www.tremorgames.com/playgame/3452/tremor-rocket.html','http://www.tremorgames.com/games/files/Tremor-Rocket.swf',11,'gbniyw'],
['http://www.tremorgames.com/playgame/3657/mole-and-zombie-whack.html','http://www.tremorgames.com/games/files/mole-and-zombie-whack.swf',18,'fbhgt6'],
['http://www.tremorgames.com/playgame/3440/ninja-terror.html','http://www.tremorgames.com/games/files/ninjaterror.swf',9,'ythr56'],
['http://www.tremorgames.com/playgame/4612/zombie-last-night-2.html','http://www.tremorgames.com/games/files/zombie_last_night2_tremor_v9_secure.swf',39,'a5g678'],
['http://www.tremorgames.com/playgame/5046/battleship-the-beginning.html','http://www.tremorgames.com/games/files/RCN_battleship.swf',72,'vf5jnyu76'],
['http://www.tremorgames.com/playgame/5685/empires-of-arkeia.html','http://www.tremorgames.com/games/files/eoa.swf',122,'gf45tgh67yj'],
['http://www.tremorgames.com/playgame/5906/skullhunter-players-pack.html','http://www.tremorgames.com/games/files/SkullHunter_PlayersPack.swf',137,'agt54fghy67u'],
['http://www.tremorgames.com/playgame/5932/arcs.html','http://www.tremorgames.com/games/files/1349701419_5932_ArcsGo.swf',143,'gtr45bhn678'],
['http://www.tremorgames.com/playgame/7098/rawr.html','http://www.tremorgames.com/games/files/1352801906_7098_rawr.swf',176,'fgVB65&jh*9;{}kmLOpo2'],
['http://www.tremorgames.com/playgame/7113/pike-club-2.html','http://www.tremorgames.com/games/files/1355161019_7113_pike_club2.swf',183,'FVBGTR54$#@#rfgTpo9'],
['http://www.tremorgames.com/playgame/7009/bazooki-a-silent-affair.html','http://www.tremorgames.com/games/files/bazooki.swf',156,'n6fv3x9r56'],
['http://www.tremorgames.com/playgame/7022/endless-war-3.html','http://www.tremorgames.com/games/files/1355333577_7022_ew3 Tremor.swf',169,'kjnh67gbf43']])
 
def IsNumeric( v ):
	try:
		v2 = int( v )
		return True
	except (ValueError, TypeError):
		return False
 
def LoginTremorGames( s, username, password ):
	s.headers.update( { 'Origin': 'http://www.tremorgames.com' } )
	s.headers.pop( 'X-Requested-With', None )
	s.headers.update( { 'Referer': 'http://www.tremorgames.com/index.php' } )
	r = s.post( 'http://www.tremorgames.com/index.php', data={ 'loginuser': username, 'loginpassword': password, 'Submit': '' }, allow_redirects=False )
	return
 
def GetUserCoins( s ):
	s.headers.pop( 'Origin', None )
	s.headers.update( { 'X-Requested-With': 'XMLHttpRequest' } )
	s.headers.update( { 'Referer': GameURL } )
	r = s.get( 'http://www.tremorgames.com/achievements/ajax_getusercoins.php' )
	return int( r.text )
 
def GetGameAchievements( s ):
	s.headers.pop( 'Origin', None )
	s.headers.pop( 'X-Requested-With', None )
	s.headers.pop( 'Referer', None )
	r = s.get( GameURL, allow_redirects=False )
	
	jsonStartIdx = r.text.find( 'AchievementsJS = jQuery.parseJSON(\'' ) + len( 'AchievementsJS = jQuery.parseJSON(\'' )
	jsonEndIdx = r.text.find( '\');', jsonStartIdx )
	
	return json.loads( r.text[jsonStartIdx:jsonEndIdx] )
 
def GetGameStats( s, playerName ):
	s.headers.pop( 'Origin', None )
	s.headers.update( { 'X-Requested-With': 'ShockwaveFlash/24.0.0.194' } )
	s.headers.update( { 'Referer': GameURL } )
	r = s.get( 'http://www.tremorgames.com/achievements/json_get_stats.php', params={ 'PlayerName': playerName, 'GameID': GameID } )
	return r.json()
 
def UpdateGameStat( s, playerName, statName, statValue ):
	# calculate key
	requestKey = hashlib.md5( (playerName + Key + str( statValue )).encode( 'utf-8' ) ).hexdigest().lower()
	
	s.headers.update( { 'Origin': 'http://www.tremorgames.com' } )
	s.headers.update( { 'X-Requested-With': 'ShockwaveFlash/24.0.0.194' } )
	s.headers.update( { 'Referer': GameSWF } )
	r = s.post( 'http://www.tremorgames.com/achievements/record_stats.php', data={ 'StatValue': statValue, 'StatName': statName, 'PlayerName': playerName, 'GameID': GameID, 'Key': requestKey } )
	return
 
random.seed()
s = requests.Session()
s.headers.update( { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' } )
s.headers.update( { 'Accept-Language': 'en-US,en;q=0.8' } )
 
username = input( 'Login for Tremor: ' )
password = input( 'Pass: ' )
LoginTremorGames( s, username, password )
print( 'Entered Tremor' )
i = 0
while i < 92:
    GameID = int(kek[i,2])
    Key = (kek[i,3])
    GameURL = (kek[i,0])
    GameSWF = (kek[i,1])
    gameAchievements = GetGameAchievements( s )
#gameStats = GetGameStats( s, username )
 
    for achievement in gameAchievements:
	# currently only Max and Cumulative stat types supported
            if achievement['StatType'] != 'Max' and achievement['StatType'] != 'Cumulative':
                    continue
	
	# usually the current stat value isn't 0 but something like null or none, so we set it to 0
            if not IsNumeric( achievement['ProgressValue'] ):
                    achievement['ProgressValue'] = '0'
	
            statIncrease = 1
            statGoal = int( achievement['StatValue'] )
            if statGoal >= 100000:
                    statIncrease = random.randrange( 1, 10000 )
            elif statGoal >= 10000:
                    statIncrease = random.randrange( 1, 1000 )
            elif statGoal >= 1000:
                    statIncrease = random.randrange( 1, 100 )
	
            print( 'Achievement accomplished - "' + achievement['AchievementName'] + '"' )
            while int( achievement['ProgressValue'] ) < int( achievement['StatValue'] ):
                    achievement['ProgressValue'] = str( int( achievement['ProgressValue'] ) + statIncrease )
		
                    if achievement['StatType'] == 'Cumulative':
                            UpdateGameStat( s, username, achievement['StatName'], statIncrease )
                    else:
                            UpdateGameStat( s, username, achievement['StatName'], int( achievement['ProgressValue'] ) )
		
		# so we don't do it too fast
                    time.sleep( 1 )
	
            print( 'Achievement got\n' )
    print( 'The game is over: ',i+1 )
    i = i + 1
i = 0
while (i < 74):
    GameID = int(kek2[i,2])
    Key = (kek2[i,3])
    GameURL = (kek2[i,0])
    GameSWF = (kek2[i,1])
    gameAchievements = GetGameAchievements( s )
#gameStats = GetGameStats( s, username )
 
# Начало фа ма ачивок
    for achievement in gameAchievements:
	# currently only Max and Cumulative stat types supported
            if achievement['StatType'] != 'Max' and achievement['StatType'] != 'Cumulative':
                    continue
	
	# usually the current stat value isn't 0 but something like null or none, so we set it to 0
            if not IsNumeric( achievement['ProgressValue'] ):
                    achievement['ProgressValue'] = '0'
	
            statIncrease = 1
            statGoal = int( achievement['StatValue'] )
            if statGoal >= 100000:
                    statIncrease = random.randrange( 1, 10000 )
            elif statGoal >= 10000:
                    statIncrease = random.randrange( 1, 1000 )
            elif statGoal >= 1000:
                    statIncrease = random.randrange( 1, 100 )
	
            print( 'Achievement accomplished - "' + achievement['AchievementName'] + '"' )
            while int( achievement['ProgressValue'] ) < int( achievement['StatValue'] ):
                    achievement['ProgressValue'] = str( int( achievement['ProgressValue'] ) + statIncrease )
		
                    if achievement['StatType'] == 'Cumulative':
                            UpdateGameStat( s, username, achievement['StatName'], statIncrease )
                    else:
                            UpdateGameStat( s, username, achievement['StatName'], int( achievement['ProgressValue'] ) )
		
		# so we don't do it too fast
                    time.sleep( 1 )
	
            print( 'Achievement got\n' )
    print( 'The game is over: ',i+1 )
    i = i + 1
 
 
print( 'Finished :)' )
