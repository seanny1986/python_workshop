"""
        Config file for the aircraft. We define the following parameters:
        
        mass = the mass of the vehicle in kg
        prop_radius = the radius of the propellers in meters (this is cosmetic only, no momentum theory)
        n_motors = number of motors on the vehicle
        hov_p = the % max thrust at which we hover. Typically 50%
        l = the length between the centre of mass and the centre of the prop disk (i.e. arm length)
        Jxx = the mass moment of inertia about the x-axis (roll)
        Jyy = the mass moment of inertia about the y-axis (pitch)
        Jzz = the mass moment of inertia about the z-axis (yaw)
        kt = motor thrust coefficient
        kq = motor torque coefficient
        kd = aerodynamic drag coefficient
        km = aerodynamic moment coefficient
        g = gravitational acceleration (positive in config, corrected in simulated)
        dt = solver time step
    """

# Implement a dictionary here containing the parameters for the simulation. You can find the parameter
# values in Table 1 of the handout. If you’re unsure of how to implement a dictionary, refer to the
# workshop slides and the cheatsheet (hint: dictionary = {“name1”: value1, “name2”: value2, … “nameN”: valueN}).
# the name of the dictionary should be params.

params = None
