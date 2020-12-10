import random
import time

class QA:
  def __init__(self, question, correctAnswer):
    self.question = question
    self.corrAnsw = correctAnswer

qaList = [QA("Sledge - Assault Rifle", "L85A2"
          QA("Thatcher - Assault Rifle", "AR33"),
          QA("Fuze - Assault Rifle", "AK-12"),
          QA("IQ - Assault Rifle (A)", "AUG A2"),
          QA("IQ - Assault Rifle (C)", "552 Commando"),
          QA("Jager - Assault Rifle", "416-C"),
          QA("Twitch - Assault Rifle", "F2"),
          QA("Ash - Assault Rifle (G)", "G36C"),
          QA("Ash - Assault Rifle (R)", "R4-C"),
          QA("Thermite - Assault Rifle", "556xi"),
          QA("Buck - Assault Rifle", "C8-CFW"),
          QA("Blackbeard - Assault Rifle", "MK17"),
          QA("Capitao - Assault Rifle", "PARA-308"),
          QA("Hibana - Assault Rifle", "Type-89"),
          QA("Jackal - Assault Rifle", "C7E"),
          QA("Zofia - Assault Rifle", "M762"),
          QA("Lion - Assault Rifle", "V308"),
          QA("Finka - Assault Rifle", "Spear .308"),
          QA("Maverick - Assault Rifle (Automatic)", "M4"),
          QA("Maverick - Assault Rifle (Semi-Automatic)", "AR-15.50"),
          QA("Nomad - Assault Rifle (X)", "ARX200"),
          QA("Nomad - Assault Rifle (K)", "AK-74M"),
          QA("Smoke - SMG", "FMG-9"),
          QA("Mute - SMG", "MP5K"),
          QA("Bandit - SMG", "MP7"),
          QA("Doc/Rook - SMG (5)", "MP5"),
          QA("Doc/Rokk - SMG (90)", "P90"),
          QA("FBI SWAT - SMG", "UMP45"),
          QA("Frost - SMG", "9mm C1"),
          QA("Valkyrie - SMG", "MPX"),
          QA("Caveira - SMG", "M12"),
          QA("Echo - SMG", "MP5SD"),
          QA("Jackal - SMG", "PDW9"),
          QA("Lesion - SMG", "T-5 SMG"),
          QA("Vigil - SMG", "K1A"),
          QA("Alibi - SMG", "Mx4 Storm"),
          QA("SAS - Shotgun", "M590A1"),
          QA("Spetsnaz - Shotgun", "SASG-12"),
          QA("GSG9 - Shotgun", "M870"),
          QA("GIGN - Shotgun", "SG-CQB"),
          QA("FBI Swat - Shotgun", "M1014"),
          QA("Frost - Shotgun", "Super 90"),
          QA("Valkyrie - Shotgun", "SPAS-12"),
          QA("Caveira - Shotgun", "SPAS-15"),
          QA("Hibana/Echo - Shotgun", "Supernova"),
          QA("Ela - Shotgun", "FO-12"),
          QA("Maestro/Alibi - Shotgun", "ACS12"),
          QA("GIGN - DMR", "417"),
          QA("Buck - DMR", "CAMRS"),
          QA("Blackbeard - DMR", "SR-25"),
          QA("Dokkaebi - DMR", "MK14 EBR"),
          QA("Kali - DMR", "CSRX 300"),
          QA("SAS - Machine Pistol", "SMG-11"),
          QA("Hibana/Echo - Machine Pistol", "Bearing 9"),
          QA("Vigil - Machine Pistol (12)", "SMG-12"),
          QA("Vigil - Machine Pistol (75)", "C75 Auto"),
          QA("Sledge - Ability", "Breaching Hammer"),
          QA("Thatcher - Ability", "EMP Grenade"),
          QA("Mute - Ability", "Signal Disruptor"),
          QA("Smoke - Ability", "Remote Gas Grenade"),
          QA("Glaz - Ability", "Flip Sight"),
          QA("Fuze - Ability", "Cluster Charge"),
          QA("Tachanka - Ability", "Mounted LMG"),
          QA("Kapkan - Ability", "Entry Denial Device"),
          QA("Blitz - Ability", "Flash Shield"),
          QA("IQ - Ability", "Electronics Detector"),
          QA("Jager - Ability", "Active Defense System"),
          QA("Bandit - Ability", "Shock Wire"),
          QA("Montagne - Ability", "Extendable Shield"),
          QA("Twitch - Ability", "Shock Drone"),
          QA("Doc - Ability", "Stim Pistol"),
          QA("Rook - Ability", "Armor Pack"),
          QA("Ash - Ability", "Breaching Round"),
          QA("Thermite - Ability", "Exothermic Charge"),
          QA("Pulse - Ability", "Cardiac Sensor"),
          QA("Castle - Ability", "Armored Panel"),
          QA("Buck - Ability", "Skeleton Key"),
          QA("Frost - Ability", "Welcome Mat"),
          QA("Blackbeard - Ability", "Rifle Shield"),
          QA("Capitao - Ability", "Crossbow"),
          QA("Caveira - Ability", "Silent Step"),
          QA("Hibana - Ability", "X-Kairos"),
          QA("Echo - Ability", "Yokai"),
          QA("Mira - Ability", "Black Mirror"),
          QA("Ying - Ability", "Candela"),
          QA("Lesion - Ability", "Gu Mine"),
          QA("Zofia - Ability", "KS79 Lifeline"),
          QA("Ela - Ability", "Grzmot Mine"),
          QA("Dokkaebi - Ability", "Logic Bomb"),
          QA("Vigil - Ability", "ERC-7"),
          QA("Lion - Ability", "EE-ONE-D"),
          QA("Finka - Ability", "Adrenal Surge"),
          QA("Maestro - Ability", "Evil Eye"),
          QA("Maverick - Ability", "Breaching Torch"),
          QA("Clash - Ability", "CCE Shield"),
          QA("Nomad - Ability", "Airjab"),
          QA("Kaid - Ability", "Electroclaw"),
          QA("Gridlock - Ability", "Trax Stingers"),
          QA("Mozzie - Ability", "Pest Launcher")]

corrCount = 0
random.shuffle(qaList)
for qaItem in qaList:
    print(qaItem.question)
    print("Your answer: ")
    userAnsw = input()
    if userAnsw.lower() == qaItem.corrAnsw.lower():
        print("Your answer was correct.")
        corrCount += 1
    else:
        print("Your answer was wrong")
        print("Correct answer was: " + qaItem.corrAnsw)
    print("")

print("You answered " + str(corrCount) + " of " + str(len(qaList)) + " questions correctly.")
time.sleep(5)
