#!/bin/sh

jupyter nbconvert --output-dir='./html' --template my_template.tpl --to html notebooks/doppler_radar.ipynb

jupyter nbconvert --output-dir='./html' --template my_template.tpl --to html notebooks/fmcw_radar.ipynb

jupyter nbconvert --output-dir='./html' --template my_template.tpl --to html notebooks/fmcw_reflector_raytracing.ipynb

jupyter nbconvert --output-dir='./html' --template my_template.tpl --to html notebooks/lidar.ipynb

jupyter nbconvert --output-dir='./html' --template my_template.tpl --to html notebooks/multi_path_raytracing.ipynb

jupyter nbconvert --output-dir='./html' --template my_template.tpl --to html notebooks/pmcw_radar.ipynb

jupyter nbconvert --output-dir='./html' --template my_template.tpl --to html notebooks/rcs_raytracing.ipynb

jupyter nbconvert --output-dir='./html' --template my_template.tpl --to html notebooks/roc.ipynb

jupyter nbconvert --output-dir='./html' --template my_template.tpl --to html notebooks/tdm_mimo_fmcw_radar.ipynb