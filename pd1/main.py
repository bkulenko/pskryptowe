import turtle as t
import tkinter as tk
from tkinter import ttk

from anims import anims

animation_mapping = {
    "Koch snowflake": anims.koch,
    "Sierpiński triangle": anims.striangle,
    "Sierpiński carpet": anims.scarpet,
    "Peano curve": anims.peano,
    "Dragon curve": anims.dragon,
    "Binary tree": anims.btree,
    "Pythagoras tree": anims.ptree_base,
    "Modified Pythagoras tree": anims.ptree_mod,
    "Modified Pythagoras tree - no trunk": anims.ptree_notrunk,
    "Modified Pythagoras tree - no trunk, random tilt": anims.ptree_tilt
}


class FractalApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("asdf")
        main_frame = ttk.Frame(root, padding=10)
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(main_frame, text="Fractal type").grid(
            row=0, column=0, sticky=tk.W, pady=2)
        self.fractalv = tk.StringVar()
        self.fractal_combo = ttk.Combobox(
            main_frame, textvariable=self.fractalv, width=25)
        self.fractal_combo["values"] = tuple(animation_mapping.keys())
        self.fractal_combo.grid(
            row=1, column=0, sticky=(tk.W, tk.E), pady=2, padx=2)

        ttk.Label(main_frame, text="Depth").grid(
            row=0, column=1, sticky=tk.W, pady=2, padx=2)
        self.depthv = tk.StringVar()
        self.depth_combo = ttk.Combobox(
            main_frame, textvariable=self.depthv, width=25)
        self.depth_combo["values"] = tuple((str(i) for i in range(1, 5)))
        self.depth_combo.grid(
            row=1, column=1, sticky=(tk.W, tk.E), pady=2, padx=2)

        self.draw_btn = ttk.Button(
            main_frame, text="Draw", command=self.draw_fractal)
        self.draw_btn.grid(row=2, column=0, columnspan=2, pady=10)

        self.canvas = tk.Canvas(main_frame, width=500, height=500, bg="white")
        self.canvas.grid(row=3, column=0, columnspan=2, pady=10)

        self.turtle = t.RawTurtle(self.canvas)  # , visible=False)
        self.turtle.screen.colormode(255)

        main_frame.columnconfigure(1, weight=1, uniform="combo_cols")
        main_frame.columnconfigure(0, weight=1, uniform="combo_cols")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.drawing = False

    def draw_fractal(self):
        self.drawing = True
        self.turtle.reset()
        self.turtle.speed(250)
        animfunc = animation_mapping.get(self.fractalv.get(), None)
        depth = int(self.depthv.get())
        try:
            animfunc(self.turtle, depth)
        except TypeError:
            pass
        self.drawing = False


if __name__ == "__main__":
    root = tk.Tk()
    app = FractalApp(root)
    root.mainloop()
