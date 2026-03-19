import matplotlib.pyplot as plt
import pandas as pd

class HFSSPlotter:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = None

        self.col_h = "h [mm]"
        self.col_w = "w [mm]"
        self.col_freq = "Freq [GHz]"
        self.col_s11 = "dB(S(1,1)) []"
        self.col_s21 = "dB(S(2,1)) []"

    def load_data(self):
        self.data = pd.read_csv(self.csv_file)

    def check_columns(self):
        required_columns = [
            self.col_h,
            self.col_w,
            self.col_freq,
            self.col_s11,
            self.col_s21,
        ]

        missing = [col for col in required_columns if col not in self.data.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")

    def plot_for_each_w(self):
        unique_w_values = sorted(self.data[self.col_w].unique())

        for w_value in unique_w_values:
            df_w = self.data[self.data[self.col_w] == w_value].copy()

            fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

            for h_value in sorted(df_w[self.col_h].unique()):
                df_wh = df_w[df_w[self.col_h] == h_value].copy()
                df_wh = df_wh.sort_values(by=self.col_freq)

                axes[0].plot(
                    df_wh[self.col_freq],
                    df_wh[self.col_s11],
                    label=f"h = {h_value} mm"
                )

                axes[1].plot(
                    df_wh[self.col_freq],
                    df_wh[self.col_s21],
                    label=f"h = {h_value} mm"
                )

            axes[0].set_ylabel("dB(S11)")
            axes[0].set_title(f"S-parameters for w = {w_value} mm")
            axes[0].grid(True)
            axes[0].legend()

            axes[1].set_xlabel("Frequency [GHz]")
            axes[1].set_ylabel("dB(S21)")
            axes[1].grid(True)
            axes[1].legend()

            plt.tight_layout()
            plt.show()

    def run(self):
        self.load_data()
        self.check_columns()
        self.plot_for_each_w()


if __name__ == "__main__":
    csv_file = "Project2_S_Parameter_Plots.csv"
    plotter = HFSSPlotter(csv_file)
    plotter.run()