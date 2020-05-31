import datetime
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

# Periodo 27/03 - 31/05
start = datetime.datetime.strptime("27-03", "%d-%m")
end = datetime.datetime.strptime("31-05", "%d-%m")
date_range = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

x_axis = list(range(1, len(date_range)+1))

# Associa cada data à um número
mapDateTime = {}
counter = 1
for date in date_range:
    mapDateTime[date] = counter
    counter += 1


# Formato dos dados: ('Nome da Série', [ ('dataBarra', duracao)], 'Texto inicial', 'Texto final')
tuplas = [
    ('Space Force', [
        ("30-05", 1)
    ], '', 'S01E01-S01E05'),
    ('The Crown', [
        ("26-05", 1)
    ], '', 'S01E01'),
    ('Defending Jacob', [
        ("23-05", 2), ("29-05", 1)
    ], 'S01E01', 'S01E08'),
    ('Westworld', [
        ("17-05", 1), ("21-05", 1), ("23-05", 1), ("25-05", 1), ("27-05", 2)
    ], 'S01E01', 'S01E08'),
    ('Fleabag', [
        ("14-05", 6)
    ], 'S01E01', 'S02E06'),
    ('Rick and Morty', [
        ("05-05", 1), ("13-05", 1), ("21-05", 1), ("25-05", 1)
    ], 'S04E06', 'S04E09'),
    ('The Man in the High Castle', [
        ("27-04", 2), ("30-04", 16)
    ], 'S01E01', 'S04E10'),
    ('The Good Place', [
        ("25-04", 6)
    ], 'S01E01', 'S04E13'),
    ('FBI: Most Wanted', [
        ("23-04", 1),("25-04", 1),("30-04", 2),("11-05", 1)
    ], 'S01E10', 'S01E14'),
    ('Brooklyn Nine-Nine', [
        ("28-03", 28)
    ], 'S01E01', 'S07E13'),
    ('Doctor Who', [
        ("27-03", 1),("29-03", 1),("31-03", 1),("08-04", 1),
        ("20-04", 1),("25-04", 1),("07-05", 1),("15-05", 6)
    ], 'S11E01', 'S12E10')
]

barsShows = {}

# Inicia as listas de barras de cada show
for i in range(len(tuplas)):
    barsShows[i] = []

# Cria uma barra de comprimento duration a partir do dia dayString
def createBar(show, dayString, duration):
    day = datetime.datetime.strptime(dayString, "%d-%m")
    mapped = mapDateTime[day] # busca a posição em x da data
    barsShows[show].append((mapped, duration))

ylabels = []
for i, v in enumerate(tuplas):
    ylabels.append(v[0]) # Nome da série
    for periodo in v[1]:
        createBar(i, periodo[0], periodo[1]) # Cria a barra com data de inicio e duração

cmap = plt.cm.get_cmap('plasma_r')
colors = [cmap(i/(len(tuplas)+1)) for i in range(len(tuplas))]

# Configuração da figura
fig, gnt = plt.subplots()

plt.title("Séries assistidas durante a quarentena (27/03 - 30/05)")
gnt.grid(False)

gnt.set_ylim(-1, len(tuplas))
gnt.set_xlim(0, len(date_range)+1)

gnt.set_xlabel('Dia')
gnt.set_ylabel('Série')

gnt.set_xticks(x_axis)
ticks_y = list(range(len(ylabels)))
gnt.set_yticks(ticks_y)
gnt.set_yticklabels(ylabels)

desloc_y = 0.2
desloc_x_final = -2
tam_fonte = 8

for show in barsShows:
    posInicial = barsShows[show][0][0] # posicao x da primeira barra
    posFinal = barsShows[show][-1][0] + barsShows[show][-1][1] # posicao x da ultima barra + comprimento

    textoInicial = tuplas[show][2]
    textoFinal = tuplas[show][3]

    if barsShows[show]:
        for el in barsShows[show]:
            gnt.barh(show, left=el[0], width=el[1], height=0.3, color=colors[show]) 

        gnt.text(posInicial, show + desloc_y, textoInicial, fontSize=tam_fonte)
        gnt.text(posFinal + desloc_x_final, show + desloc_y, textoFinal, fontSize=tam_fonte)

plt.show()