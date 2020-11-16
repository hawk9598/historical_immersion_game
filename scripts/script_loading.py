from classes.story_generator import Story

"""
Initialize the scripts of the story with the appropriate types, story text and moment (choice) text
"""
scenario_1 = Story(story="Chapter 1 (Beginnings):\n\n"
                         "In May 1942, your superior officer approaches you and the platoon you are in charge of and "
                         "gives you all a short briefing on the upcoming battle you are all asked to join. The battle "
                         "will be held in Guadalcanal, and resistance is anticipated to be mild. Your platoon’s "
                         "soldiers are psyched about the seemingly low risk opportunity, and most agree immediately to "
                         "joining the battle.\n\nAlthough everything does indeed sound good on paper, you still have "
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
scenario_2 = Story(story="Chapter 2 (The Beginning of Tragedy):\n\n"
                         "It has been 3 months since the IJA has invaded Guadalcanal, and the construction of the "
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
                          "doubtful of your choice, you head back and end up having a good night’s rest.\n\n"
                          "The next morning arrives, and you wake up feeling all refreshed. You see the rest of your "
                          "platoon freshly awake as well in the common area of the bunk, and proceed towards the usual "
                          "patrol spot with them behind you.\n\n"
                          "However, just as you reach the patrol spot, you hear the loud blares of the air raid "
                          "emergency horn being sounded and realize that the worst is about to happen: An Allied "
                          "invasion of Guadalcanal!\n",
                    moment="At this point, you have to make a choice: A) Do you choose to immediately seek underground "
                           "shelter as per protocol or B) Go for glory and man the closest anti-aircraft artilleries "
                           "in an attempt to shoot down the invaders?\n",
                    type="normal")
scenario_2aa = Story(story="You decide that in such an air raid, safety is first and following the protocol will never "
                           "be wrong, and you immediately rally your troops and proceed to the nearest makeshift "
                           "bunker to regroup and wait for further orders.\n\n"
                           "You quickly find the nearest bunker and realize that quite a few of the other platoons "
                           "have already made it there. The senior officer, Colonel Yamaguchi, is in the midst of "
                           "issuing combat orders and you realize that all of you inside the bunker are assigned to "
                           "take up key defense positions which are located outdoors.  Your platoon is allocated to "
                           "defend the exterior of the bunker from incoming Allied ground troops and you proceed "
                           "there.\n\nAs expected, there are a massive number of incoming troops and despite the safety"
                           " of your position due to the sandbags and mounted machine guns, you still suffer some "
                           "damage.\n",
                     moment="Nevertheless, you manage to survive the skirmish! Your other troops are fine and lightly "
                            "injured as are you, and you proceed to scour the surroundings for survivors. You "
                            "encounter an injured Australian soldier who promptly surrenders at the sight of you and "
                            "your troops.\n\nYour troops, being injured from the skirmish and displaying a visible "
                            "amount of animosity towards the injured soldier, ask of you to dispose of the survivor "
                            "despite his surrender. Knowing that this is against international law and that POWs still "
                            "have their rights, do you : A) Decide to take in the surrendering Australian soldier as a "
                            "POW, or B) Follow your troops’ will and execute the invader who dares to stand up against "
                            "Japan’s conquest of Guadalcanal?\n",
                     type="luck_damage")
scenario_2aaa = Story(story="You decide that, despite your troops’ desire to kill the Australian soldier, to keep the "
                            "soldier alive as a POW. You promptly ask one of your troops to arrest the soldier, who "
                            "proceeds to then do the deed.\n\nTo your complete surprise, the Australian POW pulls out a"
                            " hidden handgun and shoots your soldier and you successively in the arm, whilst a few "
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
                             "in the process of arresting the Australian and apologize for your earlier decision.\n\n"
                             "Although this decision of yours was indeed the right thing to do at the moment, you "
                             "still can’t help but wonder whether it was the morally right choice to do. Nevertheless, "
                             "you ignore this voice in your head and proceed to scour the remains of the skirmish for "
                             "more survivors.\n",
                       moment=None,
                       type="chapter_end")
scenario_2aaab = Story(story="Despite the injury you have suffered, you still decide to comply with international law "
                             "and ask your assistant, Sergeant Tanaka to arrest the Australian. Contrary to your "
                             "expectations, Tanaka instead pulls out his own sidearms and executes the Australian "
                             "soldier via a shot to the head.\n\n'Sir, why are you planning to let this savage live"
                             " when he just took advantage of your kindness?' an enraged Tanaka shouts.\n\nThe usual"
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
                            "can before his demise!\n\nPondering to yourself, you start to applaud yourself for your "
                            "decision, with your troops heaving sighs of relief at your decision to execute the "
                            "Australian. Although this decision of yours was indeed the right thing to do at the "
                            "moment, you still can’t help but wonder whether it was the morally right choice to do. "
                            "Nevertheless, you ignore this voice in your head and proceed to scour the remains of the "
                            "skirmish for more survivors.\n",
                      moment=None,
                      type="chapter_end")
scenario_2ab = Story(story="You decide that now is the best moment to seize glory and to stop the Allied air invaders "
                           "with your platoon. You rile up the rest of your troops and proceed to man the air "
                           "artillery guns present in an attempt to stop the incoming attacks.\n\nAlthough your efforts"
                           " are initially awarded, you notice that there seemed to be a never-ending barrage of new "
                           "planes. You immediately call for your troops to retreat and proceed towards the bunker but "
                           "are then hit by some air bombardment and suffer some injuries alongside the rest.\n",
                     moment="Nevertheless, you survive and manage to make it to the underground bunker in time with "
                            "your troops, although a sizeable number of them have suffered from minor injuries as well."
                            "\n\nHaving received quick treatment for your injuries quickly and after being reprimanded "
                            "by your senior officer for breaching protocol, you are forced to guard the exterior of "
                            "the bunker with your platoon mates. Do you choose to: 1) Protest against this assignment "
                            "given the injuries you and your troops have just suffered or 2) Resign to your fate and "
                            "go defend against the incoming skirmish from land Allied troops?\n",
                     type="luck_damage")
scenario_2aba = Story(story="You protest against this assignment but your senior officer, Colonel Yamaguchi, gives you "
                            "a deathly stare and mentions that any further objection will amount to insubordination "
                            "and direct execution on the spot. Feeling rather shaken, you have no choice but to accept "
                            "the outcome and go out to defend against the incoming waves of Allied attackers even "
                            "after suffering from earlier injuries due to your misplaced bravado.\n\n"
                            "As expected, there are a massive number of incoming troops and despite the safety of "
                            "your position due to the sandbags and mounted machine guns, you still suffer damage.\n",
                      moment="Nevertheless, you manage to survive the skirmish! Your other troops are fine and lightly "
                             "injured as are you, and you proceed to scour the surroundings for survivors. You "
                             "encounter an injured Australian soldier who promptly surrenders at the sight of you and "
                             "your troops.\n\n"
                             "Your troops, being injured from the skirmish and displaying a visible amount of "
                             "animosity towards the injured soldier, ask of you to dispose of the survivor despite "
                             "his surrender. Knowing that this is against international law and that POWs still have "
                             "their rights, do you : A) Decide to take in the surrendering Australian soldier as a POW,"
                             " or B) Follow your troops’ will and execute the invader who dares to stand up against "
                             "Japan’s conquest of Guadalcanal?\n",
                      type="luck_damage")
scenario_2abaa = Story(story="You decide that, despite your troops’ desire to kill the Australian soldier, to keep the "
                             "soldier alive as a POW. You promptly ask one of your troops to arrest the soldier, who "
                             "proceeds to then do the deed.\n\nTo your surprise, the Australian POW pulls out a"
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
                              " in the process of arresting the Australian and apologize for your earlier decision.\n\n"
                              "Although this decision of yours was indeed the right thing to do at the moment, you "
                              "still can’t help but wonder whether it was the morally right choice to do. Nevertheless,"
                              " you ignore this voice in your head and proceed to scour the remains of the skirmish for"
                              "more survivors.\n",
                        moment=None,
                        type="chapter_end")
scenario_2abaab = Story(story="Despite the injury you have suffered, you still decide to comply with international law "
                              "and ask your assistant, Sergeant Tanaka to arrest the Australian. Contrary to your "
                              "expectations, Tanaka instead pulls out his own sidearms and executes the Australian "
                              "soldier via a shot to the head.\n\n'Sir, why are you still planning to let this savage "
                              "live when he has just taken advantage of your kindness?' an enraged Tanaka shouts.\n\n"
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
                             "can before his demise!\n\nPondering to yourself, you start to applaud yourself for your "
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
                          "excitedly talk about the fun ahead for the night.\n\nAs expected, most of the soldiers in "
                          "your platoon including you went wild with the amount of sake drunk, and you managed to win "
                          "a few days’ worth of rations from the gambling. You feel happy about your decision to "
                          "approve the platoon’s suggestion of the activity and scoffed at your past self for even "
                          "considering going back to the bunk and have an early night instead. As everyone else fell "
                          "asleep in the common area of the bunk, you also follow suit and pass out from the alcohol "
                          "peacefully with the rest of the others.\n\nYou are suddenly rudely awakened by the sound of "
                          "blaring fire alarms and explosions all around the vicinity and awake to see 3 of your "
                          "platoon soldiers lying down all injured from air bombardment. You immediately regret your "
                          "decision, and as you desperately try to rally your other troops to go towards the bunker, "
                          "you get struck by an air bomb and unfortunately die. Your decision to party with your "
                          "platoon mates the previous night turned out to be the wrong decision, and one can never be "
                          "lax during the war!\n",
                    moment=None,
                    type="normal")
scenario_3 = Story(story="Chapter 3 (Defeat and Beginning of the End):\n\n"
                         "Despite your first victory over the invading Allied troops whilst defending the underground "
                         "bunker, the Imperial Japanese Army was still overrun by the never-ending waves of Allied "
                         "troops. Japan was utterly defeated in terms of sheer firepower and soldiers to spare. Having "
                         "suffered defeat and having the original base you were at attacked and relinquished to the"
                         " enemy, you and your platoon were forced to retreat to the HQ of the IJA in Guadalcanal.\n\n"
                         "In an emergency meeting solely meant for officers only, General Imamura stressed on the "
                         "importance of fighting till the bitter end and the bushido spirit, whilst warning any of us "
                         "officers to not engage in any acts of surrender despite defeat. We officers were instead "
                         "expected to rally our troops in a final charge towards the enemy, where we were expected to "
                         "use our bayonets to mow down as many enemies as we can before we go down ourselves.\n\n"
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
                           ". The Allied troops were still advancing, and your position was no longer tenable.\n\n"
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
                     type="chapter_end")
scenario_3b = Story(story="You notice the low morale of your platoon and the increasing desperation that the army "
                          "has displayed in the previous meeting. Taking these as hints that engaging in a defensive "
                          "battle will not do much good, you decide to announce a retreat into the woods in an attempt "
                          "to prioritize the survival of your men.\n\nTo your surprise, your men vehemently insist "
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
                           "enough to distinguish real patriotism from trumped-up propaganda and lies.\n\n"
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
                           "position.\n\nYou immediately issue orders to your platoon to defend the rear of the HQ "
                           "and take up several defense positions in pillboxes, some mounted with machine guns. The "
                           "Allied soldiers come in huge numbers, and your fellow Japanese soldiers quickly get "
                           "overwhelmed despite having the initial advantage being the defenders.\n",
                     moment="You suffer quite a few minor injuries like abrasions and bullet grazes and have lost 5 "
                            "men from your platoon. Despite the feeling of responsibility and guilt, you decide to "
                            "withdraw your platoon from the battle and retreat the woods as the officer in charge of "
                            "your platoon. The Allied troops were still coming in droves, and your position was no "
                            "longer tenable.\n\nShould you: A) Take charge of the retreat and proceed towards the "
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
                      type="chapter_end")
scenario_4 = Story(story="It has been close to a week since you lead your platoon into the forest, and despite the "
                         "decreasing encounters with the Allied troops , you and your soldiers face the difficult "
                         "tasks of sourcing food, treating the wounded, and staying alive in the hot and humid "
                         "forest of Guadalcanal.\n\nIt is late evening and it is close to getting dark, and "
                         "you peer into the contents of your own diary, which you have been writing in every "
                         "night to keep your own sanity in check. The diary reads: \n'To Mother and Father, it has "
                         "been close to a week since I have been stuck in a jungle evading enemy forces and close "
                         "to 4 months since I have left Japan. I have lost slightly over half of my platoon and am "
                         "myself nursing some minor-moderate injuries whilst being constantly on the run.\n\nI "
                         "remember the day I signed up for this war as an officer: It was a cold and breezy "
                         "day just months after my graduation from Waseda; and I was back then a clear-eyed, "
                         "idealistic man who was passionate for Japan’s liberation of the other Asian "
                         "countries under Western colonialism. “Would it not do good for these countries "
                         "to be free of Western rule, and have Japan share the fruits of her modernization "
                         "with these countries?” I had so innocently thought. It is with this thought where "
                         "I passionately signed up for a war that purportedly claimed to liberate the other "
                         "Asian people and to ultimately glorify the Emperor via Japan’s victories.\n\nHowever, "
                         "even in officer school, I saw many atrocities occur in the name of the Emperor "
                         "that made me wonder more and more about Japan’s goal for the war. I still recall the "
                         "trembling arms of a cadet who was just forced to behead a Chinese POW as a rite of "
                         "passage, with the rest of the senior officers at the side applauding him for his ‘work’ "
                         "whilst the cadet himself seemed to have lost part of his humanity then…'\n",
                   moment="As you are about to continue reading your diary, you are interrupted by Private Yamaguchi, "
                          "who promptly urges you to take a sleep first in preparation for night guard duty where "
                          "everyone rotates to keep watch of Allied soldiers. As you drift into sleep, you struggle "
                          "to recall the remaining contents of that specific diary entry which you wrote a few days "
                          "ago. Was it something along the lines of : A) 'It is these atrocities alone that have "
                          "slowly changed my goal of participating the war. Instead of glory, all I look out for is "
                          "to survive and tell the tale of this god-forsaken war to the later generations, even if "
                          "the memory of these atrocities will forever haunt me' or B) 'However, despite these "
                          "atrocities, I still wholeheartedly believe in the need to at least glorify the "
                          "Emperor’s name and to staunchly defend Japan against the barbarians. After all, "
                          "if not for the Emperor or Japan, how would we then justify these atrocities?'\n",
                   type="normal")
scenario_4a = Story(story="You are nudged awake by one of your platoon soldiers as a signal for you to begin your "
                          "shift of guard duty. It is still late in the night, and despite having slept for close "
                          "to 3 hours, you still feel largely lethargic and tired from a lack of rest.\n\nAs your "
                          "surroundings seem to be safe and quiet for now, you ruffle through your bag and try "
                          "to find your journal to continue your diary taking. However, as hard as you try, you "
                          "can’t seem to find your diary among the remains of your rations and firearms. Just as "
                          "you are about to turn around to check whether your soldiers might have mistakenly taken "
                          "your diary, you feel the nudge of a rifle barrel against your back and immediately stop "
                          "whatever you are doing and slowly raise your arms.\n\n'Sir, might you have been looking "
                          "for this” says Sergeant Tanaka as he holds up your diary journal against your face "
                          "whilst menacingly prodding his rifle against your back.'\n\n'Shit. Sergeant Tanaka "
                          "is one of the more fanatical soldiers in the army, and him discovering that journal "
                          "does not bode well for me…”, you think as you slowly turn around to face the sergeant.'\n\n"
                          "In the army, despite the seniority of junior officers over the senior enlisted men, "
                          "this was mostly in name only and the sergeant still commands most of the respect from "
                          "the platoon given the vast difference in the number of years of army experience that "
                          "junior officers have as compared to the senior enlisted men.\n",
                    moment="'Sir, it seems like you do not have much favorable opinions of Japan and his royal "
                           "highness the Emperor, which can only mean that you are one of those liberal traitors "
                           "against Japan.', says Sergeant Tanaka who looks prepared to execute you on the spot for "
                           "this grave mistake.\n\nWhat do you do? Do you: A) Plead your case against "
                           "Sergeant Tanaka and urge him to realize the pointlessness of the war and that "
                           "survival is instead key or B) Scold Tanaka for his false allegations and berate "
                           "him for his mistaken ideas?\n",
                    type="normal")
scenario_4aa = Story(story="You plead your case against Sergeant Tanaka, but unfortunately the man does not seem to "
                           "listen to your explanations. Just as he is about to shoot you, however, the sudden sounds "
                           "of English conversations from the incoming Allied soldiers shocks him temporarily and "
                           "you use this as an opportunity to wrestle Tanaka to the ground.\n",
                     moment="Do you: A) Disarm Tanaka and leave him promptly to wake the rest of your platoon "
                            "soldiers up to warn them against the incoming enemies or B) Pick up the rifle and "
                            "quickly execute Tanaka for insubordination (which you can use to explain your actions "
                            "later on to your platoon soldiers) but risk discovery by the Allied soldiers which will "
                            "put you and your platoon in considerable danger?\n",
                     type="normal")
scenario_4aaa = Story(story="You proceed to quickly disarm Tanaka and leave him lying on the floor as you rush to warn "
                            "your comrades of the incoming Allied soldiers. However, just as you are about to warn the "
                            "first soldier you can find, you find yourself shot in the back by Tanaka, who had a hidden"
                            " handgun in his uniform all the while! You are left to bleed out in the midst of the "
                            "Allied soldier’s attack on your platoon soldiers, who have now discovered your platoon’s "
                            "presence due to Tanaka’s firing of the handgun. You die witnessing your helpless soldiers "
                            "get massacred by the Allied soldiers.\n",
                   moment=None,
                   type="normal")
scenario_4aab = Story(story="You decide to get rid of Tanaka despite the considerable risk because you can not see "
                            "how else to not get backstabbed by Tanaka in the midst of a possible Allied attack. "
                            "You pick up his rifle, shoot him in the head, and yell at your soldiers to wake up and "
                            "retreat before unleashing smoke grenades all over the place to mask your platoon’s "
                            "escape from the incoming Allied soldiers.\n",
                      moment="Despite the attack from the Allied soldiers, you and most of your platoon soldiers "
                             "make it out of the situation with minor injuries and proceed deeper into the forest "
                             "for further cover. Your platoon asks you for the whereabouts of Sergeant Tanaka, "
                             "which you simply cover up by saying that the Allied soldiers got to him first "
                             "before he managed to escape alongside the rest of you.\n\nNevertheless, the "
                             "situation over the next 2 weeks grow more and more dire for you and the rest of "
                             "your platoon, as more sneak attacks from the Allied troops leave fewer and fewer of "
                             "your platoon mates surviving. With only 5 of your soldiers and you left, you are left "
                             "to make a drastic decision. Do you: A) Surrender to the next group of Allied soldiers "
                             "you encounter or B) Press on regardless and hope for Japanese reinforcements to come?\n",
                      type="luck_damage")
scenario_4aaba = Story(story="Seeing the desperate situation that you are in, you decide (with reluctant agreement "
                             "from the rest of the survivors) to surrender to the next group of Allied soldiers "
                             "you see.\n\nThat night, you proceed to pen down your thoughts into the diary you "
                             "recovered from Tanaka after the confrontation between the two of you that day:\n\n'To "
                             "Mother and Father, it is getting closer to the day where my remaining"
                             " soldiers and I will surrender to the Allies. I can’t help but feel that "
                             "despite the highly desperate situation that my soldiers and I are in, death is "
                             "still a much better respite as compared to shamefully surrendering to the Allied "
                             "soldiers.\n\nAlthough there have been rumors that the Allied soldiers do not treat "
                             "POWs well, I believe that the case is different for the Australian soldiers and for "
                             "this battle, because the war has slowly become a war of attrition between us and the "
                             "Australians and having a Japanese officer with them will be helpful for them to end "
                             "this futile war quickly.\n\nNevertheless, I pray hope that you will be able to "
                             "understand your unfilial son’s decision in surrendering as opposed to dying on the "
                             "battlefield. I sincerely wish to see Japan once more, and despite the shamefulness of "
                             "surrendering, I truly believe that the tale of this war can serve as a warning and "
                             "lesson to learn for the generations to come. Japan might lose or surrender in the "
                             "future, but this does not mean that the Empire of Japan will be lost forever; we can "
                             "always come back in the future stronger than ever, without having to engage in such "
                             "meaningless, futile wars and sacrificing the lives of so many loyal Japanese.\n\nI hope "
                             "you all will be able to understand my sentiments. I pray hope to see you all soon and "
                             "to be able to once again drink miso soup and chat about anything and everything with "
                             "sake.'\n\nThe very next day, you wake up to notice that 2 out of 5 of your platoon’s "
                             "survivors have decided to commit ritual suicide instead of surrendering to the enemy, "
                             "and you grimly bury their bodies with the 3 remaining survivors. Although you have your "
                             "doubts (and fear that all this might lead to death regardless), you and your surviving "
                             "soldiers find an Allied platoon and immediately wave a crude white flag indicating your "
                             "surrender. You use your bare knowledge of English to indicate your surrender, shouting "
                             "at the top of your lungs all the while ensuring that you and your soldiers have both "
                             "arms in the air to indicate non-hostility. The Allied soldiers take note of your "
                             "surrender, and approach you slowly before arresting you and your soldiers as POWs.\n",
                       moment=None,
                       type="chapter_end")
scenario_4aabb = Story(story="Seeing the desperate situation that you are in, you decide to follow the wishes of your "
                             "surviving soldiers and most of them decided to press on in the forest and wait for "
                             "Japanese reinforcements.\n\n…\n\nMonths have passed and you and another one of "
                             "your soldiers are all that remains of the platoon. No reinforcements have came so "
                             "far, and the number of Allied soldiers left on Guadalcanal have dwindled down.\n",
                       moment="Facing the possibility of malnutrition after having spent months without proper food "
                              "in the jungle, you get closer to death every day, and are finally forced to make a "
                              "decision: A) Surrender to the remaining natives on the island and hope that you will "
                              "not be killed on first sight given that most Japanese are already presumed to be dead "
                              "currently, B) Die an honorable death by blowing yourself up the next time you "
                              "encounter enemies?\n",
                       type="normal")
scenario_4aabba = Story(story="Becoming desperate from the lack of water and food, you decide to immediately seek "
                              "out the help of the natives and surrender. After hours of searching, you find a "
                              "settlement of natives and proceed to wave your white flag in to surrender.\n\n"
                              "Unfortunately, you realize that the particular settlement you are surrendering to "
                              "lost a lot of natives due to the previous Japanese occupation on the island before "
                              "the arrival of the Allied forces, and they react hostilely and decide to execute you "
                              "instead. You die, wondering if it might have been a better choice to surrender earlier "
                              "to the Allied forces instead.\n",
                        moment=None,
                        type="normal")
scenario_4aabbb = Story(story="You decide against surrendering to the natives, knowing that most of them are still "
                              "hostile towards the Japanese due to the effects of the short Japanese occupation of "
                              "Guadalcanal. Being all prepared now, you write a death poem:\n\n'Wide-eyed and eager,\n"
                              "I charged to the forefront,\nAll ready to die,\nFor family and country,\n"
                              "To bring peace and safety home.'\n\nWith your death poem complete, you mentally prepare "
                              "yourself and your other soldier to blow yourselves up with grenades during the next "
                              "time you encounter an Allied soldier platoon.\n",
                        moment=None,
                        type="normal")
scenario_4ab = Story(story="You decide to accuse Sergeant Tanaka of false allegations and claim that the diary "
                           "journal does not belong to you. Unfortunately, your flimsy defense and scolding does "
                           "not persuade the fanatical soldier and he instead prepares to kill you for being a "
                           "traitor towards Japan and the Emperor. Just as he is about to shoot you, however, the "
                           "sudden sounds of English conversations from the incoming Allied soldiers shocks him "
                           "temporarily and you use this as an opportunity to wrestle Tanaka to the ground.",
                     moment="Do you: A) Disarm Tanaka and leave him promptly to wake the rest of your platoon "
                            "soldiers up to warn them against the incoming enemies or B) Pick up the rifle and "
                            "quickly execute Tanaka for insubordination (which you can use to explain your actions "
                            "later on to your platoon soldiers) but risk discovery by the Allied soldiers which will "
                            "put you and your platoon in considerable danger?\n",
                     type="normal")
scenario_4aba = Story(story="You proceed to quickly disarm Tanaka and leave him lying on the floor as you rush to warn "
                            "your comrades of the incoming Allied soldiers. However, just as you are about to warn the "
                            "first soldier you can find, you find yourself shot in the back by Tanaka, who had a "
                            "hidden handgun in his uniform all the while! You are left to bleed out in the midst of the"
                            " Allied soldier’s attack on your platoon soldiers, who have now discovered your platoon’s "
                            "presence due to Tanaka’s firing of the handgun. You die witnessing your helpless soldiers "
                            "get massacred by the Allied soldiers.\n",
                   moment=None,
                   type="normal")
scenario_4abb = Story(story="You decide to get rid of Tanaka despite the considerable risk because you can not see "
                            "how else to not get backstabbed by Tanaka in the midst of a possible Allied attack. "
                            "You pick up his rifle, shoot him in the head, and yell at your soldiers to wake up and "
                            "retreat before unleashing smoke grenades all over the place to mask your platoon’s "
                            "escape from the incoming Allied soldiers.\n",
                      moment="Despite the attack from the Allied soldiers, you and most of your platoon soldiers "
                             "make it out of the situation with minor injuries and proceed deeper into the forest "
                             "for further cover. Your platoon asks you for the whereabouts of Sergeant Tanaka, "
                             "which you simply cover up by saying that the Allied soldiers got to him first "
                             "before he managed to escape alongside the rest of you.\n\nNevertheless, the "
                             "situation over the next 2 weeks grow more and more dire for you and the rest of "
                             "your platoon, as more sneak attacks from the Allied troops leave fewer and fewer of "
                             "your platoon mates surviving. With only 5 of your soldiers and you left, you are left "
                             "to make a drastic decision. Do you: A) Surrender to the next group of Allied soldiers "
                             "you encounter or B) Press on regardless and hope for Japanese reinforcements to come?\n",
                      type="luck_damage")
scenario_4abba = Story(story="Seeing the desperate situation that you are in, you decide (with reluctant agreement "
                             "from the rest of the survivors) to surrender to the next group of Allied soldiers "
                             "you see.\n\n That night, you proceed to pen down your thoughts into the diary you "
                             "recovered from Tanaka after the confrontation between the two of you that day:\n\n'To "
                             "Mother and Father, it is getting closer to the day where my remaining"
                             " soldiers and I will surrender to the Allies. I can’t help but feel that "
                             "despite the highly desperate situation that my soldiers and I are in, death is "
                             "still a much better respite as compared to shamefully surrendering to the Allied "
                             "soldiers.\n\nAlthough there have been rumors that the Allied soldiers do not treat "
                             "POWs well, I believe that the case is different for the Australian soldiers and for "
                             "this battle, because the war has slowly become a war of attrition between us and the "
                             "Australians and having a Japanese officer with them will be helpful for them to end "
                             "this futile war quickly.\n\nNevertheless, I pray hope that you will be able to "
                             "understand your unfilial son’s decision in surrendering as opposed to dying on the "
                             "battlefield. I sincerely wish to see Japan once more, and despite the shamefulness of "
                             "surrendering, I truly believe that the tale of this war can serve as a warning and "
                             "lesson to learn for the generations to come. Japan might lose or surrender in the "
                             "future, but this does not mean that the Empire of Japan will be lost forever; we can "
                             "always come back in the future stronger than ever, without having to engage in such "
                             "meaningless, futile wars and sacrificing the lives of so many loyal Japanese.\n\nI hope "
                             "you all will be able to understand my sentiments. I pray hope to see you all soon and "
                             "to be able to once again drink miso soup and chat about anything and everything with "
                             "sake.'\n\nThe very next day, you wake up to notice that 2 out of 5 of your platoon’s "
                             "survivors have decided to commit ritual suicide instead of surrendering to the enemy, "
                             "and you grimly bury their bodies with the 3 remaining survivors. Although you have your "
                             "doubts (and fear that all this might lead to death regardless), you and your surviving "
                             "soldiers find an Allied platoon and immediately wave a crude white flag indicating your "
                             "surrender. You use your bare knowledge of English to indicate your surrender, shouting "
                             "at the top of your lungs all the while ensuring that you and your soldiers have both "
                             "arms in the air to indicate non-hostility. The Allied soldiers take note of your "
                             "surrender, and approach you slowly before arresting you and your soldiers as POWs.\n",
                       moment=None,
                       type="chapter_end")
scenario_4abbb = Story(story="Seeing the desperate situation that you are in, you decide to follow the wishes of your "
                             "surviving soldiers and most of them decided to press on in the forest and wait for "
                             "Japanese reinforcements.\n\n…\n\nMonths have passed and you and another one of "
                             "your soldiers are all that remains of the platoon. No reinforcements have came so "
                             "far, and the number of Allied soldiers left on Guadalcanal have dwindled down.\n",
                       moment="Facing the possibility of malnutrition after having spent months without proper food "
                              "in the jungle, you get closer to death every day, and are finally forced to make a "
                              "decision: A) Surrender to the remaining natives on the island and hope that you will "
                              "not be killed on first sight given that most Japanese are already presumed to be dead "
                              "currently, B) Die an honorable death by blowing yourself up the next time you "
                              "encounter enemies?\n",
                       type="normal")
scenario_4abbba = Story(story="Becoming desperate from the lack of water and food, you decide to immediately seek "
                              "out the help of the natives and surrender. After hours of searching, you find a "
                              "settlement of natives and proceed to wave your white flag to surrender.\n\n"
                              "Unfortunately, you realize that the particular settlement you are surrendering to "
                              "lost a lot of natives due to the previous Japanese occupation on the island before "
                              "the arrival of the Allied forces, and they react hostilely and decide to execute you "
                              "instead. You die, wondering if it might have been a better choice to surrender earlier "
                              "to the Allied forces instead.\n",
                        moment=None,
                        type="normal")
scenario_4abbbb = Story(story="You decide against surrendering to the natives, knowing that most of them are still "
                              "hostile towards the Japanese due to the effects of the short Japanese occupation of "
                              "Guadalcanal. Being all prepared now, you write a death poem:\n\n'Wide-eyed and eager,\n"
                              "I charged to the forefront,\nAll ready to die,\nFor family and country,\n"
                              "To bring peace and safety home.'\n\nWith your death poem complete, you mentally prepare "
                              "yourself and your other soldier to blow yourselves up with grenades during the next "
                              "time you encounter an Allied soldier platoon.\n",
                        moment=None,
                        type="normal")
scenario_4b = Story(story="You are nudged awake by one of your platoon soldiers as a signal for you to begin your "
                          "shift of guard duty. It is still late in the night, and despite having slept for close "
                          "to 3 hours, you still feel largely lethargic and tired from a lack of rest.\n\nYou turn "
                          "around and notice Sergeant Tanaka staring at you, and you proceed to ask him about what "
                          "his thoughts are about the current situation. However, instead of responding to your "
                          "question, he holds up your diary journal and applauds you for your thoughts, affirming "
                          "that he too believes that loyalty to the Emperor is most important in the war despite "
                          "the atrocities or lives lost.\n\nAlthough you are in shock over how he managed "
                          "to obtain your diary, he continues saying that he initially suspected that you were "
                          "simply yet another one of those liberal university graduates who would not care less "
                          "about the fate of the Emperor and Japan, and even muses that he considered killing you "
                          "if he were to find you being as such.\n\nHearing these words of his, you are in "
                          "complete surprise and reprimand him over his act of stealing your diary journal, before "
                          "going on to agree with him that ultimately, the Emperor and kokutai matters the most.\n\n"
                          "However, in the midst of the conversation, you overhear the footsteps of Allied soldiers "
                          "approaching and immediately proceed to rouse your soldiers so as to battle against "
                          "the enemy.\n",
                    moment="Despite the odds, you manage to survive the skirmish but proceed to realize that "
                           "you are only left with 4 other men in your charge, with the rest having perished "
                           "due to the skirmish or due to the earlier battles you all had in the forest.\n\nYou have "
                           "to now make a choice; do you decide to: A) Press on, while waiting for Japanese "
                           "reinforcements or B) Proceed in a suicidal charge towards the next group of Allied"
                           " soldiers you see?\n",
                    type="luck_damage")
scenario_4ba = Story(story="Seeing the desperate situation that you are in, you decide to follow the wishes of your "
                           "surviving soldiers and most of them decided to press on in the forest and wait for Japanese"
                           " reinforcements.\n\n…\n\nMonths have passed and you and another one of your "
                           "soldiers are all that remains of the platoon. No reinforcements have came so far, "
                           "and the number of Allied soldiers left on Guadalcanal have dwindled down.\n",
                     moment="Facing the possibility of malnutrition after having spent months without proper food in "
                            "the jungle, you get closer to death every day, and are finally forced to make a decision: "
                            "A) Die an honorable death by blowing yourself up the next time you encounter enemies or "
                            "B) Commit ritual suicide?\n",
                     type="normal")
scenario_4baa = Story(story="You decide against committing suicide, being eager to bring about the deaths of as many "
                            "other Allied soldiers as you can with your death. Being all prepared now, you write a "
                            "death poem:\n\n'Wide-eyed and eager,\nI charged to the forefront,\nAll ready to die,\n"
                            "For Emperor and country,\nFor glory and victory.'\n\nWith your death poem complete, you "
                            "mentally prepare yourself and your other soldier to blow yourselves up with grenades "
                            "during the next time you encounter an Allied soldier platoon.\n",
                      moment=None,
                      type="normal")
scenario_4bab = Story(story="You decide that committing ritual suicide would be the best way to go, given "
                            "the failure of the Imperial Japanese Army and your platoon in repelling the Allied "
                            "invaders. As the officer in charge of your platoon, it would be right for you to bear "
                            "this shame via ritual suicide. Being all prepared for your suicide, you write a "
                            "death poem:\n\n'Wide-eyed and eager,\nI charged to the forefront,\nAll ready to die,\n"
                            "For Emperor and country,\nFor glory and victory.'\n\nYou then ask your surviving soldiers "
                            "to help you in your ritual suicide, and you die as desired.\n",
                      moment=None,
                      type="normal")
scenario_4bb = Story(story="You decide that the best course of action your platoon can do now, even in the "
                           "face of defeat, is to bring about the deaths of as many other Allied soldiers as you "
                           "all can with your deaths. Being all prepared now, you write a death poem:\n\n'Wide-eyed "
                           "and eager,\nI charged to the forefront,\nAll ready to die,\nFor Emperor and country,\n"
                           "For glory and victory.'\n\nWith your death poem complete, you mentally prepare "
                           "yourself and your platoon to blow yourselves up with grenades during the next time "
                           "you encounter an Allied soldier platoon.\n",
                     moment=None,
                     type="normal")
scenario_5 = Story(story="After your surrender, you were subject to harsh interrogation about your role in the "
                         "invasion of Guadalcanal, before being released and being asked to coordinate the Allied "
                         "efforts in helping other Japanese soldiers be daring enough to surrender to the Allies, "
                         "given your position as officer.\n\nYou do your duties for the Allies, feeling deep "
                         "shame in your betrayal of the IJA. Yet, you still strive on to do so because you know "
                         "that ultimately, your actions will help save more Japanese lives and prevent futile deaths, "
                         "when so many of such deaths have already occurred in this battle.\n\n...\n\nAfter the war "
                         "ended, you return to your home in Japan and although you initially find struggle in "
                         "reconciling with your family due to your shameful act of surrendering and aiding the "
                         "Allies, you eventually manage to and become a lifelong proponent against war, having "
                         "witnessed the innumerable atrocities and futile deaths. You can now proudly look back "
                         "on your life and tell yourself that the choice to surrender and live was the right one.\n",
                   moment=None,
                   type="normal")

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
scenario_3ab.insert_story_node(scenario_4, True)
scenario_3b.insert_story_node(scenario_3ba, True)
scenario_3b.insert_story_node(scenario_3bb, False)
scenario_3bb.insert_story_node(scenario_3bba, True)
scenario_3bb.insert_story_node(scenario_3bbb, False)
scenario_3bbb.insert_story_node(scenario_4, True)

scenario_4.insert_story_node(scenario_4a, True)
scenario_4.insert_story_node(scenario_4b, False)
scenario_4a.insert_story_node(scenario_4aa,True)
scenario_4a.insert_story_node(scenario_4ab, False)
scenario_4aa.insert_story_node(scenario_4aaa, True)
scenario_4aa.insert_story_node(scenario_4aab, False)
scenario_4aab.insert_story_node(scenario_4aaba, True)
scenario_4aab.insert_story_node(scenario_4aabb, False)
scenario_4aaba.insert_story_node(scenario_5, True)
scenario_4aabb.insert_story_node(scenario_4aabba, True)
scenario_4aabb.insert_story_node(scenario_4aabbb, False)
scenario_4ab.insert_story_node(scenario_4aba, True)
scenario_4ab.insert_story_node(scenario_4abb, False)
scenario_4abb.insert_story_node(scenario_4abba, True)
scenario_4abb.insert_story_node(scenario_4abbb, False)
scenario_4abba.insert_story_node(scenario_5, True)
scenario_4abbb.insert_story_node(scenario_4abbba, True)
scenario_4abbb.insert_story_node(scenario_4abbbb, False)
scenario_4b.insert_story_node(scenario_4ba, True)
scenario_4b.insert_story_node(scenario_4bb, False)
scenario_4ba.insert_story_node(scenario_4baa, True)
scenario_4ba.insert_story_node(scenario_4bab, False)
