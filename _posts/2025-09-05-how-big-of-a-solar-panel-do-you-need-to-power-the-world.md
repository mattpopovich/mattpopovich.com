---
title: "How Big of a Solar Panel Do You Need to Power the World?"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2025-09-05 07:15:35 -0600
categories: [Blog, Not YouTube]    # <=2 values here: top category and sub category
tags: [tech, solar, math, engineering]                # TAG names should always be lowercase
layout: post                # post is the default, we will set it to be explicit
pin: false
toc: true                   # Table of contents
comments: true              # Enable/disable comments at the bottom of the post
math: true                  # Disabled by default for performance reasons
mermaid: false              # Diagram generation tool via ```mermaid [...]```
#img_cdn: https://cdn.com
#media_subpath: /img/path/
image:
  path: /assets/img/posts/2025-09-05-how-big-of-a-solar-panel-do-you-need-to-power-the-world/solar-panel-size-to-power-world-electricity.png
#   width: 1200   # in pixels
#   height: 630   # in pixels, 1.90:1 desired by chirpy
  alt: The size of a solar panel needed to power the world's electricity consumption
#   show_image_in_post: false
description: The math behind how big of a solar panel we need to power the United States and the world  # A short sentence to describe the article, used when sharing links on social media and on homepage
---

<!-- TODO: Add YouTube link -->

