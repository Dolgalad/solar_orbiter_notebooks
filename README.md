# Solar Orbiter Jupyter notebooks

Collection of Jupyter notebooks manipulating data from the Solar Orbiter mission. Data retrieval from `AMDA` using `speasy`.

## Requirements
Make sure you install the requirements: 
```bash
python -m pip install -r requirements.txt
```

## EPD/HET instrument
`solo_epd.ipynb` : Plotting Solar Orbiter EPD/HET electron and proton flux data.

![Electron flux](/img/eflux_ts.png)

![Proton flux](/img/hflux_spectro.png)

## Alfvenic Slow Solar Wind
`alfvenic_slow_solar_wind.ipynb`: Multiscale views of an Alfvenic slow solar wind: 3D velocity distribution functions observed by the Proton-Alpha Sensor of Solar Orbiter.

![PAS L2](/img/pas_l2_spectro.png)
