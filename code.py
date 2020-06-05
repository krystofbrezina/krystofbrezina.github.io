if type(trajectories) == list:
    l = trajectories
elif type(trajectories) == str:
    l = sorted(glob(trajectories))
else:
    raise TypeError('Unsupported type of entry.')

for i, name in enumerate(l):
    if verbose:
        print('Adding trajectory {:s} ............ {:d}/{:d}'.format(name, (i + 1), len(l)))

    tmp_traj = md.load(name, top=top)[:n_frames]

    if i == 0:
        traj = tmp_traj
    else:
        traj += tmp_traj

