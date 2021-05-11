# CellML model implementations

This directory contains the CellML files used for all simulations in this study.
Models were obtained from the [Physiome (CellML) model repository](https://models.physiomeproject.org) or the [Web Lab](chaste.cs.ox.ac.uk/WebLab).
All models were annotated with terms from the [oxmeta ontology](https://github.com/ModellingWebLab/ontologies/), which occasionally involved separating parts of equations out into separate variables.

Some models were modified, e.g. to fix unit inconsistencies or correct equations.
This is detailed in the supplementary materials.

Links to the original implementations that these files are based on are given below:

- [Aslanidi et al. 2009 Atrial](https://chaste.cs.ox.ac.uk/WebLab/entities/models/11/versions/7318d0a67f7077494165b4c981703c121aafb3a4)
- [Aslanidi et al. 2009 Purkinje](https://chaste.cs.ox.ac.uk/WebLab/entities/models/12/versions/2f737b824b45ed115155a0e5991aba4df74b1582)
- [Bartolucci et al. 2020](https://models.physiomeproject.org/workspace/5fd)
- [Beeler & Reuter 1977](https://chaste.cs.ox.ac.uk/WebLab/entities/models/1/versions/4680f3e8395da43250412aa3a16013090da62570)
 [Bondarenko et al. 2004](https://chaste.cs.ox.ac.uk/WebLab/entities/models/15/versions/141530c77eadc8bafe865083a5a5ccf2dc0c2ca6)
- Cabo & Boyden 2003 (ICaL): New implementation.
- [Corrias et al. 2011](https://github.com/Chaste/cellml/blob/master/cellml/corrias_purkinje_2011.cellml)
- Cortassa et al. 2006 (ICaL): New implementation.
- [Courtemanche et al. 1998](https://chaste.cs.ox.ac.uk/WebLab/entities/models/19/versions/30d0616f05d88d875cf594db2950052879aae204)
- [Decker et al. 2009](https://chaste.cs.ox.ac.uk/WebLab/entities/models/20/versions/82b79061559c63cce7ee9b4413f31f1ba580793d)
- [Demir et al. 1994](https://models.physiomeproject.org/exposure/15dc665c02ca9955b8e79fbace81a9e5)
- [DiFrancesco & Noble 1985](https://chaste.cs.ox.ac.uk/WebLab/entities/models/21/versions/34fbdc5a5676c19ef11a062606ef52702e20f895)
  - The CellML implementation for this model is based on the OXSOFT HEART source code, which corrects some of the published equations.
  - Although the paper argues against a sodium component of ICaL, the CellML version does include it.
  - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
- [Dokos et al. 1996](https://models.physiomeproject.org/exposure/462ab10275dfc099166c8a0e4f9e1be3)
  - The original CellML file had units that were internally consistent but did not match the paper.
    For example, ICaL maximum conductance was given as 400nS in the paper, but as 0.4nS in the CellML file.
    To fix this, we changed the CellML file value to 0.4μS, and updated current and capacitance to nA and μF respectively.
    Further unit issues were seen in the CellML file, but these did not affect our simulations.
- Faber 2007 (ICaL): New implementation.
- [Fink et al. 2008](https://models.physiomeproject.org/exposure/eeb81adc372c2f172399ec7160b0331e)
- [Fox et al. 2002](http://models.physiomeproject.org/exposure/13f8cb8b26258e359da674a7bf3435ad)
- [Grandi et al. 2010](https://chaste.cs.ox.ac.uk/WebLab/entities/models/26/versions/ebe0634280215163f94c1a247a78f44d6637dae7)
- [Grandi et al. 2011](https://models.physiomeproject.org/e/596/view)
- Heijman et al. 2011: New implementation.
- [Hilgemann & Noble 1987](https://models.physiomeproject.org/exposure/49f298f54f3e916fca650c8e76d82e46)
  - The CellML implementation for this model is based on the OXSOFT HEART source code, which corrects some of the published equations.
  - This model contains variables representing the inactivated fraction `F` instead of the more conventional recovered fraction `f = 1 - F`.
  - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
- [Hinch et al. 2004 (ICaL)](https://models.physiomeproject.org/exposure/8e1a590fb82a2cab5284502b430c4a4f)
- [Hund & Rudy 2004](https://chaste.cs.ox.ac.uk/WebLab/entities/models/72/versions/bd9b7bb2cf9d96abe1f6299a83da1ed9b1b013fb)
- Hund et al. 2008: New implementation.
- [Inada et al. 2009](https://models.physiomeproject.org/exposure/08bcead2dc05cf2709a598e7f61a6182)
- [Iyer et al. 2004](https://chaste.cs.ox.ac.uk/WebLab/entities/models/27/versions/b374722702a941b1beedcc0822f8f1f333f09449)
  - In the available file, `tau _yCa` is given as `1 / ( 0.00336... / (0.5 + exp(-V / 5.54...)) + 0.00790... * exp(-V / 49.5...) )`.
    This has been changed to `1 / (0.00653 / (0.5 + exp(-V / 7.1)) + 0.00512 * exp(-V / 39.8))` in accordance with the published equations.
- [Jafri et al. 1998](https://models.physiomeproject.org/exposure/5230da0476e9764a7d513a5d18af2a58)
  - The original CellML file gave the ODE for `C_Ca0` as `beta_b * C_Ca1 + gamma * C_Ca0 - (4 * alpha_a + omega) * C_Ca0`
    This has been corrected to `beta_b * C_Ca1 + gamma * C_0 - (4 * alpha_a + omega) * C_Ca0`, in accordance with the published equations.
  - The definition of the units `mm_per_ms` was corrected.
- [Kurata et al. 2002 (ICaL)](https://models.physiomeproject.org/exposure/47b969553fcfe6f875d4e38d1fd33986)
  - The original CellML file gave `alpha_fCa` as 0.021 1/ms.
    This has been set to 0.035 1/ms in accordance with the published equations.
    Please note that the corrected CellML file contains only the ICaL component.
- [Li et al. 2010](https://chaste.cs.ox.ac.uk/WebLab/entities/models/29/versions/8c33fb1cc93bed4886e30c6679a4454cff6222fe)
- Li & Rudy 2011 (ICaL): New implementation.
- [Lindblad et al. 1996](https://models.physiomeproject.org/exposure/036dcdf013d736a376bf4d8f429bb804)
  - The original CellML file have `ICaL` given as `gCaL * dL * fL * dp * (V - ECa)`.
    This has been changed to `gCaL * (dL * fL + dp) * (V - ECa)` in accordance with the published equations.
- Livshitz & Rudy 2007 HRd (ICaL): New implementation.
- [Lovell et al. 2004 (ICaL)](https://models.physiomeproject.org/exposure/5055e8e1a4fb76cc90067d9e0997bb29)
  - The original file gave the ODE for `A_CaL` contained a term `beta_1 * I_1` that was corrected to `beta_2 * I_1`,  in accordance with the published equations.
  - Similarly, in the ODE for `I_1` a term `(beta_2 + alpha_3 + Cai^2)` was updated to `(beta_2 + alpha_3 * Cai^2)`.
  - The original CellML file was described as "not functional" in its documentation, so we only used (and checked) the model's ICaL component for the central SAN cell version of the model.
- [Luo & Rudy 1994](https://chaste.cs.ox.ac.uk/WebLab/entities/models/30/versions/fca55ec8a791cfd20cff78bb9442840786fd93ed)
- [Mahajan et al. 2008](https://chaste.cs.ox.ac.uk/WebLab/entities/models/31/versions/f9862685af295d2875ae597451255d8a9f9eae0b)
- [Matsuoka et al. 2003](https://chaste.cs.ox.ac.uk/WebLab/entities/models/33/versions/9f763fef8fd410495a875ed344e66d249f589224)
- [McAllister et al. 1975](https://models.physiomeproject.org/exposure/60e23c3228a3e455699846704006a8fe)
- [Noble et al. 1991](https://chaste.cs.ox.ac.uk/WebLab/entities/models/35/versions/daaa80c551c077849993d2d310071df88aef4670)
  - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
- [Noble et al. 1998](https://chaste.cs.ox.ac.uk/WebLab/entities/models/34/versions/ea4fb7f64829a16197c54a2efd15306573bb87f3)
  - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
  - TODO: MENTION HERE THAT THIS IS OXSOFT 3.3 Model, closest paper available
- Nordin et al. 1993 (ICaL): New implementation
- [Nygren et al. 1998](https://models.physiomeproject.org/exposure/ad761ce160f3b4077bbae7a004c229e3)
- [O'Hara et al. 2011](https://chaste.cs.ox.ac.uk/WebLab/entities/models/4/versions/b6f19db6d1697e56945a9b825a7026f0799b4005)
- [Pasek et al. 2006](https://models.physiomeproject.org/exposure/e794e94916178875bc8ea12767f78c90)
- [Paci et al. 2013](https://models.physiomeproject.org/e/594)
- [Pandit et al. 2001](https://models.physiomeproject.org/exposure/ea62c9c8a502afe364350d353ebf4dd5)
- Pohl et al. 2016 (ICaL): New implementation.
- [Priebe & Beuckelmann](https://scrambler.cs.ox.ac.uk/entities/models/38/versions/2a634280b8ddfa3d9b16b396af548b07858af34d)
- [Ramirez et al. 2000](https://models.physiomeproject.org/exposure/fc3dbf2134db2e5efc2990483b27d7ae)
- Sato et al. 2006 (ICaL): New implementation
- [Shannon et al. 2004](https://scrambler.cs.ox.ac.uk/entities/models/39/versions/827a07937facdeda84fb6838c06e7676ca3c6489)
- [Ten Tusscher et al. 2004](https://scrambler.cs.ox.ac.uk/entities/models/41/versions/84972529041015ff0e5504e615d58bb303b29ef7)
  - The units for this model were corrected, and corrected versions were uploaded to the Physiome (CellML )Model Repository.
- [Ten Tusscher & Panfilov 2006](https://scrambler.cs.ox.ac.uk/entities/models/41/versions/84972529041015ff0e5504e615d58bb303b29ef7)
  - The units for this model were corrected, and corrected versions were uploaded to the Physiome (CellML )Model Repository.
- [Tomek et al. 2019](https://models.physiomeproject.org/e/5f1)
- [Trovato et al. 2020](https://models.physiomeproject.org/e/5f2)
- [Varela et al. 2016](https://models.physiomeproject.org/e/4bc)
- Wilders et al. 1991 (ICaL): New implementation.
  - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
- [Winslow et al. 1999](https://scrambler.cs.ox.ac.uk/entities/models/43/versions/a4e21d2010a87b4e79e384ddebc84e5e0e30c506)
- [Zeng et al. 1995](https://models.physiomeproject.org/exposure/15dc665c02ca9955b8e79fbace81a9e5)
  - The fCa gate is raised incorrectly to a power, this has been corrected
  - All state variables in this file are mssing an intitial valye, therefore the model has been corrected for ICaL only
- [Zhang et al. 2000](https://models.physiomeproject.org/exposure/01f6a47881da1925315d1d89d3a8d901)

## TODO: Latex for model changes, not yet incorporated above

NOTE: If we don't include these models in the study, then find way to tell PMR that they are wrong.

\citet{livshitz2007regulation} & \href{https://models.cellml.org/exposure/dedfcd1a135ddb59e9d979ec1376a44f/livshitz_rudy_2007.cellml/view}{Physiome model repository}
\\ \hline \multicolumn{2}{|p{0.95\textwidth}|}{%
    This paper discusses the development of a new \ical\ model from the \citet{hund2004rate} model. However, the available file, implements these changes into the \citet{luo1994dynamic} model.
    We have therefore created a new implementation using the published equations as the available file is not relevant to the paper.
} \\ \hline
 
\citet{varela2016atrial} & \href{https://models.cellml.org/e/4bc/Varela_RA_2016.cellml/view}{Physiome model repository}
\\ \hline \multicolumn{2}{|p{0.95\textwidth}|}{%
    In the available file, $f_{Ca\infty}$ is given by $0.29 + \frac{0.8}{1 + \textcolor{red}{\frac{Ca_i - 1.2\cdot 10^{-4}}{6\cdot 10^{-5}}}}$.
    This has been corrected to $0.29 + \frac{0.8}{1 + \textcolor{red}{e^{\frac{Ca_i - 1.2\cdot 10^{-4}}{6\cdot 10^{-5}}}}}$ in accordance with the published manuscript and Matlab and C code.
    Similarly the value of $g_{CaL}$ has been changed from \textcolor{red}{0.58 nS/pF} to \textcolor{red}{0.34 nS/pF} (the value for the right-atrial model variant).
} \\ \hline

\citet{bernus2002computationally} & \href{https://models.cellml.org/e/5/bernus_wilders_zemlin_verschelde_panfilov_2002.cellml/view}{Physiome model repository}
\\ \hline \multicolumn{2}{|p{0.95\textwidth}|}{%
    In the available, the parameter $\beta _f$ of the $f$ gate is been given as $[0.069\cdot \exp(-\textcolor{red}{11}\cdot (V+9.825)) + 0.011] / [1+\exp(-0.278\cdot (V+9.825))] + 5.75\cdot 10^{-4}$.
    This has been corrected to be in accordance with the published equations $\frac{0.069\cdot e^{-\textcolor{red}{0.11}\cdot (V+9.825)} + 0.011}{1+e^{-0.278\cdot (V+9.825)}} + 5.75\cdot 10^{-4}$.
    Please note that the \ical component of this model has been stripped out of the original file.
} \\ \hline

\citet{hinch2004simplified} & \href{https://models.cellml.org/exposure/8e1a590fb82a2cab5284502b430c4a4f/hinch_greenstein_tanskanen_xu_winslow_2004.cellml/view}{Physiome model repository}
\\ \hline \multicolumn{2}{|p{0.95\textwidth}|}{%
    In the available file, the denominator of the flux $J_{Loo}$ is given as $1+\frac{J_R}{g_D}+\frac{\frac{J_L}{g_D}\cdot FVRT_{Ca}}{1-e^{\textcolor{red}{FVRT_{Ca}}}}$.
    This was set to $1+\frac{J_R}{g_D}+\frac{\frac{J_L}{g_D}\cdot FVRT_{Ca}}{1-e^{\textcolor{red}{-FVRT_{Ca}}}}$ in accordance with the published equations.
    $I_{CaL}$ has in this model has been modified non-stochastically to more accurately represent current in Amperes rather than flux.
    Current carried by RyR and SERCA have been blocked in this model for the purpose of this study.
} \\ \hline \newpage

## Some models included only for qualitative analysis
- Bassingthwaighte 1972 : Accurate equations not found
- Liu 1993: Driving term increases exponentially!


## Not included cause equivalent
- [x] Earm 1990: CellML is unchanged from Hilgemann 1987
- [x] Luo 1991 - Beeler 1977
- [x] Noble 1984 - DiFrancesco 1984
- [x] Winslow 1993 - Hilgemann 1987
- [x] Riemer 1998 - Luo 1994
- [x] Chudin 1999 - Zeng 1995
- [x] Clancy 1999 - Zeng 1995
- [x] Demir 1999 - Demir 1994, g change only
- [x] Dumaine 1999 - Luo 1994
- [x] Viswanathan 1999 - Luo 1994
- [x] Faber 2000 - Luo 1994
- [x] Greenstein 2000 - Winslow 1999
- [x] Sakmann 2000 - Oxsoft 4.8 ICaL
- [x] Clancy 2001 - Luo 1994
- [x] Mazhari 2001 - Winslow 1999
- [x] Kneller 2002 - Ramirez 2000
- [x] Puglisi 2001 - Luo 1994
- [] Bernus 2002 - Priebe 1998 (simplified model)
- [x] Clancy 2002 - Luo 1994
- [x] Oehmen 2002 - Demir 1994
- [x] Seemann 2003 - Priebe 1998
- [x] Pandit 2003 - Pandit 2001
- [x] Sarai 2003 - Matsuoka 2003 ("Kyoto model")
- [x] Saucerman 2003 - Jafri 1998
- [x] Saucerman 2004 - Luo 1994
- [x] Coutu 2005 - Winslow 1999
- [x] Terrenoire 2005 - Nygren 1998
- [x] Fink 2006 - Iyer 2004
- [x] Flaim 2006 - Greenstein 2006
- [x] Iribe 2006 - Noble 1991
- [x] Iyer 2007 - Iyer 2004
- [x] Niederer 2007 - Pandit 2001
- [x] Benson 2008 - Hund 2004
- [x] Kuzomoto 2008 - Matsuoka 2003
- [x] Saucerman 2008 - Shannon 2004
- [x] Wang 2008 - Bondarenko 2004
- [x] Ahrens-Nicklas 2009 - Faber 2007
- [x] Christensen 2009 - Shaw 1997 / Luo 1994
- [x] Gaur 2009 - Faber 2000
- [x] Koivumaki 2009 - Bondarenk 2004, or full equations not given
- [x] Maleckar 2009 - Nygren 1998
- [x] Stewart 2009 - Ten Tusscher 2004
- [x] Wolf 2010 - Bondarenko 2004
- [x] Lemay 2011 - Faber 2007
- [x] Pueyo 2011 - Faber & Ten Tusscher 2006
- [x] Colman 2013 - Courtemanche 1998
- [x] Voigt 2013 - Grandi 2011
- [x] Schmidt 2015 - Grandi 2011
- [x] Ni 2017 - Colman 2013

## Not selected
- [x] Yanagihara 1980 - SAN (mixed SI current) 
- [x] Bristow 1982 - SAN (mixed SI current)
- [x] Irisawa 1982 - In a book and SAN
- [x] Kass & Sanguinetti 1982/1984 - No full model
- [x] Standen & Stanfield 1982 : Stick insect skeletal muscle fibers
- [x] Reiner 1985 - SAN (mixed SI current)
- [x] Hadley & Hume 1987 - No model
- [x] Egan 1987 - DN update in oxsoft, no eqs given
- [x] Hagiwara 1988 - Partial model
- [x] Rasmusson 1990a - Bullfrog
- [x] Noble, DiFrancesco, Denyer 1989 -> in a book "Neuronal and Cellular Oscillators" (and SAN?)
- [x] Rasmusson 1990b - Bullfrog
- [x] Karma 1993 - Simplified model
- [x] Endresen 1997 - SAN
- [x] Espinosa 1998 - Unable to access
- [x] Rice 1999 - Spatial model
- [x] Endresen 2000 - Simplified model
- [x] Mitchell 2003 - Simplified model
- [?] Noble 2001 - Remodelling of calcium dynamics in guinea-pig ventricular cells UNABLE TO FIND MANUSCRIPT
- [x] Fenton 2002 - Simplified model
- [x] Greenstein 2002 - Spatial model
- [x] Pandit 2003 - Diseased (and Pandit 2001)
- [x] Garny 2003 - Simplified model
- [x] Greenstein 2004 - Spatial model
- [x] Tanskanen 2005 - Spatial model
- [x] Greenstein 2006 - Spatial model
- [x] Simitev 2006 - Simplified model
- [x] Cherry 2007 - Simplified model
- [ ] Grandi 2007 - Disease mopdel
- [x] Iancu 2007 - No ICaL
- [x] Bueno-Orovio 2008 - Simplified model
- [x] Chiba 2008 - No ICaL
- [x] Restrepo 2008 - Spatial model
- [x] Xin 2008 - No ICaL
- [x] Violin 2008 - No ICaL
- [x] Hashambhoy 2009 - Spatial model
- [x] Hashamboy 2010 - Spatial model
- [x] Sampson 2010 - Iyer 2004
- [x] Koivumaki 2011 - Complex subspaces
- [x] Tao 2011 - Mixed Ca current
- [x] Thul 2012 - Spatial model
- [x] Davies 2014 - Equations not given.
