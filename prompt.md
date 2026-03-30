# 2026-03-10
I have this code:
    from math import *
    import numpy as np

    def effective_permittivity(eps_r, h_subs, w_line):
        return (eps_r + 1) / 2 + (eps_r - 1) / 2 * (1 / np.sqrt(1 + 12 * h_subs / w_line))
    # Define constants
    c = 3e8  # Speed of light in vacuum (m/s)

    eps_r = 12
    h_subs, w_line = np.array((0.050,0.1,0.25))*1e-3, np.array((0.030,0.050,0.200))*1e-3
    eps_eff = effective_permittivity(eps_r, h_subs, w_line)
    print(f"Effective permittivity: {eps_eff}")
    # Frequency of the first higher-order surface wave mode
    f_c = c / (4 * h_subs * sqrt(eps_r - 1))
    print(f"Cutoff frequency for the first higher-order surface wave mode: {f_c*1e-9} GHz")
    # Guided wavelength calculation
    f = 9.4e9  # Hz
    lambda_g = c / f * (1/np.sqrt(eps_eff))
    print(f"Guided wavelength at {f*1e-9:.2f} GHz: {lambda_g*1e3} mm")
I want to make the output more readable. Since I have eps_eff for nine different combinations of h_subs and w_line, I want to print the results in a table format. Can you help me with that?
    
Take these two paragraphs:
    As illustrated in Fig. \ref{fig:ni_det_Vdc}.a $V_{DC,1}$ is swept from 1.42 to 1.54 V, which changes the free running frequency $f_{0,1}$ from 4.996 to 4.617 GHz inversely proportional ($f_{0,1}$ decreases with the increase of $V_{DC,1}$). Moreover, the frequency detuning of the STNOs, which has been shown to be a relevant parameter, is varied through the variation of the frequency $f_{RF}$ of the external RF field between 9.282 and 9.666 GHz, while $V_{DC,2}$ is kept fixed at 1.5 V. 

    The change of Vdc1 causes an inversely proportional variation in f01, which shifts the solution phase psi1, which as can be noted in Fig. \ref{fig:ni_det_Vdc}.a, shifts the locking range $\Delta\Omega$ of STNO 1. Depending on the magnitude of this shift, there are some values of the frequency $f_{RF}$ for which STNO 1 is not synchronized, and therefore, the correlation is expected to be zero. This can be seen in Fig. \ref{fig:ni_det_Vdc}.b in the shift of the zero correlation region with respect to $V_{DC,1}$.
Adapt them to be more suitable for a scientific paper such as Applied Physics Review. Do not hesitate to reorganize ideas or remove unnecessary information to improve the flow and clarity of the text.

Do the same for the paragraph below. Give me a “PRL/Applied Physics Letters–style” ultra-compact version and a “review-paper style” (more explanatory and pedagogical) version.
    To interpret these results, the phase potential $U$ of the STNOs upon the variation of $V_{DC,1}$ is calculated. Some parameters do not change much with $V_{DC,1}$: the locking range $\Delta\Omega$ varies only 5 \% within the range of DC voltage considered. This was verified through simulations of a single, $2f$ injection-locked STNO; the power ratio $\frac{p_j}{p_i}$  (see Eq. \ref{eq:psi1_simp}), does not deviate from unity, because while both STNOs are injection locked, their power differs at maximum by 1 \% and only at the edges of the locking range $\Delta\Omega$; the effects on phase solution at zero detuning $\psi_0$ can be neglected, for a large nonlinearity factor $\nu>>1$, which is the case here. Therefore, the main effect of the variation in $V_{DC,1}$ is the change in the detuning and the phase solution of STNO 1. The resulting phase potentials are:

##########################################################################################################################################################
# 2026-03-11

I have a csv file with the following columns: h [mm],"w [mm]","Freq [GHz]","dB(S(1,1)) []","dB(S(2,1)) []","dB(S(1,2)) []","dB(S(2,2)) []"
Using Python, I need to extract the data. Then I want to plot the dB(S(1,1)) and dB(S(2,1)) as a function of frequency in a figure of two different subplots. I need three figures, one for each value of 'w'. Can you help me with that?
Please try to implement OOP principles but keep the code simple and easy to understand.

Using the csv data from the previous questions, I want to make a plot like this: one rectangle of width 'w' and height w/10, which is exactlyon top of another rectangle of height 'h' and width w*10. The color of the rectangles should be different, and the plot should have a title indicating the values of 'h' and 'w'. Thus, for each unique pair of 'h' and 'w', you will have a separate plot. Distribute these plots in three figures, one corresponding to each unique value of 'w'. Can you help me with that? As in the previous case, please try to implement OOP principles but keep the code simple and easy to understand.

##########################################################################################################################################################
# 2026-03-12

I have a .txt file where the first three lines are the following:
    Grid Output Min: [0mm -1.1mm -0.1mm] Max: [0mm 1.05mm 0.1mm] Grid Size: [0mm 0.05mm 0.005mm] 
    X, Y, Z, Complex data "Hx"
    0.0000000000000000e+00 -1.1000000000000001e-03 -1.0000000000000000e-04  2.3027258673235650e+01 1.9532243417722331e-01
    ...
I want to plot the real part of the complex data "Hx" as a function of X and Y. The plot should be a 2D color map with X and Y on the axes and the real part of "Hx" represented by the color intensity. Try to implement OOP principles but keep the code simple and easy to understand. Can you help me with that?

##########################################################################################################################################################
# 2026-03-18

I have this code that I used to extract the Real and Imaginary part of the complex impedance vs frequency in a microstrip line:
    import matplotlib.pyplot as plt
    class HFSSPlotter:
        def __init__(self, csv_file):
            self.csv_file = csv_file
            self.data = None

            self.col_h = "h [mm]"
            self.col_w = "w [mm]"
            self.col_freq = "Freq [GHz]"
            self.col_ReZo = "re(Zo(Port_In)) []"
            self.col_ImZo = "im(Zo(Port_In)) []"
            self.col_s11 = "dB(S(Port_In,Port_In)) []"
            self.col_s21 = "dB(S(Port_Out,Port_In)) []"

        def load_data(self):
            self.data = pd.read_csv(self.csv_file)

        def check_columns(self):
            required_columns = [
                self.col_h,
                self.col_w,
                self.col_freq,
                self.col_ReZo,
                self.col_ImZo,
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
                        df_wh[self.col_ReZo],
                        label=f"h = {h_value} mm"
                    )

                    axes[1].plot(
                        df_wh[self.col_freq],
                        df_wh[self.col_ImZo],
                        label=f"h = {h_value} mm"
                    )

                axes[0].set_ylabel("Re(Zo)")
                axes[0].set_title(f"Zo for w = {w_value} mm")
                axes[0].grid(True)
                axes[0].legend()

                axes[1].set_xlabel("Frequency [GHz]")
                axes[1].set_ylabel("Im(Zo)")
                axes[1].grid(True)
                axes[1].legend()

                plt.tight_layout()
                plt.show()

        def run(self):
            self.load_data()
            self.check_columns()
            self.plot_for_each_w()


    if __name__ == "__main__":
        csv_file = "Project3_param_sweep_ReZo_ImZo_S.csv"
        plotter = HFSSPlotter(csv_file)
        plotter.run()

Now I want to make a table where the Real, Imaginary and magnitude of the impedance at a frequency of 9.4 GHz are listed for each combination of 'h' and 'w'. 'w' should be in the leftmost column, but the rows should be sorted by 'h' values first and then 'w'. Can you help me with that? Please keep the code simple and easy to understand and remove the pplotting part that you do not need here.

I am trying to create a Python environment with conda in the Linux system of my computer cluster. I isntalled conda. Then, I got the message below, which I answered as it is shown:
    Do you wish to update your shell profile to automatically initialize conda?
    This will activate conda on startup and change the command prompt when activated.
    If you'd prefer that conda's base environment not be activated on startup,
    run the following command when conda is activated:

    conda config --set auto_activate_base false

    You can undo this by running `conda init --reverse $SHELL`? [yes|no]
    [no] >>> no

    You have chosen to not have conda modify your shell scripts at all.
    To activate conda's base environment in your current shell session:

    eval "$(/home/i/ibarragom/anaconda3/bin/conda shell.YOUR_SHELL_NAME hook)" 

    To install conda's shell functions for easier access, first activate, then:

    conda init

    Thank you for installing Anaconda3!
    [ibarragom@visu01 anaconda]$ export ANSYSEM_ROOT242=/home/soft/AnsysEM2024R2/v242/Linux64
    [ibarragom@visu01 anaconda]$ export LD_LIBRARY_PATH=$ANSYSEM_ROOT242/common/mono/Linux64/lib64:$A
    [ibarragom@visu01 anaconda]$ NSYSEM_ROOT242/Delcross:$LD_LIBRARY_PATH
    bash: NSYSEM_ROOT242/Delcross:/home/soft/AnsysEM2024R2/v242/Linux64/common/mono/Linux64/lib64:: No such file or directory
    [ibarragom@visu01 anaconda]$ export LD_LIBRARY_PATH=$ANSYSEM_ROOT242/common/mono/Linux64/lib64:$ANSYSEM_ROOT242/Delcross:$LD_LIBRARY_PATH
    [ibarragom@visu01 anaconda]$ conda create -n AnsysEnv
    bash: conda: command not found...
but it seems that the conda command is not available, how to meke it available?

