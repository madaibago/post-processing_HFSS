import math
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


class GeometryCase:
    """Represents one (w, h) geometry configuration."""

    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h

    @property
    def top_width(self) -> float:
        return self.w

    @property
    def top_height(self) -> float:
        return self.w / 10

    @property
    def bottom_width(self) -> float:
        return self.w * 10

    @property
    def bottom_height(self) -> float:
        return self.h

    def draw(self, ax):
        """Draw the stacked rectangles on the given axis."""
        # Bottom rectangle: centered at x = 0, base at y = 0
        bottom_x = -self.bottom_width / 2
        bottom_y = 0

        # Top rectangle: centered at x = 0, exactly on top of bottom rectangle
        top_x = -self.top_width / 2
        top_y = self.bottom_height

        bottom_rect = Rectangle(
            (bottom_x, bottom_y),
            self.bottom_width,
            self.bottom_height,
            facecolor="lightblue",
            edgecolor="black",
            label="Bottom rectangle"
        )

        top_rect = Rectangle(
            (top_x, top_y),
            self.top_width,
            self.top_height,
            facecolor="salmon",
            edgecolor="black",
            label="Top rectangle"
        )

        ax.add_patch(bottom_rect)
        ax.add_patch(top_rect)

        total_height = self.bottom_height + self.top_height
        max_width = max(self.bottom_width, self.top_width)

        ax.set_xlim(-max_width / 2 - 0.1 * self.w, max_width / 2 + 0.1 * self.w)
        ax.set_ylim(0, total_height + 0.1 * total_height)

        ax.set_aspect("equal")
        ax.set_title(f"h = {self.h}")
        ax.set_xlabel("x (mm)")
        ax.set_ylabel("z (mm)")
        ax.grid(True, linestyle="--", alpha=0.5)


class GeometryPlotter:
    """Loads data and creates grouped figures by unique w."""

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.df = None

    def load_data(self):
        """Read the CSV and keep only unique (w, h) pairs."""
        df = pd.read_csv(self.csv_path)

        # Keep only required columns
        df = df[["w [mm]", "h [mm]"]].dropna()

        # Remove duplicate (w, h) pairs
        df = df.drop_duplicates().sort_values(["w [mm]", "h [mm]"]).reset_index(drop=True)

        self.df = df

    def plot_grouped_by_w(self):
        """Create one figure per unique w value."""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        unique_w_values = sorted(self.df["w [mm]"].unique())

        for w_value in unique_w_values:
            group = self.df[self.df["w [mm]"] == w_value].sort_values("h [mm]")
            n = len(group)

            ncols = min(4, n)
            nrows = math.ceil(n / ncols)

            fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(5 * ncols, 4 * nrows))

            # Make axes always iterable
            if n == 1:
                axes = [axes]
            else:
                axes = axes.flatten()

            fig.suptitle(f"Geometries for w = {w_value} mm", fontsize=14)

            for ax, (_, row) in zip(axes, group.iterrows()):
                case = GeometryCase(w=row["w [mm]"], h=row["h [mm]"])
                case.draw(ax)

            # Hide unused axes
            for ax in axes[len(group):]:
                ax.axis("off")

            plt.tight_layout(rect=[0, 0, 1, 0.95])
            plt.show()


if __name__ == "__main__":
    plotter = GeometryPlotter("Project2_S_Parameter_Plots.csv")
    plotter.load_data()
    plotter.plot_grouped_by_w()