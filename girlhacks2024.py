genre = ['pop', 'rock', 'hip-hop', 'rap', 'r&b', 'metal', 'salsa', 'lo-fi', 'reggaeton']
userInput = input("Whats your jam from the above list 😏? ")
print(userInput)
pop = ['Levitating by Dua Lipa feat. DaBaby','Dont Start Now” by Dua Lipa','Blinding Lights” by The Weeknd', 'Stayin Alive” by Bee Gees', 'Cant Stop the Feeling! by Justin Timberlake','Dancing Queen by ABBA','Shut Up and Dance by WALK THE MOON', 'I Feel Love” by Donna Summer',]
rock = ['Another One Bites the Dust” by Queen','You Shook Me All Night Long” by AC/DC','Miss You by The Rolling Stones', 'Lets Dance by David Bowie','Crazy Little Thing Called Love” by Queen', 'I Was Made for Lovin You” by KISS', 'Sweet Child O Mine by Guns N Roses' ]
hip_hop = ['Uptown Funk” by Mark Ronson (feat. Bruno Mars)','Cant Hold Us by Macklemore & Ryan Lewis (feat. Ray Dalton)', 'Yeah! by Usher (feat. Lil Jon & Ludacris)', 'Old Town Road (Remix) by Lil Nas X (feat. Billy Ray Cyrus)' 'Hey Ya! by OutKast', 'In Da Club” by 50 Cent','This Is How We Do It by Montell Jordan','Gold Digger by Kanye West (feat. Jamie Foxx)','Jump” by Kris Kross' ]
rap = ['Get Lucky by Daft Punk (feat. Pharrell Williams','Rappers Delight by The Sugarhill Gang','Low by Flo Rida (feat. T-Pain)','Good Life by Kanye West (feat. T-Pain)','Jump Around by House of Pain','Party Up (Up In Here) by DMX','Juicy by The Notorious B.I.G.','Not Like Us by Kendrick Lamar']
r_b = ['Good Times by Chic','Can You Feel It by The Jacksons','Dont Stop Til You Get Enough by Michael Jackson','Candy Rain by Soul for Real','Youre the One by SWV','Dance, Dance, Dance (Yowsah, Yowsah, Yowsah) by Chic','Aint Nobody” by Chaka Khan','Le Freak by Chic']
metal = ['Walk” by Pantera','Crazy Train by Ozzy Osbourne','The Number of the Beast by Iron Maiden','Living After Midnight by Judas Priest', 'Paranoid by Black Sabbath','Symphony of Destruction by Megadeth', 'Holy Wars...The Punishment Due by Megadeth','I Want It All by Queen', 'Bodies by Drowning Pool']
salsa = ['La Rebelión by Joe Arroyo','Bailando” by Enrique Iglesias (feat. Sean Paul & Descemer Bueno)','Vivir Mi Vida” by Marc Anthony','Aquel Lugar by El Gran Combo de Puerto Rico','Idilio by Willie Colón','Che Che Colé by Willie Colón','Oye Como Va by Tito Puente','Me Gusta La Salsa” by La Sonora Ponceña','El Cantante by Héctor Lavoe','Te Quiero by Gilberto Santa Rosa']
lofi = ['Night Owl by DâM-FunK', 'I Wanna Be Your Girl by Jungle', 'Dancing in the Moonlight by Toploader', 'Aint Nobody Chakan Khan', '"Undercover by ALOK & Vintage Culture', 'Get You by Daniel Caesar', 'Take It Easy by Mndsgn', 'Love Is the Message by MFSB', 'Dont Start Now by Dua Lipa', 'You & I Kaytranada', 'Electric Feel by MGMT']
reggaeton = ['Despacito” by Luis Fonsi (feat. Daddy Yankee)','Taki Taki by DJ Snake (feat. Selena Gomez, Ozuna & Cardi B) ','Mi Gente by J Balvin & Willy William','Baila Baila Baila by Rosalía','Criminal by Natti Natasha & Ozuna','Reggaetón Lento (Bailemos) by CNCO & Little Mix','Calma (Remix) by Pedro Capó & Farruko','']
if userInput in genre:
    if userInput == 'pop':
        print(pop[:])
        print()
        userPreference = input("Rate this suggestion on a scale of 1 to 5, 5 being amazing and 1 being awful." )
        print()
        if int(userPreference) < 3:
            print("If this didnt satisfy you, add songs to the list that you recommend")
            userInput2 = input("Add your songs: ")
            pop.append(userInput2)
            print(pop[:])
            print()
            print("Thank you for adding your suggestions")
        else:
            print("You're welcome for the recommendation")
    if userInput == 'rock':
        print(rock[:])
        print()
        userPreference = input("Rate this suggestion on a scale of 1 to 5, 5 being amazing and 1 being awful." )
        print()
        if int(userPreference) < 3:
            print("If this didnt satisfy you, add songs to the list that you recommend")
            userInput2 = input("Add your songs: ")
            rock.append(userInput2)
            print(rock[:])
            print()
            print("Thank you for adding your suggestions")
        else:
            print("You're welcome for the recommendation")
    if userInput == 'hip-hop':
        print(hip_hop[:])
        print()
        userPreference = input("Rate this suggestion on a scale of 1 to 5, 5 being amazing and 1 being awful." )
        print()
        if int(userPreference) < 3:
            print("If this didn't satisfy you, add songs to the list that you recommend")
            userInput2 = input("Add your songs: ")
            hip_hop.append(userInput2)
            print(hip_hop[:])
            print()
            print("Thank you for adding your suggestions")
        else:
            print("You're welcome for the recommendation")
    if userInput == 'rap':
        print(rap[:])
        print()
        userPreference = input("Rate this suggestion on a scale of 1 to 5, 5 being amazing and 1 being awful." )
        print()
        if int(userPreference) < 3:
            print("If this didn't satisfy you, add songs to the list that you recommend")
            userInput2 = input("Add your songs: ")
            rap.append(userInput2)
            print(rap[:])
            print()
            print("Thank you for adding your suggestions")
        else:
            print("You're welcome for the recommendation")
    if userInput == 'r&b':
        print(r_b[:])
        print()
        userPreference = input("Rate this suggestion on a scale of 1 to 5, 5 being amazing and 1 being awful." )
        print()
        if int(userPreference) < 3:
            print("If this didnt satisfy you, add songs to the list that you recommend")
            userInput2 = input("Add your songs: ")
            r_b.append(userInput2)
            print(r_b[:])
            print()
            print("Thank you for adding your suggestions")
        else:
            print("You're welcome for the recommendation")
    if userInput == 'metal':
        print(metal[:])
        print()
        userPreference = input("Rate this suggestion on a scale of 1 to 5, 5 being amazing and 1 being awful." )
        print()
        if int(userPreference) < 3:
            print("If this didnt satisfy you, add songs to the list that you recommend")
            userInput2 = input("Add your songs: ")
            metal.append(userInput2)
            print(metal[:])
            print()
            print("Thank you for adding your suggestions")
        else:
            print("You're welcome for the recommendation")
    if userInput == 'salsa':
        print(salsa[:])
        print()
        userPreference = input("Rate this suggestion on a scale of 1 to 5, 5 being amazing and 1 being awful." )
        print()
        if int(userPreference) < 3:
            print("If this didnt satisfy you, add songs to the list that you recommend")
            userInput2 = input("Add your songs: ")
            salsa.append(userInput2)
            print(salsa[:])
            print()
            print("Thank you for adding your suggestions")
        else:
            print("You're welcome for the recommendation")
    if userInput == 'lo-fi':
        print(lofi[:])
        print()
        userPreference = input("Rate this suggestion on a scale of 1 to 5, 5 being amazing and 1 being awful." )
        print()
        if int(userPreference) < 3:
            print("If this didnt satisfy you, add songs to the list that you recommend")
            userInput2 = input("Add your songs: ")
            lofi.append(userInput2)
            print(lofi[:])
            print()
            print("Thank you for adding your suggestions")
        else:
            print("You're welcome for the recommendation")
    if userInput == 'reggaeton':
        print(reggaeton[:])
        print()
        userPreference = input("Rate this suggestion on a scale of 1 to 5, 5 being amazing and 1 being awful." )
        print()
        if int(userPreference) < 3:
            print("If this didnt satisfy you, add songs to the list that you recommend")
            userInput2 = input("Add your songs: ")
            reggaeton.append(userInput2)
            print(reggaeton[:])
            print()
            print("Thank you for adding your suggestions")
        else:
            print("You're welcome for the recommendation")
else:
    print("Sorry couldn't get that")
    userInput = input("Whats your jam from the above list 😏? ")
    print(userInput)