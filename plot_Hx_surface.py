import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

class HxMapPlotter:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        """
        Load numeric data from the file.
        Assumes:
          - line 1: metadata
          - line 2: column names
          - line 3 onward: numeric data
        """
        return np.loadtxt(self.filename, skiprows=2)

    def build_grid(self, data):
        y = data[:, 1]
        z = data[:, 2]
        hx_real = data[:, 3]

        y_unique = np.unique(y)
        z_unique = np.unique(z)

        grid = np.full((len(z_unique), len(y_unique)), np.nan)

        y_index = {val: i for i, val in enumerate(y_unique)}
        z_index = {val: i for i, val in enumerate(z_unique)}

        for yi, zi, hi in zip(y, z, hx_real):
            grid[z_index[zi], y_index[yi]] = hi*4*np.pi/1000

        return y_unique, z_unique, grid

    def plot(self):
        """
        Plot the real part of Hx as a 2D color map.
        """
        data = self.load_data()
        y_unique, z_unique, grid = self.build_grid(data)
        vmax = np.nanmax(np.abs(grid))
        norm = colors.TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)
        
        plt.figure(figsize=(8, 6))
        plt.pcolormesh(y_unique*1e3, z_unique*1e3, grid, shading="auto",cmap="RdBu",norm=norm)
        plt.colorbar(label="Re(Hx)")
        plt.xlabel("Y [mm]")
        plt.ylabel("Z [mm]")
        plt.title('Real part of $H_x$ (Oe)')
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    plotter = HxMapPlotter("h_x_data2.txt")
    plotter.plot()