After recording, this is the code I got (I already added a couple of things):
    import ScriptEnv

    ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
    oDesktop.RestoreWindow()
    oProject = oDesktop.SetActiveProject("Project3_Microstrip_param_sweep")
    oDesign = oProject.SetActiveDesign("Wave port forced 2")

    w_values = ["0.03", "0.05", "0.2"]
    h_values = ["0.05", "0.1", "0.2", "0.5"]

    for h in h_values:
        for w in w_values:
            oDesign.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:LocalVariableTab",
                        [
                            "NAME:PropServers", 
                            "LocalVariables"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:w",
                                "Value:="		, "{w}mm"
                            ]
                        ]
                    ]
                ])
            oDesign.ChangeProperty(
                [
                    "NAME:AllTabs",
                    [
                        "NAME:LocalVariableTab",
                        [
                            "NAME:PropServers", 
                            "LocalVariables"
                        ],
                        [
                            "NAME:ChangedProps",
                            [
                                "NAME:h",
                                "Value:="		, "{h}mm"
                            ]
                        ]
                    ]
                ])
            oModule = oDesign.GetModule("FieldsReporter")
            oModule.CopyNamedExprToStack("Hx")
            oModule.ExportOnGrid("/home/i/ibarragom/Ansoft/Projects_HFSS/hx_w{w}_h{h}.fld", ["-w_subs/2", "-L/2", "-h/2"], ["w_subs/2", "L/2", "3/4*h"], ["w_subs/100", "L/100", "h/100"], "Setup1 : LastAdaptive", 
                [
                    "Freq:="		, "9.4GHz",
                    "L:="			, "2mm",
                    "L_air:="		, "L/1mm mm",
                    "Phase:="		, "0deg",
                    "h:="			, "0.05mm",
                    "h_air:="		, "10*h/1mm mm",
                    "t_line:="		, "0.001mm",
                    "w:="			, "0.03mm",
                    "w_air:="		, "10*w/1mm mm",
                    "w_subs:="		, "w*10/1mm mm"
                ], 
                [
                    "NAME:ExportOption",
                    "IncludePtInOutput:="	, True,
                    "RefCSName:="		, "Global",
                    "PtInSI:="		, True,
                    "FieldInRefCS:="	, False
                ], "Cartesian", ["0mm", "0mm", "0mm"], False)
Is there a way it can be improved?

I got this error:
    AttributeError                            Traceback (most recent call last)
    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:116, in AedtObjWrapper.__Invoke__(self, funcName, argv)
        115     self.dllapi.recreate_application(True)
    --> 116 ret = _retry_ntimes(
        117     settings.number_of_grpc_api_retries,
        118     self.dllapi.AedtAPI.InvokeAedtObjMethod,
        119     self.objectID,
        120     funcName,
        121     argv,
        122 )  # Call C function
        123 if ret and isinstance(ret, (AedtObjWrapper, AedtPropServer)):

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:607, in _retry_ntimes(n, function, *args, **kwargs)
        606 if "__name__" in dir(function):
    --> 607     raise AttributeError(f"Error in Executing Method {function.__name__}.")
        608 else:

    AttributeError: Error in Executing Method InvokeAedtObjMethod.

    During handling of the above exception, another exception occurred:

    GrpcApiError                              Traceback (most recent call last)
    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/visualization/post/post_common_3d.py:656, in PostProcessor3D.export_field_file_on_grid(self, quantity, solution, variations, file_name, grid_type, grid_center, grid_start, grid_stop, grid_step, is_vector, intrinsics, phase, export_with_sample_points, reference_coordinate_system, export_in_si_system, export_field_in_reference)
        655 try:
    --> 656     self.ofieldsreporter.EnterQty(quantity)
        657 except Exception:

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:138, in AedtObjWrapper.__GetObjMethod__.<locals>.DynamicFunc(self, *args)
        137 def DynamicFunc(self, *args):
    --> 138     return self.__Invoke__(funcName, args)

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:129, in AedtObjWrapper.__Invoke__(self, funcName, argv)
        128 pyaedt_logger.debug(f"{funcName}({argv})")
    --> 129 raise GrpcApiError(f"Failed to execute gRPC AEDT command: {funcName}")

    GrpcApiError: Failed to execute gRPC AEDT command: EnterQty

    During handling of the above exception, another exception occurred:

    AttributeError                            Traceback (most recent call last)
    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:116, in AedtObjWrapper.__Invoke__(self, funcName, argv)
        115     self.dllapi.recreate_application(True)
    --> 116 ret = _retry_ntimes(
        117     settings.number_of_grpc_api_retries,
        118     self.dllapi.AedtAPI.InvokeAedtObjMethod,
        119     self.objectID,
        120     funcName,
        121     argv,
        122 )  # Call C function
        123 if ret and isinstance(ret, (AedtObjWrapper, AedtPropServer)):

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:607, in _retry_ntimes(n, function, *args, **kwargs)
        606 if "__name__" in dir(function):
    --> 607     raise AttributeError(f"Error in Executing Method {function.__name__}.")
        608 else:

    AttributeError: Error in Executing Method InvokeAedtObjMethod.

    During handling of the above exception, another exception occurred:

    GrpcApiError                              Traceback (most recent call last)
    File ~/Ansoft/Projects_HFSS/untitled0.py:59
        45 variations = {
        46     "Freq": "9.4GHz",
        47     "Phase": "0deg",
    (...)     55     "w_subs": f"{10*w_num}mm",
        56 }
        58 # Export Hx on a Cartesian grid
    ---> 59 ok = hfss.post.export_field_file_on_grid(
        60     quantity="Hx",
        61     solution=solution_name,
        62     variations=variations,
        63     file_name=output_file,
        64     grid_type="Cartesian",
        65     grid_start=["-w_subs/2", "-L/2", "-h/2"],
        66     grid_stop=["w_subs/2", "L/2", "3/4*h"],
        67     grid_step=["w_subs/100", "L/100", "h/100"],
        68     is_vector=False,
        69     intrinsics={"Freq": "9.4GHz", "Phase": "0deg"},
        70 )
        72 if ok:
        73     print(f"Exported: {output_file}")

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:236, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
        234 except GrpcApiError as e:
        235     _exception(sys.exc_info(), user_function, args, kwargs, "AEDT API Error")
    --> 236     return raise_exception_or_return_false(e)
        237 except BaseException as e:
        238     msg = str(sys.exc_info()[1])

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:208, in raise_exception_or_return_false(e)
        205         for v in list(_desktop_sessions.values())[:]:
        206             v.release_desktop(close_projects=v.close_on_exit, close_on_exit=v.close_on_exit)
    --> 208     raise e
        209 elif "__init__" in str(e):  # pragma: no cover
        210     return

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:221, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
        219 try:
        220     settings.time_tick = time.time()
    --> 221     out = user_function(*args, **kwargs)
        222     _log_method(user_function, args, kwargs)
        223     return out

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/visualization/post/post_common_3d.py:658, in PostProcessor3D.export_field_file_on_grid(self, quantity, solution, variations, file_name, grid_type, grid_center, grid_start, grid_stop, grid_step, is_vector, intrinsics, phase, export_with_sample_points, reference_coordinate_system, export_in_si_system, export_field_in_reference)
        656     self.ofieldsreporter.EnterQty(quantity)
        657 except Exception:
    --> 658     self.ofieldsreporter.CopyNamedExprToStack(quantity)
        659 if is_vector:
        660     self.ofieldsreporter.CalcOp("Smooth")

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:138, in AedtObjWrapper.__GetObjMethod__.<locals>.DynamicFunc(self, *args)
        137 def DynamicFunc(self, *args):
    --> 138     return self.__Invoke__(funcName, args)

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:129, in AedtObjWrapper.__Invoke__(self, funcName, argv)
        127 pyaedt_logger.debug("Failed to execute gRPC AEDT command:")
        128 pyaedt_logger.debug(f"{funcName}({argv})")
    --> 129 raise GrpcApiError(f"Failed to execute gRPC AEDT command: {funcName}")

    GrpcApiError: Failed to execute gRPC AEDT command: CopyNamedExprToStack

And in ansys the following messages:

    *Global - Messages
    [info] GRPC server running on port: 48697. 
    Project3_Microstrip_param_sweep (/home/i/ibarragom/Ansoft/Projects_HFSS/)
    Wave port forced 2 (Terminal Network)
        [error] Script macro error: Abnormal script termination. (04:41:33 PM  Mar 18, 2026)
        [error] Script macro error: Cannot find the named expression (04:41:33 PM  Mar 18, 2026)

How can I fix this ?

##########################################################################################################################################################
# 2026-03-19

