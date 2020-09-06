# Solar Panel Forecast

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rogeramitchell/solar-panel-forecast/tree/master/master?urlpath=lab) 

## Overview 

Our Sprinter van has a 2 [175W NewPowa solar panels](https://www.newpowa.com/products/newpowa-175w-12v-monocrystalline-high-efficiency-solar-panel) wired into a [Victron SmartSolar Charge Controller](https://www.victronenergy.com/solar-charge-controllers/smartsolar-100-30-100-50), which provides data in CSV format for a trailing 30 day period. Based on our usage of the van in New England, we're interested to predict solar panel outputs based on time of year and weather forecast.

## Hypothesis

We suspect the three contributing factors to solar panel output are:

1. Cloud coverage
1. Cloud height (i.e. height of the given cloud layer from top to base)
1. Time of year
