from classes.story_generator import Story

"""
Initialize the scripts of the story with the appropriate types, story text and moment (choice) text
"""
scenario_1 = Story(story="In May 1942, your superior officer approaches you and the platoon you are in charge of and "
                         "gives you all a short briefing on the upcoming battle you are all asked to join. The battle "
                         "will be held in Guadalcanal, and resistance is anticipated to be mild. Your platoon’s "
                         "soldiers are psyched about the seemingly low risk opportunity, and most agree immediately to "
                         "joining the battle.\nAlthough everything does indeed sound good on paper, you still have "
                         "your doubts: it seems like the Americans just joined in WW2 a short while back due to the "
                         "Japanese attack on Pearl Harbour and a part of you feels some doubt towards the invasion of "
                         "Guadalcanal.\n",
                   moment="Do you choose to also: A) Enthusiastically sign up for the upcoming battle for your platoon,"
                          " or B) Refuse the offer and have your platoon stay put in Japan as a reserve force for any "
                          "upcoming wars?\n",
                   type="normal")
scenario_1a = Story(story="You decide to put your doubts to rest and enthusiastically raise your voice, bringing "
                          "excitement to your platoon’s soldiers who have already decided to partake in the "
                          "Guadalcanal battle while ignoring that very slight voice of doubt within you. In the next "
                          "week, you are transported to Guadalcanal and sure enough, the invasion was smooth and was "
                          "a success with little significant resistance as expected.\n",
                    moment=None,
                    type="chapter_end")
scenario_1b = Story(story="Although the chance to partake in this rather low-risk battle seems like the logical choice "
                          "over staying put in Japan and risking being asked to join another higher risk battle, you "
                          "decide to follow that tiny voice of doubt in your heart and voice out your refusal to join "
                          "the war. However, you realized the mood of enthusiasm was immediately dampened by your sole "
                          "refusal to join the battle, with many of the soldiers under you snickering and being "
                          "clearly confused. Being hugely aware of the awkward situation as well as the fact that "
                          "despite of your seniority over your own platoon, respect is earned and not automatically "
                          "gained, you immediately retract your statement and play it off as a joke sheepishly, before "
                          "relenting to sign your platoon up for the battle. In the next week, you are transported to "
                          "Guadalcanal and sure enough, the invasion was smooth and was a success with little "
                          "significant resistance as expected.\n",
                    moment=None,
                    type="chapter_end")
scenario_2 = Story(story="It has been 3 months since the IJA has invaded Guadalcanal, and the construction of the "
                         "airstrip critical to Japanese war efforts seem to have been undergoing fine. You and your "
                         "platoon, with nothing much to do apart from routine patrols and defenses, are bored out of "
                         "your minds. One of your assistants, Sergeant Kenichi Tanaka, suggests for a night of "
                         "gambling and drinking with sake smuggled from the occasional new Japanese arrivals in "
                         "Guadalcanal. Although you yourself are also bored out of your mind, you wonder whether this "
                         "is well worth the considerable risk, given that this is war time and literally anything can "
                         "occur despite the past uneventful 3 months. Your platoon all agree to Tanaka’s suggestion, "
                         "and are waiting for your reply to Tanaka’s suggestion as well, given your position as"
                         " leader.\n",
                   moment="Do you choose to : A) Shoot down Tanaka’s suggestion and insist that your platoon head "
                          "back for a good night’s rest, or B) Relent and join the platoon and have a rare night "
                          "of fun?\n",
                   type="normal")
scenario_2a = Story(story="Despite the insistence of your platoon, you resolutely stand your ground and refuse "
                          "Tanaka’s invitation. As you leave and call for your platoon to head back to the bunks, you "
                          "hear several of your own soldiers muttering behind your back, calling you a spoilsport in "
                          "disdaining voices. Although these comments leave you feeling rather down and slightly "
                          "doubtful of your choice, you head back to the bunk and end up having a good night’s rest.\n"
                          "The next morning arrives, and you wake up feeling all refreshed. You see the rest of your "
                          "platoon freshly awake as well in the common area of the bunk, and proceed towards the usual "
                          "patrol spot with them behind you.\n"
                          "However, just as you reach the patrol spot, you hear the loud blares of the air raid "
                          "emergency horn being sounded and realize that the worst is about to happen: An Allied "
                          "invasion of Guadalcanal!\n",
                    moment="At this point, you have to make a choice: A) Do you choose to immediately seek underground "
                           "shelter as per protocol or B) Go for glory and man the closest anti-aircraft artilleries "
                           "in an attempt to shoot down the invaders?\n",
                    type="normal")
