#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:32:25 2026

@author: ibarragom

script for extracting Hx from HFSS results
- Modify the 'offset' parameter between 0.1 and 1.3 inches.
- Launch simulations on a remote compute node.
- Export S-parameters to CSV files for each 'offset' value.
"""

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
project_name = "Project3_Microstrip_param_sweep_copy"
project_path = script_dir / f"{project_name}.aedt"
batchinfo_dir = script_dir / f"{project_name}.aedt.batchinfo"  # Corrected path
result_folder = script_dir / "results"
result_folder.mkdir(exist_ok=True)  # Create results folder if it doesn't exist

hfss = None

units = 1e-0
w, h = 0.05*units, 0.05*units
w_subs, L = 10*w, 2*units

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

        # hfss.post.fields_calculator.export(
        # # quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
        # quantity="Mag_H",
        # solution="Setup1 : LastAdaptive",
        # variations=hfss.available_variations.nominal_values,
        # output_file=str(script_dir / "Hx_L-0p5_pyaedt.fld"),
        # intrinsics={"Freq": "9.4GHz", "Phase": "0deg"},
        # sample_points=sample_points,
        # export_with_sample_points=True,
        # reference_coordinate_system="Global",
        # export_in_si_system=False,
        # is_vector=True,
        # )
        
        hfss.post.export_field_file_on_grid(
        # quantity="ScalarXAtPhase(Phase, Smooth(<Hx,Hy,Hz>))",
        quantity="Hx",
        solution="Setup1 : LastAdaptive",
        variations=hfss.available_variations.nominal_values,
        file_name=str(script_dir / "Hx_L-0p5_pyaedt.fld"),
        grid_type="Cartesian",
        grid_start=[-w_subs/2, -L/4, -h/2],
        grid_stop =[ w_subs/2, -L/4, 3/4*h],
        grid_step=[w_subs/500, 0, h/400],
        intrinsics={"Freq": "9.4GHz", "Phase": "0deg"},
        is_vector=True,
        export_in_si_system=True,
        )
    
    finally:
        if hfss:
            print("All simulations completed. GREAAAT JOB!!!!!!!!!!!!!")
            hfss.release_desktop(close_projects=True, close_desktop=True)

    