---
title: "How Big of a Solar Panel Do You Need to Power the World"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2025-09-05 07:15:35 -0600
categories: [Blog, TODO]    # <=2 values here: top category and sub category
tags: [todo]                # TAG names should always be lowercase
layout: post                # post is the default, we will set it to be explicit
pin: false
toc: true                   # Table of contents
comments: true              # Enable/disable comments at the bottom of the post
math: true                 # Disabled by default for performance reasons
mermaid: false              # Diagram generation tool via ```mermaid [...]```
#img_cdn: https://cdn.com
#media_subpath: /img/path/
#image:
#   path: /path/to/image.jpg
#   width: 1200   # in pixels
#   height: 630   # in pixels, 1.90:1 desired by chirpy
#   alt: image alternative text
#   show_image_in_post: false
#description:               # A short sentence to describe the article, used when sharing links on social media and on homepage
---

## TODO: Add Heading Here
TODO: Add text here


Via [ourworldindata.org](https://ourworldindata.org/energy-production-consumption), we currently (2024) consume 186,383TWh of energy per year. This includes energy from coal, oil, natural gas, renewables, everything. The big assumption for this post is assuming everything is powered by *electricity*. So instead of using oil for jet fuel, let's use its equivalent energy content in electricity. Granted, currently, if we did this, we don't have the technology to store that much electricity at a weight that will allow a plane to fly... but let's *assume* we did...
We also need to assume we can store / transmit this energy to whoever wants to use it, wherever they are. If we have one big solar panel, it's only going to get sun for half the day. The other half of the day, we won't be generating any electricity. We will also need to run transmission lines around the world and (not currently possible) assume they have very minimal losses.

But this is just meant to be a number crunching calculation.

186,383TWh of energy per year is 510.64TWh per day. That's what we need our solar panels to generate.

How much electricity does a panel generate? Well, it depends where you live. [globalsolaratlas.info](https://globalsolaratlas.info/map?c=43.55651,-100.437012,6&s=40.722283,-79.266357&m=site) has a fantastic site that will give you an approximate answer. Their `PVOUT` map will tell you how much energy (kWh) a 1kWp (killowatt-peak) panel that has optimized tilt, orientation, and is 100% efficient will generate to the end user. For example, in Denver, CO that number is ~4.7kWh/kWp per day. `PVOUT` takes the `GTI_opta` (global optimally tiltled irradiance) but also adds on some solar-specific losses, such as temperature (solar panels are less efficient at higher temperatures), inverter efficiency (solar panels generate direct current [AC], our power grid is alternating current [AC]), wiring losses, etc.

["Besides for solar radiation, air temperature and consequently the temperature of PV modules, have the most relevance for the solar electricity simulation. In addition, wind speed, wind direction, relative humidity, and other parameters are also important"](https://globalsolaratlas.info/support/methodology)

Defining some terms:
* `DNI` $kWh/m^2$ (direct normal irradiance) = the amount of solar radiation coming directly from the sun measured on a surface that is **always** perpendicular to the sun's rays. Clear day --> high value. Cloudy day --> low value.
* `DIF`  $kWh/m^2$(Diffuse Horizontal Irradiance) = the amount of solar radiation received on a horizontal surface excluding the direct beam from the sun. In other words, it's scattered sunlight only.
* `GHI`  $kWh/m^2$(global horizontal irradiation) = the solar energy falling on a horizontal surface at ground level.
* `GTI` $kWh/m^2$ (global tilted irradiance) = the total solar irradiance (direct + diffuse + ground-reflected) falling on a tilted surface.
* `PVOUT` $kWh/kW_{peak}$ (solar panel output) = how much energy a 1kWp (killowatt-peak) panel that has optimized tolt, orientation, and is 100% efficient will generate for the end user. Includes efficiency losses from temperature, inverter, wiring, etc.

Notice that `PVOUT` does not define any area. We can note that `efficiency = kWp / m^2`. Therefore, a 100% efficient panel will generate `1kWp/m^2` and `kWp = efficiency * m^2`. Thus, `PVOUT = kWh/kWp` and `PVOUT * efficiency = (kWh/kWp) * (kWp / m^2) = kWh/m^2`.


$$
\begin{equation}
    \text{Solar panel efficiency} = {\text{Panel's output in watts} \over \text{Panel's area in m}^2 \times \text{irradiance in W/m}^2}
\end{equation}
$$

Let $\eta\ =$ solar panel efficiency, $P =$ panels output in watts, $A=$ panel's area in $m^2$, $G_{STC}=$ irradiance in $W/m^2$ at **s**tandard **t**est **c**onditions:

<!--
> Normally, power (panel's output) is represented by $P$, but we are representing it as $W$ to simplify the resulting equation.
{ : .prompt-info }
-->

$$
\begin{equation}
    \eta = {P \over A \times G_{STC}}
\end{equation}
$$

Rearranging:
$$
\begin{equation}
    {P \over A} = {\eta \times {G_{STC}}}
\end{equation}
$$

Standard test conditions are $1000W/m^2$:

$$
\begin{equation}
    {P \over A} = {\eta \times {1000W/m^2}}
\end{equation}
$$

Let's substitute the units in for these variables. $P$ is measured in watts, $A$ is measured in $m^2$:
$$
\begin{equation}
    {W \over m^2} = {\eta \times {1000W/m^2}}
\end{equation}
$$

$1000W = 1kW$. Let's convert from $W$ to $kW_{peak}$ by multiplying both sides by $kW_{peak}/1000W$
$$
\begin{equation}
    {kW_{peak} \over 1000W} \times {W \over m^2} = {\eta \times {1000W/m^2}} \times {kW_{peak} \over 1000W}
\end{equation}
$$

$$
\begin{equation}
    {kW_{peak} \over 1000W} \times {W \over m^2} = {\eta \times {1/m^2}} \times {kW_{peak}}
\end{equation}
$$

$$
\begin{equation}
    {kW_{peak} \over 1000W} \times {W \over m^2} = {\eta \times kW_{peak} / m^2}
\end{equation}
$$









For standard test conditions, let's assume the irradiance $= G_{STC} = 1000W/m^2 = 1kW/m^2$.

$$
\begin{equation}
    \eta = {\text{Panel's output in watts} \over \text{Panel's area in m}^2 \times 1kW/m^2}
\end{equation}
$$

Let's assume we have a 100% efficient panel. If that is true, then we will have `Panel's output in watts = irradiance in W`, and they will cancel each other out. For simplicity, we can substitute in $1kW$:

$$
\begin{equation}
    1 = {1kW \over \text{Panel's area in m}^2 \times 1kW/m^2 }
\end{equation}
$$

Solving for the panel's area:

$$
\begin{equation}
    \text{Panel's area in m}^2 = {1kW \over 1kW/m^2} = 1m^2
\end{equation}
$$



How big of a panel do we need for 1kWp? 1kWp requires area 1/Mu (m^2) where Mu = your panel efficiency.
(citation needed, got from chatGPT)

Thus, we can expect ~4.7kWh/kWp = ~4.7kWh/(1/Mu) (m^2) = ~4.7kWh * Mu energy generated by 1 square meter of solar panel.

Unfortunately, our solar panels are currently ~20% efficient. This means, we can expect ~4.7kWh * .2 = 0.94kWh/m^2 of solar panel in Denver.

We now know how much energy we need and how much land we need to create electricity. Let's combine them!

510.64TWh / (0.94kWh/m^2) = 510.64*10^9kWh / (0.94kWh/m^2) = 543,000,000km^2 = 209,000mi^2

Unfortunately, this is much bigger than the size of Denver.

This is more along the size of North Dakota (70,698 mi^2), South Dakota (77,116 mi^2), and Nebraska (77,348 mi^2) combined (225,162 mi^2)

But if we want to put the solar panel there, we will need to adjust our kWh/kWp figure as those states might have more clouds which means less solar radiation, etc. Southwestern Nebraska looks to be about ~4.6kWh/kWp with northeast North Dakota around ~4.0kWh/kWp. Let's take a SWAG and say that area averages to ~4.3kWh/kWp. Running our equation again:

510.64Twh / (4.3kWh/kWp * 20% efficiency) = 593,000km^2 = 229,000mi^2

This number is very close (98.3%) to the area provided by North Dakota + South Dakota + Nebraska.

So there's your answer! If the whole world ran off of electricity, you could power the whole world with a solar panel as big as 3 US states.
The US is ~3.8million mi^2. So this would be 6% of the US's land area... to power the whole world.

Crazy! Lots of solar power out there for the taking. Hopefully we start to [grab more of it](https://ourworldindata.org/grapher/installed-solar-pv-capacity?country=CHN~IND~ESP~BRA~MEX~CHL~USA~OWID_EU27~OWID_ASI).





https://www.youtube.com/watch?v=v2IVTM0N2SE
US needs 4M GWh/yr = 0.010958M GWh/day = 10.958k GWh/day = 10958GWh/day = 11TWh/day
2.8Acres = 0.0113km^2 = 11331m^2 gives 1GWh/yr = 1000MWh/yr = 2.74 MWh/day
2.74MWh/day / 11331m^2 = 248Wh/day/m^2
Thus, US needs 11.2M Acres for 4M GWh/yr



https://poweroutage.us/solar/co/denver#:~:text=Installing%20a%205%20kW%20solar,%243.59%20per%20watt%20for%20installation
6.69m^2 = 1kW system = 1683kWh/yr = 4.611kWh/day
1kW/6.69m^2 = 150W/m^2 = 689Wh/day


https://a1solarstore.com/gstar-400w-solar-panel-108-cell-black-bifacial-gsp7g54m-h-wholesale-36-panels-per-pallet.html?srsltid=AfmBOoq87WE15TojscjkH0jQ4UX5OsMCuaYh8DGfvnPNscY7Uoqn76Vd7l0
400W panel = 67.8" * 44.6" = 1.951m^2
20.5% efficient
205W/m^2
205W/m^2 * 4.7kWh/kWp = 963.5Wh/m^2



Explaining STC: https://www.solarpaneltalk.com/forum/solar-panels-for-home/solar-panel-installation/17719-solar-irradiance-unit-defintion?p=207179#post207179



Efficiency is defined as % of 1kW irradiated at 1m^2 that is turned into electricity. 20% panel will have 200W/m^2.


20% efficient = 200W/m^2
4.7kWh/kWp --> 940Wh/m^2 in Denver



&nbsp;

TODO: Add spotify link here (if applicable)
<div style="text-align:center">
<iframe
style="border-radius:12px"
src="https://open.spotify.com/embed/track/5fEThMYHHyoohPxqsCvz1l?utm_source=generator"
width="80%" height="352" frameBorder="0"
allowfullscreen=""
allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
loading="lazy">
</iframe>
</div>