scenario_2aa = Story(story="You decide that in such an air raid, safety is first and following the protocol will never "
                           "be wrong, and you immediately rally your troops and proceed to the nearest makeshift "
                           "bunker to regroup and wait for further orders.\n"
                           "You quickly find the nearest bunker and realize that quite a few of the other platoons "
                           "have already made it there. The senior officer, Colonel Yamaguchi, is in the midst of "
                           "issuing combat orders and you realize that all of you inside the bunker are assigned to "
                           "take up key defense positions which are located outdoors.  Your platoon is allocated to "
                           "defend the exterior of the bunker from incoming Allied ground troops and you proceed "
                           "there.\nAs expected, there are a massive number of incoming troops and despite the safety "
                           "of your position due to the sandbags and mounted machine guns, you still suffer some "
                           "damage.\n",
                     moment="Nevertheless, you manage to survive the skirmish! Your other troops are fine and lightly "
                            "injured as are you, and you proceed to scour the surroundings for survivors. You "
                            "encounter an injured Australian soldier who promptly surrenders at the sight of you and "
                            "your troops.\nYour troops, being injured from the skirmish and displaying a visible "
                            "amount of animosity towards the injured soldier, ask of you to dispose of the survivor "
                            "despite his surrender. Knowing that this is against international law and that POWs still "
                            "have their rights, do you : A) Decide to take in the surrendering Australian soldier as a "
                            "POW, or B) Follow your troops’ will and execute the invader who dares to stand up against "
                            "Japan’s conquest of Guadalcanal?\n",
                     type="luck_damage")
scenario_2aaa = Story(story="You decide that, despite your troops’ desire to kill the Australian soldier, to keep the "
                            "soldier alive as a POW. You promptly ask one of your troops to arrest the soldier, who "
                            "proceeds to then do the deed.\nTo your complete surprise, the Australian POW pulls out a "
                            "hidden handgun and shoots your soldier and you successively in the arm, whilst a few "
                            "other of your faster troops immediately spring on the POW and disarm him.",
                      moment="Thankfully, your soldier was only lightly injured as the bullet just grazed his upper "
                             "arm and did not cause serious injuries, but at this point your troops are all fuming "
                             "with anger and disappointment at your earlier decision. At this point, you are once "
                             "again forced to decide on the fate of this POW who dared to pose for surrender. Do you: "
                             "A) Execute the Australian soldier on the spot for daring to fake surrender or B) Go "
                             "ahead and still arrest the Australian soldier?\n",
                      type="luck_damage")
scenario_2aaaa = Story(story="In a fit of anger, you swiftly execute the Australian soldier by beheading him using the "
                             "sword you were bestowed as an officer. Your fellow troops cheer your choice of actions, "
                             "and you proceed to flick the blood off your sword. You tend to the troop who got injured "
                             "in the process of arresting the Australian and apologize for your earlier decision.\n"
                             "Although this decision of yours was indeed the right thing to do at the moment, you "
                             "still can’t help but wonder whether it was the morally right choice to do. Nevertheless, "
                             "you ignore this voice in your head and proceed to scour the remains of the skirmish for "
                             "more survivors.\n",
                       moment=None,
                       type="chapter_end")
scenario_2aaab = Story(story="Despite the injury you have suffered, you still decide to comply with international law "
                             "and ask your assistant, Sergeant Tanaka to arrest the Australian. Contrary to your "
                             "expectations, Tanaka instead pulls out his own sidearms and executes the Australian "
                             "soldier via a shot to the head.\n'Sir, why are you still planning to let this savage live"
                             " when he has just taken advantage of your kindness?' an enraged Tanaka shouts.\nThe usual"
                             " course of action for you would be to mark down this act as an act of insubordination, "
                             "but seeing the eyes of your other troops who express agreement with Tanaka’s words "
                             "convinces you to drop the subject. You proceed to ask Tanaka to cool down and proceed "
                             "to scour the remains of the skirmish for more Allied survivors.\n",
                       moment=None,
                       type="chapter_end")
