from shiny import App, render, ui
import pandas as pd
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.input_file("file", "Upload a CSV file", accept=[".csv"]),
    ui.input_action_button("run", "Generate plot"),
    ui.output_plot("hist"),
)

def server(input, output, session):
    @output
    @render.plot
    def hist():
        if input.file() is None:
            return
        df = pd.read_csv(input.file()[0]["datapath"])
        numeric_cols = df.select_dtypes(include="number").columns
        if len(numeric_cols) == 0:
            return
        fig, ax = plt.subplots()
        df[numeric_cols[0]].hist(ax=ax)
        ax.set_title(f"Distribution of {numeric_cols[0]}")
        return fig

app = App(app_ui, server)