I created this Python program to extract the Hx field from an HFSS simulation and export it on a grid:
    import os
    import time
    from pathlib import Path
    # from UTIL_ANSYSEDT_BOUCLE import submit_job, wait_for_batch_to_stop, find_next_var_file
    from UTIL_KILL_PROCESS_ANSYS import kill_hfss_processes_for_user, handle_lock_file
    import ansys.aedt.core
    from ansys.aedt.core import hfss
    import numpy as np

    # HFSS parameters
    aedt_version = "2024.2"  # To modify if necessary
    non_graphical = True  # Set to False if you want to open HFSS

    # Paths
    script_path = Path(__file__).resolve()  # Path of the script
    script_dir = script_path.parent  # Directory containing the script
    project_name = "Project3_Microstrip_param_sweep_19_03_2026"
    project_path = script_dir / f"{project_name}.aedt"
    batchinfo_dir = script_dir / f"{project_name}.aedt.batchinfo"  # Corrected path
    result_folder = script_dir / "results"
    result_folder.mkdir(exist_ok=True)  # Create results folder if it doesn't exist

    # Main script
    if __name__ == "__main__":
        kill_hfss_processes_for_user()
        handle_lock_file(project_path)

        last_seen_file = None

        # Open HFSS and modify the offset parameter
        hfss = ansys.aedt.core.Hfss(
            project=str(project_path),
            version=aedt_version,
            design="Wave port forced 2",
            non_graphical=non_graphical,
            new_desktop=True,
            close_on_exit=False,
            solution_type="Modal",
            remove_lock=True,
        )
        hfss.post.export_field_file_on_grid(
        quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
        solution="Setup1 : LastAdaptive",
        variation_dict={"Freq": "9.4GHz"},
        export_path="Hx_L-0p5_pyaedt.fld",
        grid_start=["-w_subs/2", "-L/4", "-h/2"],
        grid_stop =["-w_subs/2", "-L/4", "3/4*h"],
        grid_step=["w_subs/500", "L/500", "h/400"]
        )
        
        # hfss.variable_manager.set_variable("offset", expression=f"{offset}in")
        # hfss.save_project()
        hfss.release_desktop(close_projects=True, close_desktop=True)
Nevertheless, I get this error:
    TypeError                                 Traceback (most recent call last)
    File ~/Ansoft/Projects_HFSS/export_Hx_step01.py:59
        48 # Open HFSS and modify the offset parameter
        49 hfss = ansys.aedt.core.Hfss(
        50     project=str(project_path),
        51     version=aedt_version,
    (...)     57     remove_lock=True,
        58 )
    ---> 59 hfss.post.export_field_file_on_grid(
        60 quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
        61 solution="Setup1 : LastAdaptive",
        62 variation_dict={"Freq": "9.4GHz"},
        63 export_path="Hx_L-0p5_pyaedt.fld",
        64 grid_start=["-w_subs/2", "-L/4", "-h/2"],
        65 grid_stop =["-w_subs/2", "-L/4", "3/4*h"],
        66 grid_step=["w_subs/500", "L/500", "h/400"]
        67 )
        69 # hfss.variable_manager.set_variable("offset", expression=f"{offset}in")
        70 # hfss.save_project()
        71 hfss.release_desktop(close_projects=True, close_desktop=True)

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:246, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
        244     msg = msg.capitalize()
        245 _exception(sys.exc_info(), user_function, args, kwargs, msg)
    --> 246 return raise_exception_or_return_false(e)

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:208, in raise_exception_or_return_false(e)
        205         for v in list(_desktop_sessions.values())[:]:
        206             v.release_desktop(close_projects=v.close_on_exit, close_on_exit=v.close_on_exit)
    --> 208     raise e
        209 elif "__init__" in str(e):  # pragma: no cover
        210     return

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:221, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
        219 try:
        220     settings.time_tick = time.time()
    --> 221     out = user_function(*args, **kwargs)
        222     _log_method(user_function, args, kwargs)
        223     return out

    TypeError: PostProcessor3D.export_field_file_on_grid() got an unexpected keyword argument 'variation_dict'

How to solve this issue? 

This is the code now:
    import os
    import time
    from pathlib import Path
    # from UTIL_ANSYSEDT_BOUCLE import submit_job, wait_for_batch_to_stop, find_next_var_file
    from UTIL_KILL_PROCESS_ANSYS import kill_hfss_processes_for_user, handle_lock_file
    import ansys.aedt.core
    from ansys.aedt.core import Hfss
    import numpy as np

    # HFSS parameters
    aedt_version = "2024.2"  # To modify if necessary
    non_graphical = True  # Set to False if you want to open HFSS

    # Paths
    script_path = Path(__file__).resolve()  # Path of the script
    script_dir = script_path.parent  # Directory containing the script
    project_name = "Project3_Microstrip_param_sweep_19_03_2026"
    project_path = script_dir / f"{project_name}.aedt"
    batchinfo_dir = script_dir / f"{project_name}.aedt.batchinfo"  # Corrected path
    result_folder = script_dir / "results"
    result_folder.mkdir(exist_ok=True)  # Create results folder if it doesn't exist

    w, h = 0.05, 0.05
    w_subs, L = 10*w, 2

    # Main script
    if __name__ == "__main__":
        kill_hfss_processes_for_user()
        handle_lock_file(project_path)

        last_seen_file = None

        # Open HFSS and modify the offset parameter
        hfss = Hfss(
            project=str(project_path),
            version=aedt_version,
            design="Wave port forced 2",
            non_graphical=non_graphical,
            new_desktop=True,
            close_on_exit=False,
            solution_type="Modal",
            remove_lock=True,
        )
        hfss.variable_manager.set_variable("w", expression=f"{w}mm")
        hfss.variable_manager.set_variable("h", expression=f"{h}mm")
        
        hfss.post.export_field_file_on_grid(
        quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
        solution="Setup1 : LastAdaptive",
        variations=hfss.available_variations.nominal_values,
        file_name=str(script_dir / "Hx_L-0p5_pyaedt.fld"),
        grid_type="Cartesian",
        grid_start=[-w_subs/2, -L/4, -h/2],
        grid_stop =[ w_subs/2, -L/4, 3/4*h],
        grid_step=[w_subs/500, L/500, h/400],
        intrinsics={"Freq": "9.4GHz", "Phase": "0deg"},
        is_vector=False,
        export_in_si_system=True,
        )
        
        # hfss.variable_manager.set_variable("offset", expression=f"{offset}in")
        # hfss.save_project()
        hfss.release_desktop(close_projects=True, close_desktop=True)
And I get this error:
    AttributeError                            Traceback (most recent call last)
    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:116, in AedtObjWrapper.__Invoke__(self, funcName, argv)
        115     self.dllapi.recreate_application(True)
    --> 116 ret = _retry_ntimes(
        117     settings.number_of_grpc_api_retries,
        118     self.dllapi.AedtAPI.InvokeAedtObjMethod,
        119     self.objectID,
        120     funcName,
        121     argv,
        122 )  # Call C function
        123 if ret and isinstance(ret, (AedtObjWrapper, AedtPropServer)):

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:607, in _retry_ntimes(n, function, *args, **kwargs)
        606 if "__name__" in dir(function):
    --> 607     raise AttributeError(f"Error in Executing Method {function.__name__}.")
        608 else:

    AttributeError: Error in Executing Method InvokeAedtObjMethod.

    During handling of the above exception, another exception occurred:

    GrpcApiError                              Traceback (most recent call last)
    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/visualization/post/post_common_3d.py:656, in PostProcessor3D.export_field_file_on_grid(self, quantity, solution, variations, file_name, grid_type, grid_center, grid_start, grid_stop, grid_step, is_vector, intrinsics, phase, export_with_sample_points, reference_coordinate_system, export_in_si_system, export_field_in_reference)
        655 try:
    --> 656     self.ofieldsreporter.EnterQty(quantity)
        657 except Exception:

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:138, in AedtObjWrapper.__GetObjMethod__.<locals>.DynamicFunc(self, *args)
        137 def DynamicFunc(self, *args):
    --> 138     return self.__Invoke__(funcName, args)

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:129, in AedtObjWrapper.__Invoke__(self, funcName, argv)
        128 pyaedt_logger.debug(f"{funcName}({argv})")
    --> 129 raise GrpcApiError(f"Failed to execute gRPC AEDT command: {funcName}")

    GrpcApiError: Failed to execute gRPC AEDT command: EnterQty

    During handling of the above exception, another exception occurred:

    AttributeError                            Traceback (most recent call last)
    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:116, in AedtObjWrapper.__Invoke__(self, funcName, argv)
        115     self.dllapi.recreate_application(True)
    --> 116 ret = _retry_ntimes(
        117     settings.number_of_grpc_api_retries,
        118     self.dllapi.AedtAPI.InvokeAedtObjMethod,
        119     self.objectID,
        120     funcName,
        121     argv,
        122 )  # Call C function
        123 if ret and isinstance(ret, (AedtObjWrapper, AedtPropServer)):

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:607, in _retry_ntimes(n, function, *args, **kwargs)
        606 if "__name__" in dir(function):
    --> 607     raise AttributeError(f"Error in Executing Method {function.__name__}.")
        608 else:

    AttributeError: Error in Executing Method InvokeAedtObjMethod.

    During handling of the above exception, another exception occurred:

    GrpcApiError                              Traceback (most recent call last)
    File ~/Ansoft/Projects_HFSS/export_Hx_step01.py:63
        60 hfss.variable_manager.set_variable("w", expression=f"{w}mm")
        61 hfss.variable_manager.set_variable("h", expression=f"{h}mm")
    ---> 63 hfss.post.export_field_file_on_grid(
        64 quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
        65 solution="Setup1 : LastAdaptive",
        66 variations=hfss.available_variations.nominal_values,
        67 file_name=str(script_dir / "Hx_L-0p5_pyaedt.fld"),
        68 grid_type="Cartesian",
        69 grid_start=[-w_subs/2, -L/4, -h/2],
        70 grid_stop =[ w_subs/2, -L/4, 3/4*h],
        71 grid_step=[w_subs/500, L/500, h/400],
        72 intrinsics={"Freq": "9.4GHz", "Phase": "0deg"},
        73 is_vector=False,
        74 export_in_si_system=True,
        75 )
        77 # hfss.variable_manager.set_variable("offset", expression=f"{offset}in")
        78 # hfss.save_project()
        79 hfss.release_desktop(close_projects=True, close_desktop=True)

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:236, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
        234 except GrpcApiError as e:
        235     _exception(sys.exc_info(), user_function, args, kwargs, "AEDT API Error")
    --> 236     return raise_exception_or_return_false(e)
        237 except BaseException as e:
        238     msg = str(sys.exc_info()[1])

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:208, in raise_exception_or_return_false(e)
        205         for v in list(_desktop_sessions.values())[:]:
        206             v.release_desktop(close_projects=v.close_on_exit, close_on_exit=v.close_on_exit)
    --> 208     raise e
        209 elif "__init__" in str(e):  # pragma: no cover
        210     return

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:221, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
        219 try:
        220     settings.time_tick = time.time()
    --> 221     out = user_function(*args, **kwargs)
        222     _log_method(user_function, args, kwargs)
        223     return out

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/visualization/post/post_common_3d.py:658, in PostProcessor3D.export_field_file_on_grid(self, quantity, solution, variations, file_name, grid_type, grid_center, grid_start, grid_stop, grid_step, is_vector, intrinsics, phase, export_with_sample_points, reference_coordinate_system, export_in_si_system, export_field_in_reference)
        656     self.ofieldsreporter.EnterQty(quantity)
        657 except Exception:
    --> 658     self.ofieldsreporter.CopyNamedExprToStack(quantity)
        659 if is_vector:
        660     self.ofieldsreporter.CalcOp("Smooth")

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:138, in AedtObjWrapper.__GetObjMethod__.<locals>.DynamicFunc(self, *args)
        137 def DynamicFunc(self, *args):
    --> 138     return self.__Invoke__(funcName, args)

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:129, in AedtObjWrapper.__Invoke__(self, funcName, argv)
        127 pyaedt_logger.debug("Failed to execute gRPC AEDT command:")
        128 pyaedt_logger.debug(f"{funcName}({argv})")
    --> 129 raise GrpcApiError(f"Failed to execute gRPC AEDT command: {funcName}")

    GrpcApiError: Failed to execute gRPC AEDT command: CopyNamedExprToStack
