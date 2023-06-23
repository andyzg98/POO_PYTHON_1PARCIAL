import tkinter as tk

class RobotArmView:
    def __init__(self, controller):
        self.controller = controller

    def validate_input(self, value, min_value, max_value):
        try:
            value = int(value)
            if value < min_value or value > max_value:
                return False
            return True
        except ValueError:
            return False

    def get_user_input(self):
        elevation = int(self.elevation_entry.get())
        rotation = int(self.rotation_entry.get())
        length = int(self.length_entry.get())
        return elevation, rotation, length

    def move_arm(self):
        elevation, rotation, length = self.get_user_input()
        self.controller.move_elevation(elevation)
        self.controller.move_rotation(rotation)
        self.controller.move_length(length)
        self.text_box.insert(tk.END, f"Moviendo a: Elevación={elevation}, Giro={rotation}, Longitud={length}\n")
        self.clear_input()

    def stop_arm(self):
        self.controller.stop()
        self.text_box.insert(tk.END, "Brazo detenido\n")

    def clear_input(self):
        self.elevation_entry.delete(0, tk.END)
        self.rotation_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)

    def run(self):
        self.window = tk.Tk()
        self.window.title("Brazo Robótico")

        self.elevation_label = tk.Label(self.window, text="Elevación:")
        self.elevation_label.pack()
        vcmd_elevation = (self.window.register(lambda value: self.validate_input(value, 0, 100)), "%P")
        self.elevation_entry = tk.Entry(self.window, validate="key", validatecommand=vcmd_elevation)
        self.elevation_entry.pack()

        self.rotation_label = tk.Label(self.window, text="Giro:")
        self.rotation_label.pack()
        vcmd_rotation = (self.window.register(lambda value: self.validate_input(value, 0, 360)), "%P")
        self.rotation_entry = tk.Entry(self.window, validate="key", validatecommand=vcmd_rotation)
        self.rotation_entry.pack()

        self.length_label = tk.Label(self.window, text="Longitud:")
        self.length_label.pack()
        vcmd_length = (self.window.register(lambda value: self.validate_input(value, 0, 100)), "%P")
        self.length_entry = tk.Entry(self.window, validate="key", validatecommand=vcmd_length)
        self.length_entry.pack()

        self.move_button = tk.Button(self.window, text="Mover brazo", command=self.move_arm)
        self.move_button.pack()

        self.stop_button = tk.Button(self.window, text="Detener brazo", command=self.stop_arm)
        self.stop_button.pack()

        self.text_box = tk.Text(self.window)
        self.text_box.pack()

        self.window.mainloop()