scenario_2aab = Story(story="You decide to promptly execute the Australian soldier and simply use your rifle to shoot "
                            "the soldier in the head to grant him a quick and painless death. As you walk past his "
                            "corpse, you discover a handgun by his side and immediately realize that the soldier was "
                            "never planning to surrender peacefully and was trying to take out as many of you as he "
                            "can before his demise!\nPondering to yourself, you start to applaud yourself for your "
                            "decision, with your troops heaving sighs of relief at your decision to execute the "
                            "Australian. Although this decision of yours was indeed the right thing to do at the "
                            "moment, you still can’t help but wonder whether it was the morally right choice to do. "
                            "Nevertheless, you ignore this voice in your head and proceed to scour the remains of the "
                            "skirmish for more survivors.\n",
                      moment=None,
                      type="chapter_end")
scenario_2ab = Story(story="You decide that now is the best moment to seize glory and to stop the Allied air invaders "
                           "with your platoon. You rile up the rest of your troops and proceed to man the air "
                           "artillery guns present in an attempt to stop the incoming attacks.\nAlthough your efforts "
                           "are initially awarded, you notice that there seemed to be a never-ending barrage of new "
                           "planes. You immediately call for your troops to retreat and proceed towards the bunker but "
                           "are then hit by some air bombardment and suffer some injuries alongside the rest.\n",
                     moment="Nevertheless, you survive and manage to make it to the underground bunker in time with "
                            "your troops, although a sizeable number of them have suffered from minor injuries as well."
                            "\nHaving received quick treatment for your injuries quickly and after being reprimanded "
                            "by your senior officer for breaching protocol, you are forced to guard the exterior of "
                            "the bunker with your platoon mates. Do you choose to: 1) Protest against this assignment "
                            "given the injuries you and your troops have just suffered or 2) Resign to your fate and "
                            "go defend against the incoming skirmish from land Allied troops?\n",
                     type="luck_damage")
scenario_2aba = Story(story="You protest against this assignment but your senior officer, Colonel Yamaguchi, gives you "
                            "a deathly stare and mentions that any further objection will amount to insubordination "
                            "and direct execution on the spot. Feeling rather shaken, you have no choice but to accept "
                            "the outcome and go out to defend against the incoming waves of Allied attackers even "
                            "after suffering from earlier injuries due to your misplaced bravado.\n"
                            "As expected, there are a massive number of incoming troops and despite the safety of "
                            "your position due to the sandbags and mounted machine guns, you still suffer some damage.",
                      moment="Nevertheless, you manage to survive the skirmish! Your other troops are fine and lightly "
                             "injured as are you, and you proceed to scour the surroundings for survivors. You "
                             "encounter an injured Australian soldier who promptly surrenders at the sight of you and "
                             "your troops.\n"
                             "Your troops, being injured from the skirmish and displaying a visible amount of "
                             "animosity towards the injured soldier, ask of you to dispose of the survivor despite "
                             "his surrender. Knowing that this is against international law and that POWs still have "
                             "their rights, do you : A) Decide to take in the surrendering Australian soldier as a POW,"
                             " or B) Follow your troops’ will and execute the invader who dares to stand up against "
                             "Japan’s conquest of Guadalcanal?\n",
                      type="luck_damage")
scenario_2abaa = Story(story="You decide that, despite your troops’ desire to kill the Australian soldier, to keep the "
                             "soldier alive as a POW. You promptly ask one of your troops to arrest the soldier, who "
                             "proceeds to then do the deed.\nTo your complete surprise, the Australian POW pulls out a"
                             " hidden handgun and shoots your soldier and you successively in the arm, whilst a few "
                             "other of your faster troops immediately spring on the POW and disarm him.\n",
                       moment="Thankfully, your soldier was only lightly injured as the bullet just grazed his upper "
                             "arm and did not cause serious injuries, but at this point your troops are all fuming "
                             "with anger and disappointment at your earlier decision. At this point, you are once "
                             "again forced to decide on the fate of this POW who dared to pose for surrender. Do you: "
                             "A) Execute the Australian soldier on the spot for daring to fake surrender or B) Go "
                             "ahead and still arrest the Australian soldier?\n",
                       type="luck_damage")
scenario_2abaaa = Story(story="In a fit of anger, you swiftly execute the Australian soldier by beheading him using the"
                              " sword you were bestowed as an officer. Your fellow troops cheer your choice of actions,"
                              "and you proceed to flick the blood off your sword. You tend to the troop who got injured"
                              " in the process of arresting the Australian and apologize for your earlier decision.\n"
                              "Although this decision of yours was indeed the right thing to do at the moment, you "
                              "still can’t help but wonder whether it was the morally right choice to do. Nevertheless,"
                              " you ignore this voice in your head and proceed to scour the remains of the skirmish for"
                              "more survivors.\n",
                        moment=None,
                        type="chapter_end")
