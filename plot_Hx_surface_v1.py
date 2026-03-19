import numpy as np
import matplotlib.pyplot as plt


class HxMapPlotter:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.y = None
        self.z = None
        self.hx_real_grid = None

    def load_data(self):
        """
        Load numeric data from the file.
        Assumes:
          - line 1: metadata
          - line 2: column names
          - line 3 onward: numeric data
        """
        self.data = np.loadtxt(self.filename, skiprows=2)

    def prepare_grid(self):
        """
        Extract X, Y, and real(Hx), then reshape into a 2D grid.
        """
        y_vals = self.data[:, 1]
        z_vals = self.data[:, 2]
        hx_real = self.data[:, 3]

        self.y = np.unique(y_vals)
        self.z = np.unique(z_vals)

        ny = len(self.y)
        nz = len(self.z)

        # Reshape assuming the file is ordered regularly on the grid
        self.hx_real_grid = hx_real.reshape(nz, ny)

    def plot(self):
        """
        Plot the real part of Hx as a 2D color map.
        """
        plt.figure(figsize=(8, 6))
        plt.pcolormesh(self.y*1e3, self.z*1e3, self.hx_real_grid, shading="auto")
        plt.colorbar(label="Re(Hx)")
        plt.xlabel("Y [mm]")
        plt.ylabel("Z [mm]")
        plt.title('Real part of complex data "Hx"')
        plt.tight_layout()
        plt.show()

    def run(self):
        self.load_data()
        self.prepare_grid()
        self.plot()


if __name__ == "__main__":
    plotter = HxMapPlotter("h_x_data2.txt")
    plotter.run()