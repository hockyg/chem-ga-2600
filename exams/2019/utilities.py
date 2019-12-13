def get_data(top_file="data/tip3_125_opt.data",trj_file="data/water_tip3_200ps_every200fs_unwrap_nve.dcd",
             vel_file="data/water_tip3_5ps_every20fs_nve.vel.lammpstrj", dtx=.2, dtv=0.05):
    #note, time step in ps
    import numpy as np
    import MDAnalysis as md
    u_trj = md.Universe(top_file,format="DATA")
    u_trj.load_new(trj_file,format="DCD")
    xyz_trajectory = np.array([u_trj.trajectory[i][:] for i in range(len(u_trj.trajectory))])
    
    u_vel = md.Universe(top_file,format="DATA")
    u_vel.load_new(vel_file,format="LAMMPSDUMP")
    box_lengths = (u_vel.trajectory[0].dimensions[:3])
    #for some reason, have to rescale by box size in this format to get what's printed in file
    vel_trajectory = np.array([np.copy(u_vel.trajectory[i].positions)/box_lengths for i in range(len(u_vel.trajectory))])
    #convert to A/ps from A/fs
    vel_trajectory = vel_trajectory*1000
    
    tx = np.arange(len(xyz_trajectory))*dtx
    tv = np.arange(len(vel_trajectory))*dtv
    return xyz_trajectory, vel_trajectory, tx, tv
