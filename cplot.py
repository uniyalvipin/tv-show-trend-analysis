import pandas as pd
from matplotlib.figure import Figure


def create_figure1(query):
    csvfile="data/"+query+".csv"
    df = pd.read_csv(csvfile)

    df = pd.DataFrame(df, columns=['polarity'])
    df = df.sort_values(by='polarity', ascending=True)

    neg = pos = neu = 0

    for polarity in df.polarity:
        # eliminate any non-numeric value
        try:
            pol = float(polarity)
        except:
            pol = 0

        # Count Values
        if pol < 0:
            neg = neg + 1

        elif pol > 0:
            pos = pos + 1

        else:
            neu = neu + 1

    fig = Figure()
    ax = fig.add_subplot(1.5, 1.5, 1)

    ax.set_title(query.upper(), pad=25)
    explode = (0.1, 0.05, 0.05)
    xs = 'Positive', 'Neutral', 'Negative'
    ys = [pos, neu, neg]

    ax.pie(ys,explode=explode, shadow=True, colors=['green', 'blue', 'brown'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    ax.legend(['Positive Tweets', 'Neutral Tweets', 'Negetive Tweets'], bbox_to_anchor=(0.78,0), loc='lower left')

    return fig
