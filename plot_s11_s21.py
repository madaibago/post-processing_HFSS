import matplotlib.pyplot as plt
import pandas as pd, numpy as np

class HFSSPlotter:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = None

        self.col_h = "h [mm]"
        self.col_w = "w [mm]"
        self.col_freq = "Freq [GHz]"
        self.col_MagZo = "mag(Zo(Port_In)) []"
        self.col_s11 = "dB(S(Port_In,Port_In)) []"
        self.col_s21 = "dB(S(Port_Out,Port_In)) []"

    def load_data(self):
        self.data = pd.read_csv(self.csv_file)

    def check_columns(self):
        required_columns = [
            self.col_h,
            self.col_w,
            self.col_freq,
            self.col_MagZo,
            self.col_s11,
            self.col_s21,
        ]

        missing = [col for col in required_columns if col not in self.data.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")

    def plot_for_each_w(self):
        unique_w_values = sorted(self.data[self.col_w].unique())
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
        for w_value in unique_w_values:
            df_w = self.data[self.data[self.col_w] == w_value].copy()

            fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True)

            for h_ix, h_value in enumerate(sorted(df_w[self.col_h].unique())):
                df_wh = df_w[df_w[self.col_h] == h_value].copy()
                df_wh = df_wh.sort_values(by=self.col_freq)
                if h_value < 0.2:
                    axes[0][0].plot(
                        df_wh[self.col_freq],
                        df_wh[self.col_s11],
                        label=f"h = {h_value} mm",
                        c=colors[h_ix]
                    )
    
                    axes[1][0].plot(
                        df_wh[self.col_freq],
                        df_wh[self.col_s21],
                        label=f"h = {h_value} mm",
                        c=colors[h_ix]
                    )
                else:
                    axes[0][1].plot(
                        df_wh[self.col_freq],
                        df_wh[self.col_s11],
                        label=f"h = {h_value} mm",
                        c=colors[h_ix]
                    )
    
                    axes[1][1].plot(
                        df_wh[self.col_freq],
                        df_wh[self.col_s21],
                        label=f"h = {h_value} mm",
                        c=colors[h_ix]
                    )
                axes[0, 1].sharey(axes[0, 0])
                axes[0][0].set_ylabel("dB(S11)")
                axes[0][0].set_title(f"S-parameters for w = {w_value} mm")
                axes[0][0].grid(True)
                axes[0][0].legend()
                # axes[0][1].set_ylabel("dB(S11)")
                # axes[0][1].set_title(f"S-parameters for w = {w_value} mm")
                axes[0][1].grid(True)
                axes[0][1].legend()

                axes[1, 0].sharey(axes[1, 1])
                axes[1][0].set_xlabel("Frequency [GHz]")
                axes[1][0].set_ylabel("dB(S21)")
                axes[1][0].grid(True)
                axes[1][0].legend()
                axes[1][1].set_xlabel("Frequency [GHz]")
                # axes[1][1].set_ylabel("dB(S21)")
                axes[1][1].grid(True)
                axes[1][1].legend()
                
            plt.tight_layout()
            plt.show()

    def run(self):
        self.load_data()
        print("Data extracted")
        self.check_columns()
        print("Columns checked")
        self.plot_for_each_w()


if __name__ == "__main__":
    csv_file = "simus.csv"
    plotter = HFSSPlotter(csv_file)
    plotter.run()