How can I fix this issue?

AttributeError                            Traceback (most recent call last)
File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:116, in AedtObjWrapper.__Invoke__(self, funcName, argv)
    115     self.dllapi.recreate_application(True)
--> 116 ret = _retry_ntimes(
    117     settings.number_of_grpc_api_retries,
    118     self.dllapi.AedtAPI.InvokeAedtObjMethod,
    119     self.objectID,
    120     funcName,
    121     argv,
    122 )  # Call C function
    123 if ret and isinstance(ret, (AedtObjWrapper, AedtPropServer)):

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:607, in _retry_ntimes(n, function, *args, **kwargs)
    606 if "__name__" in dir(function):
--> 607     raise AttributeError(f"Error in Executing Method {function.__name__}.")
    608 else:

AttributeError: Error in Executing Method InvokeAedtObjMethod.

During handling of the above exception, another exception occurred:

GrpcApiError                              Traceback (most recent call last)
File ~/Ansoft/Projects_HFSS/export_Hx_step01.py:63
     60 hfss.variable_manager.set_variable("w", expression=f"{w}mm")
     61 hfss.variable_manager.set_variable("h", expression=f"{h}mm")
---> 63 hfss.post.export_field_file_on_grid(
     64 # quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
     65 quantity="Hx",
     66 solution="Setup1 : LastAdaptive",
     67 variations=hfss.available_variations.nominal_values,
     68 file_name=str(script_dir / "Hx_L-0p5_pyaedt.fld"),
     69 grid_type="Cartesian",
     70 grid_start=[-w_subs/2, -L/4, -h/2],
     71 grid_stop =[ w_subs/2, -L/4, 3/4*h],
     72 grid_step=[w_subs/500, L/500, h/400],
     73 intrinsics={"Freq": "9.4GHz", "Phase": "0deg"},
     74 is_vector=False,
     75 export_in_si_system=False,
     76 )
     78 # hfss.variable_manager.set_variable("offset", expression=f"{offset}in")
     79 # hfss.save_project()
     80 hfss.release_desktop(close_projects=True, close_desktop=True)

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:236, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
    234 except GrpcApiError as e:
    235     _exception(sys.exc_info(), user_function, args, kwargs, "AEDT API Error")
--> 236     return raise_exception_or_return_false(e)
    237 except BaseException as e:
    238     msg = str(sys.exc_info()[1])

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:208, in raise_exception_or_return_false(e)
    205         for v in list(_desktop_sessions.values())[:]:
    206             v.release_desktop(close_projects=v.close_on_exit, close_on_exit=v.close_on_exit)
--> 208     raise e
    209 elif "__init__" in str(e):  # pragma: no cover
    210     return

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:221, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
    219 try:
    220     settings.time_tick = time.time()
--> 221     out = user_function(*args, **kwargs)
    222     _log_method(user_function, args, kwargs)
    223     return out

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/visualization/post/post_common_3d.py:665, in PostProcessor3D.export_field_file_on_grid(self, quantity, solution, variations, file_name, grid_type, grid_center, grid_start, grid_stop, grid_step, is_vector, intrinsics, phase, export_with_sample_points, reference_coordinate_system, export_in_si_system, export_field_in_reference)
    663         self.ofieldsreporter.CalcOp("AtPhase")
    664         self.ofieldsreporter.CalcOp("Mag")
--> 665 units = self._app.modeler.model_units
    666 ang_units = "deg"
    667 if grid_type == "Cartesian":

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/application/analysis_3d.py:180, in FieldAnalysis3D.modeler(self)
    177     from ansys.aedt.core.modeler.modeler_2d import Modeler2D
    178     from ansys.aedt.core.modeler.modeler_3d import Modeler3D
--> 180     self._modeler = Modeler2D(self) if self.design_type in ["Maxwell 2D", "2D Extractor"] else Modeler3D(self)
    181     self.logger.info_timer("Modeler class has been initialized!")
    182 return self._modeler

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/modeler/modeler_3d.py:61, in Modeler3D.__init__(self, application)
     60 def __init__(self, application) -> None:
---> 61     Primitives3D.__init__(self, application)

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/modeler/cad/primitives_3d.py:124, in Primitives3D.__init__(self, application)
    123 def __init__(self, application) -> None:
--> 124     GeometryModeler.__init__(self, application, is3d=True)
    125     self.multiparts = []

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/modeler/cad/primitives.py:296, in GeometryModeler.__init__(self, app, is3d)
    294 self.user_defined_components = Objects(self, "u")
    295 self.points = Objects(self, "p")
--> 296 self.refresh()

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:236, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
    234 except GrpcApiError as e:
    235     _exception(sys.exc_info(), user_function, args, kwargs, "AEDT API Error")
--> 236     return raise_exception_or_return_false(e)
    237 except BaseException as e:
    238     msg = str(sys.exc_info()[1])

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:208, in raise_exception_or_return_false(e)
    205         for v in list(_desktop_sessions.values())[:]:
    206             v.release_desktop(close_projects=v.close_on_exit, close_on_exit=v.close_on_exit)
--> 208     raise e
    209 elif "__init__" in str(e):  # pragma: no cover
    210     return

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:221, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
    219 try:
    220     settings.time_tick = time.time()
--> 221     out = user_function(*args, **kwargs)
    222     _log_method(user_function, args, kwargs)
    223     return out

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/modeler/cad/primitives.py:860, in GeometryModeler.refresh(self)
    858 self.objects = Objects(self, "o")
    859 self.user_defined_components = Objects(self, "u")
--> 860 self._refresh_object_types()
    861 if not settings.objects_lazy_load:
    862     self._refresh_all_ids_wrapper()

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:236, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
    234 except GrpcApiError as e:
    235     _exception(sys.exc_info(), user_function, args, kwargs, "AEDT API Error")
--> 236     return raise_exception_or_return_false(e)
    237 except BaseException as e:
    238     msg = str(sys.exc_info()[1])

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:208, in raise_exception_or_return_false(e)
    205         for v in list(_desktop_sessions.values())[:]:
    206             v.release_desktop(close_projects=v.close_on_exit, close_on_exit=v.close_on_exit)
--> 208     raise e
    209 elif "__init__" in str(e):  # pragma: no cover
    210     return

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:221, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
    219 try:
    220     settings.time_tick = time.time()
--> 221     out = user_function(*args, **kwargs)
    222     _log_method(user_function, args, kwargs)
    223     return out

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/modeler/cad/primitives.py:8846, in GeometryModeler._refresh_object_types(self)
   8844 @pyaedt_function_handler()
   8845 def _refresh_object_types(self) -> None:
-> 8846     self._refresh_solids()
   8847     self._refresh_sheets()
   8848     self._refresh_lines()

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:236, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
    234 except GrpcApiError as e:
    235     _exception(sys.exc_info(), user_function, args, kwargs, "AEDT API Error")
