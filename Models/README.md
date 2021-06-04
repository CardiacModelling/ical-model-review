# CellML model implementations

This directory contains the CellML files used for all simulations in this study.

Models were obtained from the [Physiome (CellML) model repository](https://models.physiomeproject.org) (PMR) or the [Web Lab](chaste.cs.ox.ac.uk/WebLab).
The origin of our model files is given by the links below.

All models were annotated with terms from the [oxmeta ontology](https://github.com/ModellingWebLab/ontologies/), to allow simulations with the Web Lab.
Occasionally, this involved involved separating parts of equations out into separate variables.

Some retrieved CellML files were found to contain unit inconsistencies or differ slightly from the published manuscripts.
We corrected these where possible, as documented in the list below.
In some cases this was difficult to do for the full action-potential model, so we isolated the ICaL component (as indicated by "ICaL only" in the list).
Where CellML implementations could not be found we attempted to create them ourselves (usually for only the ICaL component).

In the list below, models are ordered by the name of the first author.
The index in the gating type table (which is also used as a general index for each model) is shown in brackets.

- [Aslanidi et al. 2009a Atrial](https://chaste.cs.ox.ac.uk/WebLab/entities/models/11/versions/7318d0a67f7077494165b4c981703c121aafb3a4) (10)
- [Aslanidi et al. 2009 Purkinje](https://chaste.cs.ox.ac.uk/WebLab/entities/models/12/versions/2f737b824b45ed115155a0e5991aba4df74b1582) (52)
- [Bartolucci et al. 2020](https://models.physiomeproject.org/workspace/5fd) (61)
- Bassingthwaighte & Reuter 1972 (1)
  - No implementation could be found, or created from the equations in the book (which did not match the figures)
- [Beeler & Reuter 1977](https://chaste.cs.ox.ac.uk/WebLab/entities/models/1/versions/4680f3e8395da43250412aa3a16013090da62570) (2)
- [Bondarenko et al. 2004](https://chaste.cs.ox.ac.uk/WebLab/entities/models/15/versions/141530c77eadc8bafe865083a5a5ccf2dc0c2ca6) (46)
- Cabo & Boyden 2003 (ICaL only): New implementation. (14)
- [Corrias et al. 2011](https://github.com/Chaste/cellml/blob/master/cellml/corrias_purkinje_2011.cellml) (27)
  - The available CellML file has different paramaeter values for `tau_y_Ltype` and `tau_yCa` than the published paper.
  - However, after contacting the original authors it was confirmed that this was a typesetting error and that the CellML file was correct.
- Cortassa et al. 2006 (ICaL only): New implementation. (35)
- [Courtemanche et al. 1998](https://chaste.cs.ox.ac.uk/WebLab/entities/models/19/versions/30d0616f05d88d875cf594db2950052879aae204) (20)
- [Decker et al. 2009](https://chaste.cs.ox.ac.uk/WebLab/entities/models/20/versions/82b79061559c63cce7ee9b4413f31f1ba580793d) (59)
- [Demir et al. 1994](https://models.physiomeproject.org/exposure/15dc665c02ca9955b8e79fbace81a9e5) (7)
- [DiFrancesco & Noble 1985](https://chaste.cs.ox.ac.uk/WebLab/entities/models/21/versions/34fbdc5a5676c19ef11a062606ef52702e20f895) (15)
   - The CellML implementation for this model is based on the OXSOFT HEART source code, which corrects some of the published equations.
   - Although the paper argues against a sodium component of ICaL, the CellML version does include it.
   - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
- [Dokos et al. 1996](https://models.physiomeproject.org/exposure/462ab10275dfc099166c8a0e4f9e1be3) (16)
   - The original CellML file had units that were internally consistent but did not match the paper.
     For example, ICaL maximum conductance was given as 400nS in the paper, but as 0.4nS in the CellML file.
     To fix this, we changed the CellML file value to 0.4μS, and updated current and capacitance to nA and μF respectively.
   - Further unit issues were seen in the CellML file, but these did not affect our simulations.
- Faber 2007 (ICaL only): New implementation. (47)
- [Fink et al. 2008](https://models.physiomeproject.org/exposure/eeb81adc372c2f172399ec7160b0331e) (56)
- [Fox et al. 2002](http://models.physiomeproject.org/exposure/13f8cb8b26258e359da674a7bf3435ad) (23)
- [Jafri et al. 1998](https://models.physiomeproject.org/exposure/5230da0476e9764a7d513a5d18af2a58) (32)
   - The original CellML file gave the ODE for `C_Ca0` as `beta_b * C_Ca1 + gamma * C_Ca0 - (4 * alpha_a + omega) * C_Ca0`
     This has been corrected to `beta_b * C_Ca1 + gamma * C_0 - (4 * alpha_a + omega) * C_Ca0`, in accordance with the published equations.
   - The definition of the units `mm_per_ms` was corrected.
- **Greenstein 2006** (36)
- [Grandi et al. 2010](https://chaste.cs.ox.ac.uk/WebLab/entities/models/26/versions/ebe0634280215163f94c1a247a78f44d6637dae7) (18)
- [Grandi et al. 2011](https://models.physiomeproject.org/e/596/view) (19)
- Heijman et al. 2011: New implementation. (60)
- [Hilgemann & Noble 1987](https://models.physiomeproject.org/exposure/49f298f54f3e916fca650c8e76d82e46) (30)
   - The CellML implementation for this model is based on the OXSOFT HEART source code, which corrects some of the published equations.
   - This model contains variables representing the inactivated fraction `F` instead of the more conventional recovered fraction `f = 1 - F`.
   - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
- [Hinch et al. 2004](https://models.physiomeproject.org/exposure/8e1a590fb82a2cab5284502b430c4a4f) (38)
  - In the available file, the denominator of the flux `J_Loo` is given as `1 + J_R / g_D + (FVRT_Ca * J_L / g_D) / (1 - exp(FVRT_Ca))`.
  - This has been changed to `1 + J_R / g_D + (FVRT_Ca * J_L / g_D) / (1 - exp^(-FVRT_Ca))` in accordance with the published equations.
  - For the purposes of this study, we further modified `I_CaL` to represent current in Amperes rather than flux, and blocked the RyR and SERCA currents.
- [Hund & Rudy 2004](https://chaste.cs.ox.ac.uk/WebLab/entities/models/72/versions/bd9b7bb2cf9d96abe1f6299a83da1ed9b1b013fb) (50)
- Hund et al. 2008 (ICaL only): New implementation. (54)
- [Inada et al. 2009](https://models.physiomeproject.org/exposure/08bcead2dc05cf2709a598e7f61a6182) (49)
- [Iyer et al. 2004](https://chaste.cs.ox.ac.uk/WebLab/entities/models/27/versions/b374722702a941b1beedcc0822f8f1f333f09449) (34)
   - In the available file, `tau _yCa` is given as `1 / ( 0.00336... / (0.5 + exp(-V / 5.54...)) + 0.00790... * exp(-V / 49.5...) )`.
     This has been changed to `1 / (0.00653 / (0.5 + exp(-V / 7.1)) + 0.00512 * exp(-V / 39.8))` in accordance with the published equations.
- Kernik et al. 2019 (ICaL only): New implementation. (29)
- [Koivumaki et al. 2011](https://models.physiomeproject.org/e/631/koivumaki-2011-pmr.cellml/) (57)
- [Kurata et al. 2002 (ICaL)](https://models.physiomeproject.org/exposure/47b969553fcfe6f875d4e38d1fd33986) (24)
   - The original CellML file gave `alpha_fCa` as 0.021 1/ms.
     This has been set to 0.035 1/ms in accordance with the published equations.
     Please note that the corrected CellML file contains only the ICaL component.
- [Li et al. 2010](https://chaste.cs.ox.ac.uk/WebLab/entities/models/29/versions/8c33fb1cc93bed4886e30c6679a4454cff6222fe) (39)
- Li & Rudy 2011 (ICaL only): New implementation. (53)
- [Lindblad et al. 1996](https://models.physiomeproject.org/exposure/036dcdf013d736a376bf4d8f429bb804) (8)
  - The original CellML file has `ICaL` given as `gCaL * dL * fL * dp * (V - ECa)`.
    This has been changed to `gCaL * (dL * fL + dp) * (V - ECa)` in accordance with the published equations.
- **Liu et al. 1993 (5)**
- Livshitz & Rudy 2007 HRd (ICaL only): New implementation. (51)
  - This study describes modifications of the Hund et al. 2004 and Luo & Rudy 1994 models.
    Only the Hund modification includes an updated ICaL, for which we created a new (ICaL only) implementation.
    A CellML file for the Luo & Rudy modification is available from PMR.
- [Lovell et al. 2004 (ICaL)](https://models.physiomeproject.org/exposure/5055e8e1a4fb76cc90067d9e0997bb29) (45)
  - The original file gave the ODE for `A_CaL` contained a term `beta_1 * I_1` that was corrected to `beta_2 * I_1`,  in accordance with the published equations.
  - Similarly, in the ODE for `I_1` a term `(beta_2 + alpha_3 + Cai^2)` was updated to `(beta_2 + alpha_3 * Cai^2)`.
  - The original CellML file was described as "not functional" in its documentation, so we only used (and checked) the model's ICaL component for the central SAN cell version of the model.
- [Luo & Rudy 1994](https://chaste.cs.ox.ac.uk/WebLab/entities/models/30/versions/fca55ec8a791cfd20cff78bb9442840786fd93ed) (11)
- [Mahajan et al. 2008](https://chaste.cs.ox.ac.uk/WebLab/entities/models/31/versions/f9862685af295d2875ae597451255d8a9f9eae0b) (48)
- [Matsuoka et al. 2003](https://chaste.cs.ox.ac.uk/WebLab/entities/models/33/versions/9f763fef8fd410495a875ed344e66d249f589224) (44)
- [McAllister et al. 1975](https://models.physiomeproject.org/exposure/60e23c3228a3e455699846704006a8fe) (6)
- **michailova_2005** (37)
- [Noble et al. 1991](https://chaste.cs.ox.ac.uk/WebLab/entities/models/35/versions/daaa80c551c077849993d2d310071df88aef4670) (3)
  - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
- [Noble et al. 1998](https://chaste.cs.ox.ac.uk/WebLab/entities/models/34/versions/ea4fb7f64829a16197c54a2efd15306573bb87f3) (21)
   - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
   - Note that the paper does not describe this model in detail, the CellML implementation is based on the OXSOFT HEART source code, version 3.3.
- Nordin et al. 1993 (ICaL only): New implementation
- [Nygren et al. 1998](https://models.physiomeproject.org/exposure/ad761ce160f3b4077bbae7a004c229e3) (40)
- [O'Hara et al. 2011](https://chaste.cs.ox.ac.uk/WebLab/entities/models/4/versions/b6f19db6d1697e56945a9b825a7026f0799b4005) (62)
- [Paci et al. 2013](https://models.physiomeproject.org/e/594) (58)
- [Pandit et al. 2001](https://models.physiomeproject.org/exposure/ea62c9c8a502afe364350d353ebf4dd5) (41)
- [Pasek et al. 2006](https://models.physiomeproject.org/exposure/e794e94916178875bc8ea12767f78c90) (42)
- Pohl et al. 2016 (ICaL only): New implementation. (43)
- [Priebe & Beuckelmann 1998](https://scrambler.cs.ox.ac.uk/entities/models/38/versions/2a634280b8ddfa3d9b16b396af548b07858af34d) (13)
- [Ramirez et al. 2000](https://models.physiomeproject.org/exposure/fc3dbf2134db2e5efc2990483b27d7ae) (22)
- Sato et al. 2006 (ICaL only): New implementation (26)
- [Shannon et al. 2004](https://scrambler.cs.ox.ac.uk/entities/models/39/versions/827a07937facdeda84fb6838c06e7676ca3c6489) (17)
- [Ten Tusscher et al. 2004](https://scrambler.cs.ox.ac.uk/entities/models/41/versions/84972529041015ff0e5504e615d58bb303b29ef7) (25)
   - The units for this model were corrected, and corrected versions were uploaded to the Physiome (CellML )Model Repository.
- [Ten Tusscher & Panfilov 2006](https://scrambler.cs.ox.ac.uk/entities/models/41/versions/84972529041015ff0e5504e615d58bb303b29ef7) (55)
  - The units for this model were corrected, and corrected versions were uploaded to the Physiome (CellML )Model Repository.
- [Tomek et al. 2019](https://models.physiomeproject.org/e/5f1) (63)
- [Trovato et al. 2020](https://models.physiomeproject.org/e/5f2) (64)
- Wilders et al. 1991 (ICaL only): New implementation. (4)
  - The variable `PCa` in this model includes a factor `F`, so that the true permeability is given by `PCa/F`.
- [Winslow et al. 1999](https://scrambler.cs.ox.ac.uk/entities/models/43/versions/a4e21d2010a87b4e79e384ddebc84e5e0e30c506) (33)
- [Zeng et al. 1995](https://models.physiomeproject.org/exposure/15dc665c02ca9955b8e79fbace81a9e5) (12)
  - The `fCa` gate is raised incorrectly to a power, this has been corrected
  - All state variables in this file are missing an intitial value, we corrected the model for ICaL only.
- [Zhang et al. 2000](https://models.physiomeproject.org/exposure/01f6a47881da1925315d1d89d3a8d901) (9)
- [Varela et al. 2016](https://models.physiomeproject.org/e/4bc) (28)
  - In the available file, `f_Ca_inf` is given as `0.29 + 0.8 / (1 + (Ca_i - 1.2e-4) / 6e-5)`, this was changed to `0.29 + 0.8 / (1 + exp((Ca_i - 1.2e-4) / 6e-5))` in accordance with the published equations and Matlab and C code.
  - Similarly, the value of `g_CaL` was changed from `0.58 nS/pF` to `0.34 nS/pF` (the value for the right-atrial model variant).

## Studies using an equivalent ICaL model (not included)

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
- [ ] Bernus 2002 - Priebe 1998 (simplified model)
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
- [x] Livshitz 2007 (Guinea Pig) - Luo 1994
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

## Studies not selected

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
- [x] Shirokov (1993) Unable to find full equations
- [x] Endresen 1997 - SAN
- [x] Espinosa 1998 - Unable to access
- [x] Rice 1999 - Spatial model
- [x] Endresen 2000 - Simplified model
- [x] Mitchell 2003 - Simplified model
- [?] Noble 2001 - Remodelling of calcium dynamics in guinea-pig ventricular cells UNABLE TO FIND MANUSCRIPT
- [x] Fenton 2002 - Simplified model
- [x] Greenstein 2002 - Stochastic calculation of whole-cell current
	- Greenstein 2004, Tanskanen 2005 are equivalent
	- Hashambhoy 2009, Hashambhoy 2010 have the have only two rate constants changed
- [x] Pandit 2003 - Diseased (and Pandit 2001)
- [x] Garny 2003 - Simplified model
- [x] Simitev 2006 - Simplified model
- [x] Cherry 2007 - Simplified model
- [ ] Grandi 2007 - Disease mopdel
- [x] Iancu 2007 - No ICaL
- [x] Bueno-Orovio 2008 - Simplified model
- [x] Chiba 2008 - No ICaL
- [x] Restrepo 2008 - Stochastic calculation of whole-cell current
- [x] Xin 2008 - No ICaL
- [x] Violin 2008 - No ICaL
- [x] Sampson 2010 - Iyer 2004
- [x] Tao 2011 - Mixed Ca current
- [x] Davies 2014 - Equations not given.

