# CellML model implementations

This directory contains the CellML files used for all simulations in this study.

Models were obtained from the [Physiome (CellML) model repository](https://models.physiomeproject.org) (PMR) or the [Web Lab](chaste.cs.ox.ac.uk/WebLab).
The origin of our model files is given by the links below.
A list of data sources cited by the model publications is given in [data.md](./data.md).

All models were annotated with terms from the [oxmeta ontology](https://github.com/ModellingWebLab/ontologies/), to allow simulations with the Web Lab.
Occasionally, this involved involved separating parts of equations out into separate variables.

Some retrieved CellML files were found to contain unit inconsistencies or differ slightly from the published manuscripts.
We corrected these where possible, as documented in the list below.
In some cases this was difficult to do for the full action-potential model, so we isolated the ICaL component (as indicated by "ICaL only" in the list).
Where CellML implementations could not be found we attempted to create them ourselves (usually for only the ICaL component).

In the list below, models are ordered by the name of the first author.
The index in the gating type table (which is also used as a general index for each model) is shown in brackets.

- [Aslanidi et al. 2009a Atrial](https://chaste.cs.ox.ac.uk/WebLab/entities/models/11/versions/7318d0a67f7077494165b4c981703c121aafb3a4) 
- [Aslanidi et al. 2009 Purkinje](https://chaste.cs.ox.ac.uk/WebLab/entities/models/12/versions/2f737b824b45ed115155a0e5991aba4df74b1582) 
- [Bartolucci et al. 2020](https://models.physiomeproject.org/workspace/5fd) 
- [Beeler & Reuter 1977](https://chaste.cs.ox.ac.uk/WebLab/entities/models/1/versions/4680f3e8395da43250412aa3a16013090da62570) 
- [Bondarenko et al. 2004](https://chaste.cs.ox.ac.uk/WebLab/entities/models/15/versions/141530c77eadc8bafe865083a5a5ccf2dc0c2ca6) 
- Cabo & Boyden 2003 (ICaL only): New implementation. 
- [Corrias et al. 2011](https://github.com/Chaste/cellml/blob/master/cellml/corrias_purkinje_2011.cellml) 
  - The available CellML file has different paramaeter values for `tau_y_Ltype` and `tau_yCa` than the published paper.
  - However, after contacting the original authors it was confirmed that this was a typesetting error and that the CellML file was correct.
- Cortassa et al. 2006 (ICaL only): New implementation. 
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
   - Further unit issues were seen in the CellML file, but these did not affect our simulations.
- Faber 2007 (ICaL only): New implementation. (48)
- [Fink et al. 2008](https://models.physiomeproject.org/exposure/eeb81adc372c2f172399ec7160b0331e) 
- [Fox et al. 2002](http://models.physiomeproject.org/exposure/13f8cb8b26258e359da674a7bf3435ad)
- [Jafri et al. 1998](https://models.physiomeproject.org/exposure/5230da0476e9764a7d513a5d18af2a58) 
   - The original CellML file gave the ODE for `C_Ca0` as `beta_b * C_Ca1 + gamma * C_Ca0 - (4 * alpha_a + omega) * C_Ca0`
     This has been corrected to `beta_b * C_Ca1 + gamma * C_0 - (4 * alpha_a + omega) * C_Ca0`, in accordance with the published equations.
   - The definition of the units `mm_per_ms` was corrected.
- [Grandi et al. 2010](https://chaste.cs.ox.ac.uk/WebLab/entities/models/26/versions/ebe0634280215163f94c1a247a78f44d6637dae7)
- [Grandi et al. 2011](https://models.physiomeproject.org/e/596/view)
- Heijman et al. 2011: New implementation. 
- [Hilgemann & Noble 1987](https://models.physiomeproject.org/exposure/49f298f54f3e916fca650c8e76d82e46)
   - The CellML implementation for this model is based on the OXSOFT HEART source code, which corrects some of the published equations.
   - This model contains variables representing the inactivated fraction `F` instead of the more conventional recovered fraction `f = 1 - F`.
   - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
- [Hund & Rudy 2004](https://chaste.cs.ox.ac.uk/WebLab/entities/models/72/versions/bd9b7bb2cf9d96abe1f6299a83da1ed9b1b013fb)
- Hund et al. 2008 (ICaL only): New implementation. 
- [Inada et al. 2009](https://models.physiomeproject.org/exposure/08bcead2dc05cf2709a598e7f61a6182) 
- [Iyer et al. 2004](https://chaste.cs.ox.ac.uk/WebLab/entities/models/27/versions/b374722702a941b1beedcc0822f8f1f333f09449)
   - In the available file, `tau _yCa` is given as `1 / ( 0.00336... / (0.5 + exp(-V / 5.54...)) + 0.00790... * exp(-V / 49.5...) )`.
     This has been changed to `1 / (0.00653 / (0.5 + exp(-V / 7.1)) + 0.00512 * exp(-V / 39.8))` in accordance with the published equations.
- Kernik et al. 2019 (ICaL only): New implementation.
- [Koivumaki et al. 2011](https://models.physiomeproject.org/e/631/koivumaki-2011-pmr.cellml/)
- [Kurata et al. 2002 (ICaL)](https://models.physiomeproject.org/exposure/47b969553fcfe6f875d4e38d1fd33986)
   - The original CellML file gave `alpha_fCa` as 0.021 1/ms.
     This has been set to 0.035 1/ms in accordance with the published equations.
     Please note that the corrected CellML file contains only the ICaL component.
- [Li et al. 2010](https://chaste.cs.ox.ac.uk/WebLab/entities/models/29/versions/8c33fb1cc93bed4886e30c6679a4454cff6222fe)
- Li & Rudy 2011 (ICaL only): New implementation.
- [Lindblad et al. 1996](https://models.physiomeproject.org/exposure/036dcdf013d736a376bf4d8f429bb804)
  - The original CellML file has `ICaL` given as `gCaL * dL * fL * dp * (V - ECa)`.
    This has been changed to `gCaL * (dL * fL + dp) * (V - ECa)` in accordance with the published equations.
- Liu et al. 1993 (ICaL only): New implementation.
- Livshitz & Rudy 2007 HRd (ICaL only): New implementation. 
  - This study describes modifications of the Hund et al. 2004 and Luo & Rudy 1994 models.
    Only the Hund modification includes an updated ICaL, for which we created a new (ICaL only) implementation.
    A CellML file for the Luo & Rudy modification is available from PMR.
- [Lovell et al. 2004 (ICaL)](https://models.physiomeproject.org/exposure/5055e8e1a4fb76cc90067d9e0997bb29)
  - The original file gave the ODE for `A_CaL` contained a term `beta_1 * I_1` that was corrected to `beta_2 * I_1`,  in accordance with the published equations.
  - Similarly, in the ODE for `I_1` a term `(beta_2 + alpha_3 + Cai^2)` was updated to `(beta_2 + alpha_3 * Cai^2)`.
  - The original CellML file was described as "not functional" in its documentation, so we only used (and checked) the model's ICaL component for the central SAN cell version of the model.
- [Luo & Rudy 1994](https://chaste.cs.ox.ac.uk/WebLab/entities/models/30/versions/fca55ec8a791cfd20cff78bb9442840786fd93ed) 
- [Mahajan et al. 2008](https://chaste.cs.ox.ac.uk/WebLab/entities/models/31/versions/f9862685af295d2875ae597451255d8a9f9eae0b) 
- [Matsuoka et al. 2003](https://chaste.cs.ox.ac.uk/WebLab/entities/models/33/versions/9f763fef8fd410495a875ed344e66d249f589224) 
- [McAllister et al. 1975](https://models.physiomeproject.org/exposure/60e23c3228a3e455699846704006a8fe)
- [Michailova et al. 2005](https://models.physiomeproject.org/exposure/720f5c67a03d513abfd43fd0027c9e41)
- [Noble et al. 1991](https://chaste.cs.ox.ac.uk/WebLab/entities/models/35/versions/daaa80c551c077849993d2d310071df88aef4670)
  - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
- [Noble et al. 1998](https://chaste.cs.ox.ac.uk/WebLab/entities/models/34/versions/ea4fb7f64829a16197c54a2efd15306573bb87f3) 
   - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
   - Note that the paper does not describe this model in detail, the CellML implementation is based on the OXSOFT HEART source code, version 3.3.
- Nordin et al. 1993 (ICaL only): New implementation
- [Nygren et al. 1998](https://models.physiomeproject.org/exposure/ad761ce160f3b4077bbae7a004c229e3)
- [O'Hara et al. 2011](https://chaste.cs.ox.ac.uk/WebLab/entities/models/4/versions/b6f19db6d1697e56945a9b825a7026f0799b4005)
- [Paci et al. 2013](https://models.physiomeproject.org/e/594)
- [Pandit et al. 2001](https://models.physiomeproject.org/exposure/ea62c9c8a502afe364350d353ebf4dd5)
- [Pasek et al. 2006](https://models.physiomeproject.org/exposure/e794e94916178875bc8ea12767f78c90)
- [Priebe & Beuckelmann 1998](https://scrambler.cs.ox.ac.uk/entities/models/38/versions/2a634280b8ddfa3d9b16b396af548b07858af34d)
- [Ramirez et al. 2000](https://models.physiomeproject.org/exposure/fc3dbf2134db2e5efc2990483b27d7ae)
- Sato et al. 2006 (ICaL only): New implementation
- [Shannon et al. 2004](https://scrambler.cs.ox.ac.uk/entities/models/39/versions/827a07937facdeda84fb6838c06e7676ca3c6489) 
- [Ten Tusscher et al. 2004](https://scrambler.cs.ox.ac.uk/entities/models/41/versions/84972529041015ff0e5504e615d58bb303b29ef7) 
   - The units for this model were corrected, and corrected versions were uploaded to the Physiome (CellML )Model Repository.
- [Ten Tusscher & Panfilov 2006](https://scrambler.cs.ox.ac.uk/entities/models/41/versions/84972529041015ff0e5504e615d58bb303b29ef7)
  - The units for this model were corrected, and corrected versions were uploaded to the Physiome (CellML )Model Repository.
- [Tomek et al. 2019](https://models.physiomeproject.org/e/5f1) 
- [Trovato et al. 2020](https://models.physiomeproject.org/e/5f2) 
- Wilders et al. 1991 (ICaL only): New implementation. 
  - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
- [Winslow et al. 1999](https://scrambler.cs.ox.ac.uk/entities/models/43/versions/a4e21d2010a87b4e79e384ddebc84e5e0e30c506)
- [Zeng et al. 1995 (ICaL only)](https://models.physiomeproject.org/exposure/15dc665c02ca9955b8e79fbace81a9e5) 
  - The `fCa` gate is raised incorrectly to a power, this has been corrected
  - All state variables in this file are missing an intitial value, we corrected the model for ICaL only.
- [Zhang et al. 2000](https://models.physiomeproject.org/exposure/01f6a47881da1925315d1d89d3a8d901)
- [Varela et al. 2016](https://models.physiomeproject.org/e/4bc)
  - In the available file, `f_Ca_inf` is given as `0.29 + 0.8 / (1 + (Ca_i - 1.2e-4) / 6e-5)`, this was changed to `0.29 + 0.8 / (1 + exp((Ca_i - 1.2e-4) / 6e-5))` in accordance with the published equations and Matlab and C code.
  - Similarly, the value of `g_CaL` was changed from `0.58 nS/pF` to `0.34 nS/pF` (the value for the right-atrial model variant).

## Models included qualitatively

The oldest ICaL (or ICaL-like) model we could find equations for was by Bassingthwaithe and Reuter, and is presented in the 1972 book [Electrical phenomena of the heart](https://www.sciencedirect.com/book/9780122089503/electrical-phenomena-in-the-heart).
No implementation of the model equations could be found online, and the equations given in the book don't match the shown figures exactly, so that we could only include this model qualitatively.

A small number of studies used a model in which L-type calcium channels (LCC) and ryanodine receptors (RyR) functioned as a single coupled calcium release unit (CRU).
These, similarly, could only be included qualitatively.

Full list:

- Bassingthwaithe and Reuter 1972 - Equations do not reproduce the published figures 
- [Rice et al. 1999](https://models.physiomeproject.org/exposure/0aaab0a02a6ad97c8a37b2fe4a345e7c) - The file is missing initial values
  - Initial values not published
- Greenstein 2002 - Stochastic simulation
- [Hinch et al. 2004](https://models.physiomeproject.org/exposure/8e1a590fb82a2cab5284502b430c4a4f) - CRU
  - In the available file, the denominator of the flux `J_Loo` is given as `1 + J_R / g_D + (FVRT_Ca * J_L / g_D) / (1 - exp(FVRT_Ca))`.
  - This should be corrected to `1 + J_R / g_D + (FVRT_Ca * J_L / g_D) / (1 - exp^(-FVRT_Ca))` in accordance with the published equations.
- Greenstein et al. 2006 - CRU
- Restrepo et al. 2008 - Stochastic simulation
- Hashambhoy et al. 2009 - Stochastic simulation
- Nivala et al. 2012 - Stochastic simulation
- Asakura et al. 2014 - CRU
- Himeno et al. 2015 - CRU
- Pohl et al. 2016 
  - Initial values of ACh equation not published
  - Incompatible units of gCa
## Unchanged ICaL

The models below were all inspected but then omitted as their equations and (non-conductance) parameters were found to be equivalent to a previous model.

- Earm 1990 - CellML is unchanged from Hilgemann 1987
- Luo 1991 - Beeler 1977
- Noble 1984 - DiFrancesco 1984
- Winslow 1993 - Hilgemann 1987
- Riemer 1998 - Luo 1994
- Chudin 1999 - Zeng 1995
- Clancy 1999 - Zeng 1995
- Demir 1999 - Demir 1994, g change only
- Dumaine 1999 - Luo 1994
- Viswanathan 1999 - Luo 1994
- Faber 2000 - Luo 1994
- Greenstein 2000 - Winslow 1999
- Sakmann 2000 - Oxsoft 4.8 ICaL
- Clancy 2001 - Luo 1994
- Mazhari 2001 - Winslow 1999
- Kneller 2002 - Ramirez 2000
- Puglisi 2001 - Luo 1994
- Bernus 2002 - Priebe 1998 (simplified model)
- Clancy 2002 - Luo 1994
- Oehmen 2002 - Demir 1994
- Seemann 2003 - Priebe 1998
- Pandit 2003 - Pandit 2001
- Sarai 2003 - Matsuoka 2003 ("Kyoto model")
- Saucerman 2003 - Jafri 1998
- Greenstein 2004 - Greenstein 2002 
- Saucerman 2004 - Luo 1994
- Coutu 2005 - Winslow 1999
- Tanskanen 2005 - Greenstein 2002
- Terrenoire 2005 - Nygren 1998
- Fink 2006 - Iyer 2004
- Flaim 2006 - Greenstein 2006
- Iribe 2006 - Noble 1991
- Iyer 2007 - Iyer 2004
- Livshitz 2007 (Guinea Pig) - Luo 1994
- Niederer 2007 - Pandit 2001
- Benson 2008 - Hund 2004
- Kuzomoto 2008 - Matsuoka 2003
- Saucerman 2008 - Shannon 2004
- Wang 2008 - Bondarenko 2004
- Ahrens-Nicklas 2009 - Faber 2007
- Christensen 2009 - Shaw 1997 / Luo 1994
- Gaur 2009 - Faber 2000
- Koivumaki 2009 - Bondarenko 2004, or full equations not given
- Maleckar 2009 - Nygren 1998
- Stewart 2009 - Ten Tusscher 2004
- Rovetti 2010 - Hinch 2004
- Sampson 2010 - Iyer 2004
- Soltis 2010 - Mahajan 2008
- Wolf 2010 - Bondarenko 2004
- Lemay 2011 - Faber 2007
- Pueyo 2011 - Faber & Ten Tusscher 2006
- Colman 2013 - Courtemanche 1998
- Voigt 2013 - Grandi 2011
- Schmidt 2015 - Grandi 2011
- Ni 2017 - Colman 2013

## Not included

The studies listed below were inspected but did not meet our inclusion criteria.

- **Yanagihara 1980 - SAN (mixed SI current)** - shown in provenance figure 
- Bristow 1982 - SAN (mixed SI current)
- Irisawa 1982 - In a book and SAN
- Kass & Sanguinetti 1982/1984 - No full model
- Standen & Stanfield 1982 - Stick insect skeletal muscle fibers
- Reiner 1985 - SAN (mixed SI current)
- Egan 1987 - DN update in oxsoft, equations not given
- Hagiwara 1988 - Partial model
- **Rasmusson 1990a - Bullfrog** - shown in provenance figure
- Noble 1989 - Unable to access (in book)
- Rasmusson 1990b - Bullfrog
- Karma 1993 - Simplified model
- **Shirokov 1993 - Unable to find full equations** - shown in provenance figure
- Endresen 1997 - SAN
- Ferreira 1997 - No full model
- Espinosa 1998 - Unable to access
- Stern 1999 - Full equations not available
- Endresen 2000 - Simplified model
- Sun 2000 - Unable to reproduce from given equations
- Noble 2001 - Unable to locate manuscript
- Fenton 2002 - Simplified model
- Sobie 2002 - Full equations not available
- Garny 2003 - Simplified model
- Hirano 2003 - Unable to find full equations
- Mitchell 2003 - Simplified model
- Miyoshi 2003 - Unable to find full equations
- Shiferaw et al. 2008 - Simplified model
- Simitev 2006 - Simplified model
- Cherry 2007 - Simplified model
- Grandi 2007 - Disease model
- Bueno-Orovio 2008 - Simplified model
- Tao 2011 - Mixed Ca current
- Davies 2014 - Equations not given