scenario_2abaab = Story(story="Despite the injury you have suffered, you still decide to comply with international law "
                              "and ask your assistant, Sergeant Tanaka to arrest the Australian. Contrary to your "
                              "expectations, Tanaka instead pulls out his own sidearms and executes the Australian "
                              "soldier via a shot to the head.\n'Sir, why are you still planning to let this savage "
                              "live when he has just taken advantage of your kindness?' an enraged Tanaka shouts.\n"
                              "The usual course of action for you would be to mark down this act as an act of "
                              "insubordination, but seeing the eyes of your other troops who express agreement with "
                              "Tanaka’s words convinces you to drop the subject. You proceed to ask Tanaka to cool "
                              "down and proceed to scour the remains of the skirmish for more Allied survivors.\n",
                        moment=None,
                        type="chapter_end")
scenario_2abab = Story(story="You decide to promptly execute the Australian soldier and simply use your rifle to shoot "
                             "the soldier in the head to grant him a quick and painless death. As you walk past his "
                             "corpse, you discover a handgun by his side and immediately realize that the soldier was "
                             "never planning to surrender peacefully and was trying to take out as many of you as he "
                             "can before his demise!\nPondering to yourself, you start to applaud yourself for your "
                             "decision, with your troops heaving sighs of relief at your decision to execute the "
                             "Australian. Although this decision of yours was indeed the right thing to do at the "
                             "moment, you still can’t help but wonder whether it was the morally right choice to do. "
                             "Nevertheless, you ignore this voice in your head and proceed to scour the remains of the "
                             "skirmish for more survivors.\n",
                       moment=None,
                       type="chapter_end")
scenario_2abb = Story(story="You head to the position of defense and bunker down with your troops against the incoming "
                            "Allied troops. As expected, there are a massive number of incoming troops but despite this"
                            "you actually somehow manage to escape without any injuries! You then proceed to scour the "
                            "remains of the skirmish for more Allied survivors.\n",
                      moment=None,
                      type='chapter_end')
scenario_2b = Story(story="You banish the unnecessary thoughts from your mind and agree to Tanaka’s suggestion to "
                          "gamble and drink your night away. The happy smiles of your soldiers leave you feeling "
                          "assured of your choice, and some of your other soldiers give you a pat on your back and "
                          "excitedly talk about the fun ahead for the night.\nAs expected, most of the soldiers in "
                          "your platoon including you went wild with the amount of sake drunk, and you managed to win "
                          "a few days’ worth of rations from the gambling. You feel happy about your decision to "
                          "approve the platoon’s suggestion of the activity and scoffed at your past self for even "
                          "considering going back to the bunk and have an early night instead. As everyone else fell "
                          "asleep in the common area of the bunk, you also follow suit and pass out from the alcohol "
                          "peacefully with the rest of the others.\nYou are suddenly rudely awakened by the sound of "
                          "blaring fire alarms and explosions all around the vicinity and awake to see 3 of your "
                          "platoon soldiers lying down all injured from air bombardment. You immediately regret your "
                          "decision, and as you desperately try to rally your other troops to go towards the bunker, "
                          "you get struck by an air bomb and unfortunately die. Your decision to party with your "
                          "platoon mates the previous night turned out to be the wrong decision, and one can never be "
                          "lax during the war!\n",
                    moment=None,
                    type="normal")
scenario_3 = Story(story="Despite your first victory over the invading Allied troops whilst defending the underground "
                         "bunker, the Imperial Japanese Army was still overrun by the never-ending waves of Allied "
                         "troops. Japan was utterly defeated in terms of sheer firepower and soldiers to spare. Having "
                         "suffered defeat and having the original base you were at attacked and relinquished to the"
                         " enemy, you and your platoon were forced to retreat to the HQ of the IJA in Guadalcanal.\n"
                         "In an emergency meeting solely meant for officers only, General Imamura stressed on the "
                         "importance of fighting till the bitter end and the bushido spirit, whilst warning any of us "
                         "officers to not engage in any acts of surrender despite defeat. We officers were instead "
                         "expected to rally our troops in a final charge towards the enemy, where we were expected to "
                         "use our bayonets to mow down as many enemies as we can before we go down ourselves.\n"
                         "As the discussions continued, an explosion suddenly rocked the building and we noticed that "
                         "the Allied troops have made their way to HQ. As the officers clamored to leave the room and "
                         "find their own troops, yet another explosion rocked the building. As the lieutenant and "
                         "commander of your platoon, you immediately rush out of the HQ and bark orders to your "
                         "platoon soldiers, immediately urging them to rendezvous with you near the exit of HQ. The "
                         "ongoing gunfire and mortar shots were deafening, indicating an intense battle ahead.\n",
                   moment="With your soldiers in tow, you can either: A) Proceed immediately to the spot you and your "
                          "platoon were assigned to defend, B) Fabricate orders and seek shelter deeper inside the "
                          "forest near you?\n",
                   type="normal")
