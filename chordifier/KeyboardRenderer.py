import numpy as np
from bokeh.io import output_notebook
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.util.hex import axial_to_cartesian

from chordifier.Models import Keyboard

output_notebook()

PALETTE = [
    '#c66900',
    '#c79100',
    '#5a9216',
    '#087f23',
    '#00675b',
    '#008ba3',
    '#0069c0',
    '#002984',
    '#320b86',
    '#6a0080',
]


class KeyboardRenderer:
    def __init__(self, keyboard: Keyboard, title=None):
        keys = aggregate_keys(keyboard.zones)
        self.qs = keys[:, 0]
        self.rs = keys[:, 1]
        self.colors = match_colors(keyboard.zones)
        self.indices = extract_indices(keyboard.zones)
        self.positions = extract_positions(keyboard.zones)

        self.plot = make_plot(title)
        self.draw()

    def present(self):
        show(self.plot)

    def draw(self):
        self.plot.hex_tile(self.qs, self.rs,
                           fill_color=self.colors, alpha=0.5,
                           line_color="white",
                           orientation="flattop")

        x, y = axial_to_cartesian(self.qs, self.rs, 1, "flattop")

        self.plot.text(x, y, text=self.indices,
                       text_baseline="middle", text_align="center")


def aggregate_keys(zones):
    return np.concatenate([zone.keys for zone in zones])


def match_colors(zones):
    zones_with_colors = zip(zones, PALETTE)
    colors = [len(zone.keys) * [color] for zone, color in zones_with_colors]
    return np.concatenate(colors)


def extract_indices(zones):
    return [index + 1 for zone in zones for index in range(len(zone.keys))]


def extract_positions(zones):
    return [key for zone in zones for key in zone.keys]


def make_plot(title):
    plot = figure(title=title, tools="pan,wheel_zoom,reset",
                  height=600, sizing_mode='stretch_width', match_aspect=True)
    plot.grid.visible = False

    return plot
