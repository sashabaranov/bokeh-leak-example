from flask import Flask, render_template, jsonify
from data import bins

from bokeh.plotting import figure
from bokeh.embed import components


app = Flask(__name__, template_folder=".")


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/bokeh")
def histos_for_path():
    scripts, divs = "", ""

    for _ in range(10):
        plot = figure(
            tools="pan,wheel_zoom,box_zoom,reset",
            active_scroll="wheel_zoom",
            toolbar_location="right"
        )

        plot.quad(
           top=[b.top for b in bins],
           bottom=[b.bottom for b in bins],
           left=[b.left for b in bins],
           right=[b.right for b in bins],
           color=[b.color for b in bins],
        )
        script, div = components(plot, wrap_script=False)
        scripts += script
        divs += div
    print(scripts)
    return jsonify({
        "html": divs,
        "script": scripts,
    })


if __name__ == "__main__":
    app.run(debug=True)