scenario_3a = Story(story="You immediately issue orders to your platoon to defend the rear of the HQ and take up "
                          "several defense positions in pillboxes, some mounted with machine guns. The Allied soldiers "
                          "come in huge numbers, and your fellow Japanese soldiers quickly get overwhelmed despite "
                          "having the initial advantage being the defenders.\n",
                    moment="You suffer quite a few minor injuries like abrasions and bullet grazes and have lost 5 men "
                           "from your platoon. Despite the feeling of responsibility and guilt, you decide to withdraw "
                           "your platoon from the battle and retreat the woods as the officer in charge of your platoon"
                           ". The Allied troops were still coming in droves, and your position was no longer tenable.\n"
                           "Should you: A) Take charge of the retreat and proceed towards the forest or B) Allow one "
                           "of your men to take charge and be the last few to leave, ensuring that no one else from "
                           "your platoon is left behind vainly?\n",
                    type="luck_damage")
scenario_3aa = Story(story="You decide to take charge of the retreat and enter the forest on your own first. To your "
                           "utter shock, you see an American platoon inside the forest and unfortunately, get shot to "
                           "death immediately. You die.\n",
                     moment=None,
                     type="normal")
scenario_3ab = Story(story="You decide that, as commander of your platoon, you have the obligation to ensure that "
                           "every soldier of yours is able to leave safely to the forest. You decide to stay on for "
                           "awhile more to scour your surroundings and see that every last man of yours has "
                           "retreated.\n",
                     moment="With all of your troops seemingly having retreated, you return to the fore of your "
                            "platoon as quickly as you can and discover to your dismay a few dead men from your "
                            "platoon. Looking to the front made you realize the reason why: there was an Australian "
                            "squad lying in wait in the jungle, but they have been disposed of by your surviving "
                            "platoon soldiers. You make a mental note to yourself of the importance of staying "
                            "vigilant even in the jungle, and proceed further in.\n",
                     type="luck_damage")
scenario_3b = Story(story="You notice the low morale of your platoon and the increasing desperation that the army "
                          "has displayed in the previous meeting. Taking these as hints that engaging in a defensive "
                          "battle will not do much good, you decide to announce a retreat into the woods in an attempt "
                          "to prioritize the survival of your men.\nTo your surprise, your men vehemently insist "
                          "against retreat despite your fabricated orders. Cries of “We must win for the Emperor” and "
                          "“Retreat is never an option!” reverberate across your platoon soldiers, and very soon you "
                          "are forced to make yet another decision.\n",
                    moment="Do you choose to still: A) Still retreat, or B) Proceed to the original position you "
                           "are supposed to defend?\n",
                    type="normal")
scenario_3ba = Story(story="You stand your ground on the need to retreat but accusations of being a coward and a "
                           "traitor to the Empire start to pile up even from the enlisted men of your platoon. You "
                           "realize to your despair the frightening extent of nationalism that has infected the minds "
                           "of your men, and that despite your own love for Japan, you have always still been smart "
                           "enough to distinguish real patriotism from trumped-up propagandas and lies.\n"
                           "As you are about to agree with your men’s suggestions to press on with the defense, "
                           "you suddenly feel a gaping pain in your chest and blood flowing out of your wound. You "
                           "have been shot! By your assistant Sergeant Tanaka! Tanaka reaches down as you fall and "
                           "shakes his head at your earlier decision to retreat. “Sir, although you are our "
                           "commanding officer, it seems that you are not as devoted to the Emperor as the rest of "
                           "us. Let me take charge of the men instead.” Tanaka said.\n"
                           "With that, you are left to die as your platoon abandons you to defend the HQ. You die.\n",
                     moment=None,
                     type="normal")
