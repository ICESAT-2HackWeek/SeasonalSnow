#!/usr/bin/env python

import argparse
import h5py
from pathlib import PurePath

# Script to convert downloaded IceSat-2 granules to digest per beam into a PDAL pipeline
# utilizing the signal_conf_ph photon flag over land surfaces.

BEAM_CHOICES=[
    'gt1r',
    'gt1l',
    'gt2r',
    'gt2l',
    'gt3r',
    'gt3l',
]

def input_data(file, beam):
    with h5py.File(file, "r") as fi:
        x = fi[f"./{beam}/heights/lon_ph"][:]
        y = fi[f"./{beam}/heights/lat_ph"][:]
        z = fi[f"./{beam}/heights/h_ph"][:]
        conf = fi[f"./{beam}/heights/signal_conf_ph"][:, 0]

        return x, y, z, conf


def convert_hdf_columns(file, beam):
    (X, Y, Z, conf) = input_data(file, beam)
    input_file = PurePath(file)
    output_file = input_file.parent / (input_file.stem + '_xyz_conf.h5')
    with h5py.File(output_file, 'w') as f:
        f['X'] = X  # write data
        f['Y'] = Y
        f['Z'] = Z
        f['conf'] = conf


def arguments():
    parser = argparse.ArgumentParser("Script to setup HDF file conversion")
    parser.add_argument(
        '--input-file', type=str, required=True, help="Path to input file"
    )
    parser.add_argument(
        '--beam', type=str, choices=BEAM_CHOICES, default=BEAM_CHOICES[0]
    )
    return parser.parse_args()


if __name__ == '__main__':
    arguments = arguments()

    convert_hdf_columns(arguments.input_file, arguments.beam)
