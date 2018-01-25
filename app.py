from flask import Flask, render_template, jsonify
from data import bins

from bokeh.plotting import figure
from bokeh.embed import components


app = Flask(__name__, template_folder=".")

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/bokeh")
def bokeh():
    x_range = ['a', 'b', 'c', 'd']
    y_values = [1., 2., 3., 4.]
    y_errors = [.1, .2, .3, .4]


    plot = figure(x_range=x_range)
    plot.square(x_range, y_values, size=7, line_alpha=0)

    err_xs = []
    err_ys = []

    for x, y, yerr in zip(x_range, y_values, y_errors):
        err_xs.append((x, x))
        err_ys.append((y - yerr, y + yerr))

    # Option A: Does not work
    # plot.multi_line(err_xs, err_ys)

    # Option B: works!
    for i in xrange(len(err_xs)):
        plot.line(err_xs[i], err_ys[i])

    scripts, divs = components(plot, wrap_script=False)

    return jsonify({
        "html": divs,
        "script": scripts,
    })


if __name__ == "__main__":
    app.run(debug=True)