--> 236     return raise_exception_or_return_false(e)
    237 except BaseException as e:
    238     msg = str(sys.exc_info()[1])

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:208, in raise_exception_or_return_false(e)
    205         for v in list(_desktop_sessions.values())[:]:
    206             v.release_desktop(close_projects=v.close_on_exit, close_on_exit=v.close_on_exit)
--> 208     raise e
    209 elif "__init__" in str(e):  # pragma: no cover
    210     return

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:221, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
    219 try:
    220     settings.time_tick = time.time()
--> 221     out = user_function(*args, **kwargs)
    222     _log_method(user_function, args, kwargs)
    223     return out

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/modeler/cad/primitives.py:8803, in GeometryModeler._refresh_solids(self)
   8801 @pyaedt_function_handler()
   8802 def _refresh_solids(self) -> None:
-> 8803     self.__refresh_object_type("Solids")

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:236, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
    234 except GrpcApiError as e:
    235     _exception(sys.exc_info(), user_function, args, kwargs, "AEDT API Error")
--> 236     return raise_exception_or_return_false(e)
    237 except BaseException as e:
    238     msg = str(sys.exc_info()[1])

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:208, in raise_exception_or_return_false(e)
    205         for v in list(_desktop_sessions.values())[:]:
    206             v.release_desktop(close_projects=v.close_on_exit, close_on_exit=v.close_on_exit)
--> 208     raise e
    209 elif "__init__" in str(e):  # pragma: no cover
    210     return

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:221, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
    219 try:
    220     settings.time_tick = time.time()
--> 221     out = user_function(*args, **kwargs)
    222     _log_method(user_function, args, kwargs)
    223     return out

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/modeler/cad/primitives.py:8786, in GeometryModeler.__refresh_object_type(self, object_type)
   8783     raise ValueError(f"Object type {object_type} is not allowed.")
   8785 try:
-> 8786     objects = self.oeditor.GetObjectsInGroup(object_type)
   8787 except (TypeError, AttributeError):
   8788     objects = []

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/modeler/cad/primitives.py:450, in GeometryModeler.oeditor(self)
    442 @property
    443 def oeditor(self):
    444     """AEDT ``oEditor`` module.
    445 
    446     References
    447     ----------
    448     >>> oEditor = oDesign.SetActiveEditor("3D Modeler")
    449     """
--> 450     return self._app.oeditor

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/application/aedt_objects.py:423, in AedtObjects.oeditor(self)
    421         self._oeditor = None
    422     else:
--> 423         self._oeditor = self._odesign.SetActiveEditor("3D Modeler")
    424 return self._oeditor

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:138, in AedtObjWrapper.__GetObjMethod__.<locals>.DynamicFunc(self, *args)
    137 def DynamicFunc(self, *args):
--> 138     return self.__Invoke__(funcName, args)

File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:129, in AedtObjWrapper.__Invoke__(self, funcName, argv)
    127 pyaedt_logger.debug("Failed to execute gRPC AEDT command:")
    128 pyaedt_logger.debug(f"{funcName}({argv})")
--> 129 raise GrpcApiError(f"Failed to execute gRPC AEDT command: {funcName}")

GrpcApiError: Failed to execute gRPC AEDT command: SetActiveEditor

The design type is HFSS and the model units mm. AEDT was opened and then, but then it printed "script macro error". Moreover, there was this error:
    AttributeError                            Traceback (most recent call last)
    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:116, in AedtObjWrapper.__Invoke__(self, funcName, argv)
        115     self.dllapi.recreate_application(True)
    --> 116 ret = _retry_ntimes(
        117     settings.number_of_grpc_api_retries,
        118     self.dllapi.AedtAPI.InvokeAedtObjMethod,
        119     self.objectID,
        120     funcName,
        121     argv,
        122 )  # Call C function
        123 if ret and isinstance(ret, (AedtObjWrapper, AedtPropServer)):

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:607, in _retry_ntimes(n, function, *args, **kwargs)
        606 if "__name__" in dir(function):
    --> 607     raise AttributeError(f"Error in Executing Method {function.__name__}.")
        608 else:

    AttributeError: Error in Executing Method InvokeAedtObjMethod.

    During handling of the above exception, another exception occurred:

    GrpcApiError                              Traceback (most recent call last)
    File ~/Ansoft/Projects_HFSS/export_Hx_step01.py:68
        63     print("model units:", hfss.modeler.model_units)
        65     # hfss.variable_manager.set_variable("w", expression=f"{w}mm")
        66     # hfss.variable_manager.set_variable("h", expression=f"{h}mm")
    ---> 68     hfss.post.export_field_file_on_grid(
        69     # quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
        70     quantity="Hx",
        71     solution="Setup1 : LastAdaptive",
        72     variations=hfss.available_variations.nominal_values,
        73     file_name=str(script_dir / "Hx_L-0p5_pyaedt.fld"),
        74     grid_type="Cartesian",
        75     grid_start=[-w_subs/2, -L/4, -h/2],
        76     grid_stop =[ w_subs/2, -L/4, 3/4*h],
        77     grid_step=[w_subs/500, L/500, h/400],
        78     intrinsics={"Freq": "9.4GHz", "Phase": "0deg"},
        79     is_vector=False,
        80     export_in_si_system=False,
        81     )
        83     # # hfss.variable_manager.set_variable("offset", expression=f"{offset}in")
        84     # # hfss.save_project()
        85     # hfss.release_desktop(close_projects=True, close_desktop=True)
        86 
        87 
        88 finally:
        89     if hfss:

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:236, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
        234 except GrpcApiError as e:
        235     _exception(sys.exc_info(), user_function, args, kwargs, "AEDT API Error")
    --> 236     return raise_exception_or_return_false(e)
        237 except BaseException as e:
        238     msg = str(sys.exc_info()[1])

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:208, in raise_exception_or_return_false(e)
        205         for v in list(_desktop_sessions.values())[:]:
        206             v.release_desktop(close_projects=v.close_on_exit, close_on_exit=v.close_on_exit)
    --> 208     raise e
        209 elif "__init__" in str(e):  # pragma: no cover
        210     return

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:221, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
        219 try:
        220     settings.time_tick = time.time()
    --> 221     out = user_function(*args, **kwargs)
        222     _log_method(user_function, args, kwargs)
        223     return out

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/visualization/post/post_common_3d.py:708, in PostProcessor3D.export_field_file_on_grid(self, quantity, solution, variations, file_name, grid_type, grid_center, grid_start, grid_stop, grid_step, is_vector, intrinsics, phase, export_with_sample_points, reference_coordinate_system, export_in_si_system, export_field_in_reference)
        694 variation.extend(intrinsics)
        696 export_options = [
        697     "NAME:ExportOption",
        698     "IncludePtInOutput:=",
    (...)    705     export_field_in_reference,
        706 ]
    --> 708 self.ofieldsreporter.ExportOnGrid(
        709     str(file_name),
        710     grid_start_wu,
        711     grid_stop_wu,
        712     grid_step_wu,
        713     solution,
        714     variation,
        715     export_options,
        716     grid_type,
        717     grid_center,
        718     False,
        719 )
        720 if Path(file_name).exists():
        721     return str(file_name)

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:138, in AedtObjWrapper.__GetObjMethod__.<locals>.DynamicFunc(self, *args)
        137 def DynamicFunc(self, *args):
    --> 138     return self.__Invoke__(funcName, args)

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:129, in AedtObjWrapper.__Invoke__(self, funcName, argv)
        127 pyaedt_logger.debug("Failed to execute gRPC AEDT command:")
        128 pyaedt_logger.debug(f"{funcName}({argv})")
    --> 129 raise GrpcApiError(f"Failed to execute gRPC AEDT command: {funcName}")

    GrpcApiError: Failed to execute gRPC AEDT command: ExportOnGrid


