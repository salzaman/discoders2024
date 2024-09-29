from django.shortcuts import render
from .forms import RecommendationForm
# Create your views here.
pop = {'Levitating by Dua Lipa feat. DaBaby','Dont Start Now” by Dua Lipa','Blinding Lights” by The Weeknd', 
       'Stayin Alive” by Bee Gees', 'Cant Stop the Feeling! by Justin Timberlake','Dancing Queen by ABBA',
       'Shut Up and Dance by WALK THE MOON', 'I Feel Love” by Donna Summer',}
rock = {'Another One Bites the Dust” by Queen','You Shook Me All Night Long” by AC/DC','Miss You by The Rolling Stones', 
        'Lets Dance by David Bowie','Crazy Little Thing Called Love” by Queen', 'I Was Made for Lovin You” by KISS', 
        'Sweet Child O Mine by Guns N Roses' }
hip_hop = {'Uptown Funk” by Mark Ronson (feat. Bruno Mars)','Cant Hold Us by Macklemore & Ryan Lewis (feat. Ray Dalton)', 
           'Yeah! by Usher (feat. Lil Jon & Ludacris)', 'Old Town Road (Remix) by Lil Nas X (feat. Billy Ray Cyrus)' 
           'Hey Ya! by OutKast', 'In Da Club” by 50 Cent','This Is How We Do It by Montell Jordan',
           'Gold Digger by Kanye West (feat. Jamie Foxx)','Jump” by Kris Kross' }
rap = {'Get Lucky by Daft Punk (feat. Pharrell Williams','Rappers Delight by The Sugarhill Gang','Low by Flo Rida (feat. T-Pain)',
       'Good Life by Kanye West (feat. T-Pain)','Jump Around by House of Pain','Party Up (Up In Here) by DMX',
       'Juicy by The Notorious B.I.G.','Not Like Us by Kendrick Lamar'}
r_b = {'Good Times by Chic','Can You Feel It by The Jacksons','Dont Stop Til You Get Enough by Michael Jackson',
       'Candy Rain by Soul for Real','Youre the One by SWV','Dance, Dance, Dance (Yowsah, Yowsah, Yowsah) by Chic',
       'Aint Nobody” by Chaka Khan','Le Freak by Chic'}
metal = {'Walk” by Pantera','Crazy Train by Ozzy Osbourne','The Number of the Beast by Iron Maiden',
         'Living After Midnight by Judas Priest', 'Paranoid by Black Sabbath','Symphony of Destruction by Megadeth', 
         'Holy Wars...The Punishment Due by Megadeth','I Want It All by Queen', 'Bodies by Drowning Pool'}
salsa = {'La Rebelión by Joe Arroyo','Bailando” by Enrique Iglesias (feat. Sean Paul & Descemer Bueno)',
         'Vivir Mi Vida” by Marc Anthony','Aquel Lugar by El Gran Combo de Puerto Rico','Idilio by Willie Colón',
         'Che Che Colé by Willie Colón','Oye Como Va by Tito Puente','Me Gusta La Salsa” by La Sonora Ponceña',
         'El Cantante by Héctor Lavoe','Te Quiero by Gilberto Santa Rosa'}
lofi = {'Night Owl by DâM-FunK', 'I Wanna Be Your Girl by Jungle', 'Dancing in the Moonlight by Toploader', 
        'Aint Nobody Chakan Khan', '"Undercover by ALOK & Vintage Culture', 'Get You by Daniel Caesar', 
        'Take It Easy by Mndsgn', 'Love Is the Message by MFSB', 'Dont Start Now by Dua Lipa', 'You & I Kaytranada', 
        'Electric Feel by MGMT'}
reggaeton = {'Despacito” by Luis Fonsi (feat. Daddy Yankee)','Taki Taki by DJ Snake (feat. Selena Gomez, Ozuna & Cardi B) ',
             'Mi Gente by J Balvin & Willy William','Baila Baila Baila by Rosalía','Criminal by Natti Natasha & Ozuna',
             'Reggaetón Lento (Bailemos) by CNCO & Little Mix','Calma (Remix) by Pedro Capó & Farruko'}

def get_music_recommendations(user_input):
    if user_input == 'pop':
        return pop
    elif user_input == 'rock':
        return rock
    elif user_input == 'hip-hop':
        return hip_hop
    elif user_input == 'rap':
        return rap
    elif user_input == 'r&b':
        return r_b
    elif user_input == 'metal':
        return metal
    elif user_input == 'salsa':
        return salsa
    elif user_input == 'lofi':
        return lofi
    elif user_input == 'reggaeton':
        return reggaeton
    
    if user_input.method == 'POST':
        form = RecommendationForm(user_input.POST)
    else:
        form = RecommendationForm()

    return render(user_input, 'recommendations.html', {'form': form})