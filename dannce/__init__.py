# Default parameters, which can be superseded by CL arguments or
# config files
_param_defaults_shared = {"immode": 'vid',
                          "verbose": 1,
                          "gpuID": "0",
                          "loss": 'mask_nan_keep_loss',
                          "start_batch": 0,
                          "viddir": "videos"}
_param_defaults_dannce = {"metric": ['euclidean_distance_3D'],
                          "sigma": 10,
                          "lr": 1e-3,
                          "n_layers_locked": 2,
                          "interp": 'nearest',
                          "depth": False,
                          "rotate": True,
                          "predict_mode": 'torch',
                          "comthresh": 0,
                          "weighted": False,
                          "com_method": 'median',
                          "channel_combo": 'None',
                          "new_last_kernel_size": [3, 3, 3],
                          "n_channels_out": 20,
                          "cthresh": 350,
                          "medfilt_window": None,
                          "com_fromlabels": False}
_param_defaults_com = {"dsmode": 'nn',
                       "sigma": 30,
                       "debug": False,
                       "lr": 5e-5,
                       "net": 'unet2d_fullbn',
                       "n_channels_out": 1,
                       "augment_hue": False,
                       "augment_brightness": False,
                       "augment_rotation": False,
                       "augment_translation": False}