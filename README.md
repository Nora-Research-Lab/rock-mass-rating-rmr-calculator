![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Rock Mass Rating (RMR) Calculator
 
*For engineering geologists and geotechnical engineers: enter intact rock strength, RQD, joint spacing, joint condition, and groundwater conditions to instantly compute Bieniawski's RMR value and rock mass class.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Engineering Geology
 
The tool implements Bieniawski's Rock Mass Rating (RMR) classification system. Inputs: (1) Intact rock strength (UCS) in MPa – numeric entry (0.1–400). The code converts the entered value to a rating using standard ranges: >250→15, 100–250→12, 50–100→7, 25–50→4, 5–25→2, 1–5→1, <1→0. (2) RQD (%) – slider 0–100, converted to rating: 90–100→20, 75–90→17, 50–75→13, 25–50→8, <25→3. (3) Joint spacing (m) – numeric entry (0.001–10), rating: >2→20, 0.6–2→15, 0.2–0.6→10, 0.06–0.2→8, <0.06→5. (4) Joint condition – dropdown: 'Very rough surfaces, no separation, hard joint wall'→30, 'Slightly rough surfaces, <1 mm separation, hard joint wall'→25, 'Smooth surfaces or 1–5 mm separation'→20, 'Slickensided or 5–10 mm separation, soft joint wall'→10, 'Soft gouge >10 mm separation'→0. (5) Groundwater conditions – dropdown: 'Completely dry'→15, 'Damp'→10, 'Wet'→7, 'Dripping'→4, 'Flowing'→0. The tool sums the five ratings to produce the total RMR (0–100) and assigns a class: 81–100→Class I (Very good), 61–80→Class II (Good), 41–60→Class III (Fair), 21–40→Class IV (Poor), 0–20→Class V (Very poor). The UI displays the total RMR as a large number, the class name with a color-coded badge (green to red), and a horizontal bar chart showing contributions from each parameter. All inputs are in a clean vertical layout. No AI component; pure deterministic classification.
 
## Run it
 
```bash
docker build -t rock-mass-rating-rmr-calculator .
docker run -p 7860:7860 rock-mass-rating-rmr-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-23.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
