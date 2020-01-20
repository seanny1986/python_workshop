import numpy as np
from math import sin, cos, tan, sqrt

class Quadrotor:
    """
        6DOF rigid body, non-linear EOM solver for a '+' configuration quadrotor. Aircraft is modeled
        with an East-North-Up axis system for convenience when plotting. This means thrust is positive
        in the body-axis z-direction, and the gravity vector is negative in the inertial axis 
        z-direction. The aircraft comes with a config file that includes the necessary parameters. For
        a description of what each parameter means, please check this file.

        I've chosen a representation for the rotation matrices that makes it easy to see what I'm doing;
        it shouldn't have a huge impact on performance since we don't have much in the way of graphics.
        For an 'x' config quadrotor, calculate thrust and moments due to the motors as normal, and then 
        rotate these vectors by pi/4 around the body z-axis. Thrust should be unaffected, but the moments
        will be, since the moment arm to the COM will change.

        You can also use this sim for standard fixed-wing aircraft or rockets by implementing new force
        and torque methods. For example, for a fixed wing, you could implement a strip theory aerodynamics 
        solver to get lift and drag in the body frame, VLM, or a linearized method. For a rocket you would 
        use standard rocket thrust equations, and update the mass of the vehicle (which has its own ODE 
        and is included in the state space). Quaternion rotations are probably better for rockets though,
        since the rotation matrices have a singularity at pitch +-90 degrees.

        -- Sean Morrison, 2018
    """
    
    def __init__(self, params):
        self.mass = params["mass"]
        self.prop_radius = params["prop_radius"]
        self.n_motors = params["n_motors"]
        self.hov_p = params["hov_p"]
        self.l = params["l"]
        self.Jxx = params["Jxx"]
        self.Jyy = params["Jyy"]
        self.Jzz = params["Jzz"]
        self.kt = params["kt"]
        self.kq = params["kq"]
        self.kd = params["kd"]
        self.km = params["km"]
        self.g = params["g"]
        self.dt = params["dt"]
	
        print("Params loaded:")
        print(params)

        self.J = np.array([[self.Jxx,   0.,         0.],
                            [0.,    self.Jyy,       0.],
                            [0.,        0.,     self.Jzz]])
        self.xyz = np.array([[0.],
                            [0.],
                            [0.]])
        self.zeta = np.array([[0.],
                            [0.],
                            [0.]])
        self.uvw = np.array([[0.],
                            [0.],
                            [0.]])
        self.pqr = np.array([[0.],
                            [0.],
                            [0.]])
        self.G = np.array([[0.],
                            [0.],
                            [-self.g]])
        self.rpm = np.array([0.0, 0., 0., 0.])

        self.u_to_rpm = np.linalg.inv(np.array([[self.kt, self.kt, self.kt, self.kt],
                                                [0., self.l*self.kt, 0., -self.l*self.kt],
                                                [-self.l*self.kt, 0., self.l*self.kt, 0.],
                                                [-self.kq, self.kq, -self.kq, self.kq]]))

        # important physical limits
        self.hov_rpm = sqrt((self.mass*self.g)/self.n_motors/self.kt)
        self.max_rpm = sqrt(1./self.hov_p)*self.hov_rpm
        self.max_thrust = self.kt*self.max_rpm**2
        self.terminal_velocity = sqrt((self.max_thrust+self.mass*self.g)/self.kd)
        self.terminal_rotation = sqrt(self.l*self.max_thrust/self.km)

    def set_state(self, xyz, zeta, uvw, pqr):
        """
            Sets the state space of our vehicle
        """

        self.xyz = xyz.copy()
        self.zeta = zeta.copy()
        self. uvw = uvw.copy()
        self.pqr = pqr.copy()
    
    def get_state(self):
        """
            Returns the current state space
        """
        return self.xyz, self.zeta, self.uvw, self.pqr
    
    def reset(self):
        """
            Resets the initial state of the quadrotor
        """

        self.xyz = np.array([[0.],
                            [0.],
                            [0.]])
        self.zeta = np.array([[0.],
                            [0.],
                            [0.]])
        self.uvw = np.array([[0.],
                            [0.],
                            [0.]])
        self.pqr = np.array([[0.],
                            [0.],
                            [0.]]) 
        self.rpm = np.array([0., 0., 0., 0.])
        return self.get_state()

    def R1(self, zeta):
        """
            Rotation matrix converting body frame linear values to the inertial frame.
            This matrix is orthonormal, so to go from the inertial frame to the body
            frame, we can take the transpose of this matrix. That is, R1^-1 = R1^T.
            These rotations are for an East-North-Up axis system, since matplotlib 
            uses this for plotting. If you wanted to use N-E-D as is more typical in
            aerospace, you would need two additional rotation matrices for plotting -- 
            a pi/2 rotation about the inertial z-axis, and then another pi/2 rotation 
            about the inertial x-axis.
        """
        
        # Implement the code that returns the rotation matrix here. You should break zeta
        # into its constituent elements, and then create the numpy arrays Rx, Ry, Rz. From
        # there, you can return Rz.dot(Ry.dot(Rx))
        return
 

    def R2(self, zeta):
        """
            Euler rates rotation matrix converting body frame angular velocities 
            to the inertial frame. This uses the East-North-Up axis convention, so 
            it looks a bit different to the rates matrix in most aircraft dynamics
            textbooks (which use an N-E-D system).
        """
        
        # Implement the code that return the Euler rates matrix here. You should break zeta
        # into theta and psi (since phi isn’t used) and then create a numpy array as in Eq. 10
        # in the handout. Return this matrix.
        return
    

    def aero_forces(self, uvw):
        """
            Calculates drag in the body xyz axis (E-N-U) due to linear velocity
        """
      
        norm = np.linalg.norm(uvw)
        if norm == 0:						# we don’t want to divide by zero
            return np.array([[0.],
                            [0.],
                            [0.]])
        else:
            unit_vector = uvw/norm
            return -(self.kd*norm**2)*unit_vector
        

    def aero_moments(self, pqr):
        """
            Models aero moments about the body xyz axis (E-N-U) as a function of angular velocity
        """
        
        # Implement the function that calculates aerodynamic moments here. You should use the aero_forces
        # function as a template.
        return
        

    def thrust_forces(self, rpm):
        """
            Calculates thrust forces in the body xyz axis (E-N-U)
        """
        # Implement the function that calculates thrust forces here. You should refer to your notes.
        # The thrust force equation is given in Eq. 5
        return


    def thrust_moments(self, rpm):
        """
            Calculates moments about the body xyz axis due to motor thrust and torque
        """
        # Implement the function that calculates thrust moments here. You should refer to your notes.
        # The thrust moment equation is given in Eq. 6
        return

        
    def step(self, rpm):
        """
            Semi-implicit Euler update of the non-linear equations of motion. Uses the
            matrix form since it's much nicer to work with. Our state space equations 
            are:
            
            v_dot = F_b/m + R1^{-1}G_i - omega x v
            omega_dot = J^{-1}[Q_b - omega x H]
            x_dot = R1*v
            zeta_dot = R2*omega

            Where F_b are the external body forces (thrust+drag) in the body frame, m 
            is the mass of the vehicle, R1^{-1} is the inverse of matrix R1 (since R1
            rotates the body frame to the inertial frame, the inverse rotates the inertial
            to the body frame), G_i is the gravity vector in the inertial frame (0,0,-9.81),
            omega is the angular velocity, v is the velocity, J is the inertia matrix,
            Q_b are the external moments about the body axes system (motor thrust, motor
            torque, and aerodynamic moments), and H is the angular momentum J*omega. I 
            assume J is a diagonal matrix here; that is, the aircraft is symmetrical about 
            the body x and y axes.
            
            Since R1 is an orthornormal matrix:

            R1^{-1} = R1^{T}

            This is not true for the Euler rates matrix R2, so we need to invert it the old
            fashioned way.

            I step the EOMs forward under the assumption that:

            x_{t+1} ~ x_{t}+h*x_dot_{t}

            Where h is the time step. This update is semi-implicit since it updates linear 
            and angular velocities using a forward Euler step, and then updates position and
            attitude using v_{t+1} and omega_{t+1} (as opposed to using v_{t} and omega_{t}).
        """

        rpm = np.clip(rpm, 0., self.max_rpm) 		# clip our RPM to a maximum value
        r1 = self.R1(self.zeta)				# calc Euler rotation matrix
        r2 = self.R2(self.zeta)				# calc Euler rates matrix
        fm = self.thrust_forces(rpm)			# calc thrust force
        tm = self.thrust_moments(rpm)			# calc thrust moment
        fa = self.aero_forces(self.uvw)			# calc aerodynamic force
        ta = self.aero_moments(self.pqr)		# calc aerodynamic moment
        H = self.J.dot(self.pqr)			# calc angular momentum vector
	
        # Implement uvw_dot and pqr_dot equations here. When using cross products in numpy, you
        # will need to specify axis=0 since we are working with column vectors (3x1). Remember,
        # you can rotate the gravity vector into the body frame using the transpose of r1, which
        # is r1.T in numpy (i.e. g_b = r1.T.dot(self.G))
         
        uvw_dot = None
        pqr_dot = None	

        self.uvw += uvw_dot*self.dt			# step linear vels forward by one timestep
        self.pqr += pqr_dot*self.dt			# step angular vels forward by one timestep

        # Implement xyz_dot and zeta_dot equations here. These are specified in the handout in Eqs.
        # 3 & 4. If you’ve already completed the body accelerations task, you can use the same method
        # here to rotate from the body frame to the inertial frame (i.e. r1.dot(uvw)).        
            
        xyz_dot = None
        zeta_dot = None

        self.xyz += xyz_dot*self.dt
        self.zeta += zeta_dot*self.dt
        return self.xyz, self.zeta, self.uvw, self.pqr