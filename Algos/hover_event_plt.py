import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def update_annot(ind):
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    attributes_to_show = [0, 1, 2, 7]
    text = df.iloc[ind["ind"][0], attributes_to_show].to_string()
    annot.set_text(text)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()


df = pd.read_csv('https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv')
fig, ax = plt.subplots()
fig.set_size_inches(17, 10)
sc = ax.scatter(df.index, df['SALARY'], s=100)
ax.set_ylabel('Salary')
annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="lightgrey"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)
fig.canvas.mpl_connect("motion_notify_event", hover)
plt.show()