## Intro
How big of a solar panel do we need to power the world? And what about the United States? This investigation was started largely due to a [stupid tweet](https://x.com/ENERGY/status/1964010741247168958) by the US Department of Energy, but also my interest in cleaner energy.

For starters, I want to touch on the difference between electricity and energy. Energy can come in many forms: electricity, coal, oil, natural gas, wood in your fireplace, etc. Electricity is a form of energy that powers our lights, TVs, microwaves, and more.

Currently, there are some things that we power with an energy other than electricity: planes (jet fuel via oil), construction vehicles and freight trains (diesel fuel via oil), and container ships (heavy fuel oil via oil) to name a few. These use energy but are going to be difficult to electrify due to our current electricity storage methods being too heavy and not having enough energy density.

In this article I'm going to talk about two different things:
1. Making all of our *electricity* generation via solar panels
2. Making all of our *energy* generation via solar panels

Making all of our electricity generation via solar is possible today. This would be replacing our coal, natural gas, wind, hydropower, etc. electricity generation plants with solar (we will also need energy storage for the nights when the sun isn't shining, but I will ignore that for simplicity). Making all of our energy generation via solar is not currently feasible as we do not have electric replacements for airplanes, construction vehicles, container ships, etc. But, we can calculate the energy of the fuel used by those machines (ex. one gallon of gasoline contains ~34kWh). From there, I can see (hypothetically) how much solar would be needed to create all the energy we use in the chance that we electrify our economy in the future.

Let's dive in.

## Math Behind Solar Panel Size
Solar panel efficiency is defined as

$$
\begin{equation}
    \text{Solar panel efficiency} = {\text{Panel's output in watts} \over \text{Panel's area in m}^2 \times \text{irradiance in W/m}^2}
\end{equation}
$$

$\eta$ is commonly used to represent solar panel efficiency:

$$
\begin{equation}
    \eta = \text{Solar panel efficiency}
\end{equation}
$$

[Standard test conditions (STC)](https://sinovoltaics.com/learning-center/quality/standard-test-conditions-stc-definition-and-problems/) for a solar panel defines solar irradiance (how strong is the sunlight) as:

$$
\begin{equation}
    G_{STC} = 1000 \ \mathrm{W/m^2}
\end{equation}
$$

To make our numbers simple, we can have the panel area be:

$$
\begin{equation}
    A_{panel} = 1 \ \mathrm{m^2}
\end{equation}
$$

This gives us:

$$
\begin{equation}
    \eta = {\text{Panel's output in watts} \over A_{panel} \times G_{STC}} = {\text{Panel's output in watts} \over 1 \ \mathrm{m^2} \times 1000 \ \mathrm{W/m^2}}
\end{equation}
$$

[Average solar panel efficiency today is 21%](https://css.umich.edu/publications/factsheets/energy/solar-pv-energy-factsheet). Let's err on the side of caution and use a round number, 20%:

$$
\begin{equation}
    \eta = 20\%
\end{equation}
$$

Now we can calculate the average solar panel output per $m^2$:

$$
\begin{equation}
    20\% = {\text{Panel's output in watts} \over 1 \ \mathrm{m^2} \times 1000 \ \mathrm{W/m^2}}
\end{equation}
$$

$$
\begin{equation}
    20\% = {\text{Panel's output in watts} \over 1000 \ \mathrm{W}}
\end{equation}
$$

$$
\begin{equation}
    200 \ \mathrm{W} = {\text{Panel's output in watts}}
\end{equation}
$$

So **for the average solar panel, we can expect 200W over 1m²**. [Manufacturers will use this value as the panel's "peak power under optimal conditions"](https://www.energuide.be/en/questions-answers/what-is-the-kilowatt-peak/1409/#:~:text=Understanding%20what%20a%20kilowatt%2Dpeak,talk%20about%20'nominal%20power'.) $(\mathrm{kWp\ or\ kW}_{peak})$.

Thus, for the average solar panel, we will see:

$$
\begin{equation}
    \mathrm{kW}_{peak} = 200 \ \mathrm{W/m^2} = 0.2 \ \mathrm{kW/m^2}
\end{equation}
$$

This value is the cornerstone of the rest of our calculations.

## Solar Panel Energy Generation
We just calculated how much *power* our solar panels will generate per square meter, but how much *energy* will they generate for us over a day? Or over a year?

The power that we calculated is during ✨ideal conditions✨. The sun's strength is not a consistent $1000 \ \mathrm{W/m^2}$. The sun's irradiance is strongest during midday, but it still shines in the mornings and evenings. And even if it is cloudy, our solar panels will still be generating some power from diffused sunlight (bouncing through clouds). So how can we calculate the energy generated while taking these factors (and more) into account? Thankfully, someone has already ran these numbers for us: [globalsolaratlas.info](https://globalsolaratlas.info) has created `PVOUT`.

> ["[`PVOUT` represents] the power output achievable by a typical configuration of the utility scale PV system, taking into account the theoretical potential, the air temperature affecting the system performance, the system configuration, shading and soiling, and topographic and land-use constraints"](https://globalsolaratlas.info/global-pv-potential-study)

`PVOUT` is given in units $\mathrm{kWh/kWp}$. This is saying "given the peak wattage of your solar panel, this is how much energy (Wh = watt-hours) your panel will generate. Previously, we calculated the average $\mathrm{kWp}$, so we are ready to use this value.

[For Denver, CO, we get](https://globalsolaratlas.info/map?c=38.664067,-105.270996,7&s=39.749434,-104.974365&m=site) $PVOUT \approx 4.7 \ \mathrm{kWh/kWp}$ per day. Thus:

$$
\begin{equation}
    PVOUT_{Denver_{\text{avg\ panel}}} \approx {4.7 \ \mathrm{kWh} \over \mathrm{kWp}} \times {0.2 \ \mathrm{kWp} \over \mathrm{m^2}} \approx 0.94 \ \mathrm{kWh/m^2} \text{ per day}
\end{equation}
$$

So for every square meter of solar panel that we install, we can expect to see almost 1kWh of generated energy per day on average.

Now, all we need to figure out is how much energy do we need to generate and that will tell us how big of a solar panel we need!

### How Big of a Solar Panel for All of USA Electricity
 [USA electricity generation](https://ourworldindata.org/electricity-mix) (2024) = 4,387 TWh per year = 12.02 TWh per day = $12.02 \times 10^9$ kWh per day.
$$
\begin{equation}
    A_{USA\ electricity} = {12.02 \times 10^{9} \ \mathrm{kWh} \over 0.94 \ \mathrm{kWh/m^2}} = 12,787,234,042 \ \mathrm{m^2}
\end{equation}
$$

$$
\begin{equation}
    A_{USA\ electricity} \approx 12,787 \ \mathrm{km^2} \approx 4,937 \ \mathrm{mi^2}
\end{equation}
$$

4,937 square miles can be accomplished via a square that has sides 70.26 miles (113km) long. This is slightly smaller than the size of Puerto Rico or the size of Connecticut.

In visual form:

<div style="text-align:center">
<iframe src="https://app.atlas.co/embeds/9fpMr5eeYAzqjxaE1dps" frameborder="0" width="80%" height="400" style="max-width: 100%; border: 1px solid #EAEAEA; border-radius: 4px;"></iframe>
</div>

The US is ~3.8 million square miles. So this would be 0.13% of the US's land area... to power the whole country's electricity.

### How Big of a Solar Panel for All of USA Energy
[USA energy consumption](https://ourworldindata.org/energy-production-consumption) (2024) = 26,500 TWh per year = 72.6 TWh per day = $72.6 \times 10^9 \ \mathrm{kWh}$ per day.

> The astute reader would notice that electricity accounts for only $ 4,387 \ \mathrm{TWh} / 26,500 \ \mathrm{TWh} \approx 16.6\% $ of the USA's energy use.
{: .prompt-info }

$$
\begin{equation}
    A_{USA\ energy} = {72.6 \times 10^{9} \ \mathrm{kWh} \over 0.94 \ \mathrm{kWh/m^2}} = 77,234,042,553 \ \mathrm{m}^2
\end{equation}
$$

$$
\begin{equation}
    A_{USA\ energy} \approx 77,234 \ \mathrm{km}^2 \approx 29,820 \ \mathrm{mi}^2
\end{equation}
$$

29,820 square miles can be accomplished via a square that has sides ~172.7 miles (278km) long. This is about 1/4 the size of Colorado.

In visual form:

<div style="text-align:center">
<iframe src="https://app.atlas.co/embeds/B5sB9ic9gdEFOmmqTq2J" frameborder="0" width="80%" height="400" style="max-width: 100%; border: 1px solid #EAEAEA; border-radius: 4px;"></iframe>
</div>

This would be 29,820mi² / 3,800,000mi² = 0.78% of the US's land area... to power the whole country.

### How Big of a Solar Panel for All of World Electricity
[World electricity generation](https://ourworldindata.org/electricity-mix) (2024) = 30,850 TWh per year = 84.5 TWh per day = $84.5 \times 10^9 \ \mathrm{kWh}$ per day.

World electricity generation is actually pretty close to USA total energy usage (which was shown [above](#how-big-of-a-solar-panel-for-all-of-usa-energy)).

$$
\begin{equation}
    A_{World\ electricity} = {84.5 \times 10^{9} \ \mathrm{kWh} \over 0.94 \ \mathrm{kWh/m^2}} = 89,893,617,021 \ \mathrm{m}^2
\end{equation}
$$

$$
\begin{equation}
    A_{World\ electricity} \approx 89,894 \ \mathrm{km}^2 \approx 34,708 \ \mathrm{mi}^2
\end{equation}
$$

34,708 square miles can be accomplished via a square that has sides ~186.3 miles (300km) long. This is slightly smaller than the size of Maine.

In visual form:

<div style="text-align:center">
<iframe src="https://app.atlas.co/embeds/WgO8JzRn4sX8pVwRMrf6" frameborder="0" width="80%" height="400" style="max-width: 100%; border: 1px solid #EAEAEA; border-radius: 4px;"></iframe>
</div>

This would be 34,708mi² / 3,800,000mi² = 0.9% of the US's land area or 34,708mi² / [58,000,000mi²](https://en.wikipedia.org/wiki/Earth#Surface) = 0.06% of the world's land area... to power the world's electricity.

### How Big of a Solar Panel for All of World Energy
[World energy consumption](https://ourworldindata.org/energy-production-consumption) (2024) = 186,383 TWh per year = 510.6 TWh per day = $510.6 \times 10^9 \ \mathrm{kWh}$ per day.

> The astute reader would again notice that electricity accounts for only $ 30,850 \ \mathrm{TWh} / 186,383 \ \mathrm{TWh} \approx 16.6\% $ of the world's energy use. This is the exact same percentage as the US's energy use. The [richest country in the world](https://www.forbes.com/sites/lewisnunn/2025/08/14/the-worlds-50-richest-countries-2025-according-to-financial-experts/) is no better than average at electrifying its economy.
{: .prompt-info }

For this solar panel, it's going to be bigger than Colorado. Let's try to put it in one contiguous location in the US that gets decent sun with minimal population disruption. I'm going to choose North Dakota, South Dakota, Nebraska, and a little sliver of Kansas.

These locations have a different `PVOUT` value than Denver. Denver has a pretty strong `PVOUT = 4.7kWh/kWp`. The lowest `PVOUT` in this location is the north-eastern part of North Dakota with `PVOUT = 3.7kWh/kWp`. The highest `PVOUT` in this location is the south-eastern part of Nebraska with `PVOUT = 4.5kWh/kWp`.

Let's take a [SWAG](https://en.wikipedia.org/wiki/Scientific_wild-ass_guess) and *assume* this 3-state area has the average of those two, which would give us a `PVOUT = (3.7+4.5)/2 = 4.2kWh/kWp`. Let's recalculate how much energy we will get per $\mathrm{m}^2$ with this reduced `PVOUT`:

$$
\begin{equation}
    PVOUT_{ND-SD-KS_{\text{avg\ panel}}} \approx {4.2 \ \mathrm{kWh} \over \mathrm{kWp}} \times {0.2 \ \mathrm{kWp} \over \mathrm{m^2}} \approx 0.84 \ \mathrm{kWh/m^2} \text{ per day}
\end{equation}
$$

Next, let's calculate how big of a solar panel that we will need:

$$
\begin{equation}
    A_{World\ energy} = {510.6 \times 10^{9} \ \mathrm{kWh} \over 0.84 \ \mathrm{kWh/m^2}} = 607.86 \times 10^9 \ \mathrm{m}^2
\end{equation}
$$

$$
\begin{equation}
    A_{World\ energy} \approx 607,860 \ \mathrm{km}^2 \approx 234,696 \ \mathrm{mi}^2
\end{equation}
$$

234,696 square miles can be accomplished via a square that has sides ~484.5 miles (780km) long. This is slightly smaller than the size of Texas.

In visual form:

<div style="text-align:center">
<iframe src="https://app.atlas.co/embeds/293U9kf6eN4aJWCvjYSB" frameborder="0" width="80%" height="400" style="max-width: 100%; border: 1px solid #EAEAEA; border-radius: 4px;"></iframe>
</div>

This would be 234,696mi² / 3,800,000mi² = 6.2% of the US's land area or 234,696mi² / [58,000,000mi²](https://en.wikipedia.org/wiki/Earth#Surface) = 0.4% of the world's land area... to power the whole world.

## Costs

How much would some of these projects cost? [Here](https://a1solarstore.com/sunspark-550w-solar-panel-144-cell-bifacial-sg7g72m-h-550-assembled-in-the-usa-wholesale-36-panels-per-pallet-min-6-pallets.html) is a wholesale solar panel with 21.3% efficiency for \\$0.20/watt. I imagine that buying these in major, major bulk would provide some cost savings, but let's ignore that.

$$
\begin{equation}
    Cost_{\mathrm{USA\ Electricity\ Solar Panels}} = {\$0.20 \over \mathrm{W}} \times {\mathrm{W} \over 4.7\ \mathrm{Wh}} \times {12.02 \times 10^{12}\ \mathrm{Wh}} \approx \$511.5\ \mathrm{Billion}
\end{equation}
$$

That is the price for the panels and does not include necessary components such as inverters, electrical and structural components, land cost, labor, etc. To get a real-world number, we can look at [installation costs for utility-scale solar in 2023](https://emp.lbl.gov/utility-scale-solar): \\$1.43/W.

$$
\begin{equation}
    Cost_{\mathrm{USA\ Electricity\ Solar\ Installation}} = {\$1.43 \over \mathrm{W}} \times {\mathrm{W} \over 4.7\ \mathrm{Wh}} \times {12.02 \times 10^{12}\ \mathrm{Wh}} \approx \$3.7\ \mathrm{Trillion}
\end{equation}
$$

$$
\begin{equation}
    Cost_{\mathrm{USA\ Energy\ Solar\ Installation}} = {\$1.43 \over \mathrm{W}} \times {\mathrm{W} \over 4.7\ \mathrm{Wh}} \times {72.6 \times 10^{12}\ \mathrm{Wh}} \approx \$22.1\ \mathrm{Trillion}
\end{equation}
$$

$$
\begin{equation}
    Cost_{\mathrm{World\ Electricity\ Solar\ Installation}} = {\$1.43 \over \mathrm{W}} \times {\mathrm{W} \over 4.7\ \mathrm{Wh}} \times {84.5 \times 10^{12}\ \mathrm{Wh}} \approx \$25.7\ \mathrm{Trillion}
\end{equation}
$$

$$
\begin{equation}
    Cost_{\mathrm{World\ Energy\ Solar\ Installation}} = {\$1.43 \over \mathrm{W}} \times {\mathrm{W} \over 4.2\ \mathrm{Wh}} \times {510.6 \times 10^{12}\ \mathrm{Wh}} \approx \$173.8\ \mathrm{Trillion}
\end{equation}
$$

## Conclusion
What do you think? Is that more or less solar panel area than you expected? I feel like the land area is quite small in the grand scheme of things. Covering 0.13% of the US’s land area to power the whole country's electricity seems like a great deal to me.

And yes, I know we would also need some way to store the energy for the nights + lots of transmission lines, both of which add losses and increase costs. Additionally, my land use numbers assume that there is 0 space between the panels + no access roads for maintenance, etc. but this was mostly a curious exercise in crunching numbers.

I know the costs sound pretty insane at first glance: \\$3.7 trillion for US electricity. But to increase the country's debt by 10% to get "free" electricity for the country indefinitely? Sounds like a good trade to me. We added this much to the country's debt [in the last 16 months](https://tradingeconomics.com/united-states/government-debt). \\$3.7 trillion is 12.7% of the country's [\\$29.2 trillion GDP](https://fred.stlouisfed.org/series/GDP).

Want to make the country a manufacturing or AI / datacenter powerhouse? Cheap electricity is a great first step.

\\$174T for world energy sounds like a lot... 2024 world GDP was \\$111T, so this would be 157% of world GDP. But the costs of refusing to decarbonize will be even higher. If we continue with business-as-usual (BAU), the estimated economic impacts of increased weather-related and other uninsurable damages, increased production costs, productivity losses, and health costs will be \\$2,328T by 2100. If we can keep the global temperature increases at or below 1.5°C ([currently 1.28°C](https://science.nasa.gov/earth/explore/earth-indicators/global-temperature/)), that drops to \\$1,062T. [Source: Figure ES4](https://www.climatepolicyinitiative.org/wp-content/uploads/2023/11/Global-Landscape-of-Climate-Finance-2023.pdf).

Solar is the [safest source of energy](https://ourworldindata.org/safest-sources-of-energy) when accounting for accidents and air pollution with 0.02 deaths per 1,000,000,000 kWh (1 TWh) produced. Coal is 1230x solar, oil is 613x, natural gas is 140x.
Solar also has [much less greenhouse gas emissions](https://ourworldindata.org/safest-sources-of-energy): 160x less than coal, 65x less than oil, and 8x less than natural gas.

We are [using more and more energy as time goes on](https://ourworldindata.org/energy-production-consumption). Making sure we can meet those energy demands is important, and solar is one piece of the puzzle that will make that possible.

There is lots of solar power out there for the taking. Hopefully we start to [grab more of it](https://ourworldindata.org/grapher/installed-solar-pv-capacity?country=CHN~IND~ESP~BRA~MEX~CHL~USA~OWID_EU27).


<!--

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

-->