scenario_3bb = Story(story="At the sight of your platoon soldiers on the brink of revolting against you and your "
                           "decision to retreat, you decide to be smart and proceed with the defense of the "
                           "HQ instead. This helps placate most of your troops, and you proceed to the defensive "
                           "position.\nYou immediately issue orders to your platoon to defend the rear of the HQ "
                           "and take up several defense positions in pillboxes, some mounted with machine guns. The "
                           "Allied soldiers come in huge numbers, and your fellow Japanese soldiers quickly get "
                           "overwhelmed despite having the initial advantage being the defenders.\n",
                     moment="You suffer quite a few minor injuries like abrasions and bullet grazes and have lost 5 "
                            "men from your platoon. Despite the feeling of responsibility and guilt, you decide to "
                            "withdraw your platoon from the battle and retreat the woods as the officer in charge of "
                            "your platoon. The Allied troops were still coming in droves, and your position was no "
                            "longer tenable.\nShould you: A) Take charge of the retreat and proceed towards the "
                            "forest or B) Allow one of your men to take charge and be the last few to leave, ensuring "
                            "that no one else from your platoon is left behind vainly?",
                     type="luck_damage")
scenario_3bba = Story(story="You decide to take charge of the retreat and enter the forest on your own first. To "
                            "your utter shock, you see an American platoon inside the forest and unfortunately, get "
                            "shot to death immediately. You die.\n",
                      moment=None,
                      type="normal")
scenario_3bbb = Story(story="You decide that, as commander of your platoon, you have the obligation to ensure that "
                            "every soldier of yours is able to leave safely to the forest. You decide to stay on for a "
                            "while more to scour your surroundings and see that every last man of yours has "
                            "retreated.\n",
                      moment="With all of your troops seemingly having retreated, you return to the fore of your "
                             "platoon as quickly as you can and discover to your dismay a few dead men from your "
                             "platoon. Looking to the front made you realize the reason why: there was an Australian "
                             "squad lying in wait in the jungle, but they have been disposed of by your surviving "
                             "platoon soldiers. You make a mental note to yourself of the importance of staying "
                             "vigilant even in the jungle, and proceed further in.\n",
                      type="luck_damage")

"""
Add the stories to the appropriate choice a or choice b branches in a bottom up manner.
"""
scenario_1.insert_story_node(scenario_1a, True)
scenario_1.insert_story_node(scenario_1b, False)
scenario_1a.insert_story_node(scenario_2, True)
scenario_1b.insert_story_node(scenario_2, True)

scenario_2.insert_story_node(scenario_2a, True)
scenario_2.insert_story_node(scenario_2b, False)
scenario_2a.insert_story_node(scenario_2aa, True)
scenario_2a.insert_story_node(scenario_2ab, False)
scenario_2aa.insert_story_node(scenario_2aaa, True)
scenario_2aa.insert_story_node(scenario_2aab, False)
scenario_2aaa.insert_story_node(scenario_2aaaa, True)
scenario_2aaa.insert_story_node(scenario_2aaab, False)
scenario_2aaaa.insert_story_node(scenario_3, True)
scenario_2aaab.insert_story_node(scenario_3, True)
scenario_2aab.insert_story_node(scenario_3, True)
scenario_2ab.insert_story_node(scenario_2aba, True)
scenario_2ab.insert_story_node(scenario_2abb, False)
scenario_2aba.insert_story_node(scenario_2abaa, True)
scenario_2aba.insert_story_node(scenario_2abab, False)
scenario_2abaa.insert_story_node(scenario_2abaaa, True)
scenario_2abaa.insert_story_node(scenario_2abaab, False)
scenario_2abab.insert_story_node(scenario_3, True)
scenario_2abaaa.insert_story_node(scenario_3, True)
scenario_2abaab.insert_story_node(scenario_3, True)
scenario_2abb.insert_story_node(scenario_3, True)

scenario_3.insert_story_node(scenario_3a, True)
scenario_3.insert_story_node(scenario_3b, False)
scenario_3a.insert_story_node(scenario_3aa, True)
scenario_3a.insert_story_node(scenario_3ab, False)
scenario_3b.insert_story_node(scenario_3ba, True)
scenario_3b.insert_story_node(scenario_3bb, False)
scenario_3bb.insert_story_node(scenario_3bba, True)
scenario_3bb.insert_story_node(scenario_3bbb, False)



