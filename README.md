\# openEBL OPA Tapeout 2026



Passive silicon-photonic optical phased array design for the openEBL 2026-10 fabrication run.



\## Objective



Design, simulate, verify, and submit a fabrication-ready passive 1x4 optical phased array on the SiEPIC EBeam platform.



\## Process



\- 220 nm SOI

\- Single full silicon etch

\- Oxide cladding

\- SiEPIC-EBeam-PDK

\- KLayout + SiEPIC verification

\- No heaters or metal phase shifters



\## Architecture



```text

&#x20;                   ┌── Path delay L0 ─────────► Antenna 0

&#x20;                   │

Input ─► 1x4 splitter├── Path delay L1 ─────────► Antenna 1

&#x20;                   │

&#x20;                   ├── Path delay L2 ─────────► Antenna 2

&#x20;                   │

&#x20;                   └── Path delay L3 ─────────► Antenna 3

```



The waveguide path lengths control the relative emitter phases:



\\\[

\\phi\_n = \\beta L\_n

\\]



with



\\\[

\\beta = \\frac{2\\pi n\_\\mathrm{eff}}{\\lambda}.

\\]



The resulting far-field array factor is



\\\[

AF(\\theta)

=

\\sum\_n A\_n

e^{j(\\phi\_n-k\_0x\_n\\sin\\theta)}.

\\]



\## Day 1 Result



Implemented and validated the first analytical 4-element array-factor model.



Initial test case:



\- N = 4

\- Equal amplitudes

\- Equal phases

\- Pitch = λ/2

\- Main beam at θ = 0°



Generated figure:



`figures/day1\_uniform\_4element\_array\_factor.png`



\## Repository Structure



\- `src/opa\_design/` — analytical and design code

\- `docs/` — requirements and documentation

\- `figures/` — generated plots

\- `simulations/` — EM simulation results

\- `layout/` — generated photonic layouts

\- `tests/` — verification tests

\- `releases/` — fabrication release files