This is the code I'm using now:
    import os
    import time
    from pathlib import Path
    # from UTIL_ANSYSEDT_BOUCLE import submit_job, wait_for_batch_to_stop, find_next_var_file
    from UTIL_KILL_PROCESS_ANSYS import kill_hfss_processes_for_user, handle_lock_file
    import ansys.aedt.core
    from ansys.aedt.core import Hfss
    import numpy as np


    # HFSS parameters
    aedt_version = "2024.2"  # To modify if necessary
    non_graphical = True  # Set to False if you want to open HFSS

    # Paths
    script_path = Path(__file__).resolve()  # Path of the script
    script_dir = script_path.parent  # Directory containing the script
    project_name = "Project3_Microstrip_param_sweep_19_03_2026"
    project_path = script_dir / f"{project_name}.aedt"
    batchinfo_dir = script_dir / f"{project_name}.aedt.batchinfo"  # Corrected path
    result_folder = script_dir / "results"
    result_folder.mkdir(exist_ok=True)  # Create results folder if it doesn't exist

    hfss = None

    w, h = 0.05, 0.1
    w_subs, L = 10*w, 2

    # Main script
    if __name__ == "__main__":
        kill_hfss_processes_for_user()
        handle_lock_file(project_path)

        last_seen_file = None
        try:
            # Open HFSS and modify the offset parameter
            hfss = Hfss(
                project=str(project_path),
                version=aedt_version,
                design="Wave port forced 2",
                non_graphical=non_graphical,
                new_desktop=True,
                close_on_exit=False,
                solution_type="Modal",
                remove_lock=True,
            )
            print("design name:", hfss.design_name)
            print("design type:", hfss.design_type)
            print("solution type:", hfss.solution_type)
            print("model units:", hfss.modeler.model_units)
            # hfss.variable_manager.set_variable("w", expression=f"{w}mm")
            # hfss.variable_manager.set_variable("h", expression=f"{h}mm")
            print(hfss.available_variations.nominal_values)

            # Build a Y = constant slice explicitly
            x_vals = np.linspace(-w_subs/2,  w_subs/2, 501)
            z_vals = np.linspace(-h/2, 3*h/4, 401)
            y0 = -L/4
        
            sample_points = []
            for x in x_vals:
                for z in z_vals:
                    sample_points.append([x, y0, z])

            hfss.post.fields_calculator.export(
            # quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
            quantity="H",
            solution="Setup1 : LastAdaptive",
            variations=hfss.available_variations.nominal_values,
            output_file=str(script_dir / "Hx_L-0p5_pyaedt.fld"),
            intrinsics={"Freq": "9.4GHz", "Phase": "0deg"},
            sample_points=sample_points,
            export_with_sample_points=True,
            reference_coordinate_system="Global",
            export_in_si_system=False,
            is_vector=True,
            )
            
            # hfss.post.export_field_file_on_grid(
            # # quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
            # quantity="Hx",
            # solution="Setup1 : LastAdaptive",
            # variations=hfss.available_variations.nominal_values,
            # file_name=str(script_dir / "Hx_L-0p5_pyaedt.fld"),
            # grid_type="Cartesian",
            # grid_start=[-w_subs/2, -L/4, -h/2],
            # grid_stop =[ w_subs/2, -L/4, 3/4*h],
            # grid_step=[w_subs/500, 0, h/400],
            # intrinsics={"Freq": "9.4GHz", "Phase": "0deg"},
            # is_vector=True,
            # export_in_si_system=False,
            # )

        
        
        finally:
            if hfss:
                print("All simulations completed. GREAAAT JOB!!!!!!!!!!!!!")
                hfss.release_desktop(close_projects=True, close_desktop=True)
This is the error I get:
    AttributeError                            Traceback (most recent call last)
    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:116, in AedtObjWrapper.__Invoke__(self, funcName, argv)
        115     self.dllapi.recreate_application(True)
    --> 116 ret = _retry_ntimes(
        117     settings.number_of_grpc_api_retries,
        118     self.dllapi.AedtAPI.InvokeAedtObjMethod,
        119     self.objectID,
        120     funcName,
        121     argv,
        122 )  # Call C function
        123 if ret and isinstance(ret, (AedtObjWrapper, AedtPropServer)):

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:607, in _retry_ntimes(n, function, *args, **kwargs)
        606 if "__name__" in dir(function):
    --> 607     raise AttributeError(f"Error in Executing Method {function.__name__}.")
        608 else:

    AttributeError: Error in Executing Method InvokeAedtObjMethod.

    During handling of the above exception, another exception occurred:

    GrpcApiError                              Traceback (most recent call last)
    File ~/Ansoft/Projects_HFSS/export_Hx_step01.py:78
        75         for z in z_vals:
        76             sample_points.append([x, y0, z])
    ---> 78     hfss.post.fields_calculator.export(
        79     # quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
        80     quantity="H",
        81     solution="Setup1 : LastAdaptive",
        82     variations=hfss.available_variations.nominal_values,
        83     output_file=str(script_dir / "Hx_L-0p5_pyaedt.fld"),
        84     intrinsics={"Freq": "9.4GHz", "Phase": "0deg"},
        85     sample_points=sample_points,
        86     export_with_sample_points=True,
        87     reference_coordinate_system="Global",
        88     export_in_si_system=False,
        89     is_vector=True,
        90     )
        92     # hfss.post.export_field_file_on_grid(
        93     # # quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
        94     # quantity="Hx",
    (...)    108 
        109 finally:
        110     if hfss:

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:236, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
        234 except GrpcApiError as e:
        235     _exception(sys.exc_info(), user_function, args, kwargs, "AEDT API Error")
    --> 236     return raise_exception_or_return_false(e)
        237 except BaseException as e:
        238     msg = str(sys.exc_info()[1])

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:208, in raise_exception_or_return_false(e)
        205         for v in list(_desktop_sessions.values())[:]:
        206             v.release_desktop(close_projects=v.close_on_exit, close_on_exit=v.close_on_exit)
    --> 208     raise e
        209 elif "__init__" in str(e):  # pragma: no cover
        210     return

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:221, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
        219 try:
        220     settings.time_tick = time.time()
    --> 221     out = user_function(*args, **kwargs)
        222     _log_method(user_function, args, kwargs)
        223     return out

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/visualization/post/fields_calculator.py:763, in FieldsCalculator.export(self, quantity, solution, variations, output_file, intrinsics, phase, sample_points, export_with_sample_points, reference_coordinate_system, export_in_si_system, export_field_in_reference, grid_type, grid_center, grid_start, grid_stop, grid_step, is_vector, assignment, objects_type)
        761         self.__app.logger.error("``sample_points`` can only be either a string or a list.")
        762         return False
    --> 763     output_file = self.__app.post.export_field_file(
        764         quantity=quantity,
        765         solution=solution,
        766         variations=variations,
        767         output_file=output_file,
        768         assignment=assignment,
        769         objects_type=objects_type,
        770         intrinsics=intrinsics,
        771         phase=phase,
        772         sample_points_file=sample_points_file,
        773         sample_points=sample_points,
        774         export_with_sample_points=export_with_sample_points,
        775         reference_coordinate_system=reference_coordinate_system,
        776         export_in_si_system=export_in_si_system,
        777         export_field_in_reference=export_field_in_reference,
        778     )
        779 elif grid_type:
        780     if grid_type not in ["Cartesian", "Cylindrical", "Spherical"]:

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:236, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
        234 except GrpcApiError as e:
        235     _exception(sys.exc_info(), user_function, args, kwargs, "AEDT API Error")
    --> 236     return raise_exception_or_return_false(e)
        237 except BaseException as e:
        238     msg = str(sys.exc_info()[1])

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:208, in raise_exception_or_return_false(e)
        205         for v in list(_desktop_sessions.values())[:]:
        206             v.release_desktop(close_projects=v.close_on_exit, close_on_exit=v.close_on_exit)
    --> 208     raise e
        209 elif "__init__" in str(e):  # pragma: no cover
        210     return

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/generic/general_methods.py:221, in _function_handler_wrapper.<locals>.wrapper(*args, **kwargs)
        219 try:
        220     settings.time_tick = time.time()
    --> 221     out = user_function(*args, **kwargs)
        222     _log_method(user_function, args, kwargs)
        223     return out

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/visualization/post/post_common_3d.py:908, in PostProcessor3D.export_field_file(self, quantity, solution, variations, output_file, assignment, objects_type, intrinsics, phase, sample_points_file, sample_points, export_with_sample_points, reference_coordinate_system, export_in_si_system, export_field_in_reference)
        896             f.write(" ".join([str(i) for i in point]) + "\n")
        897     export_options = [
        898         "NAME:ExportOption",
        899         "IncludePtInOutput:=",
    (...)    906         export_field_in_reference,
        907     ]
    --> 908     self.ofieldsreporter.ExportToFile(
        909         str(output_file),
        910         str(sample_points_file),
        911         solution,
        912         variation,
        913         export_options,
        914     )
        916 if Path(output_file).exists():
        917     return output_file

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:138, in AedtObjWrapper.__GetObjMethod__.<locals>.DynamicFunc(self, *args)
        137 def DynamicFunc(self, *args):
    --> 138     return self.__Invoke__(funcName, args)

    File ~/anaconda3/envs/AnsysEnv/lib/python3.12/site-packages/ansys/aedt/core/internal/grpc_plugin_dll_class.py:129, in AedtObjWrapper.__Invoke__(self, funcName, argv)
        127 pyaedt_logger.debug("Failed to execute gRPC AEDT command:")
        128 pyaedt_logger.debug(f"{funcName}({argv})")
    --> 129 raise GrpcApiError(f"Failed to execute gRPC AEDT command: {funcName}")

    GrpcApiError: Failed to execute gRPC AEDT command: ExportToFile
How to solve it?

#################################################################################################################################################################
2026-03-23

