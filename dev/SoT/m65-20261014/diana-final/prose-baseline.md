+-----------+----------------------------------------------------------+----------------------------------------------------------+
| \`\`      | ![](./media/image1.png){width="0.84in" height="0.84in"}  |                                                          |
|           |                                                          |                                                          |
|           | **Seismic Hazard Assessment Technical Report\            |                                                          |
|           | for the Crawford Engineering Design Project,\            |                                                          |
|           | [Canada]**                                             |                                                          |
+===========+==========================================================+==========================================================+
|           | **Prepared for**                                                                                                    |
|           |                                                                                                                     |
|           | Canada Nickel Co.                                                                                                   |
+-----------+---------------------------------------------------------------------------------------------------------------------+
|           | **Prepared by**                                                                                                     |
|           |                                                                                                                     |
|           | ![C:\\Users\\skang\\Documents\\WMF-versions\\AI-for-WMF.wmf](./media/image2.wmf){width="3.67in" height="0.42in"}    |
|           |                                                                                                                     |
|           | SRK Consulting (Canada) Inc.                                                                                        |
|           |                                                                                                                     |
|           | CAPR003324                                                                                                          |
|           |                                                                                                                     |
|           | October 2026                                                                                                        |
+-----------+---------------------------------------------------------------------------------------------------------------------+

+----+---------------------------------------------------------------------------------------------------------------------+
|    | Seismic Hazard Assessment Technical Report\                                                                         |
|    | for the Crawford Engineering Design Project,\                                                                       |
|    | [Canada]                                                                                                          |
+====+==========================================================+==========================================================+
|    | October 2026                                                                                                        |
+----+----------------------------------------------------------+----------------------------------------------------------+
|    | **Prepared for**                                         | **Prepared by**                                          |
+----+----------------------------------------------------------+----------------------------------------------------------+
|    | Canada Nickel Co.                                        | SRK Consulting (Canada) Inc.                             |
|    |                                                          |                                                          |
|    | 130 King St West, Suite 1900                             | 320 Granville Street, Suite 2600                         |
|    |                                                          |                                                          |
|    | Toronto, ON M5X 1E3                                      | Vancouver, BC V6C 1S9                                    |
|    |                                                          |                                                          |
|    |                                                          | Canada                                                   |
+----+----------------------------------------------------------+----------------------------------------------------------+
|    | Tel.:                                                    | Tel.: +1 604 681 4196                                    |
|    |                                                          |                                                          |
|    | Web: canadanickel.com                                    | Web: www.srk.com                                         |
+----+----------------------------------------------------------+----------------------------------------------------------+
|    | Project No.: CAPR003324                                                                                             |
|    |                                                                                                                     |
|    | File Name:                                                                                                          |
+----+---------------------------------------------------------------------------------------------------------------------+
|    | Copyright © SRK Consulting (Canada) Inc., 2026                                                                      |
|    |                                                                                                                     |
|    | ![C:\\Users\\skang\\Documents\\WMF-versions\\AI-for-WMF.wmf](./media/image2.wmf){width="3.67in" height="0.42in"}    |
+----+---------------------------------------------------------------------------------------------------------------------+

# Important Notice {#important-notice .ExecSum-Heading-1}

This report is a technical study of the seismic hazard at the Crawford Project site, prepared for Canada Nickel Co (“CNC”) by SRK Consulting (Canada) Inc. (“SRK”). It provides the seismic design basis for the engineering of the Project facilities. The quality of information, conclusions, and estimates contained herein is consistent with the level of effort involved in SRK’s services, based on: i) information available at the time of preparation, ii) data supplied by outside sources, and iii) the assumptions, conditions, and qualifications set forth in this report. This report is intended for use by CNC subject to the terms and conditions of its contract with SRK. Any other use of this report by a third party is at that party’s sole risk.

# Copyright {#copyright .ExecSum-Heading-1}

This report is protected by copyright vested in SRK Consulting (Canada) Inc. It may not be reproduced or transmitted in any form or by any means whatsoever to any person without the written permission of the copyright holder, other than in accordance with stock exchange and other regulatory authority requirements.

# Useful Definitions {#useful-definitions .ExecSum-Heading-1}

> This list contains definitions of symbols, units, abbreviations, and terminology that may be unfamiliar to the reader.

  ----------------------------------------------------------------------
  AEP                  Annual Exceedance Probability
  -------------------- -------------------------------------------------
                       

  CanadaSHM6           6th Generation Seismic Hazard Model of Canada

  CCSC11               Canadian Composite Seismicity Catalog

  CDA                  Canadian Dam Association

                       

  DSHA                 Deterministic Seismic Hazard Analysis

                       

  EDAP                 Earthquake Data Auto-Processor

  FEED                 Front-End Engineering Design

  GEM                  Global Earthquake Model

  GIA                  Glacial Isostatic Adjustment

  GISTM                Global Industry Standard on Tailings Management

  GMM                  Ground Motion Model

  GMPE                 Ground Motion Prediction Equation

  ICMM                 International Council on Mining and Metals

  $$k_{h}$$            Seismic Coefficient

  $$k_{y}$$            Yield Coefficient

  MDE                  Maximum Design Earthquake

  MNR                  Ontario Ministry of Natural Resources

  Mw                   Moment Magnitude

  NBCC                 National Building Code of Canada

  NBCC 2015            2015 National Building Code of Canada

  NBCC 2020            2020 National Building Code of Canada

  NGA                  Next Generation Attenuation

  NON                  Northern Ontario

  NRC                  Natural Resources Canada

                       

                       

  P&C                  Paterson and Cooke

  PGA                  Peak Ground Acceleration

  PGV                  Peak Ground Velocity

  PSHA                 Probabilistic Seismic Hazard Analysis

  $$R_{rup}$$          Rupture Distance

  *S~a~*               Pseudo-Acceleration

  SCPT                 Seismic Cone Penetration Test

  SDOF                 Single-degree-of-freedom

                       

  SRK                  SRK Consulting (Canada) Inc.

  $$T_{n}$$            Fundamental Period

  $$T_{\max}$$         Maximum Period

  TPT                  Total Probability Theorem

  TMF                  Tailings Management Facility

  UHS                  Uniform Hazard Spectrum

  $$V_{s,30}$$         Average Shear Wave Velocity in the upper 30 m

  $$Z_{top}$$          Depth to Top of Rupture
  ----------------------------------------------------------------------

# Executive Summary {#executive-summary .ExecSum-Heading-1}

SRK Consulting (Canada), Inc. (SRK) and Paterson and Cooke (P&C), referred herein as SRK-PC, were appointed by Canada Nickel Co. (CN) to undertake the site-specific seismic hazard assessment for the Crawford Project site near Timmins, Ontario as part of the activities to support of the Front-End Engineering Design (FEED) for the proposed facilities. A Probabilistic Seismic Hazard Assessment (PSHA) was carried out for representative site conditions at the Crawford site. Design ground motions and guidance for the embankments are provided in terms of peak ground acceleration, spectral accelerations, and horizontal seismic coefficients for stability analysis.

The Crawford Project site is located within the stable craton of the North American plate, in Northern Ontario region, characterized by a recently deglaciated shield terrain with numerous lakes, crystalline bedrock exposures, and variable glacial till deposits (**Chapter [0](#_Ref174451674)**). While Northern Ontario has a low rate of seismicity, notable intraplate seismicity has been recorded, driven primarily by Glacial Isostatic Adjustment (GIA) and regional intraplate stress. These forces, along with the reactivation of crustal faults and fractures, contribute to the region's earthquake activity.

The seismicity analysis for the Crawford Project site (**Chapter [0](#_Ref174451708)**) is based on data from publicly available databases, which were utilized to update the seismic catalog within a 400-kilometer radius of the site. The updated and declustered catalog documents 67 events with moment magnitudes (Mw) of 3 or greater, spanning from 1916 to August 30, 2026. Historical events such as the 1935 Temiskamingue earthquake (Mw 6.2) and the 2000 Kipawa earthquake (Mw 4.7) demonstrate the potential for notable seismic activity.

The seismic hazard assessment for the Crawford Project site (**Chapter [0](#_Ref174031794)**) utilized the 6th Generation Seismic Hazard Model of Canada (CanadaSHM6) (Canadian Comission on Building and Fires Codes and National Research Council of Canada, 2020), as implemented in the Global Earthquake Model (GEM) (2018). This model, which was used as the basis for the seismic hazard values in the 2020 National Building Code of Canada (2020 NBCC), consists of three regional models: the Western Model, the East Arctic Model, and the Southeastern Model. The Crawford Project site falls within the Southeastern Model.

The ground motion intensity for the Crawford Project site (**Chapter [0](#_Ref174451752)**) in Southeastern Canada is modeled using two sets of Ground Motion Models (GMMs) within the CanadaSHM6 framework. Each set is assigned an equal probability of 0.5. The first set, developed by Atkinson and Adams (2013)(AA13), includes three models, named "upper," "central," and "lower", to capture epistemic uncertainty. The central model, which represents the median ground motion, carries the highest weight. The second set of GMMs is derived from the Central and Eastern North America project (NGA-East-13) (Goulet, et al., 2017) and includes 13 candidate models, with weights that vary depending on the natural vibration period.

The seismic hazard assessment for the Crawford Project site was conducted using a Probabilistic Seismic Hazard Analysis (PSHA). A Deterministic Seismic Hazard Analysis (DSHA) is not necessary, as the site is located in a stable continental region with no known major active fault systems capable of producing large earthquakes. Consequently, identifying the Maximum Credible Earthquake through the DSHA approach, which depends on known faults, is less relevant for this location.

The PSHA for the Site was conducted using the OpenQuake v3.26.2 engine. Results of the PSHA are presented in terms of Annual Exceedance Probability (AEP) and Uniform Hazard Spectra (UHS) for site conditions ranging from hard to soft rock, as defined by the 2020 NBCC (**Chapter [6](#seismic-hazard)**). The analysis considers events associated with a target AEP of 1:475, 1: 975, 1:2,475, 1:5,000 and 1:10,000 years and for various confidence levels, including mean, 50^th^, 84^th^, 90^th^, and 95^th^ percentiles.

Dynamic site response analysis was used to modify the response spectra to the specific geotechnical conditions of each project facility (**Chapter [6.5](#controlling-scenarios)**). This analysis involves estimating multi-period amplification factors dependent on the average shear-wave velocity of the upper\
30 m of soil ($V_{s,30}$) as defined by the 2020 NBCC. The design demands combine the direct logic-tree evaluation at each condition with the ST20 transformation of the demand at the reference condition of 760 m/s, conditioned on the PGA of the same realization. Seismic Cone Penetration Tests (SCPT) conducted during the 2021-2022 and 2023 field investigations (SRK Consulting (Canada), Inc., 2023) (2024) provided $V_{s,30}$ values ranging from 180 to 230 m/s. A characteristic $V_{s,30}$value of 220 m/s was adopted for the site, classifying it as Stiff Soil Class D per the 2020 NBCC. The resulting UHS for these site-specific conditions were presented for target AEPs of ranging from 1:475 to 1:10,000 years and for various confidence levels.

The 2020 NBCC offers an online seismic hazard tool that provides seismic hazard values for building design across Canada (Natural Resources of Canada, 2021d). A comparison of the mean response spectra from this tool with the PSHA analysis was conducted, covering the relevant AEPs and structural periods (**Chapter [8](#national-building-code-of-canada-seismic-hazard-values)**). The ratios of the PSHA spectral ordinates to the NRC 2020 values range from 0.70 to 1.30 for the periods and site conditions compared.

The Canadian Dam Association (CDA) (2013) along with the International Council on Mining and Metals (ICMM) (2020) and the Ontario Ministry of Natural Resources (MNR) (2011), recommends performing PSHA and determining recurrence intervals based on the potential consequences of dam failure, which range from “Low” to “Extreme.” For this project, an “Extreme” consequence level has been designated for the FEED phase of the TMF, leading to a designation of the “Maximum Design Earthquake” (MDE) with an AEP of 1:10,000 years, consistent with GISTM and, for closure, with ICOLD and ANCOLD guidance. For the Clay, Rock, and Sand & Silt Impoundments, as well as the East and West Stockpiles, the MDE corresponds to an AEP of 1: 2,475 years. Response spectra and PGA values for the MDE have been provided for various site conditions, from hard rock to stiff soil, and at different confidence levels (**Chapter [0](#_Ref174785920)**). For stiff soils ($V_{s,30} = \$`<!-- -->`{=html}220 m/s), the MDE for the TMF is anticipated to result in a horizontal Peak Ground Acceleration (PGA) of 0.312 g (mean) and\
0.442 g (84^th^ percentile) and the MDE for the impoundments and stockpiles is anticipated to result in a PGA of 0.159 g (mean) and 0.229 g (84th percentile).

Seismic coefficients for the Crawford project embankments were estimated using an empirical (Bray, Macedo, & Travasauro, Simplified procedure for estimating seismic slope displacements for subduction and crustal earthquakes, 2018) (**Chapter [0](#_Ref174451918)**). The fundamental periods of the slopes were determined based on embankment configuration parameters, material types, and shear wave velocity values. The horizontal seismic coefficients were expressed as a percentage of the PGA for the MDE with an AEP of 1:10,000 years and were presented for various site conditions, including hard rock, soft rock, and stiff soil, and for different confidence levels. These coefficients, when applied to slope stability analyses, will provide estimates of the potential for failure during an MDE earthquake level.

***Disclaimer***

> *SRK Consulting (Canada), Inc. (SRK) has prepared this document for Canada Nickel Co, our client. Any use or decisions by which a third party makes of this document are the responsibility of such third parties. In no circumstance does SRK accept any consequential liability arising from commercial decisions or actions resulting from the use of this report by a third party. The opinions expressed in this document have been based on the information available to SRK at the time of preparation. SRK has exercised all due care in reviewing information supplied by others for use on this project. While SRK has compared key supplied data with expected values, the accuracy of the results and conclusions from the review are entirely reliant on the accuracy and completeness of the supplied data. SRK does not accept responsibility for any errors or omissions in the supplied information, except to the extent that SRK was hired to verify the data.*

# Table of Contents {#table-of-contents .TOC-Heading}

1 Introduction 1

1.1 Project Overview 1

1.2 Scope of Work 4

1.3 Organization of This Report 4

2 Seismotectonics 6

2.1 Seismotectonic Framework in Southeastern Canada 6

3 Seismicity 10

3.1 Seismicity Catalog 10

3.2 Historical Seismicity 11

3.2.1 The 1935 Mw 6.2 Temiskamingue Earthquake 11

3.2.2 The 2000 Magnitude Mw 4.7 Kipawa Earthquake 12

4 Seismic Source Model 13

4.1 Definitions 13

4.2 The 6^th^ Generation Seismic Hazard Model of Canada 13

5 Ground Motion Intensity Model 15

5.1 Definitions 15

5.1.1 Ground Motion Intensity Models 15

5.1.2 Fault Distance Metrics 15

5.1.3 Probability Distributions 16

5.2 Ground Motion Models for Southeastern Canada 17

5.3 Epistemic Uncertainty for the Southeastern Canada Seismic Hazard Model 18

6 Seismic Hazard 19

6.1 Definitions 19

6.1.1 Seismic Hazard Assessment 19

6.1.2 Annual Exceedance Probability 20

6.1.3 Peak Ground Acceleration and Response Spectra 20

6.2 Seismic Hazard Results 21

6.2.1 Annual Exceedance Probability 21

6.2.2 Uniform Hazard Spectra 24

6.3 Hazard Deaggregation and Controlling Seismic Scenarios 26

6.3.1 Definitions 26

6.4 Hazard Deaggregation Plots 27

6.5 Controlling Scenarios 29

7 Site Response 31

7.1 Site Class 31

7.2 Crawford Site-Specific Shear Wave Velocity Profile 32

7.3 Site Amplification Factors 40

7.4 Uniform Hazard Spectra 40

8 2020 National Building Code of Canada Seismic Hazard Values 42

9 Design Earthquakes 46

9.1 Peak Ground Acceleration 46

9.2 Design Response Spectra 47

10 Slope Design Parameters 54

10.1 Definitions 54

10.1.1 Seismic Design Criteria for Slopes 54

10.1.2 Fundamental Period of the Embankment 55

10.1.3 Seismic (Pseudo-Static) Coefficients 57

10.2 Fundamental Periods of the Crawford Embankments 60

10.3 Seismic Coefficients 61

11 Conclusions 64

References 66

# List of Tables {#list-of-tables .TOC-Heading}

Table 1‑1: Crawford Project Site Coordinates 1

Table 5‑1: Ground Motion Models for the CanadaSHM6 18

Table 7‑1: Site Classification according to the National Building Code of Canada (2020) 31

Table 7‑2: Site Classification according to the American Society of Civil Engineers ASCE 7-22 (2022) 31

Table 7‑3: Shear Wave Velocity Profile at Crawford Facilities 40

Table 9‑1: PGA of Design Ground Motions for Various Return Periods and Site Conditions – Mean Values 46

Table 9‑2: PGA of Design Ground Motions for Various Return Periods and Site Conditions – 84^th^ Percentile Values 47

Table 9‑3: Spectral Ordinates of the Design Spectra for a 10,000-year Return Period and Various Site Conditions – Mean Values 52

Table 9‑4:Spectral Ordinates of the Design Spectra for a 2,475-year Return Period and Various Site Conditions – Mean Values 53

Table 10‑1: Fundamental periods and mean dynamic properties of the evaluated slope scenarios 60

Table 10‑2: Seismic Coefficients [% of PGA] of the Ensemble Set for Design Earthquakes with AEPs of 1:2,475 and 1:10,000 Years 61

Table A‑1: Crawford Regional Catalog of Events 1916-08/30/2026 (Mw ≥ 3) 72

Table B‑1: CanadaSHM6 Southeast HY Model Seismic Sources 76

Table B‑2: CanadaSHM6 Southeast H2 Model Seismic Sources 77

Table B‑3: CanadaSHM6 Southeast R2 Model Seismic Sources 78

Table D1‑1:PGA of Design Ground Motions for Various Return Periods and Site Conditions – Mean Values 110

Table D1‑2: PGA of Design Ground Motions for Various Return Periods and Site Conditions – 50^th^ Percentile Values 110

Table D1‑3: PGA of Design Ground Motions for Various Return Periods and Site Conditions – 84^th^ Percentile Values 110

Table D1‑4: PGA of Design Ground Motions for Various Return Periods and Site Conditions – 90^th^ Percentile Values 110

Table D1‑5: PGA of Design Ground Motions for Various Return Periods and Site Conditions – 95^th^ Percentile Values 111

Table E‑1: Shear Stiffness Parameters for Gravels, Sands, and Fines 117

Table E2‑1: Mean values of $kmax$ [cm/s²] for scenario S135 and return periods $TR = 475,\ 2,475,\ 10,000$ yr. 122

Table E2‑2: Mean values of $kmax$ [cm/s²] for scenario S50 and return periods $TR = 475,\ 2,475,\ 10,000$ yr. 123

Table E2‑3: Mean values of $kmax$ [cm/s²] for scenario S32 and return periods $TR = 475,\ 2,475,\ 10,000$ yr. 123

Table E2‑4: Mean values of $kmax$ [cm/s²] for scenario S27 and return periods $TR = 475,\ 2,475,\ 10,000$ yr. 124

Table E2‑5: Mean values of $kmax$ [cm/s²] for scenario S35 and return periods $TR = 475,\ 2,475,\ 10,000$ yr. 124

Table E3‑1: Mean values of $kh$ [% of PGA] for scenario S135 and return periods $TR = 475,\ 2,475,\ 10,000$ yr. 125

Table E3‑2: Mean values of $kh$ [% of PGA] for scenario S50 and return periods $TR = 475,\ 2,475,\ 10,000$ yr. 125

Table E3‑3: Mean values of $kh$ [% of PGA] for scenario S32 and return periods $TR = 475,\ 2,475,\ 10,000$ yr. 126

Table E3‑4: Mean values of $kh$ [% of PGA] for scenario S27 and return periods $TR = 475,\ 2,475,\ 10,000$ yr. 126

Table E3‑5: Mean values of $kh$ [% of PGA] for scenario S35 and return periods $TR = 475,\ 2,475,\ 10,000$ yr. 127

# List of Figures {#list-of-figures .TOC-Heading}

Figure 1‑1: Site Location Map 2

Figure 1‑2: Layout of Project Facilities 3

Figure 2‑1: Crustal Regions in Eastern Canada 7

Figure 2‑2: Seismicity of Northern Ontario Seismic Zone 1970-1999 8

Figure 2‑3: Seismicity of Northern Ontario from 1980 to 2006 9

Figure 3‑1: Crawford Regional Catalog 1916-08/30/2026 11

Figure 3‑2: Isoseismal Map of the 1935 Mw 6.2 Temiskamingue Earthquake 12

Figure 5‑1: Source-to-Site Fault Distances 16

Figure 5‑2: Logic Tree in the CanadaSHM6 for Southeastern Canada 18

Figure 6‑1: Annual Exceedance Probability (AEP) in Hard Rock ($Vs,30$ = 1500 m/s) for various Structural Periods – Mean Values 21

Figure 6‑2: Annual Exceedance Probability (AEP) in Hard Rock ($Vs,30$ = 1500 m/s) for various Structural Periods – 84^th^ Percentile Values 22

Figure 6‑3: Annual Exceedance Probability (AEP) in Soft Rock ($Vs,30$ = 760 m/s) for various Structural Periods – Mean Values 23

Figure 6‑4: Annual Exceedance Probability (AEP) in Soft Rock ($Vs,30$ = 760 m/s) for Various Structural Periods – 84^th^ Percentile Values 23

Figure 6‑5: Uniform Hazard Spectra (UHS) in Hard Rock ($Vs,30 =$`<!-- -->`{=html}1,500 m/s) – Mean Values 24

Figure 6‑6: Uniform Hazard Spectra (UHS) in Hard Rock ($Vs,30 =$`<!-- -->`{=html}1,500 m/s) – 84^th^ Percentile Values 25

Figure 6‑7: Uniform Hazard Spectra (UHS) in Soft Rock ($Vs,30 =$`<!-- -->`{=html}760 m/s) – Mean Values 25

Figure 6‑8: Uniform Hazard Spectra (UHS) in Soft Rock ($Vs,30 =$`<!-- -->`{=html}760 m/s) – 84^th^ Percentile Values 26

Figure 6‑9: Hazard Deaggregation of Magnitudes and Distances for PGA – 1:475 AEP 27

Figure 6‑10: Hazard Deaggregation of Magnitudes and Distances for PGA – 1:975 AEP 28

Figure 6‑11: Hazard Deaggregation of Magnitudes and Distances for PGA – 1:2,475 AEP 28

Figure 6‑12: Hazard Deaggregation of Magnitudes and Distances for PGA – 1:5,000 AEP 29

Figure 6‑13: Hazard Deaggregation of Magnitudes and Distances for PGA – 1:10,000 AEP 29

Figure 7‑1: Location of Seismic CPTs used to Estimate Shear Wave Velocity Profiles 33

Figure 7‑2: Shear Wave Velocity Profile at the Crawford Rock, Sand & Till, and Clay Impoundment measured by SCPTu and average $Vs,30$ determined with Eq. 7-1 35

Figure 7‑3: Shear Wave Velocity Profile at the Crawford Open Pit measured by SCPTu and average $Vs,30$ determined with Eq. 7-1 36

Figure 7‑4: Shear Wave Velocity Profile at the Crawford Stockpile East measured by SCPTu and average $Vs,30$ determined with Eq. 7-1 37

Figure 7‑5: Shear Wave Velocity Profile at the Crawford Stockpile West measured by SCPTu and average $Vs,30$ determined with Eq. 7-1 38

Figure 7‑6: Shear Wave Velocity Profile at the Tailings Management Facility (TMF) measured by SCPTu and average $Vs,30$ determined with Eq. 7-1 39

Figure 7‑7: Uniform Hazard Spectra (UHS) in Stiff Soil ($Vs,30 =$`<!-- -->`{=html}220 m/s) – Mean Values 41

Figure 7‑8: Uniform Hazard Spectra (UHS) in Stiff Soil ($Vs,30 =$`<!-- -->`{=html}220 m/s) – 84^th^ Percentile Values 41

Figure 8‑1: Uniform Hazard Spectra (UHS) in Hard Rock ($Vs,30 =$`<!-- -->`{=html}1500 m/s/) for 2,475, 975, and 475-year return periods: Comparison with NRC (2021c) Mean Values 43

Figure 8‑2: Uniform Hazard Spectra (UHS) in Soft Rock ($Vs,30 =$`<!-- -->`{=html}760 ms/) for 2,475, 975, and 475-year return periods: Comparison with NRC (2021c) Mean Values 44

Figure 8‑3: Uniform Hazard Spectra (UHS) in Stiff Soil ($Vs,30 =$ 220 m/s) for 2,475, 975, and 475-year return periods: Comparison with NRC (2021c) Mean Values 45

Figure 9‑1: Design Response Spectra for a Return Period of 10,000 years - Mean Values 48

Figure 9‑2: Design Response Spectra for a Return Period of 10,000 years – 84^th^ Percentile Values 49

Figure 9‑3: Design Response Spectra for a Return Period of 2,475 years - Mean Values 50

Figure 9‑4: Design Response Spectra for a Return Period of 2,475 years – 84^th^ Percentile Values 51

Figure 10‑1: Mean Values of $kh$ [% of PGA] for Return Period $TR = 475$ yr, as a Function of the Allowable Permanent Displacement Relative to Slope Height, $Da/H$ [%]. The Curves Represent the Scenarios S135, S50, S32, S27, S35 Evaluated with the Rigid, Ensemble, and Flexible Sets. 62

Figure 10‑2: Mean Values of $kh$ [% of PGA] for Return Period $TR = 2,475$ yr, as a Function of the Allowable Permanent Displacement Relative to Slope Height, $Da/H$ [%]. The Curves Represent the Scenarios S135, S50, S32, S27, S35 Evaluated with the Rigid, Ensemble, and Flexible Sets. 63

Figure 10‑3: Mean Values of $kh$ [% of PGA] for Return Period $TR = 10,000$ yr, as a Function of the Allowable Permanent Displacement Relative to Slope Height, $Da/H$ [%]. The Curves Represent the Scenarios S135, S50, S32, S27, S35 Evaluated with the Rigid, Ensemble, and Flexible Sets. 64

Figure C1‑1: Annual Exceedance Probability (AEP) in Hard Rock ($Vs,30$ = 1500 m/s) for various Structural Periods – Mean Values 81

Figure C1‑2: Annual Exceedance Probability (AEP) in Hard Rock ($Vs,30$ = 1500 m/s) for various Structural Periods – 50^th^ Percentile Values 81

Figure C1‑3: Annual Exceedance Probability (AEP) in Hard Rock ($Vs,30$ = 1500 m/s) for various Structural Periods – 84^th^ Percentile Values 82

Figure C1‑4: Annual Exceedance Probability (AEP) in Hard Rock ($Vs,30$ = 1500 m/s) for various Structural Periods – 90^th^ Percentile Values 82

Figure C1‑5: Annual Exceedance Probability (AEP) in Hard Rock ($Vs,30$ = 1500 m/s) for various Structural Periods – 90^th^ Percentile Values 83

Figure C1‑6: Annual Exceedance Probability (AEP) in Medium Rock ($Vs,30$ = 910 m/s) for various Structural Periods – Mean Values 83

Figure C1‑7: Annual Exceedance Probability (AEP) in Medium Rock ($Vs,30$ = 910 m/s) for various Structural Periods – 50^th^ Percentile Values 84

Figure C1‑8: Annual Exceedance Probability (AEP) in Medium Rock ($Vs,30$ = 910 m/s) for various Structural Periods – 84^th^ Percentile Values 84

Figure C1‑9: Annual Exceedance Probability (AEP) in Medium Rock ($Vs,30$ = 910 m/s) for various Structural Periods – 90^th^ Percentile Values 85

Figure C1‑10: Annual Exceedance Probability (AEP) in Medium Rock ($Vs,30$ = 910 m/s) for various Structural Periods – 95^th^ Percentile Values 85

Figure C1‑11: Annual Exceedance Probability (AEP) in Soft Rock ($Vs,30$ = 760 m/s) for various Structural Periods – Mean Values 86

Figure C1‑12: Annual Exceedance Probability (AEP) in Soft Rock ($Vs,30$ = 760 m/s) for various Structural Periods – 50^th^ Percentile Values 86

Figure C1‑13: Annual Exceedance Probability (AEP) in Soft Rock ($Vs,30$ = 760 m/s) for various Structural Periods – 84^th^ Percentile Values 87

Figure C1‑14: Annual Exceedance Probability (AEP) in Soft Rock ($Vs,30$ = 760 m/s) for various Structural Periods – 90^th^ Percentile Values 87

Figure C1‑15: Annual Exceedance Probability (AEP) in Soft Rock ($Vs,30$ = 760 m/s) for various Structural Periods – 95^th^ Percentile Values 88

Figure C1‑16: Annual Exceedance Probability (AEP) in Very Dense Soil ($Vs,30$ = 580 m/s) for various Structural Periods – Mean Values 88

Figure C1‑17: Annual Exceedance Probability (AEP) in Very Dense Soil ($Vs,30$ = 580 m/s) for various Structural Periods – 50^th^ Percentile Values 89

Figure C1‑18: Annual Exceedance Probability (AEP) in Very Dense Soil ($Vs,30$ = 580 m/s) for various Structural Periods – 84^th^ Percentile Values 89

Figure C1‑19: Annual Exceedance Probability (AEP) in Very Dense Soil ($Vs,30$ = 580 m/s) for various Structural Periods – 90^th^ Percentile Values 90

Figure C1‑20: Annual Exceedance Probability (AEP) in Very Dense Soil ($Vs,30$ = 580 m/s) for various Structural Periods – 95^th^ Percentile Values 90

Figure C1‑21: Annual Exceedance Probability (AEP) in Stiff Soil ($Vs,30$ = 220 m/s) for various Structural Periods – Mean Values 91

Figure C1‑22: Annual Exceedance Probability (AEP) in Stiff Soil ($Vs,30$ = 220 m/s) for various Structural Periods – 50^th^ Percentile Values 91

Figure C1‑23: Annual Exceedance Probability (AEP) in Stiff Soil ($Vs,30$ = 220 m/s) for various Structural Periods – 84^th^ Percentile Values 92

Figure C1‑24: Annual Exceedance Probability (AEP) in Stiff Soil ($Vs,30$ = 220 m/s) for various Structural Periods – 90^th^ Percentile Values 92

Figure C1‑25: Annual Exceedance Probability (AEP) in Stiff Soil ($Vs,30$ = 220 m/s) for various Structural Periods – 95^th^ Percentile Values 93

Figure C2‑1: Uniform Hazard Spectra (UHS) in Hard Rock ($Vs,30 = \$`<!-- -->`{=html}1500 m/s) - Mean Values 95

Figure C2‑2: Uniform Hazard Spectra (UHS) in Hard Rock ($Vs,30 = \$`<!-- -->`{=html}1500 m/s) - 50^th^ Percentile Values 95

Figure C2‑3: Uniform Hazard Spectra (UHS) in Hard Rock ($Vs,30 = \$`<!-- -->`{=html}1500 m/s) - 84^th^ Percentile Values 96

Figure C2‑4: Uniform Hazard Spectra (UHS) in Hard Rock ($Vs,30 = \$`<!-- -->`{=html}1500 m/s) - 90^th^ Percentile Values 96

Figure C2‑5: Uniform Hazard Spectra (UHS) in Hard Rock ($Vs,30 = \$`<!-- -->`{=html}1500 m/s) - 95^th^ Percentile Values 97

Figure C2‑6: Uniform Hazard Spectra (UHS) in Medium Rock ($Vs,30 = \$`<!-- -->`{=html}910 m/s) – Mean Values 97

Figure C2‑7: Uniform Hazard Spectra (UHS) in Medium Rock ($Vs,30 = \$`<!-- -->`{=html}910 m/s) - 50^th^ Percentile Values 98

Figure C2‑8: Uniform Hazard Spectra (UHS) in Medium Rock ($Vs,30 = \$`<!-- -->`{=html}910 m/s) - 84^th^ Percentile Values 98

Figure C2‑9: Uniform Hazard Spectra (UHS) in Medium Rock ($Vs,30 = \$`<!-- -->`{=html}910 m/s) - 90^th^ Percentile Values 99

Figure C2‑10: Uniform Hazard Spectra (UHS) in Medium Rock ($Vs,30 = \$`<!-- -->`{=html}910 m/s) - 95^th^ Percentile Values 99

Figure C2‑11: Uniform Hazard Spectra (UHS) in Soft Rock ($Vs,30 = \$`<!-- -->`{=html}760 m/s) – Mean Values 100

Figure C2‑12: Uniform Hazard Spectra (UHS) in Soft Rock ($Vs,30 = \$`<!-- -->`{=html}760 m/s) – 50^th^ Percentile Values 100

Figure C2‑13: Uniform Hazard Spectra (UHS) in Soft Rock ($Vs,30 = \$`<!-- -->`{=html}760 m/s) – 84^th^ Percentile Values 101

Figure C2‑14: Uniform Hazard Spectra (UHS) in Soft Rock ($Vs,30 = \$`<!-- -->`{=html}760 m/s) – 90^th^ Percentile Values 101

Figure C2‑15: Uniform Hazard Spectra (UHS) in Soft Rock ($Vs,30 = \$`<!-- -->`{=html}760 m/s) – 95^th^ Percentile Values 102

Figure C2‑16: Uniform Hazard Spectra (UHS) in Very Dense Soil ($Vs,30 = \$`<!-- -->`{=html}580 m/s) – Mean Values 102

Figure C2‑17: Uniform Hazard Spectra (UHS) in Very Dense Soil ($Vs,30 = \$`<!-- -->`{=html}580 m/s) – 50^th^ Percentile Values 103

Figure C2‑18: Uniform Hazard Spectra (UHS) in Very Dense Soil ($Vs,30 = \$`<!-- -->`{=html}580 m/s) – 84^th^ Percentile Values 103

Figure C2‑19: Uniform Hazard Spectra (UHS) in Very Dense Soil ($Vs,30 = \$`<!-- -->`{=html}580 m/s) – 90^th^ Percentile Values 104

Figure C2‑20: Uniform Hazard Spectra (UHS) in Very Dense Soil ($Vs,30 = \$`<!-- -->`{=html}580 m/s) – 95^th^ Percentile Values 104

Figure C2‑21: Uniform Hazard Spectra (UHS) in Stiff Soil ($Vs,30 = \$`<!-- -->`{=html}220 m/s) - Mean Values 105

Figure C2‑22: Uniform Hazard Spectra (UHS) in Stiff Soil ($Vs,30 = \$`<!-- -->`{=html}220 m/s) – 50^th^ Percentile Values 105

Figure C2‑23: Uniform Hazard Spectra (UHS) in Stiff Soil ($Vs,30 = \$`<!-- -->`{=html}220 m/s) – 84^th^ Percentile Values 106

Figure C2‑24: Uniform Hazard Spectra (UHS) in Stiff Soil ($Vs,30 = \$`<!-- -->`{=html}220 m/s) – 90^th^ Percentile Values 106

Figure C2‑25: Uniform Hazard Spectra (UHS) in Stiff Soil ($Vs,30 = \$`<!-- -->`{=html}220 m/s) – 95^th^ Percentile Values 107

Figure D2‑1: Design Response Spectra for a Return Period of 10,000 years - Mean Values 113

Figure D2‑2: Design Response Spectra for a Return Period of 10,000 years – 50^th^ Percentile Values 113

Figure D2‑3: Design Response Spectra for a Return Period of 10,000 years – 84^h^ Percentile Values 114

Figure D2‑4: Design Response Spectra for a Return Period of 10,000 years – 90^h^ Percentile Values 114

Figure D2‑5: Design Response Spectra for a Return Period of 10,000 years –95^h^ Percentile Values 115

Figure E2‑1: Mean values of $kmax$ [$g$] for return period $TR = 475$ yr, as a function of the allowable permanent displacement relative to slope height, $Da/H$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the rigid, ensemble, and flexible sets. 120

Figure E2‑2: Mean values of $kmax$ [$g$] for return period $TR = 2,475$ yr, as a function of the allowable permanent displacement relative to slope height, $Da/H$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the rigid, ensemble, and flexible sets. 121

Figure E2‑3: Mean values of $kmax$ [$g$] for return period $TR = 10,000$ yr, as a function of the allowable permanent displacement relative to slope height, $Da/H$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the rigid, ensemble, and flexible sets. 122

$$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

# Introduction 

## Project Overview

SRK Consulting (Canada.) Inc (SRK) and Paterson and Cooke (P&C), referred herein as SRK-PC, were appointed by Canada Nickel Co. (CNC) to undertake the site-specific seismic hazard assessment at the Crawford project site (the Site). This assessment is part of the engineering analyses supporting the Front-End Engineering Design (FEED) activities for the proposed Rock, Sand & Till, and Clay Impoundment Facilities, Lower Value Stockpiles (stockpiles), soil and rock slopes for the open pits, and the Surface Tailings Management Facility (TMF) for the Crawford Project.

The Crawford site is located in Crawford and Lucas townships with portions in Mahaffy and Carnegie townships, about 42 km north of the City of Timmins, Ontario, as shown in [**Figure 1‑1**](#_Ref169701304). The approximate coordinates of the project facilities are listed in [**Table 1‑1**](#_Ref178150910). The layout of the facilities is shown in [**Figure 1‑2**](#_Ref174486855).

  ----------------------------------------- ----------------- ---------------
  Facility                                  Latitude          Longitude

  Open Pit and Stockpiles                   48.8338°N         81.3558°W

  Rock, Sand & Till, and Clay Impoundment   48.8719°N         81.3595°W

  TMF                                       48.7949°N         81.3406°W
  ----------------------------------------- ----------------- ---------------

  : []{#_Ref178150910 .anchor}Table 1‑1: Crawford Project Site Coordinates

![[]{#_Ref169701304 .anchor}Figure 1‑1: Site Location Map](./media/image3.png){width="8.954939851268591in" height="5.632075678040245in"}

![](./media/image4.png){width="8.968588145231847in" height="5.75in"}

[]{#_Ref174486855 .anchor}Figure 1‑2: Layout of Project Facilities

## Scope of Work

The scope of work, as defined in the proposal presented on June 7, 2024, between CNC and SRK-PC, includes the development of a Site-Specific Hazard Assessment for the Crawford Project, characterization the dynamic response of the slopes on specific dams and stockpiles, and preparation of a technical report. This work typically involves the assessment of the following aspects of this project:

- Review of project background and seismotectonic framework, geotechnics, and historical seismicity. Update of the seismic catalog representing seismicity at the Site.

- Identify and characterize seismogenic sources capable of generating significant ground motions within a 400-km radius of the project site. Select an appropriate source model.

- Select a suite of ground motion prediction equations (GMPEs) and develop a logic tree framework that address epistemic uncertainty.

- Conduct a full probabilistic seismic hazard assessment (PSHA) for the site, estimating annual exceedance probability (AEP) of ground accelerations for rock site conditions, Peak Ground Acceleration (PGA), and Uniform Hazard Spectra (UHS).

- Estimate the site response for specific geotechnical conditions at the Site using an empirical method. Determine site classification in accordance to the 2020 National Building Code of Canada (Canadian Comission on Building and Fires Codes and National Research Council of Canada, 2020) and using available geotechnical data.

- Define maximum design earthquakes (MDE) in accordance with guidelines from the Canadian Dam Association CDA (2013), Global Industry Standard on Tailings Management GISTM (International Council on Mining & Metals (ICMM), 2020), ICOLD, ANCOLD, and Seismic Hazard Criteria from the Ontario Ministry of Natural Resources (MNR) (2011).

- Define horizontal seismic coefficients for the MDE, for a range of acceptable permanent deformations in the project embankments.

- Prepare a comprehensive technical report summarizing the relevant results from the seismic hazard assessment.

## Organization of This Report

The report comprises eleven chapters and four appendices. 

- **Chapter [1](#introduction)** corresponds to the introduction to the project, background, objectives, and scope. 

- **Chapter [2](#seismotectonics)**  describes the seismotectonics framework of the area to provide an understanding of the sources that may be seismically active. 

- **Chapter [[3](#seismicity)](https://nauspr001130.srk.ar/qmd/seismicity/)** presents a brief description of the seismicity study area (defined within 400-km radius of the Site), which includes the development of a regional seismicity catalog compiled and updated to include events up to August 30, 2026 and a brief description of the most significant historic earthquakes in the seismicity study area. 

- **Chapter [4](#seismic-source-model)** describes the source model and characterizes sources capable of producing significant ground-motion at the Site to be used in the probabilistic hazard assessment. 

- **Chapter [5](#ground-motion-intensity-model)** presents the ground motion models selected to be used in the seismic hazard analysis to estimate the strong ground motion that may occur at the Site if an earthquake of a certain magnitude occurs at a nearby location. 

- **Chapter [6](#seismic-hazard)** presents the development of seismic hazard analysis in rock including hazard deaggregation, to identify contributing events for a given ground motion intensity and annual exceedance probability (AEP) or return period. 

- **Chapter [7](#site-response)** presents the site response to determine ground motions at the surface level. Chapter []{.mark}[6.5](#controlling-scenarios) also includes the characterization of the site foundation in terms of the average shear wave velocity to a depth of 30 m ($V_{s,30}$) using information from the past field geotechnical and geophysical investigations of 2021-2022 and 2023.

- **Chapter [8](#national-building-code-of-canada-seismic-hazard-values)** provides a comparison of the seismic hazard estimates developed for this study with the 2020 National Building Code of Canada.

- **Chapter [9](#design-earthquakes)** summarizes design events for this study selected for a target AEP.

- **Chapter [10](#slope-design-parameters)** provides estimates of slope design parameters, including seismic (pseudo-static) coefficients ($k_{h}$) using empirical correlations. Values of $k_{h}$ are presented for the selected design event and for a range of target displacements (𝑑𝑎) for various embankment materials (in terms of shear wave velocities) and embankment geometries. 

- **Chapter [11](#conclusions)** provides conclusions of the present study.

The report also includes four appendices.

- **Appendix A presents the Crawford updated seismic catalog of events (Table A-1).**

- **Appendix B lists the seismic sources of the CanadaSHM6 Southeast HY, H2 and R2 models (Tables B-1 to B-3).**

- **Appendix C presents the seismic hazard results as annual exceedance probability curves and uniform hazard spectra.**

- **Appendix D presents the design earthquakes as design peak ground acceleration and design response spectra for the return periods and site conditions considered.**

[]{#_Ref174451674 .anchor}

# Seismotectonics

Seismotectonics refers to the relationship between earthquake epicentral locations and active tectonic processes. In any given region, this relationship is governed by the relative motions of the Earth's lithospheric plates, which include both crustal and oceanic plates. These crustal plates can be further divided into older, more stable cratons and younger, less stable mobile belts. The interactions and relative movements of these plates generate regional stress fields, which are the primary drivers of tectonic earthquakes.

The main objective of this section is to outline the seismotectonic framework of the Site, providing insight into which sources may be seismically active.

## Seismotectonic Framework in Southeastern Canada

Eastern Canada, spanning east of the Cordillera from the United States border to the Arctic Ocean, constitutes approximately two-thirds of the stable craton of the North American plate. While majority of this area appears to be predominantly of low seismicity, it contains several zones of concentrated seismic activity, particularly along the eastern continental margin and in specific clusters within the craton. The Natural Resources of Canada (NRC) (2021a) has grouped these seismic clusters in seven regions, as shown in **[Figure 2‑1](#_Ref171095102).**

1.  Northern Ontario (NON)

2.  Southern Great Lakes (SGL)

3.  West Quebec (WQU)

4.  Charlevoix-Kamouraska (CHV)

5.  Lower St. Lawrence (BSL)

6.  Northern Appalachians (NAP)

7.  Laurentian Slope (LSP)

![[]{#_Ref171095102 .anchor}Figure 2‑1: Crustal Regions in Eastern Canada](./media/image5.png){width="5.917743875765529in" height="3.8146030183727033in"}

Source: <https://www.seismescanada.rncan.gc.ca/zones/eastcan-en.php> (Natural Resources of Canada, 2021a)

The Site is located in the Northern Ontario region (NON in [**Figure 2‑1**](#_Ref171095102)), which extends from the Great Lakes to Hudson Bay. The physiography of Northern Ontario exemplifies a recently deglaciated shield terrain, characterized by numerous lakes, large exposures of crystalline bedrock, and glacial till deposits of variable thickness (Ma, Eaton, & Adams, 2008).

Although Northern Ontario earthquake activity rate is low as is part of the stable continental region, large and damaging earthquakes have occurred. Notable intraplate seismicity has been observed, as depicted in [**Figure 2‑2**](#_Ref170738783) (Natural Resources of Canada, 2021a) and [**Figure 2‑3**](#_Ref171088203) (Ma, Eaton, & Adams, 2008). The causes of earthquakes in this region have been primarily linked to:

a.  Glacial Isostatic Adjustment (GIA): ongoing process of the Earth's crust to rebound from the weight of the last ice sheets tat has been associated with seismicity in Northern Ontario (Ma, Eaton, & Adams, 2008) (Mazzotti, 2005) (Wu & Hasegawa, 1996), and crustal faults and fractures (Adams & Basham, 1991).

b.  Regional intraplate stress: intraplate stress caused by ongoing deformation of the plate, including residual effects of ancient tectonic processes and current tectonic forces that can induce earthquakes (Natural Resources of Canada, 2021a; Adams & Basham, 1991).

c.  Crustal faults and fractures: Existing weaknesses in the crust can be reactivated by the stresses associated with GIA and intraplate tectonic forces, leading to seismic events (Adams & Basham, 1991).

![[]{#_Ref170738783 .anchor}Figure 2‑2: Seismicity of Northern Ontario Seismic Zone 1970-1999](./media/image6.gif){alt="Map of historic events in the Northeastern Ontario Seismic Zone" width="5.936833989501312in" height="6.552083333333333in"}

Source: <https://www.seismescanada.rncan.gc.ca/zones/eastcan-en.php> (Natural Resources of Canada, 2021a)

![[]{#_Ref171088203 .anchor}Figure 2‑3: Seismicity of Northern Ontario from 1980 to 2006](./media/image7.emf){width="5.931034558180228in" height="4.776510279965004in"}

Source: Ma, Eaton & Adams (2008)

[]{#_Ref174451708 .anchor}

# Seismicity

## Seismicity Catalog

The historical seismicity record used in this study for the Crawford project, was compiled using the following three publicly available databases:

a.  National Resources of Canada (NRCAN) Earthquake Database: This database developed by the Government of Canada (2021b) provides seismic data from 1985 to present (<https://www.earthquakescanada.nrcan.gc.ca/stndon/NEDB-BNDS/bulletin-en.php>)

b.  Canadian Composite Seismicity Catalog (CCSC11) for East Canada: This catalog contains seismic events recorded from 1534 to 2010 ([seismotoolbox.ca/Documents/ccsc11east.txt](https://www.seismotoolbox.ca/Documents/ccsc11east.txt)).

c.  Earthquake Data Auto-Processor (EDAP): developed by K. Assatourians and G. Atkinson (2016), this tool provides automatically generated interactive ground motion maps for Southern Ontario, with data from February 25, 2010, to February 2, 2021 (<https://www.seismotoolbox.ca/edap/index.php>).

The spatial criteria for searching the available earthquake databases for the catalog update included events occurring within 400-km radius of the Site (coordinates latitude 48.834° North and longitude 81.356° West) from January 1, 1534, to August 30, 2026.

The combined, updated, and declustered catalog contains 67 events within the study area with moment magnitudes (Mw) ≥ 3, as shown in [**Figure 3‑1**](#_Ref178151259) of which 67 have Mw ≥ 3, and listed in []{.mark}[**Table A‑1**](#_Ref178166773). These events span the period from 1916 to August 30, 2026. Declustering to remove dependent aftershocks and foreshocks followed the Gardner and Knopoff (1974) statistical method. It was applied to the combined multi-source catalog before selecting the Mw ≥ 3 subset. Records of one source catalog within 10 s and 100 km of a larger or equal event of that catalog were also removed before declustering, because they are alternative solutions of a single earthquake. The updated catalog was used solely to illustrate the most current seismicity in the project site region and was not used to update to recurrence in the 2020 National Building Code of Canada (2020 NBCC) (Canadian Comission on Building and Fires Codes and National Research Council of Canada, 2020).

The minimum magnitude considered in the Canada Southeast Model Seismic Sources, discussed further in **Section [4](#seismic-source-model)** ($M_{\min} =$`<!-- -->`{=html}4.8), is higher than the maximum magnitude registered in the region. The exception is the Temiskamingue M 6.2 event on November 1, 1935, which had its epicenter approximately 285 km southeast of the Site.

![](./media/image9.png){width="6.5in" height="5.2in"}

[]{#_Ref178151259 .anchor}Figure 3‑1: Crawford Regional Catalog 1916-08/30/2026

## 

## Historical Seismicity

The most significant historic earthquake in the study area was the 1935 Temiskamingue earthquake, which had a magnitude of Mw 6.2. Following this, the 1928 earthquake near Otter Rapids and the 2000 Kipawa earthquake, both with magnitudes of Mw 4.7, were the second and third largest events, respectively. The most recent event in the region occurred on November 15, 2025, with a magnitude of Mw 3.7, located 50 km north of Factory Island, Ontario, approximately 324 km north of the Site.

### The 1935 Mw 6.2 Temiskamingue Earthquake

On November 1, 1935, at 1:03 am local time, an earthquake occurred about 10 km east of Témiscaming, Québec, approximately 285 km southeast of the Site. The earthquake was felt as far west as Thunder Bay, Ontario (later known as Fort William), as far east as the Bay of Fundy, and as far south as Kentucky and Virginia (Natural Resources of Canada, 2021d).

In Témiscaming, Québec, around 80% of chimneys were damaged, indicating a Modified Mercalli intensity of VII. Cracks also appeared in brick walls, and minor rockfalls were observed in the epicentral area. The shake caused significant damage in nearby Mattawa and North Bay, where many chimneys were destroyed. Numerous aftershocks were felt in Témiscaming and Kipawa in the months that followed. The day after the earthquake, Tee Lake's water near the epicenter was discolored, likely due to the resuspension of gyttja (freshwater mud). Additionally, 300 km away near Parent, Québec, the earthquake triggered a 30-meter railroad embankment slide (Natural Resources of Canada, 2021d).

![Figure 3‑2: Isoseismal Map of the 1935 Mw 6.2 Temiskamingue Earthquake](./media/image10.png){width="4.305555555555555in" height="4.111805555555556in"}

Source: Natural Resources of Canada (2021d).

### The 2000 Magnitude Mw 4.7 Kipawa Earthquake 

On January 1, 2000, an Mw 4.7 earthquake occurred beneath Lac Kipawa, about 10 km north of the town of Témiscaming, Quebec, and approximately 286 km southeast of the Site. The earthquake was felt over distances exceeding 500 km. Residents within 50 km of the epicenter reported intense shaking (intensity MM VI), which caused minor damage, including fallen light objects, a broken ventilation pipe, and cracks in plaster. The earthquake was felt in Témiscaming, North Bay, and as far away as Toronto, making it one of Canada's most significant earthquakes in 2000 (Natural Resources de Canada, 2013).

[]{#_Ref174031794 .anchor}

# Seismic Source Model

## Definitions

The earthquake sources capable of generating significant ground motion at the site are identified and characterized using source models. This characterization involves defining the source geometry and the probability distributions of potential rupture locations within each source. The source models are classified into the following four seismic source model types:

1.  Background Area-Source Models: These models use broad geographic zones where earthquakes can occur anywhere with equal probability.

2.  Regional Area-Source Models: These models account for the non-uniform spatial distribution of seismicity at a regional scale, using historical seismicity patterns to forecast future earthquake occurrences.

3.  Seismotectonic Models: These models integrate regional source models with fault-source models to provide a more comprehensive understanding of seismic potential.

4.  Smoothed Seismicity Models: These data-driven models assume that historical seismicity is a reliable predictor of future seismic hazards, combining short-term data from the instrumental catalog with long-term geological information from fault-source models.

Each model type contributes unique insights to probabilistic hazard assessments. Additional epistemic uncertainty is addressed during the model parameterization process.

## The 6^th^ Generation Seismic Hazard Model of Canada

The 6th Generation Seismic Hazard Model of Canada (CanadaSHM6) (Natural Resources of Canada, 2020) is adopted for the present study as implemented in the Global Earthquake Model (GEM) for Canada (Global Earthquake Model (GEM) Foundation, 2018). This model was used to generate the seismic hazard values of 2020 NBCC (Canadian Comission on Building and Fires Codes and National Research Council of Canada, 2020). The CanadaSHM6 consists of three separate regional models:

1.  The Western Model.

2.  The East Artic Model.

3.  The Southeastern Model.

The Project Site falls within the Southeastern Model, which is further divided into three sub-models: H2, Hybrid HY, and R2, with respective weightings of 0.4, 0.4, and 0.2.

Earthquake rates are generally described in terms of a truncated distribution proposed by Gutenberg-Richter (Gutenberg & Ritcher, 1944) to describe the frequency of earthquakes as a function of their magnitude. Earthquake rates in the CanadaSHM6 are described in terms of a discretized incremental frequency distribution using the Gutenberg-Richter $a$ and$\ b$ values as follows:

$N_{0} = 10^{a}$ **[Eq. 4‑1]**

$\beta = ln({10)}^{b}$ **[Eq. 4‑2]**

where $N_{0}$ is the number of earthquakes per year with magnitude greater than or equal to 0 and $\beta$ is a constant that describes the relative number of small to large earthquakes.

[Table B‑1](#_Ref178166524)through [Table B‑3](#_Ref178166543) in [**11Appendix B**](#southeastern-model-seismic-sources-of-the-canadashm6) list the source faults, and their characteristics included in the H2, HY, and R2 sub-models of the CanadaSHM6 Southeastern Model.

[]{#_Ref174451752 .anchor}

# Ground Motion Intensity Model

## Definitions

### Ground Motion Intensity Models

Seismic ground motion is generally characterized by a scalar (spectral) measure of intensity\
$I = i^{*}$. The seismic intensity of site $i^{*}$, depends on the distance from the site to the nearest point on fault $r^{*}$ and the magnitude of the seismic event, $m^{*}$, which is directly related to the size of the fault rupture area.

Ground-motion intensity models, also known as ground motion models (GMM) or ground motion prediction equations (GMPE), are typically derived from strong ground motion recordings. For a seismic event of magnitude $m^{*}$ occurring at a distance $r^{*}$, the seismic intensity $i^{*}$ can be estimated in terms of a probabilistic model with a conditional mean $\eta_{I|M,R}$, expressed as follows:

$\eta_{I|M,R} = \phi_{I}\left( m^{*},r^{*},\theta \right) + \varepsilon$ **[Eq. 5‑1]**

This equation represents a regression model that incorporates $m^{*}$, $r^{*}$, and geological and geotechnical site conditions, denoted by $\theta.\$The model includes an error term $\varepsilon$, with has a mean $E\lbrack ln\varepsilon\rbrack = 0$ and variance $var\lbrack ln\varepsilon\rbrack = \left( \sigma_{I} \right)^{2}$.

In general, there are often insufficient strong ground-motion records available for a specific region to develop a site-specific GMPE model. To address this epistemic uncertainty, multiple models defined for similar tectonic regimes are combined using logic trees, with weights selected by expert judgement. The ground-motion intensity for a given hazard level $\beta$ can be estimated by a weighted sum of ground-motion intensities from different models for a given target event characterized by $M = m^{*}$and $R = r^{*}$:

${\tilde{i}}^{*} \approx \sum_{b = 1}^{N_{b}}{w_{b}\ \eta_{I}^{(b)}\left( m^{*},r^{*} \right)}\ \left( \sigma_{I} \right)^{\beta}$ **[Eq. 5‑2]**

where $w_{b}$is the weight assigned to the $b$-th branch of the logic tree, $\eta_{I}^{(b)}\left( m^{*},r^{*} \right)$ is the ground motion intensity model, and $\sigma_{I}$ is the standard deviation of the ground motion intensity model. A minimum number $N_{b}$ of independent region-specific ground-motion model were selected to capture the expected range of possible ground-motions in the target region. These models were chosen based on the guidelines from Bommer and Scherbaum (2008) and are weighted within logic trees to reflect their relative confidence, as determined by the available information.

### Fault Distance Metrics

Most ground-motion intensity models are defined in terms of finite fault distance metrics that assume a planar rupture geometry. The rupture trace is defined as the projection of the top edge of the rupture on the ground surface. The rupture plane, along with its trace and surface projection, allows for the definition of four finite fault distance metrics: $R_{RUP}$, $R_{JB}$ ,$R_{X}$, and $R_{Y0}$.

- The rupture distance $R_{RUP}$ is the distance from the site to the closest point on the rupture plane.

- The Joyner-Boore distance $R_{JB}$ is the shortest distance between the site and the surface projection of the rupture plane.

- The auxiliary parameters $R_{X}$, $R_{Y0}$ and $Z_{TOR}$ represent the coordinates from the site to the closest point of the top of the rupture.

[**Figure 5‑1**](#_Ref174108027) illustrates various metrics used to measure source-to-site distances. A comprehensive description of these finite fault metrics is provided in Kaklamanos, Baise & Boore (2010).

![[]{#_Ref174108027 .anchor}Figure 5‑1: Source-to-Site Fault Distances](./media/image11.jpg){width="4.166666666666667in" height="3.1330030621172353in"}

### Probability Distributions

The transformation usually performed on random variables associated with the occurrence of seismic events is the logarithmic transformation. This is to assuming that the logarithms of intensities follow a normal distribution. Under this transformation, the seismic intensity is described by a new normalized random variable $\beta_{I}$, with mean value $E\left\lbrack \beta_{I} \right\rbrack = 0$ and variance $var\left\lbrack \beta_{I} \right\rbrack = 1$, meaning it has a zero mean and unit variance.

$\beta_{I}(i,m,r) \approx \frac{\ln\ i - \ln\left\lbrack \eta_{I}(i,m,r) \right\rbrack}{\sigma_{\ln\ I}}$ **[Eq. 5‑3]**

From this transformation, the cumulative distribution functions (CDFs) $P\left\lbrack I > i^{*}/m^{*},r^{*} \right\rbrack$, can be explicitly defined in terms of the cumulative normal density function $Phi_{C}\left( \beta_{I}^{*} \right) = 1 - \Phi\left( \beta_{I}^{*} \right)$. The seismic intensity exceedance probability for a given scenario $r_{s}^{*},m_{s}^{*}$ can be obtained from this relationship:

$P\left\lbrack I > i^{*} \right\rbrack \approx \ \Phi_{C}\left\lbrack \beta_{I}\left( i^{*},r_{s}^{*},m_{s}^{*} \right) \right\rbrack$ **[Eq. 5‑4]**

Using the Total Probability Theorem (TPT), the annual exceedance rate of earthquakes with magnitude greater than $m^{*}$ can be expressed in terms of an asymptotically truncated Gutenberg-Richter magnitude-frequency distribution. The discrete mass probability for magnitudes, $P\left\lbrack M = m_{j} \right\rbrack^{(s)} = f_{M}^{(s)}\left( m_{j} \right)\, dM$, can be obtained from the first derivative of the magnitudes cumulative-density function $F_{M}^{(s)}\left( m_{j} \right)$ valid for $M_{\max}^{(s)} < m^{*} < M_{o}^{(s)}$:

$\lambda^{(s)}\left\lbrack M > m^{*} \right\rbrack = \lambda_{M}^{(s)}\left( m^{*} \right) = \nu_{o}^{(s)}\left( 1 - F_{M}^{(s)}\left( m^{*} \right) \right) \simeq \nu_{o}^{(s)}\frac{e^{- \beta\left( m^{*} - M_{o}^{(s)} \right)}}{1 - e^{- \beta\left( M_{\max}^{(s)} - M_{o}^{(s)} \right)}}$ **[Eq. 5‑5]**

The discrete mass probability function for distances, $f_{R / M}^{(s)}\left( r^{*}|m^{*} \right)dr^{*} = P\left\lbrack R = r^{*}|m^{*} \right\rbrack^{(s)}$, can be obtained numerically from the histogram of an array of epicentres within the boundaries of each seismic source.

## Ground Motion Models for Southeastern Canada

For the stable crust of Southeastern Canada, the CanadaSHM6 adopted two sets of ground GMMs, each with a probability of 0.5.

The first set of GMMs was provided by Atkinson and Adams (2013) hereafter referred to as AA13. This set was developed for eastern stable crustal earthquakes and included three GMMs to account for epistemic uncertainty. These three models were termed “upper,” “central,” and “lower” GMMs, with associated weights of 0.25, 0.50, and 0.25, respectively. The central GMM in AA13 is constructed by taking the arithmetic average of five candidate GMMs. The upper and lower GMM curves are obtained by adding and subtracting the standard deviation (in the logarithmic scale), each with a weight of 0.25. The central GMM represents the median curve with a weight of 0.50.

The second set, based on the Central and Eastern North America project (NGA-East-13), was provided by Goulet et al (2017). The NGA-East-13 is obtained by weighting a set of 13 candidate GMMs using weights that depend on the natural vibration period ($T_{n}$). The standard deviation for NGA-East-13 is the same as that for AA13.

The GMMs for the Southeastern CanadaSHM6 and their approximate ranges of applicability are shown in [Table 5‑1](#_Ref178151403)

.

+:---------------:+--------------------------------------------------------------------------------------------------------------------------------+--------------------------+--------+------------------------------------+-----------+-----------------------------------+
| Tectonic Regime | GMM                                                                                                                            | Number of GMM candidates | Weight | $\mathbf{V}_{\mathbf{s,30}}$ (m/s) | PGV (m/s) | $\mathbf{T}_{\mathbf{\max\ }}$(s) |
+-----------------+--------------------------------------------------------------------------------------------------------------------------------+--------------------------+--------+------------------------------------+-----------+-----------------------------------+
| Stable Crust    | AA13                                                                                                                           | 5                        | 0.5    | 760                                | Yes       | 10                                |
|                 |                                                                                                                                |                          |        |                                    |           |                                   |
|                 | (Atkinson & Adams, Ground motion prediction equations for application to the 2015 Canadian national seismic hazard maps, 2013) |                          |        |                                    |           |                                   |
|                 +--------------------------------------------------------------------------------------------------------------------------------+--------------------------+--------+------------------------------------+-----------+-----------------------------------+
|                 | NGA-East-13                                                                                                                    | 13                       | 0.5    | 3,000                              | Yes       | 10                                |
|                 |                                                                                                                                |                          |        |                                    |           |                                   |
|                 | (Goulet, et al., 2017)                                                                                                         |                          |        |                                    |           |                                   |
+-----------------+--------------------------------------------------------------------------------------------------------------------------------+--------------------------+--------+------------------------------------+-----------+-----------------------------------+

: []{#_Ref178151403 .anchor}Table 5‑1: Ground Motion Models for the CanadaSHM6

Notes:

$V_{s,30}$: shear wave velocity in the upper 30 m (m/s)

$PGV$: Peak ground velocity (m/s)

$T_{\max\ }$: Maximum period (s)

## Epistemic Uncertainty for the Southeastern Canada Seismic Hazard Model 

Epistemic uncertainty in model parameters is addressed using the logic tree shown in **\
[Figure 5‑2](#_Ref171359863)** for the CanadaSHM6 Southeastern Model. Each source region includes preferred values (central, c) for the maximum magnitude ($M_{\max})\$and recurrence parameters ($N_{0}$ and $b$ pairs), which are assigned the highest weights in the logic tree. Additionally, each parameter has an "upper" (u) and a "lower" (l) value, which are assigned lower weights.

![](./media/image12.png){width="6.083333333333333in" height="2.9006321084864393in"}

[]{#_Ref171359863 .anchor}Figure 5‑2: Logic Tree in the CanadaSHM6 for Southeastern Canada

Source: (Kolaj, Adams, & Halchuk, 2020). Note: The symbols mu, mc, ml, bu, bc, and bl refer to the upper, central (preferred) and lower values for $\mathbf{M}_{\mathbf{\max}}$ and magnitude recurrence parameters, respectively. Note that the b-branches are composed of $\mathbf{N}_{\mathbf{0}}$ and $\mathbf{b}$-value pairs (e.g., “bc” refers to $\mathbf{N}_{\mathbf{0}}$c and bc). The logic-tree weights for the NGA-East Ground Motion Models depend on the ground motion parameter (Goulet, et al., 2017)

# Seismic Hazard

## Definitions

### Seismic Hazard Assessment

The probability of exceeding a certain level of seismic intensity $i^{*}$ at a given location is known as the seismic hazard of the site and can be estimated from the contribution of intensities from the different active faults of interest in the region.

A deterministic seismic hazard assessment (DSHA) postulates the existence of a seismic scenario where the maximum rupture size and the location of possible hypocenters are assumed to be known, upon which a ground-motion hazard evaluation is based. The controlling scenario from all possible seismic scenarios defines the maximum credible earthquake (MCE) in terms of magnitude and source-to-site distances.

Due to the random nature associated with the location of earthquake hypocenters and the size of the rupture area associated with during a seismic event, the distance to the fault $R$ and the magnitude M are random variables that express in a simplified way the temporal and spatial variability, respectively, of the seismic motion.

A seismic event at a known location $R = r_{S}^{*}$ and rupture size $M = m_{S}^{*}$, with a proper ground-motion intensity model $\eta_{I}$ $\eta_{I}^{*}$, defines a seismic scenario with the following ground-motion intensity:

$P\left\lbrack I > i^{*} \right\rbrack \approx P\left\lbrack I > i^{*}/M = m_{S}^{*},R = r_{S}^{*} \right\rbrack$ **[Eq. 6‑1]**

A *probabilistic seismic hazard assessment* (PSHA) quantifies the contributions of all sources for all possible magnitudes within the affected area. In the same way as a DSHA, the PSHA stages identify all earthquake sources capable of producing significant ground-motion at the site and captures the expected range of all possible ground-motions in the target region. For a given source $(s)$:

$P\left\lbrack I > i^{*} \right\rbrack^{(s)} \approx \sum_{all\ m^{*}}^{}{\sum_{all\ r^{*}}^{}P}\left\lbrack I > i^{*}/m^{*},r^{*},\theta^{*} \right\rbrack\ P\left\lbrack M = m^{*},R = r^{*} \right\rbrack$ **[Eq. 6‑2]**

The spatial variability is given by all possible locations of the hypocenters of future seismic events that may affect the site. Temporal variability, on the other hand, is associated with the number of events per unit time that we should expect in each region and can be linked to the seismic magnitude and rupture area through the Guttenberg-Richter (1944) probability model.

The fundamental difference between PSHA and DSHA methodologies, is the inclusion of random uncertainty in the calculation of the spatial and temporal distribution of earthquakes, as well as the (aleatory) uncertainty associated with the ground-motion models.

DSHA analyses are not needed in geologically stable regions where major active fault systems capable of producing large earthquakes are absent. With no known active faults, the likelihood of a significant earthquake is low. In such areas, the deterministic approach, which relies on identifying the maximum credible earthquake from known faults, becomes less relevant.

### Annual Exceedance Probability

The annual exceedance probability (AEP) is the rate of exceedance of a specific level of seismic intensity due to the potential occurrence of earthquakes from that source over a one-year period. The Return Period $T_{R}$ is defined as the inverse of the total AEP:

$T_{R} = 1/\lambda_{I}\left( i^{*} \right) = - T_{e}/ln\left( 1 - P_{T_{e}}\left\lbrack I > i^{*} \right\rbrack \right)$ **[Eq. 6‑3]**

The methodology employed for estimating the AEP is based on the Cornell-McGuire methodology (Cornell C. A., 1968) (McGuire, 1993) (Kramer, 1996), which combines earthquake occurrence models, seismic source zone models, magnitude-recurrence relationships, and ground-motion intensity models through the total probability theorem. Assuming the occurrence of earthquakes follows a Poisson process, the probability that a certain strong motion intensity $I$ exceeds a certain value $i^{*}$ during a time interval $T_{e}$ is given by:

$P_{T_{e}}\left\lbrack I > i^{*} \right\rbrack = 1 - \exp\left( - \lambda_{I}\left( i^{*} \right)\, T_{e} \right)$ **[Eq. 6‑4]**

where $\lambda_{I}\left( i^{*} \right)$ is the annual rate of exceedance and $T_{e}$ is the exposure time. For a given source, the annual rate of exceedance of an intensity target level $i^{*}$ $\lambda_{I}\left( i^{*} \right)$ can be expressed by the Total Probability Theorem (TPT):

$\lambda_{I}^{(s)}\left( i^{*} \right) \simeq \nu_{o}^{(s)}\sum_{N_{R}}^{}{\sum_{N_{M}}^{}P}\left\lbrack I > i^{*}|m_{j},r_{k} \right\rbrack^{(s)}f_{M}^{(s)}\left( m_{j} \right)\,\Delta m\, f_{R|M}^{(s)}\left( r_{k}|m_{j} \right)\Delta r$ **[Eq. 6‑5]**

where $M_{\max}^{(s)}$ is the maximum earthquake size of the source $(s)$ and $\nu_{o} = P\left\lbrack M > M_{o}^{(s)} \right\rbrack$ is the annual frequency of occurrence of earthquakes with magnitude greater than a minimum value $M_{o}$. The conditional probability $P\left\lbrack I > i^{*} \right\rbrack$ can be obtained by assuming a probability distribution law for the seismic intensity I. Details of probability density functions used in the proposed model can be found in **Section [5.1.3](#probability-distributions).**

### Peak Ground Acceleration and Response Spectra

The peak ground acceleration (PGA) is an intensity measure of the maximum acceleration (in absolute value) that occurred during an earthquake. The PGA value for different fractiles and service levels is obtained from the spectral ordinates evaluated at a structural period of $T_{n} = 0$.

The spectral ordinate $S_{a}\left( T_{n} \right)$ is the maximum acceleration reported by a single-degree-of-freedom (SDOF) oscillator with fundamental period $T_{n}$ and represents the seismic ground-motion defined of a given target service level for each structural period. The response spectra represent the uniform hazard spectra (UHS) for all spectral ordinates $S_{a}\left( T_{n} \right)$ expressed in terms of the SDOF’s fundamental period $T_{n}$ for a given target AEP. The UHS represents spectral ordinates $S_{a}\left( T_{n} \right)$ with the same probability of exceedance defined for all structural periods $T_{n}$.

## Seismic Hazard Results

A PSHA for the Site was conducted using the CanadaSHM6 hazard model (Natural Resources of Canada, 2020) as implemented in the OpenQuake engine v.3.26.2 (Pagani, Monelli, & Weatgerill, 2014). The AEP curves present the direct logic-tree calculation. The tabulated design values and UHS combine this evaluation with the ST20 transformation of the demand at the reference condition of 760 m/s, conditioned on the PGA of the same realization. The results are presented in terms of AEP and UHS for various site conditions as defined by the 2020 NBCC (Canadian Comission on Building and Fires Codes and National Research Council of Canada, 2020). Site classification, described in **Section [7.1](#site-class),** are based on a shear wave velocity profile measured from the ground surface to a depth of 30 meters ($V_{s,30}$).

Seismic hazard results for the Site are provided in this section for hard rock site conditions (Site Class A, $V_{s,30} =$ 1500 m/s) and soft rock site conditions (Site Class B/C, $V_{s,30} =$ 760 m/s). Seismic hazard results for the soil conditions present at the Site are provided in **Section [7](#site-response)**. Seismic hazard results for medium rock site conditions ($V_{s,30} =$ 910 m/s) are included in [**11Appendix C**](#seismic-hazard-results-1).

### Annual Exceedance Probability

[**Figure 6‑1**](#_Ref178151472) and [**Figure 6‑2**](#_Ref174527344) present the AEP for hard rock site conditions (with $V_{s,30}$ = 1500 m/s) in terms of pseudo-acceleration $(S_{a\ })$ for various structural periods$\ {(T}_{n})$, ranging from 0 seconds (PGA) to 2.5 seconds. [**Figure 6‑1**](#_Ref178151472) presents the mean values, while **[Figure 6‑2](#_Ref174527344)** shows the 84th percentile values. Additional results for other site classes, such as medium rock ($V_{s,30} =$ 910 m/s) and other percentiles (50^th^, 90^th^, and 95^th^) are included in [**11Appendix C1**](#annual-exceedance-probability-2).

![[]{#_Ref178151472 .anchor}Figure 6‑1: Annual Exceedance Probability (AEP) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 1500 m/s) for various Structural Periods – Mean Values](./media/diana-hazard-6-1.png){width="5.5in" height="3.99in"}

![[]{#_Ref174527344 .anchor}Figure 6‑2: Annual Exceedance Probability (AEP) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 1500 m/s) for various Structural Periods – 84^th^ Percentile Values](./media/diana-hazard-6-2.png){width="5.5in" height="3.99in"}

**[Figure 6‑3](#_Ref174529699)** and [**Figure 6‑4**](#_Ref174969545) present AEPs for soft rock site conditions ($V_{S,30}$ = 760 m/s) in terms of pseudo-accelerations $(S_{a\ })$ for various structural periods$\ {(T}_{n})$, ranging from 0 seconds (PGA) to 2.5 seconds. **[Figure 6‑3](#_Ref174529699)** presents the mean values, while **[Figure 6‑4](#_Ref174969545)** shows the 84^th^ percentile values.

![[]{#_Ref174529699 .anchor}Figure 6‑3: Annual Exceedance Probability (AEP) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 760 m/s) for various Structural Periods – Mean Values](./media/diana-hazard-6-3.png){width="5.5in" height="3.99in"}

![](./media/diana-hazard-6-4.png){width="5.5in" height="3.99in"}

[]{#_Ref174969545 .anchor}Figure 6‑4: Annual Exceedance Probability (AEP) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 760 m/s) for Various Structural Periods – 84^th^ Percentile Values

### Uniform Hazard Spectra 

[**Figure 6‑5**](#_Ref174543929) and **[Figure 6‑6](#_Ref174544799)** present the UHS with 5% damping for hard rock site conditions ($V_{s,30}$ = 1,500 m/s) in terms of pseudo accelerations $S_{a}(g)\$for various return periods, ranging from 475 to 10,000 years. [**Figure 6‑5**](#_Ref174543929) presents the mean values, while **[Figure 6‑6](#_Ref174544799)** shows the 84^th^ percentile values. Similarly, [**Figure 6‑7**](#_Ref174378646) and [**Figure 6‑8**](#_Ref174545092) present the UHS with 5% damping for soft rock site conditions ($V_{s,30}$ = 760 m/s) for various return periods, ranging from 475 to 1,0000 years. **[Figure 6‑7](#_Ref174378646)** presents the mean values, while **[Figure 6‑8](#_Ref174545092)** shows the 84^th^ percentile values. Additional UHS values for other site classes, such as medium rock ($V_{s,30} =$ 910 m/s) and other percentiles (50^th^, 90^th^, and 95^th^) are included in [**11Appendix C2**](#uniform-hazard-spectra-2).

![[]{#_Ref174543929 .anchor}Figure 6‑5: Uniform Hazard Spectra (UHS) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$`<!-- -->`{=html}1,500 m/s) – Mean Values](./media/diana-hazard-6-5.png){width="5.862096456692913in" height="3.9339621609798776in"}

![[]{#_Ref174544799 .anchor}Figure 6‑6: Uniform Hazard Spectra (UHS) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$`<!-- -->`{=html}1,500 m/s) – 84^th^ Percentile Values](./media/diana-hazard-6-6.png){width="5.867924321959755in" height="3.981786964129484in"}

![[]{#_Ref174378646 .anchor}Figure 6‑7: Uniform Hazard Spectra (UHS) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$`<!-- -->`{=html}760 m/s) – Mean Values](./media/diana-hazard-6-7.png){width="5.971182195975503in" height="3.9902252843394574in"}

![[]{#_Ref174545092 .anchor}Figure 6‑8: Uniform Hazard Spectra (UHS) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$`<!-- -->`{=html}760 m/s) – 84^th^ Percentile Values](./media/diana-hazard-6-8.png){width="5.982244094488189in" height="4.037736220472441in"}

## Hazard Deaggregation and Controlling Seismic Scenarios

### Definitions

The PSHA integrates the probabilities of multiple earthquake scenarios with predictions of resulting ground motion intensity, as described in previous sections. To determine the events contributing to a specific ground motion intensity and AEP (or return period), the seismic hazard deaggregation computes the relative contribution of earthquake parameters magnitude $M$ and distance $R$ to the total hazard (Kramer, 1996) (Bazurro & Cornell, 1999). Conceptually, the contribution of a specific magnitude $\bar{m}$ and distance $\bar{r}$ to the total hazard is derived from the Bayes’ theorem (Cornell & Benjamin, 1970) from the total and marginal AEP:

$\bar{m} = m_{l}\ \ \ ;\ \ \ l \in max\left\lbrack \frac{\lambda\left\lbrack I > i^{*}|M = m_{1} \right\rbrack}{\lambda_{I}\left( i^{*} \right)},..,\frac{\lambda\left\lbrack I > i^{*}|M = m_{k} \right\rbrack}{\lambda_{I}\left( i^{*} \right)}..,\frac{\lambda\left\lbrack I > i^{*}|M = m_{N} \right\rbrack}{\lambda_{I}\left( i^{*} \right)} \right\rbrack$ **[Eq. 6‑6]**

$\bar{r} = r_{l}\ \ \ ;\ \ \ l \in max\left\lbrack \frac{\lambda\left\lbrack I > i^{*}|R = r_{1} \right\rbrack}{\lambda_{I}\left( i^{*} \right)},..,\frac{\lambda\left\lbrack I > i^{*}|R = r_{j} \right\rbrack}{\lambda_{I}\left( i^{*} \right)},..,\frac{\lambda\left\lbrack I > i^{*}|R = r_{N} \right\rbrack}{\lambda_{I}\left( i^{*} \right)} \right\rbrack$ **[Eq. 6‑7]**

where $\lambda\left\lbrack I > i^{*} \right\rbrack$ is the total AEP for all sources defined, and $\lambda\left\lbrack I > i^{*}|M = m_{u} \right\rbrack$ and $\lambda\left\lbrack I > i^{*}|R = r_{v} \right\rbrack$ are the marginal probabilities for events of magnitude $\bar{m}$ and distance $\bar{r}$:

> $\lambda\left\lbrack I > i^{*}|M = m_{u} \right\rbrack \simeq \sum_{N_{S}}^{}v_{0}^{s}\sum_{N_{R}}^{}{\sum_{N_{M}}^{}\Phi_{C}^{(s)}}\left( \varepsilon_{j,k}^{*} \right)f_{M}^{(s)}\left( \bar{m} \right)\,\Delta mf_{R|M}^{(s)}\left( r_{k}|m_{u} \right)\Delta r$ **[Eq. 6‑8]**
>
> $\lambda\left\lbrack I > i^{*}|R = r_{v} \right\rbrack \simeq \sum_{N_{S}}^{}\nu_{o}^{(s)}\sum_{N_{R}}^{}{\sum_{N_{M}}^{}\Phi_{C}^{(s)}}\left( \varepsilon_{j,k}^{*} \right)f_{M}^{(s)}\left( m_{j} \right)\,\Delta mf_{R|M}^{(s)}\left( r_{v}|m_{j} \right)\Delta r$ **[Eq. 6‑9]**

Using this procedure, the fractional contribution of different subsets of events to the total hazard is computed. Deaggregation by magnitude and distance bins allows for the identification of the dominant earthquake scenario ($M - R$ bins) to be identified. When multiple mechanisms contribute to the total hazard, the deaggregation can be performed for each family of sources, identifying the $M - R$ bins for each mechanism and thereby pinpointing the dominant seismic source.

In a probabilistic framework, the magnitude-distance bins $M - R$ that control the seismic hazard is defined as the *controlling scenario* for a given target AEP and structural period $T_{n}$.

## Hazard Deaggregation Plots

[**Figure 6‑9**](#_Ref175169907) and [**Figure 6‑10**](#_Ref175169909) present the 3D deaggregation plots for PGA or $S_{a}(Tn = 0)$, for target AEPs of 1:475, 1:975, 1:2,475, 1:5,000 and 1:1,0000 years.

![[]{#_Ref175169907 .anchor}Figure 6‑9: Hazard Deaggregation of Magnitudes and Distances for PGA – 1:475 AEP](./media/diana-hazard-6-9.png){width="2.7in" height="3.75in"}

![[]{#_Ref175169909 .anchor}Figure 6‑10: Hazard Deaggregation of Magnitudes and Distances for PGA – 1:975 AEP](./media/diana-hazard-6-10.png){width="2.7in" height="3.8in"}

![Figure 6‑11: Hazard Deaggregation of Magnitudes and Distances for PGA – 1:2,475 AEP](./media/diana-hazard-6-11.png){width="2.7in" height="3.7in"}

![Figure 6‑12: Hazard Deaggregation of Magnitudes and Distances for PGA – 1:5,000 AEP](./media/diana-hazard-6-12.png){width="2.7in" height="3.54in"}

![Figure 6‑13: Hazard Deaggregation of Magnitudes and Distances for PGA – 1:10,000 AEP](./media/diana-hazard-6-13.png){width="2.7in" height="3.61in"}

## Controlling Scenarios

The deaggregation plots show that the largest joint contributions to the seismic hazard for PGA occur at magnitude bin centers ranging between 4.875 and 5.125 and distance bin centers ranging between 18.75 and 31.25 km. The magnitudes at the peaks of the marginal distributions range from 5.125 to 6.875. There are no known fault sources in the study area that can contribute to the hazard or influence the deaggregation results.

# Site Response

Seismic ground motions are influenced by the geotechnical and dynamic characteristics of the soil layers that overly the bedrock. The process of determining ground motions at the surface level is known as dynamic site response. The site response spectrum is obtained for the specific geotechnical conditions of the foundation soil of each facility.

This section outlines the methodology used to estimate ground motions under the geotechnical conditions at the Site and presents the results of the site response analysis. It includes a description of the site classification system, which represents soil conditions based on the $V_{S,30}\$value, as defined in the 2020 NBCC. Results of the site response are presented in terms of UHS for the site-specific soil conditions.

## Site Class

The 2020 NBCC site classification system was used to categorize the geological and geotechnical properties of the Site.

The 2020 NBCC classifies sites based on the average shear wave velocity in the top 30 meters of the soil profile, denoted as $V_{s,30}$. [Table 7‑1:](#_Ref178061837) **[Table 7‑1](#_Ref178061837)** presents the site classes according to NBCC 2020.

  ------------ ------------------------------- ------------------------------------
  Site Class   Description                     $\mathbf{V}_{\mathbf{s,30}}$ (m/s)

  A            Hard rock                       \>1,500

  B            Rock                            1500-760

  C            Very dense soil and soft rock   360-760

  D            Stiff soil                      180-360

  E            Soft soil                       140-180

  F            Other soils                     \< 140
  ------------ ------------------------------- ------------------------------------

  : []{#_Ref178061837 .anchor}Table 7‑1: Site Classification according to the National Building Code of Canada (2020)

Source: Table 4.1.8.4 B National Building Code of Canada (Canadian Comission on Building and Fires Codes and National Research Council of Canada, 2020)

A broader classification is proposed by the American Society of Civil Engineers ASCE/SEI 7-22 (2022), identifying average velocity ranges for the boundaries between major site classes, is presented in [**Table 7‑2**:](#_Ref174438610) as reference.

  ------------ --------------------------------- ------------------------------------
  Site Class   Description                       $\mathbf{V}_{\mathbf{s,30}}$ (m/s)

  A            Hard rock                         \>1,500

  B            Medium Rock                       910 – 1500

  B/C          Soft Rock                         640 – 910

  C            Very Dense Soil or Hard Clay      440 – 640

  C/D          Dense Sand or Very Stiff Clay     300 – 440

  D            Medium Dense Sand of Stiff Clay   210 – 300

  D/E          Loose Sand or Medium Stiff Clay   150 – 210

  E            Very Loose Sand or Soft Clay      \< 150

  F            Other soils                       \*See section 20.2.1
  ------------ --------------------------------- ------------------------------------

  : []{#_Ref174438610 .anchor}Table 7‑2: Site Classification according to the American Society of Civil Engineers ASCE 7-22 (2022)

Source: Table 20.3-1 American Society of Civil Engineers ASCE 7-22 (2022)

For rock and hard soils site conditions (i.e., site class A and B), it can be assumed that the ground has virtually no effect on the frequency content of seismic ground motions. For Site Class E or F soils, the site response must be obtained from a site-specific dynamic (time-history) analysis. For Site Class C, D, and E soils, spectral ordinates $S_{a}\left( T_{n} \right)^{sc}$ can be obtained from an amplification factors, as discussed in **Section [7.3](#site-amplification-factors)**.

## Crawford Site-Specific Shear Wave Velocity Profile

Seismic Cone Penetration Test (SCPT) measurements collected from the 2021-2022 and 2023 field investigations (SRK Consulting (Canada), Inc., 2024) (2023) were used to estimate shear wave velocity profiles of the foundation materials at the Site. **[Figure 7‑1](#_Ref178064632)** shows the location of the SCPTs used to estimate the shear wave velocity profiles.

![](./media/image26.png){width="9.0in" height="5.768055555555556in"}

[]{#_Ref178064632 .anchor}Figure 7‑1: Location of Seismic CPTs used to Estimate Shear Wave Velocity Profiles

For profiles containing distinct soil and rock layers were subdivided into those layers designated by a number that ranges from $1$ to $n$ at the bottom, where there is a total of $n$ distinct layers with the 30-m depth. The symbol $i$ refers to any one of the layers between $1$ and $n$. The average shear wave velocity, ${\bar{v}}_{S}$ (or $V_{s,\ 30}$ for the 30-m profile depth), was determined according to the following formula:

${\bar{v}}_{S} = \frac{30\ m}{\sum_{j = 1}^{n}\frac{d_{j}}{v_{S_{j}}}}$ **[Eq. 7‑1]**

where $d_{i},d_{j}$ is the thickness of any layer between 0 and 30 m, $v_{S_{j}}$ is the shear-wave velocity in $m/s$, and $\sum_{i = 1}^{n}d_{i} = 30$ m represents the profile depth.

[**Figure 7‑2**](#_Ref178061995) to **[Figure 7‑6](#_Ref178062137)** show the shear wave velocity profile measurements and the estimated $V_{s,\ 30}$ values at each facility at the Crawford Project Site. The $V_{S,30}$ value calculated using the SCPT measurements ranges from 180 to 230 m/s, as listed in **[Table 7‑3](#_Ref178062173)** for each facility. A characteristic value of $V_{s,30}$ of 220 m/s can be assumed as representative for the Site, which corresponds to a Stiff Soil Class D per NBCC 2020. Note that the geotechnical conditions at the site may not align with the soil classification categories specified in the NBCC 2020.

![[]{#_Ref178061995 .anchor}Figure 7‑2: Shear Wave Velocity Profile at the Crawford Rock, Sand & Till, and Clay Impoundment measured by SCPTu and average $\mathbf{V}_{\mathbf{s,30}}$ determined with Eq. 7-1](./media/image27.png){width="5.0in" height="7.332536089238845in"}

![Figure 7‑3: Shear Wave Velocity Profile at the Crawford Open Pit measured by SCPTu and average $\mathbf{V}_{\mathbf{s,30}}$ determined with Eq. 7-1](./media/image28.png){width="5.009433508311461in" height="7.29457239720035in"}

![Figure 7‑4: Shear Wave Velocity Profile at the Crawford Stockpile East measured by SCPTu and average $\mathbf{V}_{\mathbf{s,30}}$ determined with Eq. 7-1](./media/image29.png){width="4.943396762904637in" height="7.223126640419948in"}

![Figure 7‑5: Shear Wave Velocity Profile at the Crawford Stockpile West measured by SCPTu and average $\mathbf{V}_{\mathbf{s,30}}$ determined with Eq. 7-1](./media/image30.png){width="4.962263779527559in" height="7.238291776027997in"}

![](./media/image31.png){width="4.990566491688539in" height="7.279575678040245in"}

[]{#_Ref178062137 .anchor}Figure 7‑6: Shear Wave Velocity Profile at the Tailings Management Facility (TMF) measured by SCPTu and average $\mathbf{V}_{\mathbf{s,30}}$ determined with Eq. 7-1

  ----------------------------------------- -----------------------------------
  Facility                                  $\mathbf{V}_{\mathbf{s30}}$ (m/s)

  Rock, Sand & Till, and Clay Impoundment   220

  Open Pit                                  210

  Stockpile (East)                          230

  Stockpile (West)                          200

  TMF                                       220
  ----------------------------------------- -----------------------------------

  : []{#_Ref178062173 .anchor}Table 7‑3: Shear Wave Velocity Profile at Crawford Facilities

## Site Amplification Factors

Site amplification factors from GMMs of the CanadaSHM6 were adopted in the direct calculation. The design demands combine the direct logic-tree evaluation at each condition with the ST20 transformation of the demand at the reference condition of 760 m/s, conditioned on the PGA of the same realization. These GMMs use the following amplification factors (Kolaj, Allen, Mayfied, Adams, & Halchuk, 2019):

- The AA13 GMMs (Atkinson & Adams, Ground motion prediction equations for application to the 2015 Canadian national seismic hazard maps, 2013) employ of amplification factors from the 2015 National Building Code of Canada (2015 NBCC) (Canadian Commission on Building and Fire Codes and National Research Council of Canada, 2015). For sites with $V_{s,30}\  \leq$ 760 m/s, these amplification factors $F(T)$ were derived from the active crust GMM of Boore & Atkinson (BA08) (2008). For sites with $V_{s,30} >$ 760 m/s, the factors are based on a conversion from 2000 to 760 m/s using the AA13 model, which is derived from the stable crust GMM by Atkinson and Boore (2006). These amplification factors vary the spectral period and the probabilistic PGA hazard for Site Class C, allowing the adjustment of the hazard spectra to match the specific Site Class.

- For the NGA-East-13 (Goulet, et al., 2017), the approach involves using the larger of: a) a continuous function based on the 2015 NBCC amplification factors and extended to $V_{s,30}$ of 3,000 m/s using the model from Boore & Campbell (2017); or b) the L1 model of Harmon, et al. (2017) with modification to the non-linear term as recommended to the USGS in Petersen et al. (2018).

## Uniform Hazard Spectra

[**Figure 7‑7**](#_Ref174732139) and [**Figure 7‑8**](#_Ref174732146) present the UHS with 5% damping for the Crawford specific soil conditions, estimated using a characteristic value of $V_{s,30}$ = 220 m/s, as discussed in **Section [7.2](#crawford-site-specific-shear-wave-velocity-profile)**. Site Response results are presented in terms of pseudo-accelerations $S_{a}(g)\$for various return periods, ranging from 475 to 10,000 years. [**Figure 7‑7**](#_Ref174732139) presents the mean values, while **[Figure 7‑8](#_Ref174732146)** shows the 84^th^ percentile values. Additional results for other site classes, such as very dense soil ($V_{s,30} =$ 580 m/s) and other percentiles (50^th^, 90^th^, and 95^th^) are included in [**11Appendix C2**](#uniform-hazard-spectra-2).

![[]{#_Ref174732139 .anchor}Figure 7‑7: Uniform Hazard Spectra (UHS) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$`<!-- -->`{=html}220 m/s) – Mean Values](./media/diana-hazard-7-7.png){width="5.849056211723535in" height="4.000024059492564in"}

![](./media/diana-hazard-7-8.png){width="5.905660542432196in" height="4.026803368328959in"}

[]{#_Ref174732146 .anchor}Figure 7‑8: Uniform Hazard Spectra (UHS) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$`<!-- -->`{=html}220 m/s) – 84^th^ Percentile Values

# 2020 National Building Code of Canada Seismic Hazard Values

The 2020 National Building Code of Canada (2020 NBCC or NRC 2020) (Natural Resources of Canada, 2021c) provides an online seismic hazard tool that offers seismic hazard values for building design across Canada. Users can input parameters such as:

- Location: Site latitude and longitude, or site address.

- Site Designation: Specific $V_{s,30}$ value or site class (A, B, C, D, or E).

The tool then provides seismic hazard values based on the following available parameters:

- Fractiles: Mean values.

- Annual Exceedance Probability (AEP)s: 0.002 (or 1:475 years), 0.001 (or 1:975 years), and 0.0004 (or 1:2,475 years).

- Structural periods: PGA and spectral periods of 0.05, 0.10, 0.20, 0.30, 0.50, 1.00, 2.00, 5.00, and 10.00 seconds.

The tool is available online at: <https://www.earthquakescanada.nrcan.gc.ca/hazard-alea/interpolat/nbc2020-cnb2020-en.php>).

**[Figure 8‑1](#_Ref174442866)** compares the response spectra for spectral ordinates with 5% damping in hard rock ($V_{s,30} = \$`<!-- -->`{=html}1500 m/s), showing mean values obtained from the PSHA analysis alongside those from the 2020 NRC (2021c) seismic hazard tool obtained for the Site. Similarly, [**Figure 8‑2**](#_Ref174635807) and\
[**Figure 8‑3**](#_Ref174635809) provide a comparison for soft rock ($V_{s,30} =$ 760 m/s) and stiff soil ($V_{s,30} =$ 220 m/s), respectively, presenting the mean values from both the PSHA analysis and the NRC 2020 seismic hazard tool. The ratios of the PSHA spectral ordinates to the NRC 2020 values range from 0.70 to 1.30 for the periods and site conditions compared.

![[]{#_Ref174442866 .anchor}Figure 8‑1: Uniform Hazard Spectra (UHS) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$`<!-- -->`{=html}1500 m/s/) for 2,475, 975, and 475-year return periods: Comparison with NRC (2021c) Mean Values](./media/diana-hazard-8-1.png){width="5.877358923884515in" height="4.283062117235346in"}

![[]{#_Ref174635807 .anchor}Figure 8‑2: Uniform Hazard Spectra (UHS) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$`<!-- -->`{=html}760 ms/) for 2,475, 975, and 475-year return periods: Comparison with NRC (2021c) Mean Values](./media/diana-hazard-8-2.png){width="5.933962160979878in" height="4.32331583552056in"}

![[]{#_Ref174635809 .anchor}Figure 8‑3: Uniform Hazard Spectra (UHS) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 220 m/s) for 2,475, 975, and 475-year return periods: Comparison with NRC (2021c) Mean Values](./media/diana-hazard-8-3.png){width="5.952830271216098in" height="4.339300087489064in"}

[]{#_Ref174785920 .anchor}

# Design Earthquakes

The Canadian Dam Association (CDA) Dam Safety Guidelines (2013) along with the Global Industry Standard on Tailings Management (GISTM) from the International Council on Mining and Metals (ICMM) (2020) and the Technical Bulletin for Seismic Hazard Criteria from the Ontario Ministry of Natural Resources (MNR) (2011), advocate for performing Probabilistic Seismic Hazard Analysis (PSHA) and setting design recurrence intervals based on potential failure consequences, ranging from “Low” to “Extreme.”

The dam classification for the TMF, reviewed during the feasibility study (WSP, 2023) (Ausenco, 2023), indicated a “Very High” consequence during construction, operation, and transition and closure active care phases, and “Significant” during the closure passive care phase. For this study, an “Extreme” consequence level has been designated for the FEED phase of the project TMF embankments as defined by CDA (2013). Consequently, the “Maximum Design Earthquake” (MDE) for the TMF embankments is set with an AEP of 1:10,000 years, as required by GISTM and, for closure, consistent with ICOLD and ANCOLD guidance.

The MDE for the impoundments and stockpiles facilities has been set by the FEED design team with an AEP of 1:2,475 years.

## Peak Ground Acceleration

**[Table 9‑1](#_Ref178064924)** and[Error! Reference source not found.](#_Ref175137289) [**Table 9‑2**](#_Ref178064962) present the PGA values for return periods ranging from 475 to 10,000 years for various rock and soil site conditions, with $V_{s,30}$ values ranging from 220 to 1,500 m/s. **[Table 9‑1](#_Ref178064924)** presents the mean values, while **[Table 9‑2](#_Ref178064962)** lists the 84^th^ percentile values. Design PGA values for other confidence levels (50^th^, 90^th^, and 95^th^ percentiles) are included in [**11Appendix D1**](#design-peak-ground-acceleration).

+:---------------------:+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                       | PGA (g)                                                                                                                                                                                                                                             |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| Return Period (years) | Hard Rock                                       | Medium Rock                                    | Soft Rock                                      | Very Dense Soil                                | Stiff Soil                                     |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | Site Class A                                    | Site Class B                                   | Site Class B/C                                 | Site Class C                                   | Site Class D                                   |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 1500 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 910 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 760 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 580 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 220 m/s |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 475                   | 0.0374                                          | 0.0361                                         | 0.0351                                         | 0.0388                                         | 0.0515                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 975                   | 0.0653                                          | 0.0629                                         | 0.0610                                         | 0.0671                                         | 0.0876                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **2,475**             | **0.1261**                                      | **0.1210**                                     | **0.1171**                                     | **0.1278**                                     | **0.1588**                                     |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 5,000                 | 0.1943                                          | 0.1862                                         | 0.1800                                         | 0.1948                                         | 0.2288                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **10,000**            | 0.2852                                          | 0.2726                                         | 0.2632                                         | 0.2828                                         | **0.3123**                                     |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+

: []{#_Ref178064924 .anchor}Table 9‑1: PGA of Design Ground Motions for Various Return Periods and Site Conditions – Mean Values

+:---------------------:+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                       | PGA (g)                                                                                                                                                                                                                                             |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| Return Period (years) | Hard Rock                                       | Medium Rock                                    | Soft Rock                                      | Very Dense Soil                                | Stiff Soil                                     |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | Site Class A                                    | Site Class B                                   | Site Class B/C                                 | Site Class C                                   | Site Class D                                   |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 1500 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 910 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 760 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 580 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 220 m/s |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 475                   | 0.0524                                          | 0.0501                                         | 0.0474                                         | 0.0539                                         | 0.0736                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 975                   | 0.0929                                          | 0.0887                                         | 0.0840                                         | 0.0947                                         | 0.1264                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **2,475**             | **0.1803**                                      | **0.1717**                                     | **0.1623**                                     | **0.1812**                                     | **0.2288**                                     |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 5,000                 | 0.2794                                          | 0.2654                                         | 0.2509                                         | 0.2773                                         | 0.3271                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **10,000**            | 0.4122                                          | 0.3899                                         | 0.3684                                         | 0.4040                                         | **0.4424**                                     |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+

: []{#_Ref178064962 .anchor}Table 9‑2: PGA of Design Ground Motions for Various Return Periods and Site Conditions – 84^th^ Percentile Values

For the stiff soils on the Site ($V_{s,30} =$`<!-- -->`{=html}220 m/s, Site Class D), the design event for the TMF, with an AEP of 1:10,000 years, will have a PGA of 0.312 g (mean) and 0.442 g (84^th^ percentile). The design event for the Clay, Rock, and Sand & Silt Impoundments, as well as the East and West Stockpiles, with an AEP of 1:2,475 years, will have a PGA of 0.159 g (mean) and 0.229 (84^th^ percentile).

## Design Response Spectra

**[Figure 9‑1](#_Ref174655456)** and **[Figure 9‑2](#_Ref174655469)** present the design response spectra with 5% damping for the design event with an AEP of 1:10,000 years, and various site conditions, ranging from hard rock ($V_{s,30}$ = 1500 m/s) to stiff soil ($V_{s,30}$ = 220 m/s). **[Figure 9‑1](#_Ref174655456)** presents the mean values, while **[Figure 9‑2](#_Ref174655469)** shows the 84^th^ percentile values. Similarly, [**Figure 9‑3**](#_Ref178065125) and [**Figure 9‑4**](#_Ref178016135) [**Error! Reference source not found.**](#_Ref178015982)show the design response spectra with 5% damping for the design event with an AEP of 1:2,475 years, and various site conditions ranging from hard rock ($V_{s,30}$ = 1500 m/s) to stiff soil ($V_{s,30}$ = 220 m/s), with [**Figure 9‑3**](#_Ref178065125) [Error! Reference source not found.](#_Ref178015982) presenting the mean values and **[Figure 9‑4](#_Ref178016135)** showing the 84^th^ percentile values.

**[Table 9‑3](#_Ref178065304)** and [**Table 9‑4**](#_Ref178065306) present the ordinate values of the design response spectra for the design events with AEP of 1:10,000 and 1:2,475 years.

Design response spectra for other confidence levels (50^th^, 90^th^, and 95^th^ percentiles) are included in [**11Appendix D2**](#design-response-spectrum).

![[]{#_Ref174655456 .anchor}Figure 9‑1: Design Response Spectra for a Return Period of 10,000 years - Mean Values](./media/diana-hazard-9-1.png){width="5.952830271216098in" height="4.573180227471566in"}

![[]{#_Ref174655469 .anchor}Figure 9‑2: Design Response Spectra for a Return Period of 10,000 years – 84^th^ Percentile Values](./media/diana-hazard-9-2.png){width="6.0in" height="4.61in"}

![[]{#_Ref178065125 .anchor}Figure 9‑3: Design Response Spectra for a Return Period of 2,475 years - Mean Values](./media/diana-hazard-9-3.png){width="6.0in" height="4.45in"}

![[]{#_Ref178016135 .anchor}Figure 9‑4: Design Response Spectra for a Return Period of 2,475 years – 84^th^ Percentile Values](./media/diana-hazard-9-4.png){width="6.0in" height="4.45in"}

+:-----------------------------:+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                               | Pseudo-Acceleration                                                                                                                                                                                                                                 |
|                               |                                                                                                                                                                                                                                                     |
|                               | $$\mathbf{S}_{\mathbf{a}}\mathbf{(}\mathbf{T}_{\mathbf{n}}\mathbf{)\ \lbrack g\rbrack}$$                                                                                                                                                            |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| Spectral Period               | Hard Rock                                       | Medium Rock                                    | Soft Rock                                      | Very Dense Soil                                | Stiff Soil                                     |
|                               |                                                 |                                                |                                                |                                                |                                                |
| $\mathbf{T}_{\mathbf{n}}$ (s) | Site Class A                                    | Site Class B                                   | Site Class B/C                                 | Site Class C                                   | Site Class D                                   |
|                               |                                                 |                                                |                                                |                                                |                                                |
|                               | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 1500 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 910 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 760 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 580 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 220 m/s |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.000                         | 0.285                                           | 0.273                                          | 0.263                                          | 0.283                                          | 0.312                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.050                         | 0.593                                           | 0.599                                          | 0.602                                          | 0.620                                          | 0.557                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.075                         | 0.558                                           | 0.620                                          | 0.632                                          | 0.653                                          | 0.568                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.100                         | 0.520                                           | 0.601                                          | 0.619                                          | 0.650                                          | 0.592                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.120                         | 0.471                                           | 0.550                                          | 0.569                                          | 0.602                                          | 0.561                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.150                         | 0.405                                           | 0.487                                          | 0.509                                          | 0.545                                          | 0.526                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.180                         | 0.374                                           | 0.432                                          | 0.457                                          | 0.499                                          | 0.516                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.200                         | 0.361                                           | 0.403                                          | 0.428                                          | 0.474                                          | 0.512                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.220                         | 0.328                                           | 0.360                                          | 0.384                                          | 0.430                                          | 0.486                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.250                         | 0.291                                           | 0.314                                          | 0.332                                          | 0.378                                          | 0.454                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.280                         | 0.264                                           | 0.283                                          | 0.298                                          | 0.340                                          | 0.430                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.300                         | 0.250                                           | 0.269                                          | 0.281                                          | 0.319                                          | 0.418                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.350                         | 0.218                                           | 0.234                                          | 0.245                                          | 0.279                                          | 0.380                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.400                         | 0.194                                           | 0.209                                          | 0.217                                          | 0.250                                          | 0.356                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.450                         | 0.174                                           | 0.187                                          | 0.194                                          | 0.226                                          | 0.336                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.500                         | 0.157                                           | 0.169                                          | 0.175                                          | 0.206                                          | 0.324                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.600                         | 0.124                                           | 0.133                                          | 0.137                                          | 0.163                                          | 0.268                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.700                         | 0.103                                           | 0.111                                          | 0.114                                          | 0.137                                          | 0.234                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.750                         | 0.096                                           | 0.102                                          | 0.105                                          | 0.126                                          | 0.223                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.850                         | 0.084                                           | 0.089                                          | 0.091                                          | 0.110                                          | 0.195                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.900                         | 0.079                                           | 0.083                                          | 0.086                                          | 0.103                                          | 0.184                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 1.000                         | 0.071                                           | 0.075                                          | 0.076                                          | 0.092                                          | 0.169                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 1.250                         | 0.054                                           | 0.057                                          | 0.058                                          | 0.071                                          | 0.129                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 1.500                         | 0.044                                           | 0.046                                          | 0.047                                          | 0.057                                          | 0.107                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 1.750                         | 0.037                                           | 0.039                                          | 0.039                                          | 0.048                                          | 0.088                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 2.000                         | 0.032                                           | 0.033                                          | 0.034                                          | 0.041                                          | 0.075                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 2.500                         | 0.023                                           | 0.024                                          | 0.024                                          | 0.030                                          | 0.054                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 3.000                         | 0.018                                           | 0.018                                          | 0.019                                          | 0.023                                          | 0.041                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 3.500                         | 0.014                                           | 0.015                                          | 0.015                                          | 0.018                                          | 0.033                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 4.000                         | 0.012                                           | 0.012                                          | 0.012                                          | 0.015                                          | 0.027                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 4.500                         | 0.010                                           | 0.010                                          | 0.010                                          | 0.013                                          | 0.023                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 5.000                         | 0.009                                           | 0.009                                          | 0.009                                          | 0.011                                          | 0.019                                          |
+-------------------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+

: []{#_Ref178065304 .anchor}Table 9‑3: Spectral Ordinates of the Design Spectra for a 10,000-year Return Period and Various Site Conditions – Mean Values

\

+:---------------:+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                 | Pseudo-Acceleration                                                                                                                                                                                                                                 |
|                 |                                                                                                                                                                                                                                                     |
|                 | $\mathbf{S}_{\mathbf{a}}\mathbf{(}\mathbf{T}_{\mathbf{n}}\mathbf{)\ \lbrack g\rbrack}$                                                                                                                                                              |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| Spectral Period | Hard Rock                                       | Medium Rock                                    | Soft Rock                                      | Very Dense Soil                                | Stiff Soil                                     |
|                 |                                                 |                                                |                                                |                                                |                                                |
| Tn (s)          | Site Class A                                    | Site Class B                                   | Site Class B/C                                 | Site Class C                                   | Site Class D                                   |
|                 |                                                 |                                                |                                                |                                                |                                                |
|                 | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 1500 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 910 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 760 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 580 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 220 m/s |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.000           | 0.126                                           | 0.121                                          | 0.117                                          | 0.128                                          | 0.159                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.050           | 0.245                                           | 0.244                                          | 0.246                                          | 0.259                                          | 0.269                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.075           | 0.238                                           | 0.261                                          | 0.266                                          | 0.281                                          | 0.284                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.100           | 0.228                                           | 0.261                                          | 0.269                                          | 0.288                                          | 0.304                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.120           | 0.207                                           | 0.241                                          | 0.249                                          | 0.268                                          | 0.289                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.150           | 0.180                                           | 0.215                                          | 0.224                                          | 0.244                                          | 0.272                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.180           | 0.166                                           | 0.192                                          | 0.203                                          | 0.224                                          | 0.267                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.200           | 0.161                                           | 0.180                                          | 0.191                                          | 0.214                                          | 0.266                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.220           | 0.147                                           | 0.161                                          | 0.172                                          | 0.194                                          | 0.253                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.250           | 0.130                                           | 0.140                                          | 0.149                                          | 0.170                                          | 0.236                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.280           | 0.118                                           | 0.127                                          | 0.134                                          | 0.153                                          | 0.223                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.300           | 0.112                                           | 0.120                                          | 0.126                                          | 0.144                                          | 0.216                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.350           | 0.097                                           | 0.104                                          | 0.109                                          | 0.125                                          | 0.195                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.400           | 0.087                                           | 0.093                                          | 0.097                                          | 0.112                                          | 0.180                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.450           | 0.078                                           | 0.083                                          | 0.087                                          | 0.101                                          | 0.169                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.500           | 0.070                                           | 0.075                                          | 0.078                                          | 0.092                                          | 0.162                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.600           | 0.056                                           | 0.060                                          | 0.062                                          | 0.073                                          | 0.134                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.700           | 0.047                                           | 0.050                                          | 0.052                                          | 0.062                                          | 0.115                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.750           | 0.043                                           | 0.046                                          | 0.048                                          | 0.057                                          | 0.109                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.850           | 0.038                                           | 0.041                                          | 0.042                                          | 0.050                                          | 0.095                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 0.900           | 0.036                                           | 0.038                                          | 0.039                                          | 0.047                                          | 0.090                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 1.000           | 0.033                                           | 0.035                                          | 0.035                                          | 0.043                                          | 0.082                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 1.250           | 0.025                                           | 0.026                                          | 0.027                                          | 0.033                                          | 0.063                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 1.500           | 0.020                                           | 0.022                                          | 0.022                                          | 0.027                                          | 0.051                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 1.750           | 0.017                                           | 0.018                                          | 0.018                                          | 0.022                                          | 0.042                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 2.000           | 0.015                                           | 0.016                                          | 0.016                                          | 0.019                                          | 0.036                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 2.500           | 0.011                                           | 0.011                                          | 0.011                                          | 0.014                                          | 0.026                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 3.000           | 0.008                                           | 0.008                                          | 0.009                                          | 0.011                                          | 0.019                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 3.500           | 0.006                                           | 0.007                                          | 0.007                                          | 0.008                                          | 0.015                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 4.000           | 0.005                                           | 0.005                                          | 0.006                                          | 0.007                                          | 0.012                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 4.500           | 0.004                                           | 0.005                                          | 0.005                                          | 0.006                                          | 0.010                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 5.000           | 0.004                                           | 0.004                                          | 0.004                                          | 0.005                                          | 0.009                                          |
+-----------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+

: []{#_Ref178065306 .anchor}Table 9‑4: Spectral Ordinates of the Design Spectra for a 2,475-year Return Period and Various Site Conditions – Mean Values []{#_Ref174451918 .anchor}

# Slope Design Parameters

This section reports the dynamic properties of the slopes analyzed, the permanent displacements induced by the design earthquakes accumulate in their potential sliding masses, and the performance-based seismic coefficients derived from those displacements. The flexible sliding-block displacement models require the fundamental period of each potential sliding mass and the dynamic soil stiffness that determines it: the analyses considered 5 geometry–material scenarios with heights between 27 and 135 m, and the estimated fundamental period varies between 0.22 and 1.28 s.

The Newmark permanent displacement $D_{n}$ quantifies the displacement induced by an earthquake accumulates in the sliding mass and is the performance measure from which the seismic coefficients are derived. The $D_{n}(k_{y})$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_{y}$ to the expected permanent displacement; they were computed with an ensemble set of AM88 (Ambraseys & Menu, 1988), JB07 (Jibson, 2007), SR08 (Saygili & Rathje, 2008), BT07 (Bray & Travasarou, 2007), and BM19 (Bray, Macedo, & Travasauro, 2018), with reference magnitudes $M_{w}$ = 5.5 and $M_{w}$ = 6.5 assigned according to the seismic demand and 300 realizations per demand and are read at the fractiles $q = 1 - p_{e}$. The horizontal pseudostatic coefficient $k_{h}$ is in turn derived from the allowable permanent displacement $D_{a}$ of the potentially sliding mass (Bray & Travasarou, Pseudostatic Coefficient for Use in Simplified Seismic Slope Stability Evaluation, 2009; Macedo, Bray, Abrahamson, & Travasarou, 2018); the coefficients are reported at four relative displacement limits, $D_{a}/H_{s}$ = 0.1, 0.4, 1.0, 2.5%, and the tables in Section [**10.3**](#idm-identifies-the-material-scenario-and-uscs-the-classification-of-the-slope-materials.-h_s-is-the-slope-height-and-b-the-berm-width-both-in-ms-is-the-slope-ratio-tanbeta-1s-and-lambda_o-the-truncation-ratio-both-dimensionless-g_o-is-the-shear-modulus-of-the-profile-at-zh_s-1-in-mpa-and-m_o-the-exponent-of-its-power-law-dimensionlessa_1-is-the-first-modal-root-dimensionlessv_so-is-the-basal-shear-wave-velocity-and-v_s30-the-travel-time-averaged-shear-wave-velocity-in-the-uppermost-30-m-both-in-ms.seismic-coefficients) and [**11Appendix E**](#section-2) report, for the demands and scenarios analyzed, the coefficient at each limit, expressed as a percentage of the PGA.

## Definitions

### Seismic Design Criteria for Slopes

Slope Performance under the design earthquakes is evaluated through successive tiers of analysis including pseudostatic stability checks, simplified estimates of permanent deformation, and dynamic analyses where warranted by the consequences of failure, anticipated response, or complexity of the failure mechanism (International Commission on Large Dams, 2016; Federal Emergency Management Agency, 2005). Within this framework, the Newmark method provides a deformation-based assessment that complements the limit-equilibrium analysis. The pseudostatic seismic coefficient is a project-specific value rather than assigned as a universal value for a particular structure type. USACE manuals EM 1110-2-1902 and EM 1110-2-2100 discuss pseudostatic analysis sliding block methods for evaluating seismic stability and permanent deformation Selection of the coefficient considers the site-specific seismic hazard, potential failure mechanism, and project performance criteria (U.S. Army Corps of Engineers, 2003; U.S. Army Corps of Engineers, 2005).

The allowable permanent displacement is expressed as a percentage of the reference slope height. This report evaluates four relative displacement thresholds, $D_{a}/H$ = 0.1, 0.4, 1.0, 2.5%, based on the crest-settlement ratios reported by Alberti et. al. (Aliberti, Biondi, Cascone, & Rampello, 2019). The reference height includes the embankment height and the thickness of the deformable foundation and is adopted here as the slope height for normalization. The seismic coefficient tables are presented for these four thresholds. Section [**10.1.3**](#seismic-pseudo-static-coefficients) describes the derivation of the coefficients from the allowable displacement.

### Fundamental Period of the Embankment

Flexible sliding-block models account for the dynamic response of the potential sliding mass through spectral acceleration evaluated at a period proportional to its fundamental period, so each slope geometry–material combination needs $T_{s}$, which is derived from the geometry and the depth-dependent small-strain shear stiffness, described by $G_{o}$, $m_{o}$, and $V_{S}^{o}$; the mean value of $T_{s}$ provides a dynamic input to the permanent-displacement models, while $V_{S30}$ the site conditions used to determine the seismic demand. The fundamental period of the potential sliding mass is estimated from the first mode of the truncated inhomogeneous shear-beam model of Dakoulas and Gazetas (1985) as

$T_{s} = \frac{4\pi H}{a_{1}(2 - m_{o})V_{S}^{o}},$ **[****Eq. 10‑1]**

where $H_{s}$ is the slope height, $V_{S}^{o}$ is the basal shear-wave velocity associated with $G_{o}$, $m_{o}$ is the inhomogeneity factor governing the shear-modulus profile, and $a_{1}$ is the first modal root of the characteristic equation. The height from the virtual apex to the base of the equivalent wedge is $H = H_{s}/(1 - \lambda_{o}).$ The modal root depends jointly on $m_{o}$ and the truncation ratio $\lambda_{o}$, which geometric similarity gives as

$\lambda_{o} = \frac{b}{b_{\max}},$ **[****Eq. 10‑2]**

where $b$ and $b_{\max}$ are the berm and base widths, respectively. The equivalent truncated section in the Dakoulas–Gazetas model (1985) is specified by the height $H_{s}$, slope ratio $s$, expressed as horizontal to vertical, and truncation ratio $\lambda_{o}$; with $\tan\beta = 1/s$, where $\beta$ is the slope angle, the crest width is given, for a symmetric section, by

$b = \frac{2H_{s}s}{1/\lambda_{o} - 1}.$ **[****Eq. 10‑3]**

and the base width is

$b_{\max} = b + 2H_{s}s.$ **[****Eq. 10‑4]**

For each profile realization, the basal shear-wave velocity is

$V_{S}^{o} = \left( \frac{gG_{o}}{\gamma_{sat}^{(k_{b})}} \right)^{1/2},$ **[****Eq. 10‑5]**

where $G_{o}$ is the fitted small-strain shear modulus at the base, $g$ is the acceleration of gravity, and $\gamma_{sat}^{(k_{b})}$ is the saturated unit weight of the basal layer, indexed by $k_{b}$; all quantities are expressed in consistent units. The depth dependence of small-strain shear stiffness is represented for each realization by the power-law profile

$G(z) = G_{o}\left( \frac{z}{H_{s}} \right)^{m_{o}},$ **[****Eq. 10‑6]**

where $z$ is depth below the crest, $G_{o}$ is the fitted shear modulus at the base ($z/H_{s} = 1$), and $m_{o}$ is obtained from a logarithmic fit to the layer moduli $G_{m}^{(k)}$. Those layer moduli come from the soil classification: the USCS classification assigned to layer $k$ selects its soil family and the associated set of $J^{(k)}$ small-strain shear-modulus correlations compiled by Ishihara (1997), and the layer modulus is taken as their arithmetic mean,

$G_{m}^{(k)} = \frac{1}{J^{(k)}}\sum_{j = 1}^{J^{(k)}}A^{(j)}F_{e}^{(k,j)}\left\lbrack {OCR}^{(k)} \right\rbrack^{m_{1}^{(k)}}p_{ref}^{n^{(j)}}\left( \frac{p_{m}^{(k)}}{p_{ref}} \right)^{n^{(j)}}.$ **[****Eq. 10‑7]**

Here $A^{(j)}$ and $n^{(j)}$ are tabulated correlation parameters, $F_{e}^{(k,j)}$ is the void-ratio function, $m_{1}^{(k)}$ is the overconsolidation exponent, $p_{m}^{(k)}$ is the layer-averaged effective octahedral normal stress, and $p_{ref} = 100$ kPa is the reference pressure. Under at-rest conditions, the layer-averaged effective octahedral normal stress $p_{m}^{(k)}$ (Hardin & Black, Vibration Modulus of Normally Consolidated Clay, 1968; Hardin & Drnevich, Shear Modulus and Damping in Soils: Measurement and Parameter Effects, 1972) is

$p_{m}^{(k)} = \frac{1 + 2K_{0}}{3}\left( \sum_{\mathcal{l} = 1}^{k - 1}\gamma^{(\mathcal{l})}h^{(\mathcal{l})} + \frac{\gamma^{(k)}h^{(k)}}{2} \right),$ **[****Eq. 10‑8]**

where $K_{0}$ is the at-rest lateral earth pressure coefficient, $\gamma^{(\mathcal{l})}$ and $h^{(\mathcal{l})}$ are the effective unit weight adopted for the groundwater condition and the thickness of layer $\mathcal{l}$, and $\mathcal{l} < k$ denotes the overlying layers. For hydrostatic groundwater conditions, the bulk unit weight is used above the groundwater table and the submerged unit weight below it; layers intersected by the groundwater table are subdivided accordingly. The layer overconsolidation ratio is

${OCR}^{(k)} = max\lbrack(p_{m}^{(k)} + POP)/p_{m}^{(k)},1\rbrack$, **[Eq.** **10‑9]**

where $POP$ is the preconsolidation pressure increment, expressed on the same mean-effective-stress basis as $p_{m}^{(k)}$; for fine-grained soils, $m_{1}^{(k)} = f_{IP}({IP}^{(k)})$, where ${IP}^{(k)}$is the plasticity index, whereas for sands and gravels $m_{1}^{(k)} = 0$ and the OCR multiplier is therefore unity. The void ratio $e_{0}^{(k)}$ enters all three soil families through $F_{e}^{(k,j)}$, which the correlations compiled by Ishihara (1997) define in terms of $e_{0}^{(k)}$ and $C_{e}^{(j)}$, with the index $j_{SS75}$ identifying the Shibata–Soelarno formulation (1975):

$F_{e}^{(k,j)} = \left\{ \begin{matrix}
C_{e}^{(j)} - \frac{e_{0}^{(k)}}{1 + e_{0}^{(k)}}, & j = j_{SS75}, \\
\frac{\left( C_{e}^{(j)} - e_{0}^{(k)} \right)^{2}}{1 + e_{0}^{(k)}}, & j \neq j_{SS75}.
\end{matrix} \right.\$ **[****Eq. 10‑10]**

The shear-wave velocity of layer $k$ then follows from

$V_{S}^{(k)} = \left( \frac{gG_{m}^{(k)}}{\gamma_{sat}^{(k)}} \right)^{1/2},$ **[****Eq. 10‑11]**

where $G_{m}^{(k)}$ is the adopted layer modulus and $\gamma_{sat}^{(k)}$ is its saturated unit weight; all quantities are expressed in consistent units. The parameters of the stiffness correlations are listed in [Table E‑1](#section-4).

For each geometry–material combination, the analysis generates $N$ synthetic realizations of the layered profile, and each of $G_{o}$, $m_{o}$, $V_{S}^{o}$, and $V_{S30}$ is summarized by its mean and selected marginal fractiles; for the mean and for each reported fractile, $a_{1}$ and $T_{s}$ are evaluated from the corresponding $m_{o}$ and $V_{S}^{o}$ values, and the estimates calculated from the mean parameter values provide the dynamic properties used in the displacement analysis. $V_{S30}$ is the travel-time-averaged shear-wave velocity in the uppermost 30 m:

$V_{S30} = \frac{30}{\sum_{i}^{}\frac{h_{30}^{(i)}}{V_{S}^{(i)}} + \frac{max(30 - H_{s},0)}{V_{ref}}}.$ **[****Eq. 10‑12]**

In this expression, $h_{30}^{(i)}$ is the portion of layer $i$ within the uppermost 30 m and $V_{S}^{(i)}$ is its shear-wave velocity; when $H_{s} < 30$ m, the reference velocity $V_{ref}$ is assigned to the remaining thickness.

### Seismic (Pseudo-Static) Coefficients

Pseudostatic seismic design of slopes requires a horizontal coefficient representing earthquake loading on the sliding mass. In this section the coefficient is derived from displacement-based performance: the Newmark permanent displacement $D_{n}$ is the slope-deformation performance measure, and the coefficient $k_{\max}$ is the lowest yield coefficient $k_{y}$ consistent with a performance objective defined by the allowable displacement $D_{a}$ and the target maximum exceedance probability $p_{e}$, such that $D_{n}$ exceeds $D_{a}$. The normalized coefficient $k_{h}$ expresses $k_{\max}$ as a percentage of the site-adjusted PGA expressed in units of (g) after site response is accounted for in each geometry–material combination, and the coefficients are reported by geometry, material and seismic demand. For the slopes considered, $D_{n}$ is estimated probabilistically by combining empirical regression models within a lognormal framework.

The horizontal pseudostatic coefficient is derived in this assessment from the allowable permanent displacement $D_{a}$ of the potentially sliding mass (Bray & Travasarou, Pseudostatic Coefficient for Use in Simplified Seismic Slope Stability Evaluation, 2009; Macedo, Bray, Abrahamson, & Travasarou, 2018). The seismic demand and the fundamental periods established in the preceding sections allow the $D_{n}(k_{y})$ relations between the Newmark permanent displacement and the yield coefficient to be computed; their inversion at the target exceedance probability yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry–material combination yields $k_{h}$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification. The yield acceleration $a_{y}$ represents the acceleration level at which the limit-equilibrium factor of safety equals unity and its dimensionless form is $k_{y} = a_{y}/g$; for each allowable displacement and target exceedance probability, the analysis determines the minimum $k_{y}$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient applied in the pseudostatic limit-equilibrium verification. A factor of safety of at least unity under this applied coefficient indicates that the calculated yield coefficient meets or exceeds the required threshold.

In the Newmark sliding-block method (Newmark, 1965), the potentially sliding wedge is represented as a rigid block resting on an inclined plane: relative motion begins when the driving acceleration exceeds the yield acceleration $a_{y} = k_{y}g$ and continues until the relative velocity returns to zero, and the permanent displacement is the sum of those episodes over the duration of the earthquake motion, obtained by double integration of the acceleration excess. The extension of the procedure to dams and embankments (Makdisi & Seed, 1978) derived the equivalent acceleration of the sliding mass from its dynamic response and is the direct antecedent of the flexible formulations. The adopted empirical relations represent the accumulated displacement statistically through two idealizations: rigid-block models relate the displacement to measures of the base excitation, and flexible-block models additionally incorporate the dynamic response of the mass through $T_{s}$ and the spectral acceleration evaluated at a period proportional to $T_{s}$.

The displacement calculation uses the seismic demand and the fundamental periods established in Section [**10.1.2**](#fundamental-period-of-the-embankment). For each geometry, material and seismic demand – the probabilistic spectrum of each evaluated return period – a joint sample of the intensity measures required by the rigid-block and flexible formulations is constructed; that sample is common to all models, so their differences represent the displacement formulation rather than incompatible seismic demands. The input for each return period is the reference-rock UHS, which for 10,000 years represents the MDE; it specifies spectral acceleration ordinates at a common annual exceedance rate and is defined for $V_{S30} = V_{ref} = 760$ m/s. For each geometry and material scenario, the spectral ordinates and the PGA are transformed to the corresponding $V_{S30}$ through the ST20 amplification model (Stewart, et al., 2020; Hashash, Ilhan, & Harmon, 2020).

At the site condition of each scenario, the joint sample comprises PGA, $S_{a}(1.3T_{s})$, and $S_{a}(1.5T_{s})$. The three measures are represented through empirical marginals in $\ln{(S}_{a})$ and a Gaussian copula with the full inter-period correlation matrix (Baker & Jayaram, 2008), and the samples are recentered to preserve the mean of each amplified marginal; in each realization, the three intensities remain paired, and each displacement formulation uses the measures entering its regression. The Arias intensity that JB07 and SR08 require completes the set of intensity measures; it is estimated deterministically for each realization from the PGA, so that each PGA realization determines a single value of $I_{A}$ and the displacement sample propagates the PGA variability.

For each scenario, 30 values of $k_{y}$ are evaluated, logarithmically spaced between 0.01 and $max(\overline{PGA},0.80)$, where $\overline{PGA}$ is the mean site-condition PGA of the scenario; that interval establishes the computed range of the $D_{n}(k_{y})$ relations, over which the formulations are evaluated and the inversion to $k_{\max}$ operates.

Each active formulation estimates the Newmark permanent displacement (Newmark, 1965) of the sliding mass from the yield acceleration and the intensity measures of its regression, and all of them express the positive displacement $D_{n}$, in centimeters, through

$D_{n} = exp\left( \mu_{\ln D} + \epsilon\sigma_{\ln D} \right),\quad\quad\epsilon \sim \mathcal{N}(0,1),$ **[****Eq. 10‑13]**

where $\mu_{\ln D}$ and $\sigma_{\ln D}$ are the mean and standard deviation of $\ln D_{n}$ defined by each model, and $\epsilon$ is a standard-normal residual. Some source formulations contain a discrete branch of zero or negligible displacement; the implemented evaluation uses exclusively the positive lognormal branch, conditional on displacement exceeding the model’s zero-or-negligible-displacement threshold. In every formulation, $k_{y}$, PGA, and $S_{a}$ are expressed in units of $g$ – the acceleration of gravity – $I_{A}$ in m/s, and $T_{s}$ in seconds; the Arias intensity is derived from the PGA of each realization, and the reference magnitude is $M_{w} =$ 5.5 for return periods up to 2,500 years and $M_{w} =$ 6.5 for return periods of 5,000 and 10,000 years and the MCE. Within each demand, that magnitude is common to the geometry, material and site combinations evaluated. The published form of each formulation is reproduced in [**11Appendix E**](#section-2). The performance-based seismic coefficient is defined by

$k_{\max}(p_{e} \mid D_{a}) = inf\left\{ k_{y}:P\lbrack D_{n}(k_{y}) > D_{a}\rbrack \leq p_{e} \right\}.$ **[**[]{#_Ref_gmdp_eq_eq_kmax_criterion .anchor}**Eq. 10‑14]**

where $p_{e}$ is the target probability that $D_{n}$ exceeds $D_{a}$: $k_{\max}$ is the smallest $k_{y}$ for which the probability of exceeding the allowable displacement is at most $p_{e}$. The normalized coefficient, reported as a percentage of the PGA [% of PGA], is calculated using the site-adjusted PGA transformed to the $V_{S30}$ of the geometry–material combination evaluated for each demand:

$k_{h} = 100\,\frac{k_{\max}}{PGA(V_{S30})}.$ **[****Eq. 10‑15]**

$k_{\max}$ is expressed in units of $g$ and $k_{h}$ as a percentage of the PGA of the corresponding site condition. These two quantities express the displacement criterion as the horizontal action of the pseudostatic verification.

The five formulations are evaluated individually and combined into the three sets that the tables and figures identify as IDn: rigid, flexible and ensemble. The displacement model provides individual realizations for AM88, JB07, SR08, BT07, and a fifth formulation selected by the tectonic context: BM17 for projects with subduction control and BM19 for projects with shallow crustal control. The overall design set, identified as ensemble, combines AM88, JB07, SR08, BT07, and the active BM branch with equal weights; the rigid family combines AM88, JB07, and SR08, and the flexible family combines BT07 and the active BM branch. The rigid family thus relates the displacement to measures of the base excitation, the flexible family additionally incorporates the dynamic response of the sliding mass through $T_{s}$, and the ensemble is the design set that combines both. For each $k_{y}$, the displacements of a family are summarized from the weighted empirical distribution of the realizations of its models.

All models receive the same joint sample of PGA and spectral accelerations, and a single realization of $\epsilon$ is shared across the models and across all values of $k_{y}$; each formulation scales that residual through its own $\sigma_{\ln D}$, and the sampled PGA is retained with each realization so that the inversion preserves the pairing between displacement and seismic demand. The realizations of $D_{n}$ are calculated for each material class with its mean dynamic properties; the fractiles of the stiffness profiles and of $T_{s}$ are not propagated as additional realizations in the displacement calculation, and each material class is kept as an separate scenario through the inversion to $k_{\max}$, so the displacement curves are not averaged across materials before that operation.

For each model and realization, the computed $D_{n}(k_{y})$ relation is projected onto a non-increasing curve and inverted in the $(lnD_{n},lnk_{y})$ plane to solve the criterion of [**Eq. 10‑14**](#_Ref_gmdp_eq_eq_kmax_criterion); when $D_{a}$ falls outside the calculated range, the relation is extrapolated in that plane from the two points at the corresponding end, with the single exception of the AM88 limit treated in [**11Appendix E**](#section-2). The inversion is performed first for each model within each realization.

The root distributions of the models are then combined with the family weights and summarized through the arithmetic mean and the empirical fractiles $q = 0.05$, 0.10, 0.16, 0.50, 0.84, 0.90, and 0.95 (Verri Kozlowski, 2026). Because of the decreasing relation between $D_{n}$ and $k_{y}$, the fractile associated with the exceedance target satisfies [**Eq. 10‑16**](#_Ref_gmdp_eq_eq_kmax_fractile), where $q = 0.84$ corresponds to an exceedance probability of $p_{e} = 16\%$.

$q = 1 - p_{e}$ **[**[]{#_Ref_gmdp_eq_eq_kmax_fractile .anchor}**Eq. 10‑16]**

The $q$ fractiles are therefore the statistics associated with the criterion expressed through $p_{e}$; the arithmetic mean summarizes the center of the simulated distribution and does not represent a target probability. The evaluation uses 300 realizations for each demand – the probabilistic spectrum of each return period $T_{R}$ = 475, 2,475, 10,000 years – and a grid of allowable displacements $D_{a}/H_{s}$ ranging from 0.05 to 2.50 %. This grid contains, for every slope height, the damage thresholds $D_{a}/H$ = 0.1, 0.4, 1.0, 2.5% of Section [**10.1.1**](#seismic-design-criteria-for-slopes), at which the coefficient tables are reported; values of $D_{a}$ that exceed the calculated range of a realization are obtained through the logarithmic extrapolation defined above.

## Fundamental Periods of the Crawford Embankments

[Table 10‑1](#_Ref_gmdp_tbl_periods) presents the fundamental periods and the mean dynamic properties of the slope scenarios evaluated for the Crawford facilities. Each scenario is named with the letter S followed by its slope height in meters. The scenarios are S135, S50, S32, S27, and S35, which correspond to material identifiers (IDm) U1 to U5 in [Table 10‑1](#_Ref_gmdp_tbl_periods), respectively.

  ---------------------------------------------------------------------------------------------------------------------------------------------------
   **IDm**  **USCS**      $$H_{s}$$   $$b$$   $$s$$   $$\lambda_{o}$$   $$m_{o}$$   $$a_{1}$$   $$G_{o}$$   $$V_{S}^{o}$$   $$V_{S30}$$   $$T_{s}$$
  --------- ------------- ----------- ------- ------- ----------------- ----------- ----------- ----------- --------------- ------------- -----------
     U1     ML MH         135         363     2.50    0.350             0.484       3.6538      263.8       368.8           194.0         1.278

     U2     SP SM         50          108     2.75    0.282             0.479       3.3699      213.4       324.7           218.0         0.526

     U3     SP SM ML MH   32          52      3.00    0.213             0.464       3.1306      147.6       271.3           205.7         0.392

     U4     GP GW         27          29      3.25    0.142             0.546       3.1036      365.1       400.1           309.9         0.219

     U5     GP GW SP SM   35          20      3.50    0.075             0.506       2.9528      272.7       353.1           251.6         0.305
  ---------------------------------------------------------------------------------------------------------------------------------------------------

  : []{#_Ref_gmdp_tbl_periods .anchor}Table 10‑1: Fundamental periods and mean dynamic properties of the evaluated slope scenarios

Notes:

- 
- 
- 
- 
- 
- 

## IDm identifies the material scenario and USCS the classification of the slope materials. $H_{s}$ is the slope height and $b$ the berm width, both in m$s$ is the slope ratio ($\tan\beta = 1/s$) and $\lambda_{o}$ the truncation ratio, both dimensionless; $G_{o}$ is the shear modulus of the profile at $z/H_{s} = 1$, in MPa, and $m_{o}$ the exponent of its power law, dimensionless$a_{1}$ is the first modal root, dimensionless$V_{S}^{o}$ is the basal shear-wave velocity and $V_{S30}$ the travel-time-averaged shear-wave velocity in the uppermost 30 m, both in m/s.Seismic Coefficients

[Figure 10‑1](#_Ref_gmdp_fig_kh_1) through [Figure 10‑3](#_Ref_gmdp_fig_kh_3) show the performance-based horizontal seismic coefficient, expressed as a percentage of the PGA, as a function of the allowable permanent displacement relative to the slope height, for design earthquakes with AEPs of 1:475, 1:2,475, and 1:10,000 years. [Table 10‑2](#_Ref_gmdp_tbl_summary) lists the coefficients of the ensemble set at the four relative displacement limits for the 1:2,475 and 1:10,000-year return period design earthquakes. The coefficients of the rigid and flexible sets, and the coefficients in acceleration units, are included in [**11Appendix E**](#section-2).

  ---------------------------------------------------------------------------------------------------------------------------------
   **Scenario**  **AEP**    $$\mathbf{T}_{\mathbf{s}}$$   $$\mathbf{V}_{\mathbf{S30}}$$   **0.1%**   **0.4%**   **1%**   **2.5%**
  -------------- ---------- ----------------------------- ------------------------------- ---------- ---------- -------- ----------
       S135      1:2,475    1.278                         194                             14.3       5.8        2.9      1.4

       S135      1:10,000   1.278                         194                             18.6       8.5        4.3      2.3

       S50       1:2,475    0.526                         218                             25.2       11.4       5.6      2.6

       S50       1:10,000   0.526                         218                             32.5       17.4       9.8      4.8

       S32       1:2,475    0.392                         205.7                           33.1       16.6       8.8      4.2

       S32       1:10,000   0.392                         205.7                           41.5       23.5       14.3     7.5

       S27       1:2,475    0.219                         309.9                           39.4       20.4       11.2     5.2

       S27       1:10,000   0.219                         309.9                           49.3       27.9       17.3     9.3

       S35       1:2,475    0.305                         251.6                           33.3       16.2       8.4      3.8

       S35       1:10,000   0.305                         251.6                           42.6       23.6       14.1     7.2
  ---------------------------------------------------------------------------------------------------------------------------------

  : []{#_Ref_gmdp_tbl_summary .anchor}Table 10‑2: Seismic Coefficients [% of PGA] of the Ensemble Set for Design Earthquakes with AEPs of 1:2,475 and 1:10,000 Years

Notes:

> Values are for the ensemble set. The column headings give the allowable permanent displacement relative to the slope height, expressed as a percentage. The fundamental period of the slope is in seconds and the time-averaged shear-wave velocity of the upper 30 m is in m/s.

![Figure 10‑1: Fig. 5: Mean values of kh [% of PGA] for site CFD and return period TR=500 yr, as a function of the allowable permanent displacement relativ](./media/image41.png){width="5.5in" height="4.126454505686789in"}

[]{#_Ref_gmdp_fig_kh_1 .anchor}Figure 10‑1: Mean Values of $\mathbf{k}_{\mathbf{h}}$ [% of PGA] for Return Period $\mathbf{T}_{\mathbf{R}}\mathbf{= 475}$ yr, as a Function of the Allowable Permanent Displacement Relative to Slope Height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%]. The Curves Represent the Scenarios S135, S50, S32, S27, S35 Evaluated with the Rigid, Ensemble, and Flexible Sets.

Notes:

> The coefficient is expressed as $100\, k_{\max}/PGA(V_{S30})$. Color identifies the scenario and line pattern identifies the set: solid for rigid, short dashes for ensemble, and long dashes for flexible. The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.

![Figure 10‑2: Fig. 6: Mean values of kh [% of PGA] for site CFD and return period TR=2,500 yr, as a function of the allowable permanent displacement relat](./media/image42.png){width="5.5in" height="4.126454505686789in"}

Figure 10‑2: Mean Values of $k_{h}$ [% of PGA] for Return Period $T_{R} = 2,475$ yr, as a Function of the Allowable Permanent Displacement Relative to Slope Height, $D_{a}/H$ [%]. The Curves Represent the Scenarios S135, S50, S32, S27, S35 Evaluated with the Rigid, Ensemble, and Flexible Sets.${}_{}$${}_{}$${}_{}$

Notes:

> The coefficient is expressed as $100\, k_{\max}/PGA(V_{S30})$. Color identifies the scenario and line pattern identifies the set: solid for rigid, short dashes for ensemble, and long dashes for flexible. The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.

![Figure 10‑3: Fig. 7: Mean values of kh [% of PGA] for site CFD and return period TR=10,000 yr, as a function of the allowable permanent displacement rela](./media/image43.png){width="5.5in" height="4.126454505686789in"}

[]{#_Ref_gmdp_fig_kh_3 .anchor}Figure 10‑3: Mean Values of $k_{h}$ [% of PGA] for Return Period $T_{R} = 10,000$ yr, as a Function of the Allowable Permanent Displacement Relative to Slope Height, $D_{a}/H$ [%]. The Curves Represent the Scenarios S135, S50, S32, S27, S35 Evaluated with the Rigid, Ensemble, and Flexible Sets.${}_{}$${}_{}$${}_{}$

Notes:

> The coefficient is expressed as $100\, k_{\max}/PGA(V_{S30})$. Color identifies the scenario and line pattern identifies the set: solid for rigid, short dashes for ensemble, and long dashes for flexible. The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.

# Conclusions

SRK Consulting (Canada), Inc. (SRK) and Paterson and Cooke (P&C), collectively referred to as SRK-PC, were engaged by Canada Nickel Co. (CN) to perform a site-specific seismic hazard assessment for the Crawford Project near Timmins, Ontario. This assessment is part of the Front-End Engineering Design (FEED) for the proposed facilities. The key outcomes of the seismic hazard analysis are summarized below:

- 
- 
- 
- 
- 
- 
- 
- 

Seismic Hazard Assessment: A Probabilistic Seismic Hazard Analysis (PSHA) was conducted, providing essential design parameters such as peak ground acceleration (PGA) and spectral accelerations $s_{a}(T_{n})$.Seismicity of the Region: Although Northern Ontario is generally considered to be a region of low seismicity, the region experiences intraplate seismicity primarily driven by Glacial Isostatic Adjustment (GIA) and regional stress. Notable historical events, including the 1935 Temiskamingue earthquake (Mw 6.2) and the 2000 Kipawa earthquake (Mw 4.7), demonstrate the potential for earthquake activity.Seismic Hazard Model: The assessment utilized the 6th Generation Seismic Hazard Model of Canada (CanadaSHM6), implemented through the Global Earthquake Model (GEM) (2018). This model forms the basis for seismic hazard values in the 2020 National Building Code of Canada (2020 NBCC) (Natural Resources of Canada, 2020).Ground Motion Models: Two sets of Ground Motion Models (GMMs) were employed, capturing epistemic uncertainty. The models, developed by Atkinson and Adams (2013) and the NGA-East project (Goulet, et al., 2017) were used to model the ground motion intensity for the site.PSHA: The PSHA for the site was conducted using the OpenQuake v3.26.2 engine (Pagani, Monelli, & Weatgerill, 2014). Results are presented in terms of Annual Exceedance Probability (AEP) and Uniform Hazard Spectra (UHS) for site conditions ranging from hard to soft rock, as defined by the 2020 NBCC. The analysis considers events with target AEPs of 1:475, 1:975, 1:2,475, 1:5,000, and 1:10,000 years, and covers various confidence levels, including mean, 50th, 84th, 90th, and 95th percentiles.Site-Specific Adjustments: The design demands combine the direct logic-tree evaluation at each condition with the ST20 transformation of the demand at the reference condition of 760 m/s, conditioned on the PGA of the same realization. Seismic Cone Penetration Tests (SCPT) classified the site as Stiff Soil Class D ($V_{s,30} = \$`<!-- -->`{=html}220 m/s) per the 2020 NBCC.Design Earthquake (MDE): Based on GISTM, and for closure on ICOLD and ANCOLD guidance, an "Extreme" consequence level was adopted for the TMF, resulting in a Maximum Design Earthquake (MDE) with an AEP of 1:10,000 years. For Site Class D soils, the MDE corresponds to a horizontal PGA of 0.312 g (mean) and 0.442 g (84th percentile). For the Clay, Rock, and Sand & Silt Impoundments, as well as the East and West Stockpiles, the MDE corresponds to an AEP of 1:2,475 years, with a PGA of 0.159 g (mean) and 0.229 (84th percentile).Seismic Coefficients: Performance-based seismic coefficients for embankments were derived from Newmark permanent displacements for use in pseudo-static slope stability analyses. The coefficients are reported at four relative displacement limits (0.1, 0.4, 1.0, and 2.5% of the slope height) for design earthquakes with AEPs of 1:475, 1:2,475, and 1:10,000 years.

# 

ReferencesAdams, J., & Basham, P. (1991). The seismicity and seismotectonics of eastern Canada. In *Neotectonics of North America.* Geological Society of America.

Aliberti, D., Biondi, G., Cascone, E., & Rampello, S. (2019). Performance Indexes for Seismic Analyses of Earth Dams. In F. Silvestri, & N. Moraci (Eds.), *Earthquake Geotechnical Engineering for Protection and Development of Environment and Constructions.* Associazione Geotecnica Italiana.

Ambraseys, N. N., & Menu, J. M. (1988). Earthquake-Induced Ground Displacements. *Earthquake Engineering & Structural Dynamics, 16*(7), 985-1006. Retrieved from https://doi.org/10.1002/eqe.4290160704

American Society of Civil Engineers. (2022). *Minimum Design Loads for Buildings and Other Structures, ASCE/SEI 7-22* (Vol. 7). Reston, VA. Retrieved from https://doi.org/10.1061/978078441578

Anderson, D. G., Martin, G. R., Lam, I. P., & Wang, J. N. (2008). *Seismic Analysis and Design of Retaining Walls, Buried Structures, Slopes, and Embankments. NCHRP Report No. 611.* Transportation Research Board. Retrieved from https://www.ce.memphis.edu/7137/PDFs/Seismic%20Manual/nchrp_rpt_611.pdf

Assatourians, K., & Atkinson, G. (2016). *Automatically Generated Interactive Ground Motion Maps for Southern Ontario* . Retrieved from Earthquake Data Auto-Processor (EDAP): https://www.seismotoolbox.ca/edap/index.php

Atkinson, G. M., & Adams, J. (2013). Ground motion prediction equations for application to the 2015 Canadian national seismic hazard maps. *Canadian Journal of Civil Engineering, 40*, 988-998.

Atkinson, G. M., & Boore, D. M. (2006). ., & Boore, D. M. (2006). *Bulletin of the Seismological Society of America, 96*(6), 2181-2205.

Ausenco. (2023). *Crawford Nickel Sulfide Project - Technical Report and Feasibility Study.*

Australian National Committee on Large Dams. (2012). *Guidelines on Tailings Dams: Planning, Design, Construction, Operation and Closure.* Australian National Committee on Large Dams.

Baker, J. W., & Jayaram, N. (2008). Correlation of Spectral Acceleration Values from NGA Ground Motion Models. *Earthquake Spectra, 24*(1), 299-317. Retrieved from https://doi.org/10.1193/1.2857544

Bazurro, P., & Cornell, A. (1999). Disaggregation of Seismic Hazard. *Bulletin of the Seismological Society of America, 89*(2), 501-520.

Bommer, J., & Scherbaum, F. (2008). The Use and Misuse of Logic Trees in Probabilistic Seismic Hazard Analysis. *Earthquake Spectra, 24*(4), 997-1009.

Boore, D. M., & Campbell, K. W. (2017). Updated Ground-Motion Relations for the Next Generation of Ground-Motion Prediction Equations. *Bulletin of the Seismological Society of America, 107*(2).

Boore, D., & Atkinson, G. (2008). Ground-Motion Prediction Equations for the Average Horizontal Component of PGA, PGV, and 5%-Damped PSA at Spectral Periods between 0.01 s and 10.0 s. *Earthquake Spectra, 24*(1).

Bray, J. D., & Macedo, J. (2019). Procedure for Estimating Shear-Induced Seismic Slope Displacement for Shallow Crustal Earthquakes. *Journal of Geotechnical and Geoenvironmental Engineering, 145*(12), 04019106. Retrieved from https://doi.org/10.1061/(ASCE)GT.1943-5606.0002143

Bray, J. D., & Travasarou, T. (2007). Simplified Procedure for Estimating Earthquake-Induced Deviatoric Slope Displacements. *Journal of Geotechnical and Geoenvironmental Engineering, 133*(4), 381-392. Retrieved from https://doi.org/10.1061/(ASCE)1090-0241(2007)133:4(381)

Bray, J. D., & Travasarou, T. (2009). Pseudostatic Coefficient for Use in Simplified Seismic Slope Stability Evaluation. *Journal of Geotechnical and Geoenvironmental Engineering, 135*(9), 1336-1340. Retrieved from https://doi.org/10.1061/(ASCE)GT.1943-5606.0000012

Bray, J. D., Macedo, J., & Travasauro, T. (2018). Simplified procedure for estimating seismic slope displacements for subduction and crustal earthquakes. *Journal of Geotechnical and Geoenvironmental Engineering, 144*(11).

Canadian Comission on Building and Fires Codes and National Research Council of Canada. (2020). *National Building Code of Canada.*

Canadian Commission on Building and Fire Codes and National Research Council of Canada. (2015). *National Building Code of Canada.* Ottawa: National Research Council of Canada.

Canadian Dam Association. (2013). *Dam Safety Guidelines 2007 (Revised 2013).*

Canadian Dam Association. (2019). *Application of CDA Dam Safety Guidelines to Mining Dams, Technical Bulletin.*

Cornell, C. A. (1968). Engineering Seismic Risk Analysis. *Bulletin of the Seismological Society of America, 58*(5), 1583-1606.

Cornell, C. A., & Benjamin, J. R. (1970). *Probability, Statistics, and Decision for Civil Engineers.* McGraw-Hill.

Dakaoulas , P., & Gazetas, G. (1985). A class of inhomogeneous shear models for seismic response of dams and embankments. *Soil Dynamics and Earthquake Engineering, 4*(4), 166-182.

European Committee for Standardization. (2004). *Eurocode 8: Design of Structures for Earthquake Resistance – Part 5: Foundations, Retaining Structures and Geotechnical Aspects. European Standard EN 1998-5.* European Committee for Standardization.

Federal Emergency Management Agency. (2005). *Federal Guidelines for Dam Safety: Earthquake Analyses and Design of Dams. P-65.* Federal Emergency Management Agency.

Geological Survey of Canada. (2023). *Sixth-generation seismic hazard model of Canada: grid values of mean hazard to be used with the 2020 National Building Code of Canada, Open File No. 8950.* Geological Survey of Canada.

Global Earthquake Model (GEM) Foundation. (2018). The GEM Global Seismic Hazard Map (Version 2018.1). Pravia, Italy. Retrieved from https://www.globalquakemodel.org/

Goulet, C. A., Bozorgnia, Y., Abrahamson, N. A., Kuehn, N., Al Atik, L., Youngs, R. R., & Graves, L. W. (2017). *NGA-East Ground-Motion Models for the U.S. Geological Survey National Seismic Hazard Maps, PEER Report No. 2017/03.* Pacific Earthquake Engineering Research Center (PEER).

Gutenberg, B., & Ritcher, C. F. (1944). Frequency of earthquakes in California. *Bulletin of the Seismological Society of America, 34*(4), 185-188.

Hardin, B. O., & Black, W. L. (1968). Vibration Modulus of Normally Consolidated Clay. *Journal of the Soil Mechanics and Foundations Division, 94*(2), 353-369. Retrieved from https://doi.org/10.1061/JSFEAQ.0001100

Hardin, B. O., & Drnevich, V. P. (1972). Shear Modulus and Damping in Soils: Measurement and Parameter Effects. *Journal of the Soil Mechanics and Foundations Division, 98*(6), 603-624. Retrieved from https://doi.org/10.1061/JSFEAQ.0001756

Harmon, J. K., Edwards, B. D., & Wu, J. (2017). Site Response Analysis and Ground Motion Prediction in the Eastern United States. *Seismological Research Letters, 88*(4), 985-995.

Hashash, Y. M., Ilhan, O., & Harmon, J. A. (2020). Nonlinear Site Amplification Model for Ergodic Seismic Hazard Analysis in Central and Eastern North America. *Earthquake Spectra, 36*(1), 69-86. Retrieved from https://doi.org/10.1177/8755293019878193

International Commission on Large Dams. (2016). *Selecting Seismic Parameters for Large Dams – Guidelines. Bulletin No. 148.* International Commission on Large Dams.

International Council on Mining & Metals (ICMM). (2020). *Global Industry Standard on Tailings Management (GISTM).* International Council on Mining & Metals.

Ishihara, K. (1997). *Soil Behaviour in Earthquake Geotechnics* (Vol. 34).

Jibson, R. W. (2007). Regression Models for Estimating Coseismic Landslide Displacement. *Engineering Geology, 91*(2-4), 209-218. Retrieved from https://doi.org/10.1016/j.enggeo.2007.01.013

Kaklamanos, J., Baise, L. G., & Boore, D. M. (2010). Estimating Unknown Input Parameters when Implementing the NGA Ground-Motion Predition Equations in Engineering Practice. *Earthquake Spectra, 27*(4), 1219-35.

Kolaj, M., Adams, J., & Halchuk, S. (2020). Seismic Hazard in Southeastern Canada: Uncertainty and Controls on Seismic Hazard in a Region of Low-To-Moderate Seismicity. *7th World Conference on Earthquake Engineering, 17WCEE.* Sendai, Japan.

Kolaj, M., Allen, T., Mayfied, R., Adams, J., & Halchuk, S. (2019). Ground-motion models for the 6th Generation Seismic Hazard Model of Canada. *12th Canadian Conference on Earthquake Engineering, June 17-20, 2019.* Quebec.

Kramer, S. (1996). *Geotechnical Earthquake Engineering.* New Jersey: Prentice Hall.

Ma, S., Eaton, D. W., & Adams, J. (2008). Intraplate Seismicity of a Recently Deglaciated Shield Terrain: A Case from Northern Ontario, Canada. *Bulletin of the Seismological Society of America, 98*(6), 2828-2848.

Macedo, J., Bray, J. D., Abrahamson, N. A., & Travasarou, T. (2018). Performance-Based Probabilistic Seismic Slope Displacement Procedure. *Earthquake Spectra, 34*(2), 673-695. Retrieved from https://doi.org/10.1193/122516EQS251M

Makdisi, F. I., & Seed, H. B. (1978). Simplified Procedure for Estimating Dam and Embankment Earthquake-Induced Deformations. *Journal of the Geotechnical Engineering Division, 104*(GT7), 849-867. Retrieved from https://doi.org/10.1061/AJGEB6.0000668

Mazzotti, S. (2005). Rates and uncertainties on seismic moment and deformationin eastern Canada. *Journal of Geophysical Research, 1110*.

McGuire, R. K. (1993). Computations of Seismic Hazard. *Annals of Geophysics, XXXVI*(3-4).

Natural Resources de Canada. (2013, 04 26). Retrieved from The 01 January 2000 Kipawa Earthquake (mn=5.2): https://web.archive.org/web/20181123032543/http://www.earthquakescanada.nrcan.gc.ca//pprs/pubs/esssa00_temis.php

Natural Resources of Canada. (2020). *The 6th Generation Seismic Hazard Model of Canada: Technical Report. Open File 8630. Natural Resources Canada, 2020.* Goverment of Canada.

Natural Resources of Canada. (2021a, 04 06). *Earthquake zones in Eastern Canada*. Retrieved from https://www.earthquakescanada.nrcan.gc.ca/zones/eastcan-en.php

Natural Resources of Canada. (2021b, 04 06). *Search the Earthquake Database*. Retrieved from Earthquakes Canada: https://www.earthquakescanada.nrcan.gc.ca/stndon/NEDB-BNDS/bulletin-en.php

Natural Resources of Canada. (2021c). Retrieved from 2020 National Building Code of Canada Seismic Hazard Tool: https://www.earthquakescanada.nrcan.gc.ca/hazard-alea/interpolat/nbc2020-cnb2020-en.php

Natural Resources of Canada. (2021d, 04 06). *The 1935 Magnitude 6.1 Timiskaming earthquake*. Retrieved from https://www.seismescanada.rncan.gc.ca/historic-historique/events/19351101-en.php

Newmark, N. M. (1965). Effects of Earthquakes on Dams and Embankments. *Géotechnique, 15*(2), 139-160. Retrieved from https://doi.org/10.1680/geot.1965.15.2.139

Ontario Ministry of Natural Resources. (2011). *Technical Bulletin for Seismic Hazard Criteria, Assessment and Considerations .*

Pagani, M., Monelli, M., & Weatgerill, G. (2014). OpenQuake Engine: An Open Hazard (and Risk) Software for the Global Earthquake Model. *Seismological Research Letters, 85*(3), 692-702.

Peltier, W. R. (2004). Global Glacial Isostasy and the Surface of the Ice-Age Earth: The ICE-5G (VM2) Model and Grace. *Annual Review of Eartha and Planetary Sciences, 32*, 111-149.

Petersen, M. D., Shumway, A. M., Powers, P. M., Mueller, C. S., Moschetti, M. P., Frankel, A. D., . . . Yeng, Y. (2018). *Preliminary 2018 Update of the U.S.* United States Geological Survey.

Saygili, G., & Rathje, E. M. (2008). Empirical Predictive Models for Earthquake-Induced Sliding Displacements of Slopes. *Journal of Geotechnical and Geoenvironmental Engineering, 134*(6), 790-803.

Shibata, T., & Soelarno, D. S. (1975). Stress-Strain Characteristics of Sands Under Cyclic Loading. *Proceedings of the Japan Society of Civil Engineers*(239), 57-65. Retrieved from https://doi.org/10.2208/jscej1969.1975.57

SRK Consulting (Canada), Inc. (2023). *Crawford Q1-2024 Winter Geotechnical Exploration Program, Technical Memorandum, Draft, Project No. CAPR000801, December 8.*

SRK Consulting (Canada), Inc. (2024). *Crawford Overburden Geotechnical Investigation, Factual Report 2024-Q1, Draft, Project No. CAPR003118.*

Stewart, J. P., Parker, G. A., Atkinson, G. M., Boore, D. M., Hashash, Y. M., & Silva, W. J. (2020). Ergodic Site Amplification Model for Central and Eastern North America. *Earthquake Spectra, 36*(1), 42-68. Retrieved from https://doi.org/10.1177/8755293019878185

U.S. Army Corps of Engineers. (1995). *Earthquake Design and Evaluation for Civil Works Projects. Engineer Regulation ER 1110-2-1806.* U.S. Army Corps of Engineers. Retrieved from https://www.publications.usace.army.mil/Portals/76/Publications/EngineerRegulations/ER_1110-2-1806.pdf

U.S. Army Corps of Engineers. (2003). *Slope Stability. Engineer Manual EM 1110-2-1902.* U.S. Army Corps of Engineers. Retrieved from https://www.publications.usace.army.mil/Portals/76/Publications/EngineerManuals/EM_1110-2-1902.pdf

U.S. Army Corps of Engineers. (2005). *Stability of Concrete Structures. Engineer Manual EM 1110-2-2100.* U.S. Army Corps of Engineers. Retrieved from https://www.publications.usace.army.mil/portals/76/publications/engineermanuals/em_1110-2-2100.pdf

Verri Kozlowski, A. (2026). *Probabilistic Estimation of Newmark Displacements and Seismic Coefficients Under Hazard Uncertainty.*

WSP. (2023). *Crawford Project - Tailings Management Feasibility Design.*

Wu, P., & Hasegawa, H. S. (1996). Induced Stresses and Fault Potential In Eastern Canada Due to A Disc Load: A Preliminary Analysis. *Geophysical Journal International*.

# Date and Signature Page  {#date-and-signature-page .ExecSum-Heading-1}

This technical report was written by the following “Qualified Persons” and contributing authors. The effective date of this technical report is August 31, 2026.

Prepared by

Diana K. Reyes, PhD, PE

Principal Consultant

SRK Consulting (U.S.), Inc.

Alejandro Verri, PEng

Principal Consultant, Practice Leader

SRK Consulting (Argentina) S.A.

Reviewed by

Osvaldo Ledesma, PhD, PEng

Principal Consultant, Practice Leader

SRK Consulting (Canada) Inc.

Arcesio Lizcano, PhD

Corporate Consultant

SRK Consulting (Canada), Inc.

All data used as source material plus the text, tables, figures, and attachments of this document have been reviewed and prepared in accordance with generally accepted professional engineering and environmental practices.

######## – Crawford Updated Seismic Catalog

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   Year  **Month**   **Day**   **Ho*ur***   **Min**   **Sec**   **Lat. (°)**   **Long.\      **Depth\   **Original Mag.**   **Original Mag. Type**   **Mw**    **ID**
                                                                               (°)**         (km)**                                                            
  ------ ----------- --------- ------------ --------- --------- -------------- ------------- ---------- ------------------- ------------------------ --------- -------------------
   1916  04          24        16           07        00        47.000         -77.000       0.0        3.7                 Mw                       3.7       CCSC11_036029

   1928  **12**      **01**    **00**       **00**    **00**    **50.000**     **-81.500**   **0.0**    **4.7**             **Mw**                   **4.7**   **CCSC11_036298**

   1935  **11**      **01**    **06**       **03**    **00**    **46.780**     **-79.070**   **0.0**    **6.2**             **Mw**                   **6.1**   **CCSC11_036454**

                                                                                                                                                               

                                                                                                                                                               

   1935  11          02        14           31        00        47.230         -78.170       0.0        4.4                 Mw                       4.4       CCSC11_036460

                                                                                                                                                               

                                                                                                                                                               

                                                                                                                                                               

                                                                                                                                                               

                                                                                                                                                               

   1938  04          12        18           55        00        46.885         -79.004       10.0       3.6                 Mw                       3.6       CCSC11_036524

   1939  02          06        05           21        00        46.500         -81.000       0.0        3.0                 Mw                       3.0       CCSC11_036560

   1942  08          26        17           54        00        46.679         -77.637       18.0       3.2                 Mw                       3.2       CCSC11_036655

   1944  03          08        12           49        00        46.700         -78.900       0.0        3.6                 Mw                       3.6       CCSC11_036692

                                                                                                                                                               

   1944  11          05        19           07        00        48.818         -81.085       18.0       3.8                 Mw                       3.8       CCSC11_036710

   1945  07          02        13           29        00        48.630         -76.919       18.0       3.3                 Mw                       3.3       CCSC11_036727

   1947  08          08        05           39        00        46.500         -81.100       0.0        3.9                 Mw                       3.9       CCSC11_036775

   1947  09          14        19           29        00        47.000         -81.300       0.0        3.8                 Mw                       3.8       CCSC11_036779

   1947  11          03        19           51        00        45.700         -81.200       0.0        4.0                 Mw                       4.0       CCSC11_036782

   1952  04          26        04           59        00        46.793         -78.894       10.0       3.1                 Mw                       3.1       CCSC11_036876

   1958  05          14        17           41        00        47.129         -76.776       12.3       3.9                 Mw                       3.9       CCSC11_037085

   1961  10          07        22           36        00        48.828         -76.828       18.0       3.0                 Mw                       3.0       CCSC11_037168

   1963  10          15        12           28        00        46.464         -77.620       18.0       3.5                 Mw                       3.5       CCSC11_037270

                                                                                                                                                               

   1964  01          08        10           04        00        46.378         -77.495       18.0       3.9                 Mw                       3.9       CCSC11_037291

   1964  04          05        13           21        00        46.400         -81.100       0.0        3.3                 Mw                       3.3       CCSC11_037324

   1965  09          15        17           56        00        46.517         -79.047       10.0       3.1                 Mw                       3.1       CCSC11_037425

   1965  12          19        00           49        00        51.012         -81.179       18.0       3.6                 Mw                       3.6       CCSC11_037459

   1975  08          21        21           42        00        48.123         -78.118       1.0        3.1                 Mw                       3.1       CCSC11_038699

   1975  12          19        15           25        00        46.991         -78.782       18.0       3.4                 Mw                       3.4       CCSC11_038735

   1977  12          22        14           57        00        46.836         -76.937       18.0       3.0                 Mw                       3.0       CCSC11_038960

   1980  04          13        22           40        00        49.590         -81.760       7.0        3.6                 Mw                       3.6       CCSC11_039255

   1982  06          23        00           22        00        47.370         -77.060       13.0       3.0                 Mw                       3.0       CCSC11_039597

   1982  08          13        01           06        00        46.660         -78.610       18.0       3.8                 Mw                       3.8       CCSC11_039625

   1984  06          20        16           10        00        46.630         -80.780       1.0        3.0                 Mw                       3.0       CCSC11_039956

   1984  07          06        17           24        00        46.530         -81.170       1.0        3.5                 Mw                       3.5       CCSC11_039966

   1984  12          17        09           38        00        46.500         -82.600       0.0        3.0                 Mw                       3.0       CCSC11_040031

   1987  04          05        07           27        00        51.861         -82.798       18.0       3.1                 Mw                       3.1       CCSC11_040337

   1989  02          13        21           52        00        45.850         -79.350       2.0        3.0                 Mw                       3.0       CCSC11_040621

   1991  06          16        16           46        00        47.040         -76.770       8.0        3.7                 Mw                       3.7       CCSC11_040954

   1995  10          10        07           19        00        46.440         -78.770       18.0       3.0                 Mw                       3.0       CCSC11_041526

   1995  12          06        22           52        00        49.550         -81.830       5.0        3.0                 Mw                       3.0       CCSC11_041543

   1996  08          16        04           56        00        49.240         -82.950       4.5        3.2                 Mw                       3.2       CCSC11_041629

   1998  03          09        05           05        00        46.490         -81.070       1.0        3.4                 Mw                       3.4       CCSC11_041875

   1998  05          25        15           47        00        46.457         -81.174       1.0        3.4                 Mw                       3.4       CCSC11_041906

   2000  **01**      **01**    **11**       **22**    **00**    **46.840**     **-78.930**   **14.0**   **4.7**             **Mw**                   **4.7**   **CCSC11_042143**

   2005  01          30        18           06        00        48.130         -77.970       19.0       3.3                 Mw                       3.3       CCSC11_043132

   2005  03          13        17           08        00        46.540         -80.980       3.0        3.1                 Mw                       3.1       CCSC11_043158

   2006  01          03        11           05        00        49.320         -81.120       22.0       3.2                 Mw                       3.2       CCSC11_043344

   2006  11          29        07           22        00        46.480         -81.180       2.5        3.6                 Mw                       3.6       CCSC11_043581

   2006  12          07        04           44        00        49.510         -81.530       15.0       3.7                 Mw                       3.7       CCSC11_043598

   2007  10          01        16           42        00        47.056         -76.878       17.0       3.5                 Mw                       3.5       CCSC11_043792

   2008  09          11        11           21        00        46.476         -81.042       1.0        3.5                 Mw                       3.5       CCSC11_044091

   2012  05          02        00           03        40        51.899         -80.926       17.0       4.2                 MN                       3.7       GOC_000342

   2012  09          22        16           10        40        48.405         -83.280       8.0        3.9                 MN                       3.4       GOC_000332

   2013  02          19        04           59        44        48.425         -83.298       8.0        3.8                 MN                       3.3       GOC_000321

                                                                                                                                                               

   2018  01          23        14           48        47        48.054         -78.237       10.0       3.0                 Mw                       3.0       EDAP_000130

   2018  01          23        20           05        13        47.682         -78.186       10.0       3.0                 Mw                       3.0       EDAP_000131

   2018  08          12        15           14        18        46.590         -77.701       10.0       3.3                 Mw                       3.3       EDAP_000376

   2018  12          20        20           38        26        48.221         -78.380       10.0       3.2                 Mw                       3.2       EDAP_000564

                                                                                                                                                               

   2019  01          31        04           39        57        48.796         -85.938       10.0       3.3                 Mw                       3.3       EDAP_000650

                                                                                                                                                               

   2019  01          31        19           45        47        50.241         -80.125       10.0       3.0                 Mw                       3.0       EDAP_000655

                                                                                                                                                               

                                                                                                                                                               

                                                                                                                                                               

                                                                                                                                                               

   2019  02          08        07           23        37        46.571         -81.177       10.0       3.2                 Mw                       3.2       EDAP_000678

                                                                                                                                                               

   2019  02          08        18           45        25        49.826         -79.416       10.0       3.2                 Mw                       3.2       EDAP_000684

                                                                                                                                                               

   2019  02          13        19           12        30        49.630         -79.627       10.0       3.1                 Mw                       3.1       EDAP_000691

                                                                                                                                                               

                                                                                                                                                               

   2019  02          19        19           44        03        50.129         -79.938       10.0       3.3                 Mw                       3.3       EDAP_000704

                                                                                                                                                               

   2019  02          24        14           59        35        50.292         -79.509       10.0       3.5                 Mw                       3.5       EDAP_000713

                                                                                                                                                               

   2019  02          25        16           11        45        48.118         -78.076       10.0       3.0                 Mw                       3.0       EDAP_000717

   2020  08          07        18           13        26        46.319         -80.066       2.0        3.5                 MN                       3.0       GOC_000169

   2020  10          14        13           48        53        49.611         -82.423       3.5        3.6                 MN                       3.1       GOC_000159

   2021  01          16        03           19        43        46.548         -81.219       10.0       3.1                 Mw                       3.1       EDAP_001927

   2021  04          13        19           08        25        46.807         -78.233       1.0        3.5                 MN                       3.1       GOC_000131

   2023  12          17        20           19        14        47.306         -76.533       18.0       3.9                 MN                       3.4       GOC_000032

   2025  11          15        09           58        35        51.705         -80.555       18.0       3.7                 Mw                       3.7       GOC_004183
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : []{#_Ref178166773 .anchor}Table A‑1: Crawford Regional Catalog of Events 1916-08/30/2026 (Mw ≥ 3)

######## - Southeastern Model Seismic Sources of the CanadaSHM6

[]{#_Ref178166524 .anchor}Table B‑1: CanadaSHM6 Southeast HY Model Seismic Sources

![](./media/image44.emf){width="8.80188757655293in" height="6.067596237970254in"}

Table B‑2: CanadaSHM6 Southeast H2 Model Seismic Sources

![](./media/image45.emf){width="9.0in" height="4.799305555555556in"}

[]{#_Ref178166543 .anchor}Table B‑3: CanadaSHM6 Southeast R2 Model Seismic Sources

![](./media/image46.emf){width="9.0in" height="2.265277777777778in"}

######## – Seismic Hazard Results

######### **- Annual Exceedance Probability**

**\**

![](./media/diana-hazard-c1-1.png){width="5.059027777777778in" height="3.909326334208224in"}

Figure C1‑1: Annual Exceedance Probability (AEP) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 1500 m/s) for various Structural Periods – Mean Values

![](./media/diana-hazard-c1-2.png){width="5.998333333333333in" height="3.3147933070866142in"}

Figure C1‑2: Annual Exceedance Probability (AEP) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 1500 m/s) for various Structural Periods – 50^th^ Percentile Values

![](./media/diana-hazard-c1-3.png){width="5.999143700787402in" height="3.390670384951881in"}

Figure C1‑3: Annual Exceedance Probability (AEP) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 1500 m/s) for various Structural Periods – 84^th^ Percentile Values

![](./media/diana-hazard-c1-4.png){width="5.998818897637795in" height="3.3333727034120737in"}

Figure C1‑4: Annual Exceedance Probability (AEP) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 1500 m/s) for various Structural Periods – 90^th^ Percentile Values

![](./media/diana-hazard-c1-5.png){width="5.999630358705162in" height="3.3432119422572177in"}

Figure C1‑5: Annual Exceedance Probability (AEP) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 1500 m/s) for various Structural Periods – 95th Percentile Values

![](./media/diana-hazard-c1-6.png){width="5.0in" height="3.86in"}

Figure C1‑6: Annual Exceedance Probability (AEP) in Medium Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 910 m/s) for various Structural Periods – Mean Values

![](./media/diana-hazard-c1-7.png){width="5.999305555555556in" height="3.362450787401575in"}

Figure C1‑7: Annual Exceedance Probability (AEP) in Medium Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 910 m/s) for various Structural Periods – 50^th^ Percentile Values

![](./media/diana-hazard-c1-8.png){width="5.999517716535433in" height="3.3525951443569553in"}

Figure C1‑8: Annual Exceedance Probability (AEP) in Medium Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 910 m/s) for various Structural Periods – 84^th^ Percentile Values

![](./media/diana-hazard-c1-9.png){width="5.999867672790901in" height="3.3338965441819775in"}

Figure C1‑9: Annual Exceedance Probability (AEP) in Medium Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 910 m/s) for various Structural Periods – 90^th^ Percentile Values

![](./media/diana-hazard-c1-10.png){width="5.999399606299213in" height="3.3242279090113738in"}

Figure C1‑10: Annual Exceedance Probability (AEP) in Medium Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 910 m/s) for various Structural Periods – 95^th^ Percentile Values

![](./media/diana-hazard-c1-11.png){width="5.335016404199475in" height="4.0185279965004375in"}

Figure C1‑11: Annual Exceedance Probability (AEP) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 760 m/s) for various Structural Periods – Mean Values

![](./media/diana-hazard-c1-12.png){width="5.55625in" height="3.1044674103237093in"}

Figure C1‑12: Annual Exceedance Probability (AEP) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 760 m/s) for various Structural Periods – 50^th^ Percentile Values

![](./media/diana-hazard-c1-13.png){width="5.999280402449694in" height="3.361910542432196in"}

Figure C1‑13: Annual Exceedance Probability (AEP) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 760 m/s) for various Structural Periods – 84^th^ Percentile Values

![](./media/diana-hazard-c1-14.png){width="5.9996325459317585in" height="3.399816272965879in"}

Figure C1‑14: Annual Exceedance Probability (AEP) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 760 m/s) for various Structural Periods – 90^th^ Percentile Values

![](./media/diana-hazard-c1-15.png){width="5.999047462817148in" height="3.3240562117235344in"}

Figure C1‑15: Annual Exceedance Probability (AEP) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}$ = 760 m/s) for various Structural Periods – 95^th^ Percentile Values

![](./media/diana-hazard-c1-16.png){width="5.2347222222222225in" height="3.9350470253718286in"}

Figure C1‑16: Annual Exceedance Probability (AEP) in Very Dense Soil ($\mathbf{V}_{\mathbf{s,30}}$ = 580 m/s) for various Structural Periods – Mean Values

![](./media/diana-hazard-c1-17.png){width="5.999867672790901in" height="3.409367891513561in"}

Figure C1‑17: Annual Exceedance Probability (AEP) in Very Dense Soil ($\mathbf{V}_{\mathbf{s,30}}$ = 580 m/s) for various Structural Periods – 50^th^ Percentile Values

![](./media/diana-hazard-c1-18.png){width="5.9990496500437445in" height="3.3806594488188977in"}

Figure C1‑18: Annual Exceedance Probability (AEP) in Very Dense Soil ($\mathbf{V}_{\mathbf{s,30}}$ = 580 m/s) for various Structural Periods – 84^th^ Percentile Values

![](./media/diana-hazard-c1-19.png){width="5.999630358705162in" height="3.4186843832020997in"}

Figure C1‑19: Annual Exceedance Probability (AEP) in Very Dense Soil ($\mathbf{V}_{\mathbf{s,30}}$ = 580 m/s) for various Structural Periods – 90^th^ Percentile Values

![](./media/diana-hazard-c1-20.png){width="5.999397419072616in" height="3.361963035870516in"}

Figure C1‑20: Annual Exceedance Probability (AEP) in Very Dense Soil ($\mathbf{V}_{\mathbf{s,30}}$ = 580 m/s) for various Structural Periods – 95^th^ Percentile Values

![](./media/diana-hazard-c1-21.png){width="4.999777996500438in" height="3.6864654418197724in"}

Figure C1‑21: Annual Exceedance Probability (AEP) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}$ = 220 m/s) for various Structural Periods – Mean Values

![](./media/diana-hazard-c1-22.png){width="5.998693132108486in" height="3.399358048993876in"}

Figure C1‑22: Annual Exceedance Probability (AEP) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}$ = 220 m/s) for various Structural Periods – 50^th^ Percentile Values

![](./media/diana-hazard-c1-23.png){width="5.9996325459317585in" height="3.362080052493438in"}

Figure C1‑23: Annual Exceedance Probability (AEP) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}$ = 220 m/s) for various Structural Periods – 84^th^ Percentile Values

![](./media/diana-hazard-c1-24.png){width="5.999399606299213in" height="3.4563024934383204in"}

Figure C1‑24: Annual Exceedance Probability (AEP) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}$ = 220 m/s) for various Structural Periods – 90^th^ Percentile Values

![](./media/diana-hazard-c1-25.png){width="5.999867672790901in" height="3.324463035870516in"}

Figure C1‑25: Annual Exceedance Probability (AEP) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}$ = 220 m/s) for various Structural Periods – 95^th^ Percentile Values

######### **- Uniform Hazard Spectra**

![](./media/diana-hazard-c2-1.png){width="5.0in" height="3.87in"}

Figure C2‑1: Uniform Hazard Spectra (UHS) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}1500 m/s) - Mean Values

![](./media/diana-hazard-c2-2.png){width="6.0in" height="3.4in"}

Figure C2‑2: Uniform Hazard Spectra (UHS) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}1500 m/s) - 50^th^ Percentile Values

![](./media/diana-hazard-c2-3.png){width="6.0in" height="3.4in"}

Figure C2‑3: Uniform Hazard Spectra (UHS) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}1500 m/s) - 84^th^ Percentile Values

![](./media/diana-hazard-c2-4.png){width="6.0in" height="3.4in"}

Figure C2‑4: Uniform Hazard Spectra (UHS) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}1500 m/s) - 90^th^ Percentile Values

![](./media/diana-hazard-c2-5.png){width="6.0in" height="3.4in"}

Figure C2‑5: Uniform Hazard Spectra (UHS) in Hard Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}1500 m/s) - 95^th^ Percentile Values

![](./media/diana-hazard-c2-6.png){width="5.0in" height="3.86in"}

Figure C2‑6: Uniform Hazard Spectra (UHS) in Medium Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}910 m/s) – Mean Values

![](./media/diana-hazard-c2-7.png){width="6.0in" height="3.41in"}

Figure C2‑7: Uniform Hazard Spectra (UHS) in Medium Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}910 m/s) - 50^th^ Percentile Values

![](./media/diana-hazard-c2-8.png){width="6.0in" height="3.4in"}

Figure C2‑8: Uniform Hazard Spectra (UHS) in Medium Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}910 m/s) - 84^th^ Percentile Values

![](./media/diana-hazard-c2-9.png){width="6.0in" height="3.4in"}

Figure C2‑9: Uniform Hazard Spectra (UHS) in Medium Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}910 m/s) - 90^th^ Percentile Values

![](./media/diana-hazard-c2-10.png){width="6.0in" height="3.4in"}

Figure C2‑10: Uniform Hazard Spectra (UHS) in Medium Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}910 m/s) - 95^th^ Percentile Values

![](./media/diana-hazard-c2-11.png){width="5.0in" height="3.86in"}

Figure C2‑11: Uniform Hazard Spectra (UHS) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}760 m/s) – Mean Values

![](./media/diana-hazard-c2-12.png){width="6.0in" height="3.4in"}

Figure C2‑12: Uniform Hazard Spectra (UHS) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}760 m/s) – 50^th^ Percentile Values

![](./media/diana-hazard-c2-13.png){width="6.0in" height="3.4in"}

Figure C2‑13: Uniform Hazard Spectra (UHS) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}760 m/s) – 84^th^ Percentile Values

![](./media/diana-hazard-c2-14.png){width="6.0in" height="3.4in"}

Figure C2‑14: Uniform Hazard Spectra (UHS) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}760 m/s) – 90^th^ Percentile Values

![](./media/diana-hazard-c2-15.png){width="6.0in" height="3.4in"}

Figure C2‑15: Uniform Hazard Spectra (UHS) in Soft Rock ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}760 m/s) – 95^th^ Percentile Values

![](./media/diana-hazard-c2-16.png){width="5.0in" height="3.87in"}

Figure C2‑16: Uniform Hazard Spectra (UHS) in Very Dense Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}580 m/s) – Mean Values

![](./media/diana-hazard-c2-17.png){width="6.0in" height="3.4in"}

Figure C2‑17: Uniform Hazard Spectra (UHS) in Very Dense Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}580 m/s) – 50^th^ Percentile Values

![](./media/diana-hazard-c2-18.png){width="6.0in" height="3.4in"}

Figure C2‑18: Uniform Hazard Spectra (UHS) in Very Dense Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}580 m/s) – 84^th^ Percentile Values

![](./media/diana-hazard-c2-19.png){width="6.0in" height="3.4in"}

Figure C2‑19: Uniform Hazard Spectra (UHS) in Very Dense Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}580 m/s) – 90^th^ Percentile Values

![](./media/diana-hazard-c2-20.png){width="6.0in" height="3.4in"}

Figure C2‑20: Uniform Hazard Spectra (UHS) in Very Dense Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}580 m/s) – 95^th^ Percentile Values

![](./media/diana-hazard-c2-21.png){width="5.0in" height="3.87in"}

Figure C2‑21: Uniform Hazard Spectra (UHS) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}220 m/s) - Mean Values

![](./media/diana-hazard-c2-22.png){width="6.0in" height="3.4in"}

Figure C2‑22: Uniform Hazard Spectra (UHS) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}220 m/s) – 50^th^ Percentile Values

![](./media/diana-hazard-c2-23.png){width="6.0in" height="3.4in"}

Figure C2‑23: Uniform Hazard Spectra (UHS) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}220 m/s) – 84^th^ Percentile Values

![](./media/diana-hazard-c2-24.png){width="6.0in" height="3.4in"}

Figure C2‑24: Uniform Hazard Spectra (UHS) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}220 m/s) – 90^th^ Percentile Values

![](./media/diana-hazard-c2-25.png){width="6.0in" height="3.41in"}

Figure C2‑25: Uniform Hazard Spectra (UHS) in Stiff Soil ($\mathbf{V}_{\mathbf{s,30}}\mathbf{= \ }$`<!-- -->`{=html}220 m/s) – 95^th^ Percentile Values

######## - Design Earthquakes

######### **- Design Peak Ground Acceleration**

**\**

+:---------------------:+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                       | PGA (g)                                                                                                                                                                                                                                             |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| Return Period (years) | Hard Rock                                       | Medium Rock                                    | Soft Rock                                      | Very Dense Soil                                | Stiff Soil                                     |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | Site Class A                                    | Site Class B                                   | Site Class B/C                                 | Site Class C                                   | Site Class D                                   |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 1500 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 910 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 760 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 580 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 220 m/s |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 475                   | 0.0374                                          | 0.0361                                         | 0.0351                                         | 0.0388                                         | 0.0515                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 975                   | 0.0653                                          | 0.0629                                         | 0.0610                                         | 0.0671                                         | 0.0876                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 2,475                 | 0.1261                                          | 0.1210                                         | 0.1171                                         | 0.1278                                         | 0.1588                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 5,000                 | 0.1943                                          | 0.1862                                         | 0.1800                                         | 0.1948                                         | 0.2288                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 10,000                | 0.2852                                          | 0.2726                                         | 0.2632                                         | 0.2828                                         | 0.3123                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+

: Table D1‑1:PGA of Design Ground Motions for Various Return Periods and Site Conditions – Mean Values

+:---------------------:+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                       | PGA (g)                                                                                                                                                                                                                                             |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| Return Period (years) | Hard Rock                                       | Medium Rock                                    | Soft Rock                                      | Very Dense Soil                                | Stiff Soil                                     |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | Site Class A                                    | Site Class B                                   | Site Class B/C                                 | Site Class C                                   | Site Class D                                   |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 1500 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 910 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 760 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 580 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 220 m/s |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 475                   | 0.0340                                          | 0.0330                                         | 0.0328                                         | 0.0354                                         | 0.0474                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 975                   | 0.0586                                          | 0.0567                                         | 0.0562                                         | 0.0607                                         | 0.0801                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 2,475                 | 0.1127                                          | 0.1086                                         | 0.1074                                         | 0.1153                                         | 0.1456                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 5,000                 | 0.1729                                          | 0.1665                                         | 0.1645                                         | 0.1751                                         | 0.2120                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 10,000                | 0.2525                                          | 0.2430                                         | 0.2398                                         | 0.2535                                         | 0.2919                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+

: Table D1‑2: PGA of Design Ground Motions for Various Return Periods and Site Conditions – 50^th^ Percentile Values

+:---------------------:+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                       | PGA (g)                                                                                                                                                                                                                                             |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| Return Period (years) | Hard Rock                                       | Medium Rock                                    | Soft Rock                                      | Very Dense Soil                                | Stiff Soil                                     |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | Site Class A                                    | Site Class B                                   | Site Class B/C                                 | Site Class C                                   | Site Class D                                   |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 1500 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 910 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 760 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 580 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 220 m/s |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 475                   | 0.0524                                          | 0.0501                                         | 0.0474                                         | 0.0539                                         | 0.0736                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 975                   | 0.0929                                          | 0.0887                                         | 0.0840                                         | 0.0947                                         | 0.1264                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 2,475                 | 0.1803                                          | 0.1717                                         | 0.1623                                         | 0.1812                                         | 0.2288                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 5,000                 | 0.2794                                          | 0.2654                                         | 0.2509                                         | 0.2773                                         | 0.3271                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 10,000                | 0.4122                                          | 0.3899                                         | 0.3684                                         | 0.4040                                         | 0.4424                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+

: Table D1‑3: PGA of Design Ground Motions for Various Return Periods and Site Conditions – 84^th^ Percentile Values

+:---------------------:+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                       | PGA (g)                                                                                                                                                                                                                                             |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| Return Period (years) | Hard Rock                                       | Medium Rock                                    | Soft Rock                                      | Very Dense Soil                                | Stiff Soil                                     |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | Site Class A                                    | Site Class B                                   | Site Class B/C                                 | Site Class C                                   | Site Class D                                   |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 1500 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 910 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 760 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 580 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 220 m/s |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 475                   | 0.0596                                          | 0.0567                                         | 0.0528                                         | 0.0610                                         | 0.0831                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 975                   | 0.1063                                          | 0.1012                                         | 0.0943                                         | 0.1077                                         | 0.1433                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 2,475                 | 0.2070                                          | 0.1963                                         | 0.1829                                         | 0.2066                                         | 0.2589                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 5,000                 | 0.3215                                          | 0.3041                                         | 0.2834                                         | 0.3169                                         | 0.3683                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 10,000                | 0.4754                                          | 0.4477                                         | 0.4170                                         | 0.4624                                         | 0.4958                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+

: Table D1‑4: PGA of Design Ground Motions for Various Return Periods and Site Conditions – 90^th^ Percentile Values

+:---------------------:+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
|                       | PGA (g)                                                                                                                                                                                                                                             |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| Return Period (years) | Hard Rock                                       | Medium Rock                                    | Soft Rock                                      | Very Dense Soil                                | Stiff Soil                                     |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | Site Class A                                    | Site Class B                                   | Site Class B/C                                 | Site Class C                                   | Site Class D                                   |
|                       |                                                 |                                                |                                                |                                                |                                                |
|                       | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 1500 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 910 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 760 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 580 m/s | $\mathbf{V}_{\mathbf{s,30}}\mathbf{=}$ 220 m/s |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 475                   | 0.0705                                          | 0.0665                                         | 0.0604                                         | 0.0715                                         | 0.0968                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 975                   | 0.1267                                          | 0.1198                                         | 0.1092                                         | 0.1272                                         | 0.1675                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 2,475                 | 0.2472                                          | 0.2331                                         | 0.2128                                         | 0.2443                                         | 0.3021                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 5,000                 | 0.3851                                          | 0.3621                                         | 0.3307                                         | 0.3755                                         | 0.4272                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| 10,000                | 0.5709                                          | 0.5343                                         | 0.4877                                         | 0.5490                                         | 0.5723                                         |
+-----------------------+-------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+

: Table D1‑5: PGA of Design Ground Motions for Various Return Periods and Site Conditions – 95^th^ Percentile Values

######### **- Design Response Spectrum**

**\**

  ----------------------- ------------------ ----- ------ ----- ----- -----
                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      

                                                                      
  ----------------------- ------------------ ----- ------ ----- ----- -----

$$\mathbf{C}_{\mathbf{e}}$$ $$\mathbf{e}_{\mathbf{\min}}$$ $$\mathbf{e}_{\mathbf{\max}}$$

![](./media/diana-hazard-d2-1.png){width="5.0in" height="3.87in"}

Figure D2‑1: Design Response Spectra for a Return Period of 10,000 years - Mean Values

![](./media/diana-hazard-d2-2.png){width="6.0in" height="3.4in"}

Figure D2‑2: Design Response Spectra for a Return Period of 10,000 years – 50^th^ Percentile Values

![](./media/diana-hazard-d2-3.png){width="6.0in" height="3.4in"}

Figure D2‑3: Design Response Spectra for a Return Period of 10,000 years – 84^h^ Percentile Values

![](./media/diana-hazard-d2-4.png){width="6.0in" height="3.4in"}

Figure D2‑4: Design Response Spectra for a Return Period of 10,000 years – 90^h^ Percentile Values

![](./media/diana-hazard-d2-5.png){width="6.0in" height="3.4in"}

Figure D2‑5: Design Response Spectra for a Return Period of 10,000 years –95^h^ Percentile Values

######## 

######## 

######## 

+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ######## ${}_{}$ | ########  | ######## ${}_{}$ | ######## ${}_{}$ |
+======================+=================+===========+==================+===========+==================+==================+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+
| ########             | ########        | ########  | ########         | ########  | ########         | ########         |
+----------------------+-----------------+-----------+------------------+-----------+------------------+------------------+

######## 

######## 

######## 

######## ${}_{}$${}_{}$

######## 

######## ${}^{}{}_{}$

######## $\begin{array}{r}
{}_{}\left\lbrack {}_{}\left( {}^{}{}^{}{}^{}{}^{} \right) \right\rbrack \\
{}_{}
\end{array}$

######## ${}_{}$$$${}_{}$${}_{}$

######## $\begin{array}{r}
{}_{}\left\lbrack {}_{}{}_{}{}_{}\left( \frac{{}_{}}{} \right) \right\rbrack \\
{}_{}
\end{array}$

######## ${}_{}$

######## $\begin{array}{r}
{}_{}{}^{}{}^{}{}^{} \\
{}_{} \\
{}_{}
\end{array}$

######## ${}_{}{}_{}$${}_{}$${}_{}{}_{}{}_{}$${}_{}$${}_{}$${}_{}{}_{}$${}_{}$

######## ${}_{}{}_{}{}_{}{}_{}{}_{}{}_{}{}_{}$

######## ${}_{}$${}_{}$${}_{}$${}_{}$${}_{}{}_{}$

######## 

######## ${}_{}$${}_{}{}_{}{}_{}$${}_{}$

######## $\begin{array}{r}
{}_{}{}_{}{}_{}{}_{}{}^{}{}_{}{}_{} \\
{}_{}{}_{}{}^{}{}_{}{}_{} \\
{}_{}\left\{ \begin{matrix}
 & {}_{} \\
 & {}_{}
\end{matrix} \right.\  \\
{}_{}
\end{array}$

######## ${}_{}{}_{}{}_{}$

######## $\begin{array}{r}
{}_{}{}_{}{}_{}{}_{}{}_{}{}^{} \\
{}_{}{}_{} \\
{}_{}{}_{}{}_{} \\
{}_{}{}_{}{}^{} \\
{}_{}{}_{}{}_{}{}_{}^{} \\
{}_{}{}_{}{}^{} \\
{}_{}\left\{ \begin{matrix}
{}_{} & {}_{} \\
{}_{} & {}_{}
\end{matrix} \right.\  \\
{}_{}
\end{array}$

######## ${}_{}{}_{}{}_{}$

######## $\begin{array}{r}
{}_{}{}_{}\left( {}_{} \right){}_{}{}_{}{}^{} \\
{}_{}{}_{}{}_{} \\
{}_{}{}_{}{}^{} \\
{}_{}{}_{}{}_{}{}_{}^{} \\
{}_{}{}_{}{}^{} \\
{}_{}\left\{ \begin{matrix}
{}_{} & {}_{} \\
{}_{} & {}_{}
\end{matrix} \right.\  \\
{}_{}
\end{array}$

######## 

######## 

######## 

######## 

######## 

######## ${}_{}$$$${}_{}$${}_{}$

######## 

######## ${}_{}$

######## 

######## ${}_{}$$$${}_{}$${}_{}$

######## 

######## ${}_{}$

######## 

######## ${}_{}$$$${}_{}$${}_{}$

######## 

######## ${}_{}$

######## ${}_{}$${}_{}$

+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ######## ${}_{}$ | ######## ${}_{}$ | ########  | ########  | ########  | ########  |
+===========+===========+==================+==================+===========+===========+===========+===========+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+

######## 

######## ${}_{}$${}_{}$${}_{}$${}_{}$

######## ${}_{}$${}_{}$

+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ######## ${}_{}$ | ######## ${}_{}$ | ########  | ########  | ########  | ########  |
+===========+===========+==================+==================+===========+===========+===========+===========+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+

######## 

######## ${}_{}$${}_{}$${}_{}$${}_{}$

######## ${}_{}$${}_{}$

+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ######## ${}_{}$ | ######## ${}_{}$ | ########  | ########  | ########  | ########  |
+===========+===========+==================+==================+===========+===========+===========+===========+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+

######## 

######## ${}_{}$${}_{}$${}_{}$${}_{}$

######## ${}_{}$${}_{}$

+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ######## ${}_{}$ | ######## ${}_{}$ | ########  | ########  | ########  | ########  |
+===========+===========+==================+==================+===========+===========+===========+===========+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+

######## 

######## ${}_{}$${}_{}$${}_{}$${}_{}$

######## ${}_{}$${}_{}$

+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ######## ${}_{}$ | ######## ${}_{}$ | ########  | ########  | ########  | ########  |
+===========+===========+==================+==================+===========+===========+===========+===========+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+

######## 

######## ${}_{}$${}_{}$${}_{}$${}_{}$

######## 

######## 

######## ${}_{}$${}_{}$

+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ######## ${}_{}$ | ######## ${}_{}$ | ########  | ########  | ########  | ########  |
+===========+===========+==================+==================+===========+===========+===========+===========+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+

######## 

######## ${}_{}$${}_{}$${}_{}$${}_{}{}_{}$

######## ${}_{}$${}_{}$

+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ######## ${}_{}$ | ######## ${}_{}$ | ########  | ########  | ########  | ########  |
+===========+===========+==================+==================+===========+===========+===========+===========+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+

######## 

######## ${}_{}$${}_{}$${}_{}$${}_{}{}_{}$

######## ${}_{}$${}_{}$

+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ######## ${}_{}$ | ######## ${}_{}$ | ########  | ########  | ########  | ########  |
+===========+===========+==================+==================+===========+===========+===========+===========+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+

######## 

######## ${}_{}$${}_{}$${}_{}$${}_{}{}_{}$

######## ${}_{}$${}_{}$

+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ######## ${}_{}$ | ######## ${}_{}$ | ########  | ########  | ########  | ########  |
+===========+===========+==================+==================+===========+===========+===========+===========+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+

######## 

######## ${}_{}$${}_{}$${}_{}$${}_{}{}_{}$

######## ${}_{}$${}_{}$

+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ######## ${}_{}$ | ######## ${}_{}$ | ########  | ########  | ########  | ########  |
+===========+===========+==================+==================+===========+===========+===========+===========+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+
| ########  | ########  | ########         | ########         | ########  | ########  | ########  | ########  |
+-----------+-----------+------------------+------------------+-----------+-----------+-----------+-----------+

######## 

######## ${}_{}$${}_{}$${}_{}$${}_{}{}_{}$

990: – Seismic Coefficients
991: 
992: Table E1: Shear Stiffness Parameters for Gravels, Sands, and Fines
994: 
995: 
996: - Newmark Permanent-Displacement Formulations
997: The seismic-coefficient section applies five Newmark permanent-displacement formulations: three rigid-block models, two flexible-block models and, among the latter, the BM branch selected by the tectonic control of the project. This section reproduces the published form of each formulation, including both BM branches, and states the rule that defines the active configuration. The rigid-block formulations relate the displacement to measures of the base excitation, whereas the flexible-block formulations additionally incorporate the dynamic response of the sliding mass through its fundamental period Ts and the spectral acceleration evaluated at a period proportional to Ts.
998: Rigid-Block Models
999: The AM88 formulation (Ambraseys & Menu, 1988)(Ambraseys & Menu, 1988) uses the ratio of yield acceleration to PGA, capped to preserve the logarithmic domain, r⋆=min(ky/PGA,0.9999):
1000: μlnD&=ln(10)0.90+log10​(1-r⋆)2.53(r⋆)-1.09,σlnD&=0.30ln(10).[Eq. E11]
1001: The two remaining rigid-block formulations, JB07 and SR08, use the Arias intensity, which is estimated for each realization from the PGA; IA is expressed in m/s and PGA in units of g, and the estimate is applied deterministically, so that each PGA realization determines a single value of IA and the displacement sample propagates the PGA variability. The JB07 formulation (Jibson, 2007)(Jibson, 2007) incorporates the Arias intensity and the ratio ky/PGA:
1002: μlnD&=ln(10)0.561log10IA-3.833log10​kyPGA-1.474,σlnD&=0.616ln(10).[Eq. E12]
1003: The SR08 formulation (Saygili & Rathje, 2008)(Saygili & Rathje, 2008) defines r=ky/PGA and combines PGA and Arias intensity:
1004: μlnD=​&2.39-5.24r-18.78r2+42.01r3-29.15r4&-1.56lnPGA+1.38lnIA,σlnD=​&0.46+0.56r.[Eq. E13]
1005: The logarithmic extension of the Dn(ky) relations beyond their computed support has one exception, the AM88 limit. If the sampled PGA of a realization, PGAs, is smaller than the lower end of the grid, all stored points may satisfy ky/PGAs≥rmax=0.9999 and form a plateau D0,s. In that case the physical branch 0<r<rmax of Eq. E11 is solved for Da>D0,s, instead of extrapolating the plateau or assigning kmax=0:
1006: μlnD(r)=lnDa-lnD0,s+μlnD(rmax),  kmax,s=PGAsr.[Eq. E14]
1007: The random residual cancels between Da and D0,s, and dμlnD/dr=-2.53/(1-r)-1.09/r<0, so the root is unique. An AM88 plateau is accepted only when the original curve is exactly constant and PGAs itself shows that the entire grid reached that limit; a flat curve from another model, or a target Da≤D0,s, is rejected as non-identifiable support.
1008: Flexible-Block Models
1009: The flexible-block formulations evaluate the spectral acceleration at a period proportional to the fundamental period Ts of the sliding mass. The BT07 formulation (Bray & Travasarou, Simplified Procedure for Estimating Earthquake-Induced Deviatoric Slope Displacements, 2007)(Bray & Travasarou, 2007) employs Sa=Sa(1.5Ts) and Mw:
1010: μlnD=​&a0-2.83lnky-0.333(lnky)2+0.566lnkylnSa&+3.04lnSa-0.244(lnSa)2+1.50Ts+0.278(Mw-7),a0=​&-0.22,Ts<0.05 s,-1.10,Ts≥0.05 s,σlnD=​&0.66.[Eq. E15]
1011: The BM17 formulation (Bray, Macedo, & Travasauro, Simplified procedure for estimating seismic slope displacements for subduction and crustal earthquakes, 2018)(Bray, Macedo, & Travasauro, 2018) represents subduction-interface motions with Sa=Sa(1.5Ts):
1012: μlnD&=a0+a1lnSa-0.225(lnSa)2,a1&=3.060+0.538lnky,a0,<=​&-5.864+0.550Mw-9.421Ts&-3.353lnky-0.390(lnky)2,a0,≥=​&-6.896+0.550Mw+3.081Ts-0.803Ts2&-3.353lnky-0.390(lnky)2,a0&=a0,<,Ts<0.1 s,a0,≥,Ts≥0.1 s,σlnD&=0.73.[Eq. E16]
1013: The BM19 formulation (Bray & Macedo, Procedure for Estimating Shear-Induced Seismic Slope Displacement for Shallow Crustal Earthquakes, 2019)(Bray & Macedo, 2019) represents ordinary shallow crustal motions with Sa=Sa(1.3Ts):
1014: μlnD&=a0+2.649+0.344lnkylnSa-0.090(lnSa)2,a0,<=​&-4.684+0.603Mw-9.471Ts&-2.482lnky-0.244(lnky)2,a0,≥=​&-5.981+0.603Mw+3.223Ts-0.945Ts2&-2.482lnky-0.244(lnky)2,a0&=a0,<,Ts<0.1 s,a0,≥,Ts≥0.1 s,σlnD&=0.72.[Eq. E17]
1015: Ensemble
1016: The active configuration applies five formulations: AM88, JB07, SR08, BT07, and one BM branch – BM17 when the project declares subduction control, BM19 when it declares crustal control; each evaluation therefore applies five formulations, never both BM branches at once. The predictors and dispersions are applied in the published form of each model, and the five formulations are combined with the equal weights and the rigid and flexible families defined in Section 10.1.3.
1017: - Seismic Coefficient in Acceleration Units
1018: Figure E21Figure E21 to Figure E23Figure E23 show the horizontal seismic coefficient in units of g, as a function of the allowable permanent displacement relative to the slope height, for design earthquakes with AEPs of 1:475, 1:2,475, and 1:10,000 years. Table E21Table E21 to Table E25Table E25 list the coefficient in cm/s² for each scenario at the four relative displacement limits. The tables include the rigid, ensemble, and flexible sets.
1019: 
1020: Figure E21: Mean values of kmax [g] for return period TR=475 yr, as a function of the allowable permanent displacement relative to slope height, Da/H [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the rigid, ensemble, and flexible sets.
1021: Notes:
1022: Color identifies the scenario and line pattern identifies the set: solid for rigid, short dashes for ensemble, and long dashes for flexible. The shaded bands are delimited by the damage thresholds Da/H=0.1,0.4,1.0,2.5 %.
1023: 
1024: Figure E22: Mean values of kmax [g] for return period TR=2,475 yr, as a function of the allowable permanent displacement relative to slope height, Da/H [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the rigid, ensemble, and flexible sets.
1025: Notes:
1026: Color identifies the scenario and line pattern identifies the set: solid for rigid, short dashes for ensemble, and long dashes for flexible. The shaded bands are delimited by the damage thresholds Da/H=0.1,0.4,1.0,2.5 %.
1027: 
1028: Figure E23: Mean values of kmax [g] for return period TR=10,000 yr, as a function of the allowable permanent displacement relative to slope height, Da/H [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the rigid, ensemble, and flexible sets.
1029: Notes:
1030: Color identifies the scenario and line pattern identifies the set: solid for rigid, short dashes for ensemble, and long dashes for flexible. The shaded bands are delimited by the damage thresholds Da/H=0.1,0.4,1.0,2.5 %.
1031: Table E21: Mean values of kmax [cm/s²] for scenario S135 and return periods TR=475, 2,475, 10,000 yr.
1033: Notes:
1034: ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). Ts is the fundamental period of the slope [s] and VS30 the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, Da/H [%]. The fractiles associated with the exceedance target pe are defined in the seismic-coefficient section.
1035: Table E22: Mean values of kmax [cm/s²] for scenario S50 and return periods TR=475, 2,475, 10,000 yr.
1037: Notes:
1038: ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). Ts is the fundamental period of the slope [s] and VS30 the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, Da/H [%]. The fractiles associated with the exceedance target pe are defined in the seismic-coefficient section.
1039: Table E23: Mean values of kmax [cm/s²] for scenario S32 and return periods TR=475, 2,475, 10,000 yr.
1041: Notes:
1042: ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). Ts is the fundamental period of the slope [s] and VS30 the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, Da/H [%]. The fractiles associated with the exceedance target pe are defined in the seismic-coefficient section.
1043: Table E24: Mean values of kmax [cm/s²] for scenario S27 and return periods TR=475, 2,475, 10,000 yr.
1045: Notes:
1046: ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). Ts is the fundamental period of the slope [s] and VS30 the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, Da/H [%]. The fractiles associated with the exceedance target pe are defined in the seismic-coefficient section.
1047: Table E25: Mean values of kmax [cm/s²] for scenario S35 and return periods TR=475, 2,475, 10,000 yr.
1049: Notes:
1050: ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). Ts is the fundamental period of the slope [s] and VS30 the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, Da/H [%]. The fractiles associated with the exceedance target pe are defined in the seismic-coefficient section.
1051: - Seismic Coefficient as a Percentage of PGA
1052: Table E31Table E31 to Table E35Table E35 list the horizontal seismic coefficient, expressed as a percentage of the PGA, for each scenario at the four relative displacement limits. The tables include the rigid, ensemble, and flexible sets. The coefficients of the ensemble set for the 1:2,475 and 1:10,000 year design earthquakes are also summarized in Table 102Table 102.
1053: Table E31: Mean values of kh [% of PGA] for scenario S135 and return periods TR=475, 2,475, 10,000 yr.
1055: Notes:
1056: ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). Ts is the fundamental period of the slope [s] and VS30 the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, Da/H [%], expressed as 100,kmax/PGA(VS30).
1057: Table E32: Mean values of kh [% of PGA] for scenario S50 and return periods TR=475, 2,475, 10,000 yr.
1059: Notes:
1060: ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). Ts is the fundamental period of the slope [s] and VS30 the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, Da/H [%], expressed as 100,kmax/PGA(VS30).
1061: Table E33: Mean values of kh [% of PGA] for scenario S32 and return periods TR=475, 2,475, 10,000 yr.
1063: Notes:
1064: ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). Ts is the fundamental period of the slope [s] and VS30 the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, Da/H [%], expressed as 100,kmax/PGA(VS30).
1065: Table E34: Mean values of kh [% of PGA] for scenario S27 and return periods TR=475, 2,475, 10,000 yr.
1067: Notes:
1068: ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). Ts is the fundamental period of the slope [s] and VS30 the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, Da/H [%], expressed as 100,kmax/PGA(VS30).
1069: Table E35: Mean values of kh [% of PGA] for scenario S35 and return periods TR=475, 2,475, 10,000 yr.
1071: Notes:
1072: ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). Ts is the fundamental period of the slope [s] and VS30 the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, Da/H [%], expressed as 100,kmax/PGA(VS30).