The temperature below which spontaneous magnetization may
occur in paramagnets may be estimated by equating the energy due to the
Lorentz field to the thermal energy kT, at temperature T_c, giving :
\T_c \approx (mu_s*M) / (3 * k) \approx (mu_B^'*M) / (3 * k)
assuming 4\pi*M=1e3 gauss
Explain me where this expression comes from


###
2026-03-25

I have this code to make a figure of 2x2 subplots:
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

            for w_value in unique_w_values:
                df_w = self.data[self.data[self.col_w] == w_value].copy()

                fig, axes = plt.subplots(2, 2, figsize=(8, 6), sharex=True)

                for h_value in sorted(df_w[self.col_h].unique()):
                    df_wh = df_w[df_w[self.col_h] == h_value].copy()
                    df_wh = df_wh.sort_values(by=self.col_freq)
                    if h_value < 0.2:
                        axes[0].plot(
                            df_wh[self.col_freq],
                            df_wh[self.col_s11],
                            label=f"h = {h_value} mm"
                        )
        
                        axes[2].plot(
                            df_wh[self.col_freq],
                            df_wh[self.col_s21],
                            label=f"h = {h_value} mm"
                        )
                    else:
                        axes[1].plot(
                            df_wh[self.col_freq],
                            df_wh[self.col_s11],
                            label=f"h = {h_value} mm"
                        )
        
                        axes[3].plot(
                            df_wh[self.col_freq],
                            df_wh[self.col_s21],
                            label=f"h = {h_value} mm"
                        )

                    axes[0].set_ylabel("dB(S11)")
                    axes[0].set_title(f"S-parameters for w = {w_value} mm")
                    axes[0].grid(True)
                    axes[0].legend()
                    axes[1].set_ylabel("dB(S11)")
                    axes[1].set_title(f"S-parameters for w = {w_value} mm")
                    axes[1].grid(True)
                    axes[1].legend()

                    axes[2].set_xlabel("Frequency [GHz]")
                    axes[2].set_ylabel("dB(S21)")
                    axes[2].grid(True)
                    axes[2].legend()
                    axes[3].set_xlabel("Frequency [GHz]")
                    axes[3].set_ylabel("dB(S21)")
                    axes[3].grid(True)
                    axes[3].legend()
                    
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
but I get this error, which I don't understand:
    AttributeError                            Traceback (most recent call last)
    Cell In[4], line 101
        99 csv_file = "simus.csv"
        100 plotter = HFSSPlotter(csv_file)
    --> 101 plotter.run()

    Cell In[4], line 95, in HFSSPlotter.run(self)
        93 self.check_columns()
        94 print("Columns checked")
    ---> 95 self.plot_for_each_w()

    Cell In[4], line 45, in HFSSPlotter.plot_for_each_w(self)
        43 df_wh = df_wh.sort_values(by=self.col_freq)
        44 if h_value < 0.2:
    ---> 45     axes[0].plot(
        46         df_wh[self.col_freq],
        47         df_wh[self.col_s11],
        48         label=f"h = {h_value} mm"
        49     )
        51     axes[2].plot(
        52         df_wh[self.col_freq],
        53         df_wh[self.col_s21],
        54         label=f"h = {h_value} mm"
        55     )
        56 else:

    AttributeError: 'numpy.ndarray' object has no attribute 'plot'


###########################################################################################################################################
2026-03-25

A certain scientific author defines this situation: there is a magnetic film of length 'l', thickness 'd', a,d width 'w'. A DC magnetic field 'H_0' and a small RF field 'H_{RF}' are applied along y (the plane of the film is x-y), which is in the width direction.
The corresponding complex resonant frequency is \omega_r^'=(\omega_0+j\alpha\omega)(\omega_m+\omega_0+j\alpha\omega) where \omega_0=2\pi\cdot 2.8\times 10^{6}\cdot H_0 is the precession frequency, \omega_m=2\pi\cdot 2.8\times 10^{6}\cdot 4\pi M_s, \alpha is the Gilbert damping parameter.
What is this factor 2\pi\cdot 2.8\times 10^{6} in the expressions of \omega_0 and \omega_m? Where does it come from?
He models the effective field H_{eff} in the magnetic film including the exchange field H_{ex} between spins:
H_{eff,x}=1/\omega_m\cdot (\omega_0 m_x + j\omega m_y ) - H_{ex,x}
H_{eff,y}=1/\omega_m\cdot (-\omega m_x + (\omega_0+\omega_m \sin(\theta)^2) m_y ) - H_{ex,y}
where m_x and m_y are the components of the magnetization vector M along x and y.
Where do these expressions for H_{eff} come from?
Moreover, the exchange field is defined as:
H_{ex,x}=\frac{2\lambda_{ex}}{a^2}\cdot (1-\cos(ka))m_x
H_{ex,y}=\frac{2\lambda_{ex}}{a^2}\cdot (1-\cos(ka))m_y
Similar question here, where do these expressions come from?

Explain me this:
There is a RLC periodic circuit with a thickness resolution 'd'. It can be studied using the ABCD matrix method:
    \cos(kd)=1-\frac{1}{2}\omega^2L_cC_m+\frac{L_c}{2L_m}

The film is excited by a microstrip line of width 'w' and length 'l' placed at a distance 's' from the film. The microstrip line carries an RF current 'I_{RF}' which generates the RF field 'H_{RF}' at the location of the film. The RF field can be approximated as H_{RF} = (I_{RF} / (2 * pi * s)) * exp(-j * k * l) where k is the wavenumber of the RF signal. The power absorbed by the magnetic film can be calculated using P_abs = (1/2) * Re{H_{RF} * M^*} where M is the complex magnetization of the film given by M = (M_s / (1 - j * alpha)) * (H_{RF} / (H_0 + H_{RF})).

#################################################################################################################
2026-03-26

For the Python code below, add a part that handles exceptions when dealing with my hfss file, so that the file is not deleted or corrupted:
    if __name__ == "__main__":

        projects_name = ["Microstrip_paramSweep_p1","Microstrip_paramSweep_p1_2","Microstrip_paramSweep_p2","Microstrip_paramSweep_p3"]
        h_lst = [[0.05,0.1], [0.05,0.1],[0.2,0.5],  [0.2,0.5]]
        w_lst = [[0.03,0.05],[0.2],     [0.03,0.05],[0.2]]
        L_lst = [4,4,6,6]
        design_name = "Design 1"

        
        for p_ix, pname in enumerate(projects_name):
            project_path = script_dir / f"{pname}.aedt"
            batchinfo_dir = script_dir / f"{pname}.aedt.batchinfo"  # Corrected path
            
            kill_hfss_processes_for_user()
            handle_lock_file(project_path)
            last_seen_file = None
            
            try:
                # Open HFSS and modify the offset parameter
                hfss = Hfss(
                    project=str(project_path),
                    version=aedt_version,
                    design=design_name,
                    non_graphical=non_graphical,
                    new_desktop=True,
                    close_on_exit=False,
                    solution_type="Modal",
                    remove_lock=True,
                )
                print("  project name:", pname)
                print("  design name:",  hfss.design_name)
                print("  design type:",  hfss.design_type)
                print("  solution type:", hfss.solution_type)
                print("  model units:", hfss.modeler.model_units)
                # print("  nominal variation:",hfss.available_variations.nominal_values)
                
                hw_values = [(wval, hval) for wval in w_lst[p_ix] for hval in h_lst[p_ix]]
                
                # Loop through each variation
                for hw in hw_values:
                    w, h = hw[0], hw[1]
                    eps_eff = effective_permittivity(eps_r, h, w)
                    wlen_g = c / f / np.sqrt(eps_eff) * 1e3 # mm
                    L = L_lst[p_ix]
                    phase = 2*np.pi/wlen_g*L/8 * 180/np.pi
                    
                    print(f"  L: {L:.3f}mm, w: {w:.3f}mm, h: {h:.3f}mm, phase: {phase:.3f}deg")
                    hfss.variable_manager.set_variable("w", expression=f"{w}mm")
                    hfss.variable_manager.set_variable("h", expression=f"{h}mm")
                    print("  w and h have been changed")
                            
                    results_fname = f"Hx_p{p_ix+1:1d}_L{L:.0f}_w{w:.2f}_h{h:.2f}_pyaedt.fld"
                    print(f"  Data will be saved in: {results_fname}")
                    
                    hfss.post.export_field_file_on_grid(
                    # quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
                    quantity="Hx",
                    solution="Setup1 : LastAdaptive",
                    variations=hfss.available_variations.nominal_values,
                    file_name=str(script_dir / results_fname),
                    grid_type="Cartesian",
                    grid_start=[-1/2*5*w, -3/8*L, -h/2],
                    grid_stop =[ 1/2*5*w, -3/8*L, 3/4*h],
                    grid_step=[5*w/1000, 0, h/800],
                    intrinsics={"Freq": "9.4GHz", "Phase": "0deg"},
                    is_vector=False,
                    export_in_si_system=True,
                    )
                    print("  Results exported")
            
            finally:
                if hfss:
                    print("  All simulations completed. GREAAAT JOB!!!!!!!!!!!!!\n")
                    hfss.release_desktop(close_projects=True, close_desktop=True)

I had this code to make a 2D plot:
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
            
            plt.figure(figsize=(8, 4))
            plt.pcolormesh(y_unique*1e3, z_unique*1e3, grid, shading="auto",cmap="RdBu",norm=norm)
            plt.colorbar(label="Re(Hx)")
            plt.xlabel("Y [mm]")
            plt.ylabel("Z [mm]")
            plt.title('Re($H_x$) (Oe), x=0')
            plt.tight_layout()
            plt.show()


    if __name__ == "__main__":
        plotter = HxMapPlotter("h_x_data3.txt")
        plotter.plot()

I want to do something similar. But now I want to plot the magnitude of Hx in the XZ plane, not in the YZ plane. Moreover, I have several files with names "Hx_p4_L6_wX.XX_hX.XX_pyaedt.fld" where X.XX corresponds to the values of w and h. For each w there are four files, each with a different h. I want to make one figure of 2x2 subplots for each w, where the 4 subplots correspond to the 4 different h values. Each subplot should be a color map of the magnitude of Hx in the XZ plane. A legend at each subplot should indicate the corresponding h value. The figure should have a common colorbar for all subplots, and the x and z axes should be labeled in mm. The title of each figure should indicate the corresponding w value. And a title for each figure should indicate the value of w. How can I do that? Keep the code simple and easy to understand

################################################################################################################
2026-03-27

Consider this text:
    For a ferrite sample of macroscopic size , the total number of unbalanced
    spins N would be very , very large so that N/2 >> 1. In this case , it is
    evident that \theta \approx 0. \theta is the angle between the resultant spin S and the applied field H_a. We conclude , therefore , that for a single electron (N = 1), the electron spin S makes an angle of 180 °-54.7 ° with the applied field direction, but as the number of spins N, that are coupled together
    increases, \theta decreases and finally approaches zero as N approaches infinity . Thus, in a sample of ferrite, the
    total quantum number S is so large that its macroscopic behavior may be treated by simple classical theory .
Tell me if it is fully correct from a physics point of view. Moreover, answer this question: why is it that if the total
quantum number S is very large, then, its macroscopic behaviour can be treated by simple classical theory?

Ok, I understand better, but I still have one question, I thought |S|=\sqrt{m_s(m_s+1)}\hbar, where m_s is one of the possible spin quantum numbers -s, -s+1,...,s. Therefore, for an electron with s=1/2 |S|=\frac{\sqrt{3}}{2}\hbar. I do not see how |S| can be so large, does it mean that when you have several electrons you sum up the |S| of each electron?

I have a text that says the following: \mathbf{\mu} (magnetic moment) and \mathbf{J}\hbar (total angular momentum which is the spin angular momentum in ferromagnets) are oppositely directed and their ratio \gamma is negative :
\gamma_e=|\frac{\mathbf{\mu}}{\mathbf{J}\hbar}
\gamma_e is known as the gyromagnetic ratio. From this equation it follows that:
\hbar\frac{d\mathbf{\J}}{dt} = 1/\gamma_e\frac{d\mathbf{\mu}}{dt}
I don't understand how the author gets rid off the || around \mu and J. You understand? Is ther something wrong?

In the book I'm reading regarding magnetization dynamics. They linearize the LLG equation an obtain the susceptibility tensor. Then they define two quantities that belong to this tensor: \chi and K which they express as \chi=\chi^'-j\chi^{''} and K=K^'-jK^{''}. They say that resonance occurs for the frequency of the external RF field that makes \chi^{''} and K^{''} maximum. Why is this? Does this represent a case where there is no damping?


########################################################################################################################
# 2026-03-30
This is the code I'm using to compute the gradient and plot it in a similar way as I was plotting Hx before
    import re
    from pathlib import Path

    import numpy as np
    import matplotlib.pyplot as plt


    def parse_filename(filepath):
        """
        Extract w and h from filenames like:
        Hx_p4_L6_w0.20_h0.50_pyaedt.fld
        """
        name = Path(filepath).name
        match = re.search(r"_w([0-9.]+)_h([0-9.]+)_pyaedt\.fld$", name)
        if not match:
            raise ValueError(f"Cannot read w and h from filename: {name}")
        w = float(match.group(1))
        h = float(match.group(2))
        return w, h


    def load_hx_file(filename):
        """
        Load numeric data from the file.
        Assumes:
        - line 1: metadata
        - line 2: column names
        - line 3 onward: numeric data

        Expected columns:
        x, y, z, Hx
        """
        return np.loadtxt(filename, skiprows=2)


    def build_xz_grid(data):
        """
        Build a 2D grid in the XZ plane using |Hx|.

        Assumes columns:
        data[:,0] -> x
        data[:,2] -> z
        data[:,3] -> Hx
        """
        x = data[:, 0]
        z = data[:, 2]
        hx = data[:, 3]

        hx_mag = np.abs(hx) * 4 * np.pi / 1000

        x_unique = np.unique(x)
        z_unique = np.unique(z)

        grid = np.full((len(z_unique), len(x_unique)), np.nan)

        x_index = {val: i for i, val in enumerate(x_unique)}
        z_index = {val: i for i, val in enumerate(z_unique)}

        for xi, zi, hi in zip(x, z, hx_mag):
            grid[z_index[zi], x_index[xi]] = hi

        return x_unique, z_unique, grid


    def compute_gradient_safe(x_unique, z_unique, grid):
        """
        Compute gradient of the scalar field grid robustly.

        Returns:
            dHx_dx, dHx_dz, grad_mag
        """

        # --- Ensure strictly increasing coordinates (avoid zero spacing)
        dx = np.diff(x_unique)
        dz = np.diff(z_unique)

        if np.any(dx == 0) or np.any(dz == 0):
            raise ValueError("Duplicate coordinates detected → zero spacing in grid.")

        # Use mean spacing (more stable if nearly uniform grid)
        dx_mean = np.mean(dx)
        dz_mean = np.mean(dz)

        # --- Handle NaNs in grid (avoid propagation issues)
        grid_clean = np.nan_to_num(grid, nan=0.0)

        # --- Compute gradients safely
        with np.errstate(divide='ignore', invalid='ignore'):
            dHx_dz, dHx_dx = np.gradient(grid_clean, dz_mean, dx_mean)

        # --- Restore NaN mask (optional but recommended)
        nan_mask = np.isnan(grid)
        dHx_dx[nan_mask] = np.nan
        dHx_dz[nan_mask] = np.nan

        # --- Gradient magnitude
        grad_mag = np.sqrt(dHx_dx**2 + dHx_dz**2)

        return dHx_dx, dHx_dz, grad_mag

        
    def plot_all_by_w(folder=".",figname_prefix=""):
        folder = Path(folder)
        files = sorted(folder.glob("Hx_*_w*_h*_pyaedt.fld"))

        if not files:
            print("No matching files found.")
            return

        # Group files by w
        files_by_w = {}
        for f in files:
            w, h = parse_filename(f)
            files_by_w.setdefault(w, []).append((h, f))

        # ------------------------------------------------------------------
        # FIRST PASS: load everything and compute one global color scale
        # ------------------------------------------------------------------
        all_datasets_by_w = {}
        all_grads_by_w = {}
        
        global_vmin = np.inf
        global_vmax = -np.inf
        global_vmax_grad = -np.inf

        for w, h_files in sorted(files_by_w.items()):
            h_files = sorted(h_files, key=lambda t: t[0])

            datasets, grads = [], []
            for h, f in h_files:
                data = load_hx_file(f)
                x_unique, z_unique, grid = build_xz_grid(data)

                dHx_dx, dHx_dz, grad_mag = compute_gradient(x_unique, z_unique, grid)
                
                local_min = np.nanmin(grid)
                local_max = np.nanmax(grid)

                global_vmin = min(global_vmin, local_min)
                global_vmax = max(global_vmax, local_max)
                global_vmax_grad = max(global_vmax_grad, np.nanmax(grad_mag))
                
                datasets.append((h, x_unique, z_unique, grid))
                grads.append((h, x_unique, z_unique, grad_mag))
                
            all_datasets_by_w[w] = datasets
            all_grads_by_w[w] = grads

        # Since you are plotting |Hx|, forcing vmin=0 often makes sense
        global_vmin = 0.0

        print(f"Global Hx color scale: vmin = {global_vmin}, vmax = {global_vmax}")
        print(f"Global grad Hx color scale: vmin = {global_vmin}, vmax = {global_vmax_grad}")

        # ------------------------------------------------------------------
        # SECOND PASS: plot each figure using the same vmin/vmax
        # ------------------------------------------------------------------
        for w, grads in sorted(all_grads_by_w.items()):
            fig2, axes2 = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=True)
            axes2 = axes2.ravel()
            
            mappable = None

            for i, (ax, (h, x_unique, z_unique, grad_mag)) in enumerate(zip(axes2, grads)):
                pcm = ax.pcolormesh(
                    x_unique * 1e3,   # m -> mm
                    z_unique * 1e3,   # m -> mm
                    grad_mag,
                    shading="auto",
                    cmap="rainbow",
                    vmin=global_vmin,
                    vmax=global_vmax_grad
                )
                mappable = pcm

                ax.set_title(f"h = {h:.2f} mm", fontsize=17)
                if i >= 2:
                    ax.set_xlabel("X [mm]", fontsize=17)
                if (i==0) | (i==2):
                    ax.set_ylabel("Z [mm]",fontsize=17)
                ax.tick_params(axis='both', labelsize=15)
                
            # Hide unused axes if fewer than 4 files
            for ax in axes2[len(grads):]:
                ax.axis("off")

            fig2.suptitle(f"\\nabla|Hx| in XZ plane, w = {w:.2f} mm")

            cbar2 = fig2.colorbar(mappable, ax=axes2, shrink=0.9)
            cbar2.set_label("$\\nabla$|Hx| (Oe)", fontsize=17)
            cbar2.ax.tick_params(labelsize=15)
            figname = figname_prefix+f"_w{w:.2f}.png"
            plt.savefig(figname,dpi=300)
            plt.show()

    if __name__ == "__main__":
        plot_all_by_w(".","Hx_gradient_shared cbar")

but I get this error:
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[16], line 197
        194         plt.show()
        196 if __name__ == "__main__":
    --> 197     plot_all_by_w(".","Hx_gradient_shared cbar")

    Cell In[16], line 134, in plot_all_by_w(folder, figname_prefix)
        131 data = load_hx_file(f)
        132 x_unique, z_unique, grid = build_xz_grid(data)
    --> 134 dHx_dx, dHx_dz, grad_mag = compute_gradient(x_unique, z_unique, grid)
        136 local_min = np.nanmin(grid)
        137 local_max = np.nanmax(grid)

    TypeError: cannot unpack non-iterable NoneType object
Help me solve this